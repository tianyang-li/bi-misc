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

class _ActionType(object):
    single = 1
    paired = 2

def main():
    fmt = None
    single_file = None
    single_max = float('inf')
    single_min = 0
    
    paired1_file = None
    paired2_file = None
    paired_max1 = float('inf')
    paired_max2 = float('inf')
    paired_min1 = 0
    paired_min2 = 0
    
    out_prefix = None
    
    action = None
    try:
        opts, _ = getopt.getopt(sys.argv[1:],
                                'f:s:1:2:p:',
                                ['max=', 'min=',
                                 'max1=', 'max2=',
                                 'min1=', 'min2='])
    except getopt.GetoptError as err:
        print >> sys.stderr, str(err)
        sys.exit(1)
    for opt, arg in opts:
        if opt == '-f':
            fmt = arg
        if opt == '-s':
            single_file = arg
            action = _ActionType.single
        if opt == '-1':
            paired1_file = arg
            action = _ActionType.paired
        if opt == '-2':
            paired2_file = arg
            action = _ActionType.paired
        if opt == '-p':
            out_prefix = arg
        if opt == '--min':
            single_min = int(arg)
        if opt == '--max':
            single_max = int(arg)
    if (not fmt or not action or not out_prefix
        or (action == _ActionType.single
            and not single_file)
        or (action == _ActionType.paired
            and (not paired1_file or not paired2_file))):
        print >> sys.stderr, "missing"
        sys.exit(1)
    if single_file:
        with open("%s.%s" % (out_prefix, fmt), 'w') as fout:
            for rec in SeqIO.parse(single_file, fmt):
                if len(rec.seq) >= single_min and len(rec.seq) <= single_max:
                    fout.write("%s" % rec.format(fmt))
    elif paired1_file and paired2_file:
        fout1 = open("%s_1.%s" % (out_prefix, fmt), 'w')
        fout2 = open("%s_2.%s" % (out_prefix, fmt), 'w')
        
        for rec1, rec2 in izip(SeqIO.parse(paired1_file, fmt),
                               SeqIO.parse(paired2_file, fmt)):
            if (paired_min1 <= len(rec1.seq) 
                and len(rec1.seq) <= paired_max1
                and paired_min2 <= len(rec2.seq)
                and len(rec2.seq) <= paired_max2):
                fout1.write(rec1.format(fmt))
                fout2.write(rec2.format(fmt))
        
        fout1.close()
        fout2.close()

if __name__ == '__main__':
    main()


