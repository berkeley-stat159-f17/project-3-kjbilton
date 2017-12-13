import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from mpl_toolkits.basemap import Basemap
from descartes import PolygonPatch
import shapely

def counts_in_neighborhood(data, category):
    """ Returns the number of occurences for a specific category type in a
        DataFrame.

    Parameters
    ----------
    data : DataFrame
        DataFrame containing service requests.
    category : str
        String corresponding to service request category in DataFrame.
    """
    n_category = (data[data['REQCATEGORY'] == category]
                    .groupby('neighborhood')['REQUESTID'].count())
    n_category.rename(f'N_{category}', inplace=True)

    return n_category

def neighborhood_heat_map(data, col, coords=None, label=None, ax=None,
                          xpixels=2000):
    """
    Plot a heat map on the neighborhoods listed in the data.

    Parameters
    ----------
    data : GeoDataFrame
        GeoDataFrame containing neighborhoods and their associated geometries.
    col : str
        String referring to a column name in data.
    coords : dict, default=None
        Dict with keys llcrnrlon, llcrnrlat, urcrnrlon, and urcrnrlat. If set
        to None, use max/min from 'Longitude'
        and 'Latitude' columns to determine the region.
    ax : matplotlib axis, default=None
        Plot the heat map to an axis ax. If set to None, a new figure and axis
        is created
    xpixels : int
        Resolution of the base map. Increasing this number increases the amount
        of detail contained in the base map.

    Returns
    -------
    Heat map of col overlayed on a satellite image.

    """

    # Create a canvas if an axis isn't provided
    if ax is None:
        fig = plt.figure(figsize=(10,10))
        axis = fig.add_axes([0.,0.,1.,1.])
    else:
        fig = ax.get_figure()
        axis = ax

    if coords is None:
        llcrnrlon = data['Longitude'].min()
        llcrnrlat = data['Latitude'].min()
        urcrnrlon = data['Longitude'].max()
        urcrnrlat = data['Latitude'].max()
    else:
        llcrnrlon=coords['llcrnrlon']
        llcrnrlat=coords['llcrnrlat']
        urcrnrlon=coords['urcrnrlon']
        urcrnrlat=coords['urcrnrlat']

    # Create a map to overlay data on
    bm = Basemap(epsg=3493,
                 llcrnrlon=llcrnrlon,
                 llcrnrlat=llcrnrlat,
                 urcrnrlon=urcrnrlon,
                 urcrnrlat=urcrnrlat,
                 ax=axis)

    bm.arcgisimage(service='ESRI_Imagery_World_2D', xpixels=xpixels)

    # Plot the neighborhood polygons
    patches = []

    for poly in data['geometry']:
        mpoly = shapely.ops.transform(bm, poly)
        patches.append(PolygonPatch(mpoly))

    pc = PatchCollection(patches, match_original=True)

    # Color code these patches based on the time_to_close of that neighborhood
    pc.set_array(data[col].values)
    pc.set_clim([data[col].min(), data[col].max()])


    axis.add_collection(pc)

    # Create a color bar
    cax = fig.add_axes([1.05, 0.1, 0.03, 0.8])
    cbar = fig.colorbar(pc, cax=cax)

    if label is None:
        label = col

    cbar.set_label(label, rotation=270, labelpad=40, fontsize=20)

    if ax is None:
        return fig, axis
