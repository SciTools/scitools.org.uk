import matplotlib.pyplot as plt
import cartopy.crs as ccrs

plt.figure(figsize=(3, 3))
ax = plt.axes(projection=ccrs.NearsidePerspective(
                        central_latitude=50.72,
                        central_longitude=-3.53,
                        satellite_height=10000000.0))
ax.coastlines(resolution='110m')
ax.gridlines()