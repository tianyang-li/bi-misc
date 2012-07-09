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
    flux_out = None
    fmt = None
    out_prefix = None
    try:
        opts, _ = getopt.getopt(sys.argv[1:], 'f:',
                                ['flux=', 'prefix='])
    except getopt.GetoptError as err:
        print >> sys.stderr, str(err)
        sys.exit(1)
    for opt, arg in opts:
        if opt == '-f':
            fmt = arg
        if opt == '--flux':
            flux_out = arg
        if opt == '--prefix':
            out_prefix = arg
    if (not fmt 
        or not flux_out
        or not out_prefix):
        print >> sys.stderr, "missing"
        sys.exit(1)
    fout1 = open("%s_1.%s" % (out_prefix, fmt), 'w')
    fout2 = open("%s_2.%s" % (out_prefix, fmt), 'w')
    
    read_count = 0
    
    for rec in SeqIO.parse(flux_out, fmt):
        if rec.id[-1] == "1":
            fout1.write(rec.format(fmt))
            id1 = rec.id[:-3]
        else:
            fout2.write(rec.format(fmt))
            id2 = rec.id[:-3]
            
        read_count += 1
        
        if read_count % 2 == 0:
            if id1 != id2:
                print >> sys.stderr, "wrong order"
        
    fout1.close()
    fout2.close()

if __name__ == '__main__':
    main()    


