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

from Bio import SeqIO

def main():
    fmt = None
    single_file = None
    single_max = None
    single_min = None
    
    paired1_file = None
    paired2_file = None
    paired_max1 = None
    paired_max2 = None
    paired_min1 = None
    paired_min2 = None
    try:
        opts, _ = getopt.getopt(sys.argv[1:],
                                'f:s:1:2:',
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
        if opt == '-1':
            paired1_file = arg
        if opt == '-2':
            paired2_file = arg
    if (not fmt
        or not(bool(single_file 
                    and single_max != None 
                    and single_min != None) 
               ^ bool(paired1_file and paired2_file
                      and paired_max1 != None
                      and paired_max2 != None
                      and paired_min1 != None
                      and paired_min2 != None))):
        print >> sys.stderr, "missing"
        sys.exit(1)

if __name__ == '__main__':
    main()


