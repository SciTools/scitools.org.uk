import matplotlib.pyplot as plt
import cartopy.crs as ccrs

plt.figure(figsize=(6, 3))
ax = plt.axes(projection=ccrs.RotatedPole(pole_longitude=177.5, pole_latitude=37.5))
ax.coastlines(resolution='110m')
ax.gridlines()