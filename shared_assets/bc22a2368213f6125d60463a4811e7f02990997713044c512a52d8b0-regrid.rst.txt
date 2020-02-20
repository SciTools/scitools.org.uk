.. _iris.experimental.regrid:

========================
iris.experimental.regrid
========================



.. currentmodule:: iris

.. automodule:: iris.experimental.regrid

In this module:

 * :py:obj:`regrid_area_weighted_rectilinear_src_and_grid`
 * :py:obj:`regrid_weighted_curvilinear_to_rectilinear`
 * :py:obj:`PointInCell`
 * :py:obj:`ProjectedUnstructuredLinear`
 * :py:obj:`ProjectedUnstructuredNearest`



.. autofunction:: iris.experimental.regrid.regrid_area_weighted_rectilinear_src_and_grid


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


.. autofunction:: iris.experimental.regrid.regrid_weighted_curvilinear_to_rectilinear


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


This class describes the point-in-cell regridding scheme for use
typically with :meth:`iris.cube.Cube.regrid()`.

.. warning::

    This class is now **disabled**.

    The functionality has been moved to
    :class:`iris.analysis.PointInCell`.

..

    .. autoclass:: iris.experimental.regrid.PointInCell
        :members:
        :undoc-members:
        :inherited-members:


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


This class describes the linear regridding scheme which uses the
scipy.interpolate.griddata to regrid unstructured data on to a grid.

The source cube and the target cube will be projected into a common
projection for the scipy calculation to be performed.

..

    .. autoclass:: iris.experimental.regrid.ProjectedUnstructuredLinear
        :members:
        :undoc-members:
        :inherited-members:


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


This class describes the nearest regridding scheme which uses the
scipy.interpolate.griddata to regrid unstructured data on to a grid.

The source cube and the target cube will be projected into a common
projection for the scipy calculation to be performed.

.. Note::
      The :class:`iris.analysis.UnstructuredNearest` scheme performs
      essentially the same job.  That calculation is more rigorously
      correct and may be applied to larger data regions (including global).
      This one however, where applicable, is substantially faster.

..

    .. autoclass:: iris.experimental.regrid.ProjectedUnstructuredNearest
        :members:
        :undoc-members:
        :inherited-members:

