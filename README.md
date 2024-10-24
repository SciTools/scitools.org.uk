scitools.org.uk
===============

This is the repository containing content found at scitools.org.uk.

Building content for scitools.org.uk
====================================

The content is generated by running the ``build.py`` script at the root of the
repository. ``build.py`` takes special template blocks from ``index.html`` and
injects them into the resulting html.


Adding built docs
-----------------

The html in this repository is a combination of generated and static content.
The built documentation for tools such as Iris and cartopy must be generated
using sphinx outside of this repository and subsequently added here. To do
so, create the appropriate folder (e.g. iris/docs/v2.2) with the built
documentation (typically created via sphinx).
Once the content is in place, consider running
``tools/symlink_common.py .`` from the root of the repository. This will look
through all files and share any common assets into the shared_assets
folder, thus reducing the overall repository size to those that need to clone
the repository.


Read the Docs Adoption
----------------------

As of **25/01/2021**, with the release of Iris 3 all documentation for **Iris**
will be provisioned by Read the Docs (https://scitools-iris.readthedocs.io/en/stable/),
this includes latest (master) and stable (most recent tagged release).  The
scitools.org.uk repo now has a **latest** and **stable** redirect that points towards
Read the Docs.  The older documentation (Iris 2.4 and earlier) will still be present
in this repo, and as of today should no longer need to be updated via this repo,
only via the Iris repo and then automatically built and served by Read the Docs.

cf-units is also provisioned by Read the Docs (https://cf-units.readthedocs.io/en/stable/)
since the cf-units v3.0.0 release. Older documentation (v2.0 and earlier) lives
in this repo.

Example workflow
----------------

Note, this example workflow uses Iris.  As stated in the previous section this
is not how the Iris documentation is released, it should however still apply to
Cartopy.

To update scitools.org.uk so that it includes the Iris documentation for the
Iris 1.12 release the following steps need to be followed.

1. Build the Iris documentation using sphinx and add it to the scitools.org.uk repo.
```
$ cd <path_to_iris_repo>/docs/iris
$ make html
$ cp -a build/html <path_to_scitools.org.uk_repo>/iris/docs/v1.12
```

2. Update the `latest` symlink.
```
$ cd <path_to_scitools.org.uk_repo>/iris/docs
$ unlink latest
$ ln -s v1.12 latest
```

3. Update available versions in `iris/docs/version_switch.js`.

4. Generate the shared_assets.
```
$ cd <path_to_scitools.org.uk_repo>
$ python tools/symlink_common.py .
```


Adding contributors
-------------------
Our contributors list, and Contributor License Agreement ([the "CLA"](https://scitools.org.uk/cla/v4)), are currently in the process of change.\
There is a long list of earlier SciTools contributors who signed our original CLA based explictly on [the LGPL3 License](<https://www.gnu.org/licenses/lgpl-3.0.html>).\
However, we are now attempting to re-license all the SciTools projects under a new CLA that will allow us in future to adopt _any_ OSI license,
as explained [here](https://github.com/SciTools/scitools.org.uk/wiki/Contributors-License-Agreement-processing-details).

This process will only be complete when all previous contributors have signed the new terms.
Until then, we respect the rights of all the original contributors, in addition to those on the new list.

Details of the former, original Iris CLA and contributors list were as follows :

    ``contributors.json``, in this repo, contains a JSON dictionary of all contributors who have
    signed the scitools CLA. It is the definitive source of such contributors.
    It is where the [CLA bot](https://github.com/SciTools-incubator/scitools-cla-checker)
    looks to determine if a CLA is required.
    If you've signed the CLA and aren't yet on this list, please consider submitting a PR
    to speed the process up. 
    A [rendered view](https://scitools.org.uk/signed_cla.html) of the list is also
    available.

The current [CLA bot](https://github.com/SciTools-incubator/scitools-cla-checker) checks for an entry in _either_ the old or the new contributors list.

(C) British Crown Copyright 2010 - 2022, Met Office
