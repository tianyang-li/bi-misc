#!/bin/bash

# usage
# ./bam4igv.sh [ bam file]

samtools sort $1 `basename $1 .bam`.sorted
samtools index `basename $1 .bam`.sorted.bam

