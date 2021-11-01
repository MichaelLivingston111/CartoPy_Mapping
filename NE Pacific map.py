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
max_lat = 55
min_lon = -151
max_lon = -122

# Map for multivariate linear regression model work:
data = pandas.read_csv("Lats_lons.csv")

# Map
fig = plt.figure(figsize=(8, 8))  # Set up the figure:

ax = fig.add_subplot(projection=ccrs.PlateCarree())  # Single plot
# ax.stock_img()  # Optional background image
ax.scatter(data["Station_lon"], data["Station_lat"], s=30, edgecolors='k',
           c="red",
           transform=ccrs.PlateCarree())
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.LAND, zorder=80, edgecolor='k', facecolor='silver')
ax.add_feature(cfeature.BORDERS)

bathym = cfeature.NaturalEarthFeature(name='bathymetry_J_1000', scale='10m', category='physical')
bathym = cascaded_union(list(bathym.geometries()))  # different geometries within the shapefile - need to do a union
# on the two shapes to combine them into a single one

ax.add_geometries(bathym, facecolor='none', edgecolor='black', linestyle='dashed', linewidth=1, crs=ccrs.PlateCarree())
ax.set_extent([min_lon, max_lon, min_lat, max_lat],
              crs=ccrs.PlateCarree())

