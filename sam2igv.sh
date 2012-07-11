#!/bin/bash

# usage
# ./sam2igv.sh [ sam file]

SCRIPT_DIR=`dirname $0`

samtools view -bS $1 > `basename $1 .sam`.bam
$SCRIPT_DIR/bam4igv.sh `basename $1 .sam`.bam
rm `basename $1 .sam`.bam


