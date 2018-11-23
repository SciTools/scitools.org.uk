import matplotlib.pyplot as plt
import cartopy.crs as ccrs

eq_conic = ccrs.EquidistantConic()
fig = plt.figure(figsize=(10, 5))
ax = plt.axes(projection=eq_conic)
ax.set_global()
ax.gridlines()
ax.stock_img()
ax.coastlines()
plt.show()