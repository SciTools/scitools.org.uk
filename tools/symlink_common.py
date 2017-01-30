#!/usr/bin/env python

import os
import hashlib
import subprocess
import shutil


def rationalise(root, common_directory, dry_run=False):
    """
    Share as many common assets as possible by using symlinks.

    Common assets will be put into the common_directory.
    Moves will be handled with ``git mv``.

    """
    directory = root
    shas, to_link, common_shas = compute_commonality(directory,
                                                     common_directory)
    print to_link
    if not os.path.exists(common_directory):
        if dry_run:
            print 'mkdir -p {}'.format(common_directory)
        else:
            os.mkdir(common_directory)

    new_files = []

    for fpath, common_name in sorted(to_link.items()):
        common_path = os.path.join(common_directory, common_name)
        if not os.path.exists(common_path) or (dry_run and common_path not in new_files):
            if dry_run:
                print 'git mv {} {}'.format(fpath, common_path)
                new_files.append(common_path)
            else:
                tracked = subprocess.check_output(['git', 'ls-files', fpath])
                is_tracked = bool(tracked.strip())
                if is_tracked:
                    subprocess.check_call(['git', 'mv', fpath, common_path],
                                          cwd=directory)
                else:
                    shutil.move(fpath, common_path)
        else:
            if dry_run:
                print 'rm {}'.format(fpath)
            else:
                os.unlink(fpath)
        rel_common_path = os.path.relpath(common_path,
                                          os.path.dirname(fpath))
        if dry_run:
            print 'ln -s {} {}'.format(rel_common_path, fpath)
            print 'git add {}'.format(fpath)
        else:
            os.symlink(rel_common_path, fpath)
            subprocess.check_call(['git', 'add', fpath], cwd=directory)


def compute_commonality(directory, common_directory):

    # A mapping of sha to filename. These will be unique assets.
    shas = {}
    # A mapping of filename to the common asset filename that they should
    # be (newly) linked to.
    to_link = {}
    # The shas of files in (or to be moved into) the common area.
    common_shas = {}

    for root, subdirs, files in os.walk(common_directory):
        subdirs[:] = [d for d in subdirs if not d.startswith('.')]
        for fname in files:
            fpath = os.path.join(root, fname)
            with open(fpath, 'r') as fh:
                sha = hashlib.sha224(fh.read()).hexdigest()
                common_shas[sha] = fname

    for root, subdirs, files in os.walk(directory):
        subdirs[:] = [d for d in subdirs if not d.startswith('.')]
        if root.startswith(common_directory):
            continue

        for fname in files:
            fpath = os.path.join(root, fname)
            # We don't need to modify symlinks.
            if os.path.islink(fpath):
                continue

            with open(fpath, 'r') as fh:
                sha = hashlib.sha224(fh.read()).hexdigest()
                if sha in common_shas:
                    to_link[fpath] = common_shas[sha]
                elif sha in shas:
                    existing_fname = shas.pop(sha)
                    common_shas[sha] = '{}-{}'.format(sha, fname)
                    to_link[fpath] = common_shas[sha]
                    to_link[existing_fname] = common_shas[sha]
                else:
                    shas[sha] = fpath
    return shas, to_link, common_shas


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser('Share assets as symlinks.')
    parser.add_argument("root", help="The root directory to look for sharable content. (default: %(default)s)",
                        default=os.path.dirname(__file__))
    parser.add_argument("--shared-directory", help="The subdirectory name to use for common assets. "
                        "(default: %(default)s)", default="shared_assets")
    parser.add_argument("--dry-run", help="Enable dry-run mode, which will print all of the commands it would do.",
                        action="store_true")
    args = parser.parse_args()

    root_directory = os.path.abspath(args.root)
    common = os.path.join(root_directory, args.shared_directory)
    rationalise(root=root_directory,
                common_directory=common,
                dry_run=args.dry_run)
