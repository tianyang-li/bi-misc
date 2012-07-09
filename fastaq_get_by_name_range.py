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
    locs = {}
    fmt = None
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'f:', ['locations='])
    except getopt.GetoptError as err:
        print >> sys.stderr, str(err)
        sys.exit(1)
    for opt, arg in opts:
        if opt == '--locations':
            """
            locations is a string
                range1;range2;range3
            each range
                "%s,%d,%d" % (chrm_name, start, end) 
            """
            arg = arg.split(";")
            for rng in arg:
                rng = rng.split(",")
                locs.setdefault(rng[0], []).append((int(rng[1]), int(rng[2])))
        if opt == '-f':
            # read format
            fmt = arg
    if (not locs
        or not fmt
        or not args):
        print >> sys.stderr, "missing"
        sys.exit(1)
    for arg in args:
        for rec in SeqIO.parse(arg, fmt):
            if rec.id in locs:
                for start, end in locs[rec.id]:
                    tmp_rec = rec[start:end]
                    tmp_rec.id = rec.id
                    tmp_rec.name = ""
                    tmp_rec.description = "%d,%d" % (start, end)
                    print tmp_rec.format(fmt),

if __name__ == '__main__':
    main()
