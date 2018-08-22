#! /bin/bash
## ./3.py -t table -o org_nu -b 20180510   -u  bankname -s  config/lfyh.json
#Below files are needed and also need config directory which include json file for username and password
#loadBankOrg.py
#onlyLoad.py
#fullbankOrg.json
#administrator.json
#1.sh
#6.py

table_name=$1
bank=$2
date_item=$3
debug_show=$4
echo "import data on table[${table_name}] for bank[${bank}] during date range [${date_item}]"

default_IFS="$IFS"
IFS=","
date_range=($date_item)

for date_item in ${date_range[@]}
do 
   ./6.py -t $table_name -b $date_item   -u  $bank -s  config/$bank.json
   while true
   do 
     sleep 10s
     mem_total=`free -m | awk 'NR==2' | awk '{print $2}'`
     mem_aval=`free -m | awk 'NR==2' | awk '{print $7}'`
     mem_free=`expr $mem_aval \* 100 / $mem_total`
     sqoop_cnt=`ps -ef | grep sqoop | grep java | wc -l`
     if [[ $mem_free -gt 30 ]] && [[ $sqoop_cnt -lt 15 ]]
     then
        break
     fi
    done   
done 
