import matplotlib.pyplot as plt
import cartopy.crs as ccrs

plt.figure(figsize=(3, 3))
ax = plt.axes(projection=ccrs.SouthPolarStereo())
ax.coastlines(resolution='110m')
ax.gridlines()