import matplotlib.pyplot as plt
import cartopy.crs as ccrs

fig = plt.figure(figsize=(10, 5))
ax = plt.axes(projection=ccrs.InterruptedGoodeHomolosine())
ax.set_global()
ax.stock_img()
ax.coastlines()
ax.gridlines(draw_labels=True)
plt.show()