#!/usr/bin/env python

#  Copyright (C) 2012 Tianyang Li
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

import sys
import getopt
from itertools import izip
from Bio import SeqIO

def main():
    reads1_f, reads2_f = None, None
    prefix = ""  # read name prefix
    fout = None  # output file prefix
    fmt = None
    try:
        opts, _ = getopt.getopt(sys.argv[1:], '1:2:o:', ['prefix=', 'format='])
    except getopt.GetoptError as err:
        print >> sys.stderr, str(err)
        sys.exit(1)
    for opt, arg in opts:
        if opt == '-1':
            reads1_f = arg
        if opt == '-2':
            reads2_f = arg
        if opt == '-o':
            fout = arg
        if opt == '--prefix':
            prefix = arg
        if opt == '--format':
            fmt = arg
    if (not reads1_f 
        or not reads2_f 
        or not fout
        or not fmt):
        print >> sys.stderr, "missing"
        sys.exit(1)
        
    fout1 = open("%s_1.%s" % (fout, fmt), 'w')
    fout2 = open("%s_2.%s" % (fout, fmt), 'w')
    
    pair_count = 0
    for seq1, seq2 in izip(SeqIO.parse(reads1_f, fmt), SeqIO.parse(reads2_f, fmt)):
        seq1.name = ""
        seq2.name = ""
        seq1.id = "%s.%d/1" % (prefix, pair_count)
        seq2.id = "%s.%d/2" % (prefix, pair_count)
        seq1.description = ""
        seq2.description = ""
        fout1.write(seq1.format(fmt))
        fout2.write(seq2.format(fmt))
        pair_count += 1 
    
    fout1.close()
    fout2.close()
    
    
if __name__ == '__main__':
    main()    

