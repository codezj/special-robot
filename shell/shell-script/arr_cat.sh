#!/bin/sh
 
output_files=( $(cat outfiles) )
for (( i = 0; i < ${#output_files[@]}; ++i )); 
do 
	echo "ar[$i] = ${output_files[i]}"; 
done
 
input_files=( $(cat files) )
for (( i = 0; i < ${#input_files[@]}; ++i )); 
do 
	echo "ar[$i] = ${input_files[i]}"; 
done
 
for((i=0; i<174; i++));
do
	of=${output_files[$i]}
	if=${input_files[$i]}
	echo "$if------------>$of"
	#echo "$i------------>$i"
	#echo ${input_files[$i]}
done
