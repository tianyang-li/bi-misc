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
    fmt = None
    kick_N = None
    if fmt == None or kick_N == None:
        print >> sys.stderr, "missing options"
        sys.exit(1)
    
if __name__ == '__main__':
    main(sys.argv[1:])    
    

