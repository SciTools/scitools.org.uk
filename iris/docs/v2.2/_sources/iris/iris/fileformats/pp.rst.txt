.. _iris.fileformats.pp:

===================
iris.fileformats.pp
===================



.. currentmodule:: iris

.. automodule:: iris.fileformats.pp

In this module:

 * :py:obj:`load`
 * :py:obj:`save`
 * :py:obj:`load_cubes`
 * :py:obj:`PPField`
 * :py:obj:`as_fields`
 * :py:obj:`load_pairs_from_fields`
 * :py:obj:`save_pairs_from_cube`
 * :py:obj:`save_fields`
 * :py:obj:`STASH`
 * :py:obj:`EARTH_RADIUS`



.. autofunction:: iris.fileformats.pp.load


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


.. autofunction:: iris.fileformats.pp.save


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


.. autofunction:: iris.fileformats.pp.load_cubes


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


A generic class for PP fields - not specific to a particular
header release number.

A PPField instance can easily access the PP header "words" as attributes
with some added useful capabilities::

    for field in iris.fileformats.pp.load(filename):
        print(field.lbyr)
        print(field.lbuser)
        print(field.lbuser[0])
        print(field.lbtim)
        print(field.lbtim.ia)
        print(field.t1)

..

    .. autoclass:: iris.fileformats.pp.PPField
        :members:
        :undoc-members:
        :inherited-members:


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


.. autofunction:: iris.fileformats.pp.as_fields


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


.. autofunction:: iris.fileformats.pp.load_pairs_from_fields


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


.. autofunction:: iris.fileformats.pp.save_pairs_from_cube


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


.. autofunction:: iris.fileformats.pp.save_fields


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


A class to hold a single STASH code.

Create instances using:
    >>> model = 1
    >>> section = 2
    >>> item = 3
    >>> my_stash = iris.fileformats.pp.STASH(model, section, item)

Access the sub-components via:
    >>> my_stash.model
    1
    >>> my_stash.section
    2
    >>> my_stash.item
    3

String conversion results in the MSI format:
    >>> print(iris.fileformats.pp.STASH(1, 16, 203))
    m01s16i203

A stash object can be compared directly
to its string representation:
>>> iris.fileformats.pp.STASH(1, 0, 4) == 'm01s0i004'
True

..

    .. autoclass:: iris.fileformats.pp.STASH
        :members:
        :undoc-members:
        :inherited-members:


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->



.. autodata:: iris.fileformats.pp.EARTH_RADIUS

