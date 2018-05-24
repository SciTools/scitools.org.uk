#!/usr/bin/env python
from __future__ import print_function

import os


def main():
    here = os.path.dirname(__file__)
    master = os.path.join(here, 'index.html')
    slaves = [os.path.join(here, page) for page in ['404.html']]

    blocks = {}
    with open(master, 'r') as fh:
        for line in fh:
            if line.strip().startswith('<!-- START'):
                next_line = line
                lines = []
                while not next_line.strip().startswith('<!-- END'):
                     lines.append(next_line)
                     next_line = next(fh)
                lines.append(next_line)
                blocks['STYLES'] = lines
    
    for slave in slaves:
        insert_block(slave, blocks)
    

def insert_block(slave, blocks):
    with open(slave, 'r') as fh:
        lines = list(fh)
    lines_iter = iter(lines)
    new_lines = []

    for line in lines_iter:
        if line.strip().startswith('<!-- START'):
            for new_line in blocks['STYLES']:
    	        new_lines.append(new_line)
    	    while not next(lines_iter).strip().startswith('<!-- END'):
    	        pass
        else:
    	    new_lines.append(line)

    if lines != new_lines:   
        with open(slave, 'w') as fh:
            for line in new_lines:
                fh.write(line)


if __name__ == '__main__':
    main()

