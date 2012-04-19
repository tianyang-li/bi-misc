#!/usr/bin/env python

#  Copyright (C) 2011 Tianyang Li
#  tmy1018@gmail.com
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License

import getopt
import sys
from Bio import SeqIO

def main(args):
    fmt = None  # format: FASTA, FASTQ
    try:
        opts, args = getopt.getopt(args, 'f:')
    except getopt.GetoptError as err:
        print >> sys.stderr, str(err)
        sys.exit(1)
    for opt, arg in opts:
        if opt == '-f':
            fmt = arg
    if fmt == None:
        print >> sys.stderr, "missing options"
        sys.exit(1)
    all_reads = 0
    no_ns = 0
    for fin in args:
        for seq in SeqIO.parse(fin, fmt):
            all_reads += 1
            if "N" not in str(seq.seq) and "n" not in str(seq.seq):
                print seq.format(fmt)
                no_ns += 1
    print >> sys.stderr, "%d in %d no N" % (no_ns, all_reads)
    
if __name__ == '__main__':
    main(sys.argv[1:])    


