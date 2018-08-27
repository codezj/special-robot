strA="helloworld"
strB="low"
if [[ $strA =~ $strB ]]
then
  echo "包含"
else
  echo "不包含"
fi
#利用字符串运算符 =~ 直接判断strA是否包含strB
