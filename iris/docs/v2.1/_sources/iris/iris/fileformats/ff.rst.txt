.. _iris.fileformats.ff:

===================
iris.fileformats.ff
===================



.. currentmodule:: iris

.. automodule:: iris.fileformats.ff

In this module:

 * :py:obj:`load_cubes`
 * :py:obj:`load_cubes_32bit_ieee`
 * :py:obj:`FF2PP`
 * :py:obj:`Grid`
 * :py:obj:`ArakawaC`
 * :py:obj:`NewDynamics`
 * :py:obj:`ENDGame`
 * :py:obj:`FFHeader`



.. autofunction:: iris.fileformats.ff.load_cubes


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


.. autofunction:: iris.fileformats.ff.load_cubes_32bit_ieee


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


A class to extract the individual PPFields from within a FieldsFile.

.. deprecated:: 1.10
    The module :mod:`iris.fileformats.ff` is deprecated.

..

    .. autoclass:: iris.fileformats.ff.FF2PP
        :members:
        :undoc-members:
        :inherited-members:


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


An abstract class representing the default/file-level grid
definition for a FieldsFile.

.. deprecated:: 1.10
    The module :mod:`iris.fileformats.ff` is deprecated.

..

    .. autoclass:: iris.fileformats.ff.Grid
        :members:
        :undoc-members:
        :inherited-members:


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


An abstract class representing an Arakawa C-grid.

.. deprecated:: 1.10
    The module :mod:`iris.fileformats.ff` is deprecated.

..

    .. autoclass:: iris.fileformats.ff.ArakawaC
        :members:
        :undoc-members:
        :inherited-members:


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


An Arakawa C-grid as used by UM New Dynamics.

The theta and u points are at the poles.

.. deprecated:: 1.10
    The module :mod:`iris.fileformats.ff` is deprecated.

..

    .. autoclass:: iris.fileformats.ff.NewDynamics
        :members:
        :undoc-members:
        :inherited-members:


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


An Arakawa C-grid as used by UM ENDGame.

The v points are at the poles.

.. deprecated:: 1.10
    The module :mod:`iris.fileformats.ff` is deprecated.

..

    .. autoclass:: iris.fileformats.ff.ENDGame
        :members:
        :undoc-members:
        :inherited-members:


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


A class to represent the FIXED_LENGTH_HEADER section of a FieldsFile.

.. deprecated:: 1.10
    The module :mod:`iris.fileformats.ff` is deprecated.

..

    .. autoclass:: iris.fileformats.ff.FFHeader
        :members:
        :undoc-members:
        :inherited-members:

