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

def main():
    if not sys.argv[1:]:
        print >> sys.stderr, "missing"
        sys.exit()
        
    aligned_ids = set([])
    
    for psl in sys.argv[1:]:
        with open(psl, 'r') as fin:
            for line in fin:
                aligned_ids.add(line.strip().split("\t")[9]) 
                
    print len(aligned_ids)

if __name__ == '__main__':
    main()


