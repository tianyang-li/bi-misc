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

import getopt
import sys

from Bio import SeqIO

def main(args):
    fmt = None
    try:
        opts, args = getopt.getopt(args, '', ["format="])
    except getopt.GetoptError as err:
        print >> sys.stderr, str(err)
        sys.exit(1)
    for opt, arg in opts:
        if opt == "--format":
            fmt = arg        
    if not fmt or not args:
        print >> sys.stderr, "missing"
        sys.exit(1)
        
    read_count = 0
    for arg in args:
        for _ in SeqIO.parse(arg, fmt):
            read_count += 1
    print read_count
        
if __name__ == '__main__':
    main(sys.argv[1:])    




