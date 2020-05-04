import matplotlib.pyplot as plt
import cartopy.crs as ccrs

rotated_crs = ccrs.RotatedPole(pole_longitude=120.0, pole_latitude=70.0)

ax = plt.axes(projection=rotated_crs)
ax.set_extent([-6, 3, 48, 58], crs=ccrs.PlateCarree())
ax.coastlines(resolution='50m')
ax.gridlines(draw_labels=True, dms=True, x_inline=False, y_inline=False)

plt.show()