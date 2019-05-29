.. _iris.fileformats.rules:

======================
iris.fileformats.rules
======================



.. currentmodule:: iris

.. automodule:: iris.fileformats.rules

In this module:

 * :py:obj:`aux_factory`
 * :py:obj:`has_aux_factory`
 * :py:obj:`load_cubes`
 * :py:obj:`load_pairs_from_fields`
 * :py:obj:`scalar_cell_method`
 * :py:obj:`scalar_coord`
 * :py:obj:`vector_coord`
 * :py:obj:`ConcreteReferenceTarget`
 * :py:obj:`ConversionMetadata`
 * :py:obj:`Factory`
 * :py:obj:`Loader`
 * :py:obj:`Reference`
 * :py:obj:`ReferenceTarget`



.. autofunction:: iris.fileformats.rules.aux_factory


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


.. autofunction:: iris.fileformats.rules.has_aux_factory


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


.. autofunction:: iris.fileformats.rules.load_cubes


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


.. autofunction:: iris.fileformats.rules.load_pairs_from_fields


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


.. autofunction:: iris.fileformats.rules.scalar_cell_method


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


.. autofunction:: iris.fileformats.rules.scalar_coord


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


.. autofunction:: iris.fileformats.rules.vector_coord


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


Everything you need to make a real Cube for a named reference.

..

    .. autoclass:: iris.fileformats.rules.ConcreteReferenceTarget
        :members:
        :undoc-members:
        :inherited-members:


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


ConversionMetadata(factories, references, standard_name, long_name, units, attributes, cell_methods, dim_coords_and_dims, aux_coords_and_dims)

..

    .. autoclass:: iris.fileformats.rules.ConversionMetadata
        :members:
        :undoc-members:
        :inherited-members:


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


Factory(factory_class, args)

..

    .. autoclass:: iris.fileformats.rules.Factory
        :members:
        :undoc-members:
        :inherited-members:


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


Loader(field_generator, field_generator_kwargs, converter)

..

    .. autoclass:: iris.fileformats.rules.Loader
        :members:
        :undoc-members:
        :inherited-members:


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


Convenience class for creating "immutable", hashable, and ordered classes.

Instance identity is defined by the specific list of attribute names
declared in the abstract attribute "_names". Subclasses must declare the
attribute "_names" as an iterable containing the names of all the
attributes relevant to equality/hash-value/ordering.

Initial values should be set by using ::
    self._init(self, value1, value2, ..)

.. note::

    It's the responsibility of the subclass to ensure that the values of
    its attributes are themselves hashable.

..

    .. autoclass:: iris.fileformats.rules.Reference
        :members:
        :undoc-members:
        :inherited-members:


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


ReferenceTarget(name, transform)

..

    .. autoclass:: iris.fileformats.rules.ReferenceTarget
        :members:
        :undoc-members:
        :inherited-members:

