STRING_A=$1
STRING_B=$2
if [[ ${STRING_A/${STRING_B}//} == $STRING_A ]]
 then
    ## is not substring.
    echo N
    #return 0
 else
    ## is substring.
    echo Y
    #return 1
fi
