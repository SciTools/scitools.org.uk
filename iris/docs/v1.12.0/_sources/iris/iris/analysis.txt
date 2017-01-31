.. _iris.analysis:

=============
iris.analysis
=============


.. sidebar:: Modules in this package


   .. toctree::
      :maxdepth: 2
      :titlesonly:

      analysis/calculus
      analysis/cartography
      analysis/geometry
      analysis/interpolate
      analysis/maths
      analysis/stats
      analysis/trajectory




    

.. currentmodule:: iris

.. automodule:: iris.analysis

In this module:

 * :py:obj:`COUNT`
 * :py:obj:`GMEAN`
 * :py:obj:`HMEAN`
 * :py:obj:`MAX`
 * :py:obj:`MEAN`
 * :py:obj:`MEDIAN`
 * :py:obj:`MIN`
 * :py:obj:`PEAK`
 * :py:obj:`PERCENTILE`
 * :py:obj:`PROPORTION`
 * :py:obj:`RMS`
 * :py:obj:`STD_DEV`
 * :py:obj:`SUM`
 * :py:obj:`VARIANCE`
 * :py:obj:`WPERCENTILE`
 * :py:obj:`coord_comparison`
 * :py:obj:`Aggregator`
 * :py:obj:`WeightedAggregator`
 * :py:obj:`clear_phenomenon_identity`
 * :py:obj:`Linear`
 * :py:obj:`AreaWeighted`
 * :py:obj:`Nearest`
 * :py:obj:`UnstructuredNearest`




.. autodata:: iris.analysis.COUNT


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->



.. autodata:: iris.analysis.GMEAN


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->



.. autodata:: iris.analysis.HMEAN


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->



.. autodata:: iris.analysis.MAX


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->



.. autodata:: iris.analysis.MEAN


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->



.. autodata:: iris.analysis.MEDIAN


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->



.. autodata:: iris.analysis.MIN


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->



.. autodata:: iris.analysis.PEAK


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->



.. autodata:: iris.analysis.PERCENTILE


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->



.. autodata:: iris.analysis.PROPORTION


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->



.. autodata:: iris.analysis.RMS


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->



.. autodata:: iris.analysis.STD_DEV


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->



.. autodata:: iris.analysis.SUM


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->



.. autodata:: iris.analysis.VARIANCE


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->



.. autodata:: iris.analysis.WPERCENTILE


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


.. autofunction:: iris.analysis.coord_comparison


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


The :class:`Aggregator` class provides common aggregation functionality.

..

    .. autoclass:: iris.analysis.Aggregator
        :members:
        :undoc-members:
        :inherited-members:


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


Convenience class that supports common weighted aggregation functionality.

..

    .. autoclass:: iris.analysis.WeightedAggregator
        :members:
        :undoc-members:
        :inherited-members:


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


.. autofunction:: iris.analysis.clear_phenomenon_identity


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


This class describes the linear interpolation and regridding scheme for
interpolating or regridding over one or more orthogonal coordinates,
typically for use with :meth:`iris.cube.Cube.interpolate()` or
:meth:`iris.cube.Cube.regrid()`.

..

    .. autoclass:: iris.analysis.Linear
        :members:
        :undoc-members:
        :inherited-members:


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


This class describes an area-weighted regridding scheme for regridding
between 'ordinary' horizontal grids with separated X and Y coordinates in a
common coordinate system.
Typically for use with :meth:`iris.cube.Cube.regrid()`.

..

    .. autoclass:: iris.analysis.AreaWeighted
        :members:
        :undoc-members:
        :inherited-members:


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


This class describes the nearest-neighbour interpolation and regridding
scheme for interpolating or regridding over one or more orthogonal
coordinates, typically for use with :meth:`iris.cube.Cube.interpolate()`
or :meth:`iris.cube.Cube.regrid()`.

..

    .. autoclass:: iris.analysis.Nearest
        :members:
        :undoc-members:
        :inherited-members:


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


This is a nearest-neighbour regridding scheme for regridding data whose
horizontal (X- and Y-axis) coordinates are mapped to the *same* dimensions,
rather than being orthogonal on independent dimensions.

For latitude-longitude coordinates, the nearest-neighbour distances are
computed on the sphere, otherwise flat Euclidean distances are used.

The source X and Y coordinates can have any shape.

The target grid must be of the "normal" kind, i.e. it has separate,
1-dimensional X and Y coordinates.

Source and target XY coordinates must have the same coordinate system,
which may also be None.
If any of the XY coordinates are latitudes or longitudes, then they *all*
must be.  Otherwise, the corresponding X and Y coordinates must have the
same units in the source and grid cubes.

.. Note::
    Currently only supports regridding, not interpolation.

.. Note::
      This scheme performs essentially the same job as
      :class:`iris.experimental.regrid.ProjectedUnstructuredNearest`.
      That scheme is faster, but only works well on data in a limited
      region of the globe, covered by a specified projection.
      This approach is more rigorously correct and can be applied to global
      datasets.

..

    .. autoclass:: iris.analysis.UnstructuredNearest
        :members:
        :undoc-members:
        :inherited-members:

