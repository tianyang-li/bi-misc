#!/bin/bash

# usage
# ./psl2igv.sh [ psl file ] [ fasta.fai file ]

SCRIPT_DIR=`dirname $0`

psl2sam.pl $1 > `basename $1 .psl`.sam
$SCRIPT_DIR/sam2igv_noSQ.sh `basename $1 .psl`.sam $2
rm `basename $1 .psl`.sam


