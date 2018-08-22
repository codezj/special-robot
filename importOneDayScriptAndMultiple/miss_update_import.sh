#! /bin/bash
table=$1
begdate=$2
enddate=$3

./etl_check_table_miss_data.py -t $table -b $2 -e $3| egrep -v "check|script|="  >output.$table 

cat output.$table  | awk -F "[" '{print $2 $3 }' |awk -F "]" '{print $1 $2}'|tr -s '\n' |awk -F "[,|date]" '{print "'$table'" " " $1 " "  $NF }' | grep -v "!" >result.output.$table

while 
IFS= read line
do
	./import_table_multiday.sh $line
        echo $line
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

done < result.output.$table 
