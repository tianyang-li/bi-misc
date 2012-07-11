#!/bin/bash

# usage 
# ./bed2igv.sh [ bed file ] [ fasta.fai file ]

SCRIPT_DIR=`dirname $0`

bedToBam -i $1 -g $2 > `basename $1 .bed`.bam
$SCRIPT_DIR/bam4igv.sh `basename $1 .bed`.bam
rm `basename $1 .bed`.bam


