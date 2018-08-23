#!/bin/bash
THREAD_NUM=2
mkfifo tmp
exec 9<>tmp
for ((i=0;i<$THREAD_NUM;i++))
do
	echo -ne "\n" 1>&9
done

#if [ $#!=1 ]
#then
#	echo "The parameters you enter is not correct!";
#	exit -1;
#fi

for ((i=0;i<30;i++))


do

{
	read -u 9 
	{
	echo "test"
	sleep 3
	echo -ne "\n" 1>&9
	}&

}

done 
wait
echo "run finish"
rm tmp
