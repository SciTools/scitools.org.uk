import matplotlib.pyplot as plt
import cartopy.crs as ccrs

plt.figure(figsize=(6, 3))
ax = plt.axes(projection=ccrs.PlateCarree(
    central_longitude=180))
ax.coastlines(resolution='110m')
ax.gridlines()