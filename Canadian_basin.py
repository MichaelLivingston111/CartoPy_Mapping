# Import packages
import cartopy
import cartopy.crs as ccrs
import matplotlib.pylab as plt
import numpy as np
import pandas
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.mpl.geoaxes
from shapely.ops import cascaded_union


# Define bounding coordinates
# Define lats/lons for the Northeast Pacific

min_lat = 40
max_lat = 80
min_lon = -177
max_lon = -100

# Map for multivariate linear regression model work:
data = pandas.read_csv("DBO Stations.csv")
data1 = pandas.read_csv("Major_LineP_Stations.csv")
data2 = pandas.read_csv("Cambridge_bay.csv")

# Map: Northeast Pacific, Chuchki sea, and Cambridge bay
fig = plt.figure(figsize=(8, 8))  # Set up the figure:

ax = fig.add_subplot(projection=ccrs.PlateCarree())  # Single plot
# ax.stock_img()  # Optional background image
ax.scatter(data["Station_lon"], data["Station_lat"], s=30, edgecolors='k',
           c="red",
           transform=ccrs.PlateCarree())
ax.scatter(data1["Station_lon"], data1["Station_lat"], s=30, edgecolors='k',
           c="blue",
           transform=ccrs.PlateCarree())
ax.scatter(data2["Station_lon"], data2["Station_lat"], s=30, edgecolors='k',
           c="red",
           transform=ccrs.PlateCarree())
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.LAND, zorder=80, edgecolor='k', facecolor='silver')
ax.add_feature(cfeature.BORDERS)
ax.set_extent([min_lon, max_lon, min_lat, max_lat],
              crs=ccrs.PlateCarree())

