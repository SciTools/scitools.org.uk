import matplotlib.pyplot as plt
import cartopy.crs as ccrs

plt.figure(figsize=(0.1286, 3))
ax = plt.axes(projection=ccrs.UTM(
    zone=30))
ax.coastlines(resolution='110m')
ax.gridlines()