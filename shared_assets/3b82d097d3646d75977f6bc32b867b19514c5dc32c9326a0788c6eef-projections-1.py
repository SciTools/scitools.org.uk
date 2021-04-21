import matplotlib.pyplot as plt
import cartopy.crs as ccrs

nplots = 2

fig = plt.figure(figsize=(6, 6))

for i in range(0, nplots):
    central_longitude = 0 if i == 0 else 180
    ax = fig.add_subplot(
        nplots, 1, i+1,
        projection=ccrs.PlateCarree(central_longitude=central_longitude))
    ax.coastlines(resolution='110m')
    ax.gridlines()