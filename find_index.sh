head -n1 $1 | tr '\t' '\n'  | grep -n $2
