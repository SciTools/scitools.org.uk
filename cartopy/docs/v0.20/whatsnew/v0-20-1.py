import matplotlib.pyplot as plt
import numpy as np
import cartopy.crs as ccrs

fig = plt.figure(figsize=(10, 5))
proj = ccrs.InterruptedGoodeHomolosine(central_longitude=-160,
                                       emphasis='ocean')
ax = plt.axes(projection=proj)
ax.stock_img()

plt.show()