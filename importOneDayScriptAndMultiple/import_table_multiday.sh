#! /bin/bash

declare -A banks=(["104121004004"]="zgyh" ["103121099993"]="nyyh" ["105000000000"]="jsyh" ["301290000007"]="jtyh" ["307121022501"]="payh" ["309391000011"]="xyyh" ["304100040000"]="hxyh" ["310121045016"]="pfyh" ["302100011000"]="zxyh" ["303121075176"]="gdyh" ["318121000010"]="bhyh" ["306121000017"]="gfyh" ["305121010000"]="msyh" ["308124000011"]="zsyh" ["308124000011"]="zsyh" ["313126001022"]="qhdyh" ["313141052422"]="cdyh" ["313124000018"]="tsyh" ["313146000019"]="lfyh" ["313134000011"]="bdyh" ["313143005157"]="czyh" ["313148053964"]="hsyh" ["313131000016"]="xtyh" ["313127000013"]="hdyh" ["313121039003"]="bjyh" ["313121004511"]="tjyh_sjz" ["313121006888"]="hbyh" ["502121000010"]="dyyh_sjz" ["313138000019"]="ZJKYH" ["102121000012"]="gsyh" ["403121000003"]="ycyh" ["402121000009"]="hbsls" ["201121010003"]="gjkfyh" ["203121001182"]="nyfzyh" ["320121000074"]="czyh_gchs" ["320121000082"]="czyh_jzhs" ["320121000023"]="czyh_xjql" ["320121000066"]="czyh_zdhs" ["320121001018"]="czyh_lcql" ["320121000103"]="czyh_xtlf" ["320121000040"]="czyh_lqhs" ["320121000099"]="czyh_szlf" ["320140200012"]="czyh_ccjy" ["320138100014"]="czyh_xhzc" ["320139200017"]="czyh_kbyf" ["320138100022"]="czyh_xhjy" ["320139800013"]="czyh_wqjy" ["320139500019"]="czyh_yxyt" ["320139900014"]="czyh_hllf" ["320139100016"]="czyh_zbxd" ["320140100011"]="czyh_zllf" ["320142700011"]="czyh_wchs" ["320142400018"]="czyh_lpsy" ["320126211112"]="czyh_cljy" ["320126300010"]="czyh_fnjy" ["320126400019"]="czyh_lljy" ["320124000012"]="czyh_kphj" ["320124000037"]="czyh_fnsf" ["320124600018"]="czyh_qaxl" ["320124500017"]="czyh_ltsf" ["320124300015"]="czyh_lxzc" ["320124400016"]="czyh_lnzc" ["320146300022"]="czyh_yqjy" ["320146410019"]="czyh_xhym" ["320146200013"]="czyh_gahs" ["320146133334"]="czyh_shmy" ["320146500016"]="czyh_dcsf" ["320146001014"]="czyh_gysf" ["320146000118"]="czyh_achm" ["320146600113"]="czyh_wahm" ["320146700018"]="czyh_bzsf" ["320136800017"]="czyh_fpds" ["320136600015"]="czyh_gbdzc" ["320135900017"]="czyh_wdzc" ["320136700016"]="czyh_qyzc" ["320134200018"]="czyh_qyxns" ["320135800016"]="czyh_txhz" ["320134100017"]="czyh_mclf" ["320135200019"]="czyh_zzzc" ["320136100019"]="czyh_lslf" ["320135100010"]="czyh_dzzc" ["320136900018"]="czyh_agzc" ["320144200019"]="czyh_rq" ["320144300038"]="czyh_hjhr" ["320145100086"]="czyh_hhql" ["320143200067"]="czyh_qxql" ["320144700074"]="czyh_dgql" ["320145200011"]="czyh_mcrx" ["320143000057"]="czyh_yhql" ["320148500019"]="czyh_szfy" ["320148800056"]="czyh_aphm" ["320132200014"]="czyh_shxt" ["320133600019"]="czyh_qhjn" ["320131100011"]="czyh_xtxns" ["320132900011"]="czyh_njms" ["320129500008"]="czyh_wacz" ["320132700010"]="czyh_rxxns" ["320129101015"]="czyh_cxql")

east_new_db="402121000009,313121006888,313138000019,313141052422,313126001022,313146000019,313134000011,313143005157,313148053964,313131000016,102121000012,301290000007,103121099993"
east_db_url="jdbc:db2://10.20.0.15:50000/EASTST17"
east_new_db_url="jdbc:db2://10.20.0.18:50000/EASTST17"

do_table=$1
do_bank=$2
do_date=$3
bank_schema=${banks[$do_bank]}
echo "import data on table[${do_table}] bank[${do_bank},${banks[$do_bank]}] date[${do_date}]"
OLD_IFS="$IFS"
IFS=","
all_date=($do_date)
IFS="$OLD_IFS"

if [[ $east_new_db =~ $do_bank ]]  
then
  east_db_url=$east_new_db_url
fi

for exec_date in ${all_date[@]}
do
  cmd="nohup sqoop import -Dmapreduce.map.memory.mb=20480 -Dmapreduce.reduce.memory.mb=20480 -Dmapreduce.job.queuename=root.default.sqoop --connect $east_db_url --username ${bank_schema} --password ${bank_schema} --table ${bank_schema}.${do_table} -m 1 --hcatalog-database east --hcatalog-table ${do_table} --hcatalog-partition-keys org_no,load_date --hcatalog-partition-values \"${do_bank}\",\"${exec_date}\" --where \"cjrq='${exec_date}'\" >> ${do_table}_import.log &"
  echo "exec cmd: $cmd"
  eval $cmd
  #while false
  while true
  do
    sleep 10s
    mem_total=`free -m |awk 'NR==2' |awk '{print $2}'`
    mem_aval=`free -m |awk 'NR==2' |awk '{print $7}'`
    mem_free=`expr $mem_aval \* 100 / $mem_total`
    sqoop_cnt=`ps -ef |grep sqoop |grep java |wc -l`
    if [[ $mem_free -gt 30 ]] && [[ $sqoop_cnt -lt 15 ]]
    then
      break
    fi
  done
done
echo "import success on date[${do_date}]"
