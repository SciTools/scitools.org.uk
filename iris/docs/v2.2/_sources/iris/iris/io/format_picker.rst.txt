.. _iris.io.format_picker:

=====================
iris.io.format_picker
=====================



.. currentmodule:: iris

.. automodule:: iris.io.format_picker

In this module:

 * :py:obj:`FileElement`
 * :py:obj:`FileExtension`
 * :py:obj:`FormatAgent`
 * :py:obj:`FormatSpecification`
 * :py:obj:`LeadingLine`
 * :py:obj:`MagicNumber`
 * :py:obj:`UriProtocol`



Represents a specific aspect of a FileFormat which can be identified using the given element getter function.

..

    .. autoclass:: iris.io.format_picker.FileElement
        :members:
        :undoc-members:
        :inherited-members:


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


A :class:`FileElement` that returns the extension from the filename.

..

    .. autoclass:: iris.io.format_picker.FileExtension
        :members:
        :undoc-members:
        :inherited-members:


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


The FormatAgent class is the containing object which is responsible for identifying the format of a given file
by interrogating its children FormatSpecification instances.

Typically a FormatAgent will be created empty and then extended with the :meth:`FormatAgent.add_spec` method::

    agent = FormatAgent()
    agent.add_spec(NetCDF_specification)

Less commonly, this can also be written::

    agent = FormatAgent(NetCDF_specification)

..

    .. autoclass:: iris.io.format_picker.FormatAgent
        :members:
        :undoc-members:
        :inherited-members:


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


Provides the base class for file type definition.

Every FormatSpecification instance has a name which can be accessed with the :attr:`FormatSpecification.name` property and
a FileElement, such as filename extension or 32-bit magic number, with an associated value for format identification.

..

    .. autoclass:: iris.io.format_picker.FormatSpecification
        :members:
        :undoc-members:
        :inherited-members:


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


A :class:`FileElement` that returns the first line from the file.

..

    .. autoclass:: iris.io.format_picker.LeadingLine
        :members:
        :undoc-members:
        :inherited-members:


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


A :class:`FileElement` that returns a byte sequence in the file.

..

    .. autoclass:: iris.io.format_picker.MagicNumber
        :members:
        :undoc-members:
        :inherited-members:


.. raw:: html

    <p class="hr_p"><a href="#">&uarr;&#32&#32 top &#32&#32&uarr;</a></p>
    <!--

-----------

.. raw:: html

    -->


A :class:`FileElement` that returns the "scheme" and "part" from a URI,
using :func:`~iris.io.decode_uri`.

..

    .. autoclass:: iris.io.format_picker.UriProtocol
        :members:
        :undoc-members:
        :inherited-members:

