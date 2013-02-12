import matplotlib.cm as mpl_cm
import matplotlib.pyplot as plt

import iris
import iris.quickplot as qplt


fname = iris.sample_data_path('air_temp.pp')
temperature_cube = iris.load_cube(fname)

# Load a Cynthia Brewer palette.
brewer_cmap = mpl_cm.get_cmap('brewer_RdBu_11')

# Draw the contour with 25 levels.
qplt.contourf(temperature_cube, 25, cmap=brewer_cmap)

# Add coastlines to the map created by contourf.
plt.gca().coastlines()

plt.show()
