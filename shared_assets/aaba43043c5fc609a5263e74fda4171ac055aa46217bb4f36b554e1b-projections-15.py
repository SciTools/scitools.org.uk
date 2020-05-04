import matplotlib.pyplot as plt
import cartopy.crs as ccrs

nplots = 60

fig = plt.figure(figsize=(10, 3))

for i in range(0, nplots):
    ax = fig.add_subplot(1, nplots, i+1,
                         projection=ccrs.UTM(zone=i+1,
                                             southern_hemisphere=True))
    ax.coastlines(resolution='110m')
    ax.gridlines()