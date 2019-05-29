.. _iris.fileformats.um:

===================
iris.fileformats.um
===================


.. sidebar:: Modules in this package


   .. toctree::
      :maxdepth: 2
      :titlesonly:

      




    

.. currentmodule:: iris

.. automodule:: iris.fileformats.um

In this module:

 * :py:obj:`um_to_pp`
 * :py:obj:`load_cubes`
 * :py:obj:`load_cubes_32bit_ieee`
 * :py:obj:`structured_um_loading`
 * :py:obj:`FieldCollation`



.. autofunction:: iris.fileformats.um.um_to_pp


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


.. autofunction:: iris.fileformats.um.load_cubes


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


.. autofunction:: iris.fileformats.um.load_cubes_32bit_ieee


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


.. autofunction:: iris.fileformats.um.structured_um_loading


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


An object representing a group of UM fields with array structure that can
be vectorized into a single cube.

For example:

Suppose we have a set of 28 fields repeating over 7 vertical levels for
each of 4 different data times.  If a FieldCollation is created to contain
these, it can identify that this is a 4*7 regular array structure.

This FieldCollation will then have the following properties:

* within 'element_arrays_and_dims' :
    Element 'blev' have the array shape (7,) and dims of (1,).
    Elements 't1' and 't2' have shape (4,) and dims (0,).
    The other elements (lbft, lbrsvd4 and lbuser5) all have scalar array
    values and dims=None.

.. note::

    If no array structure is found, the element values are all
    either scalar or full-length 1-D vectors.

..

    .. autoclass:: iris.fileformats.um.FieldCollation
        :members:
        :undoc-members:
        :inherited-members:

