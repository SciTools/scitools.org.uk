import matplotlib.pyplot as plt
import cartopy.crs as ccrs

rpole = ccrs.RotatedPole(pole_longitude=171.77,
                         pole_latitude=49.55,
                         central_rotated_longitude=180)
ax = plt.axes(projection=rpole)
ax.set_global()
ax.gridlines()
ax.stock_img()
ax.coastlines()
plt.show()