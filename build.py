#!/usr/bin/env python
from __future__ import print_function

import jinja2
import os


def render(source_dir, template_dir, build_dir):
    if not os.path.exists(build_dir):
        os.makedirs(build_dir)
    loader = jinja2.FileSystemLoader([source_dir, template_dir])
    template_env = jinja2.Environment(loader=loader)

    # Go through each of the source files.
    for root, dir, files in os.walk(source_dir):
        rel_root = os.path.relpath(root, source_dir)
        for file in files:
            template_name = os.path.join(rel_root, file)
            # For tidyness, remove any extraneous path components (such
            # as "/./" or "/../").
            template_name = os.path.normpath(template_name)
            output_name = os.path.join(build_dir, template_name)
            print('{} --> {}'.format(template_name, output_name))
            if not os.path.exists(os.path.dirname(output_name)):
                os.makedirs(os.path.dirname(output_name))
            with open(output_name, 'w') as fh:
                template = template_env.get_template(template_name)
                fh.write(template.render().encode('utf-8'))


if __name__ == '__main__':
    here = os.path.dirname(__file__)
    render(os.path.join(here, 'source'), os.path.join(here, 'templates'), './')
