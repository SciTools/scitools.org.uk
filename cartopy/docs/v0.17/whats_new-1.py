import matplotlib.pyplot as plt
import cartopy.crs as ccrs

eq_earth = ccrs.EqualEarth()
fig = plt.figure(figsize=(10, 5))
ax = plt.axes(projection=eq_earth)
ax.set_global()
ax.gridlines()
ax.stock_img()
ax.coastlines()
plt.show()