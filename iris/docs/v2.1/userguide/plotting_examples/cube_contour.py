
from __future__ import (absolute_import, division, print_function)
from six.moves import (filter, input, map, range, zip)  # noqa

import matplotlib.pyplot as plt

import iris
import iris.quickplot as qplt


fname = iris.sample_data_path('air_temp.pp')
temperature_cube = iris.load_cube(fname)

# Add a contour, and put the result in a variable called contour.
contour = qplt.contour(temperature_cube)

# Add coastlines to the map created by contour.
plt.gca().coastlines()

# Add contour labels based on the contour we have just created.
plt.clabel(contour, inline=False)

plt.show()
