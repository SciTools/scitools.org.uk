.. _iris.time:

=========
iris.time
=========



.. currentmodule:: iris

.. automodule:: iris.time

In this module:

 * :py:obj:`PartialDateTime`



A :class:`PartialDateTime` object specifies values for some subset of
the calendar/time fields (year, month, hour, etc.) for comparing
with :class:`datetime.datetime`-like instances.

Comparisons are defined against any other class with all of the
attributes: year, month, day, hour, minute, and second.
Notably, this includes :class:`datetime.datetime` and
:class:`netcdftime.datetime`. Comparison also extends to the
microsecond attribute for classes, such as
:class:`datetime.datetime`, which define it.

A :class:`PartialDateTime` object is not limited to any particular
calendar, so no restriction is placed on the range of values
allowed in its component fields. Thus, it is perfectly legitimate to
create an instance as: `PartialDateTime(month=2, day=30)`.

..

    .. autoclass:: iris.time.PartialDateTime
        :members:
        :undoc-members:
        :inherited-members:

