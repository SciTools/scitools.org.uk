.. _iris.aux_factory:

================
iris.aux_factory
================



.. currentmodule:: iris

.. automodule:: iris.aux_factory

In this module:

 * :py:obj:`AuxCoordFactory`
 * :py:obj:`HybridHeightFactory`
 * :py:obj:`HybridPressureFactory`
 * :py:obj:`OceanSFactory`
 * :py:obj:`OceanSg1Factory`
 * :py:obj:`OceanSg2Factory`
 * :py:obj:`OceanSigmaFactory`
 * :py:obj:`OceanSigmaZFactory`



Represents a "factory" which can manufacture an additional auxiliary
coordinate on demand, by combining the values of other coordinates.

Each concrete subclass represents a specific formula for deriving
values from other coordinates.

The `standard_name`, `long_name`, `var_name`, `units`, `attributes` and
`coord_system` of the factory are used to set the corresponding
properties of the resulting auxiliary coordinates.

..

    .. autoclass:: iris.aux_factory.AuxCoordFactory
        :members:
        :undoc-members:
        :inherited-members:


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


Defines a hybrid-height coordinate factory with the formula:
    z = a + b * orog

..

    .. autoclass:: iris.aux_factory.HybridHeightFactory
        :members:
        :undoc-members:
        :inherited-members:


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


Defines a hybrid-pressure coordinate factory with the formula:
    p = ap + b * ps

..

    .. autoclass:: iris.aux_factory.HybridPressureFactory
        :members:
        :undoc-members:
        :inherited-members:


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


Defines an Ocean s-coordinate factory.

..

    .. autoclass:: iris.aux_factory.OceanSFactory
        :members:
        :undoc-members:
        :inherited-members:


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


Defines an Ocean s-coordinate, generic form 1 factory.

..

    .. autoclass:: iris.aux_factory.OceanSg1Factory
        :members:
        :undoc-members:
        :inherited-members:


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


Defines an Ocean s-coordinate, generic form 2 factory.

..

    .. autoclass:: iris.aux_factory.OceanSg2Factory
        :members:
        :undoc-members:
        :inherited-members:


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


Defines an ocean sigma coordinate factory.

..

    .. autoclass:: iris.aux_factory.OceanSigmaFactory
        :members:
        :undoc-members:
        :inherited-members:


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


Defines an ocean sigma over z coordinate factory.

..

    .. autoclass:: iris.aux_factory.OceanSigmaZFactory
        :members:
        :undoc-members:
        :inherited-members:

