import matplotlib.pyplot as plt
import cartopy.crs as ccrs

fig = plt.figure(figsize=(6.9228, 6))

ax1 = fig.add_subplot(2, 1, 1,
                      projection=ccrs.InterruptedGoodeHomolosine(
                          emphasis='land'))
ax1.coastlines(resolution='110m')
ax1.gridlines()

ax2 = fig.add_subplot(2, 1, 2,
                      projection=ccrs.InterruptedGoodeHomolosine(
                          central_longitude=-160, emphasis='ocean'))
ax2.coastlines(resolution='110m')
ax2.gridlines()