.. _iris.analysis.trajectory:

========================
iris.analysis.trajectory
========================



.. currentmodule:: iris

.. automodule:: iris.analysis.trajectory

In this module:

 * :py:obj:`interpolate`
 * :py:obj:`Trajectory`
 * :py:obj:`UnstructuredNearestNeigbourRegridder`



.. autofunction:: iris.analysis.trajectory.interpolate


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


A series of given waypoints with pre-calculated sample points.

..

    .. autoclass:: iris.analysis.trajectory.Trajectory
        :members:
        :undoc-members:
        :inherited-members:


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


Encapsulate the operation of :meth:`iris.analysis.trajectory.interpolate`
with given source and target grids.

This is the type used by the :class:`~iris.analysis.UnstructuredNearest`
regridding scheme.

..

    .. autoclass:: iris.analysis.trajectory.UnstructuredNearestNeigbourRegridder
        :members:
        :undoc-members:
        :inherited-members:

