.. _iris.experimental.um:

====================
iris.experimental.um
====================



.. currentmodule:: iris

.. automodule:: iris.experimental.um

In this module:

 * :py:obj:`Field`
 * :py:obj:`Field2`
 * :py:obj:`Field3`
 * :py:obj:`FieldsFileVariant`
 * :py:obj:`FixedLengthHeader`



Represents a single entry in the LOOKUP component and its
corresponding section of the DATA component.

..

    .. autoclass:: iris.experimental.um.Field
        :members:
        :undoc-members:
        :inherited-members:


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


Represents an entry from the LOOKUP component with a header release
number of 2.

..

    .. autoclass:: iris.experimental.um.Field2
        :members:
        :undoc-members:
        :inherited-members:


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


Represents an entry from the LOOKUP component with a header release
number of 3.

..

    .. autoclass:: iris.experimental.um.Field3
        :members:
        :undoc-members:
        :inherited-members:


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


Represents a single a file containing UM FieldsFile variant data.

..

    .. autoclass:: iris.experimental.um.FieldsFileVariant
        :members:
        :undoc-members:
        :inherited-members:


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


Represents the FIXED_LENGTH_HEADER component of a UM FieldsFile
variant.

Access to simple header items is provided via named attributes,
e.g. fixed_length_header.sub_model. Other header items can be
accessed via the :attr:`raw` attribute which provides a simple array
view of the header.

..

    .. autoclass:: iris.experimental.um.FixedLengthHeader
        :members:
        :undoc-members:
        :inherited-members:

