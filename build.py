#!/usr/bin/env python
from __future__ import print_function

import os
import re


START_PATTERN = re.compile(r'(\s*)<!-- START ([A-Z\-]+) -->')


def main():
    here = os.path.dirname(__file__)
    master = 'index.html'
    slaves = [os.path.join(here, page) for page in ['404.html', 'organisation.html', 'privacy.html']]

    blocks = {}
    with open(os.path.join(here, master), 'r') as fh:
        for line in fh:
            match = START_PATTERN.match(line)
            if match:
                indent = match.group(1)
                block_name = START_PATTERN.match(line).group(2)
                next_line = line
                lines = [line,
                         "{}<!-- DO NOT MODIFY THIS BLOCK DIRECTLY. CHANGE {} THEN RE-BUILD -->\n".format(indent, master)]
                while not next_line.strip().startswith('<!-- END {} -->'.format(block_name)):
                     next_line = next(fh)
                     lines.append(next_line)
                blocks[block_name] = lines

    for slave in slaves:
        insert_block(slave, blocks)


def insert_block(slave, blocks):
    with open(slave, 'r') as fh:
        lines = list(fh)
    lines_iter = iter(lines)
    new_lines = []

    for line in lines_iter:
        match = START_PATTERN.match(line)
        if match:
            block_name = match.group(2)
            if block_name not in blocks:
                 raise ValueError(
                      "Looking for a {} block, but it doesn't "
                      "exist".format(block_name))
            for new_line in blocks[block_name]:
                new_lines.append(new_line)
            while not next(lines_iter).strip().startswith('<!-- END {} -->'.format(block_name)):
                pass
        else:
            new_lines.append(line)

    if lines != new_lines:
        with open(slave, 'w') as fh:
            for line in new_lines:
                fh.write(line)


if __name__ == '__main__':
    main()
