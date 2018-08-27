A="helloworld"
B="low"
if [[ $A == *$B* ]]
then
  echo "包含"
else
  echo "不包含"
fi
