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

def main():
    fmt = None
    reads_file = None
    try:
        opts, _ = getopt.getopt(sys.argv[1:], 'f:r:')
    except getopt.GetoptError as err:
        print >> sys.stderr, str(err)
        sys.exit(1)
    for opt, arg in opts:
        if opt == '-r':
            reads_file = arg
        if opt == '-f':
            fmt = arg
    if (not fmt
        or not reads_file):
        print >> sys.stderr, "missing"
        sys.exit(1)
    read_count = 0
    for rec in SeqIO.parse(reads_file, fmt):
        rec.id = "%s.%d" % (rec.id, read_count)
        print rec.format(fmt)
        read_count += 1

if __name__ == '__main__':
    main()

