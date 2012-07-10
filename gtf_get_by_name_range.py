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

"""
range limits starting positions
"""

def main():
    seqname = None
    start = None
    end = None
    gtf_file = None
    try:
        opts, _ = getopt.getopt(sys.argv[1:], '',
                                ['gtf=', 'start=', 'end=', 'seqname='])
    except getopt.GetoptError as err:
        print >> sys.stderr, str(err)
        sys.exit(1)
    for opt, arg in opts:
        if opt == '--gtf':
            gtf_file = arg
        if opt == '--start':
            if arg == "x":
                start = -1
            else:
                start = int(arg)
        if opt == '--end':
            if arg == "x":
                end = float("inf")
            else:
                end = int(arg)
        if opt == '--seqname':
            seqname = arg
    if (not seqname 
        or not start
        or not end
        or not gtf_file):
        print >> sys.stderr, "missing"
        sys.exit(1)
    with open(gtf_file, 'r') as gtf:
        for line in gtf:
            line = line.strip()
            entries = line.split("\t")
            """
            <seqname> 
            <source> 
            <feature> 
            <start> 
            <end> 
            <score> 
            <strand> 
            <frame> 
            [attributes] 
            [comments]
            """
            if (entries[0] == seqname 
                and int(entries[3]) >= start
                and int(entries[3]) <= end):
                print line

if __name__ == '__main__':
    main()    

