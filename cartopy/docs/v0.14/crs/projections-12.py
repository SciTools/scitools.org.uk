import matplotlib.pyplot as plt
import cartopy.crs as ccrs

plt.figure(figsize=(6.0100710855457855, 3))
ax = plt.axes(projection=ccrs.Sinusoidal())
ax.coastlines(resolution='110m')
ax.gridlines()