awk 'NR==1 {print FILENAME} {print $0}' $1  

