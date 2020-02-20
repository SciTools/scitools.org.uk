.. _Oceanography-load_nemo:


Load a time series of data from the NEMO model
==============================================

This example demonstrates how to load multiple files containing data output by
the NEMO model and combine them into a time series in a single cube. The
different time dimensions in these files can prevent Iris from concatenating
them without the intervention shown here.


.. plot:: examples/Oceanography/load_nemo.py
    :include-source:

