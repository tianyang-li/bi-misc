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

from Bio import SeqIO

def main():
    if not sys.argv[1:]:
        print >> sys.stderr, "missing"
        sys.exit(1)
    
    for fq_file in sys.argv[1:]:
        for rec in SeqIO.parse(fq_file, 'fasta'):
            print "@%s" % rec.id
            print "%s" % str(rec.seq)
            print "+\n%s" % ("~"*len(rec))
            
if __name__ == '__main__':
    main()

