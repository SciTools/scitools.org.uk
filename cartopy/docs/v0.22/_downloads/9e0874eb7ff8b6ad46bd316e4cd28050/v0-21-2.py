import matplotlib.pyplot as plt
import numpy as np
import cartopy.crs as ccrs

map_projection = ccrs.InterruptedGoodeHomolosine()

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(1, 1, 1, projection=map_projection)
ax.set_global()
ax.coastlines()
arrowprops = {'facecolor': 'red',
              'arrowstyle': "-|>",
              'connectionstyle': "arc3,rad=-0.2",
              }
platecarree = ccrs.PlateCarree()
mpltransform = platecarree._as_mpl_transform(ax)

ax.annotate('mpl xycoords', (-45, 43), xycoords=mpltransform,
            size=5)

# Add annotation with xycoords as projection
ax.annotate('crs xycoords', (-75, 13), xycoords=platecarree,
            size=5)

# set up coordinates in map projection space
map_coords = map_projection.transform_point(-175, -35, platecarree)
# Don't specify any args, default xycoords='data', transform=map projection
ax.annotate('default crs', map_coords, size=5)

# data in map projection using default transform, with
# text positioned in platecaree transform
ax.annotate('mixed crs transforms', map_coords, xycoords='data',
            xytext=(-175, -55),
            textcoords=platecarree,
            size=5,
            arrowprops=arrowprops,
            )

# Add annotation with point and text via transform
ax.annotate('crs transform', (-75, -20), xytext=(0, -55),
            transform=platecarree,
            arrowprops=arrowprops,
            )

# Add annotation with point via transform and text non transformed
ax.annotate('offset textcoords', (-149.8, 61.22), transform=platecarree,
            xytext=(-35, 10), textcoords='offset points',
            size=5,
            ha='right',
            arrowprops=arrowprops,
            )

plt.show()