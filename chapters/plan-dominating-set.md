{% highlight python %}
>>> import tqdm
>>> import requests
>>> import networkx as nx
{% endhighlight %}

# Get data

{% highlight python %}
>>> cities_france = sorted([
...     'Amiens', 'Avignon', 'Biarritz', 'Bordeaux', 'Brest', 'Caen', 'Calais', 'Dijon',
...     'Grenoble', 'La Rochelle', 'Le Havre', 'Le Mans', 'Lille', 'Limoges',
...     'Lyon', 'Marseilles', 'Montpellier', 'Nancy', 'Nantes', 'Nice',
...     'Orleans', 'Paris', 'Perpignon', 'Poitiers', 'Reims', 'Rennes',
...     'Rouen', 'Stranbourg', 'Toulon', 'Toulouse'
... ])

{% endhighlight %}

{% highlight python %}
>>> cities_italy = sorted([
...     'Rome', 'Milan', 'Florence', 'Verona', 'Venice', 'Salerno', 'Lecce', 'Bari', 'Pisa', 'Ravenna', 'Genoa', 'Bologna', 'Treviso', 'Catanzaro'
... ])
{% endhighlight %}

{% highlight python %}
>>> cities_usa = sorted([
...     'Albuquerque', 'New York', 'Los Angeles', 'Denver', 'Dallas', 'Houston', 'Atlanta', 'Orlando',
...     'Miami', 'Chicago', 'Seattle', 'Minneapolis', 'San Francisco', 'Nashville', 'Memphis', 'Baltimore',
...     'Philadelphia', 'Boston', 'Salt Lake City', 'Phoenix', 'New Orleans', 'El Paso', 'San Antonio',
...     'Cleveland', 'Las Vegas', 'Cincinnati', 'Washington D.C.', 'Auston', 'Oklahoma City', 'Detroit',
...     'Santa Fe', 'Colorado Springs', 'Portland', 'Jacksonville', 'Charlotte', 'Des Moines', 'Richmond',
...     'Buffalo', 'Tucson', 'St Louis'
... ])
{% endhighlight %}

{% highlight python %}
>>> google_maps_key = 'AIzaSyBaXoQi3SpN_ZMtX7HwPGOSyCEUDjM5ukM'

>>> def get_distance(origin, destination):
...     response = requests.get('https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=' + origin + '&destinations=' + destination + '&key=' + google_maps_key)
...     return float(response.json()['rows'][0]['elements'][0]['distance']['text'].split(' ')[0].replace(',', ''))
{% endhighlight %}

{% highlight python %}
>>> def get_location(loc):
...     location = loc.replace(' ', '+')
...     r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + location + '&key=' + google_maps_key)
...     lat = r.json()['results'][0]['geometry']['location']['lat']
...     lng = r.json()['results'][0]['geometry']['location']['lng']
...     return (lat, lng)
{% endhighlight %}

{% highlight python %}
>>> locations_france = []
>>> for loc in tqdm.tqdm_notebook(cities_france):
...     locations_france.append(get_location(loc))
{% endhighlight %}

{% highlight python %}
>>> locations_italy = []
>>> for loc in tqdm.tqdm_notebook(cities_italy):
...     locations_italy.append(get_location(loc))
{% endhighlight %}

{% highlight python %}
>>> locations_usa = []
>>> for loc in tqdm.tqdm_notebook(cities_usa):
...     locations_usa.append(get_location(loc))
{% endhighlight %}

{% highlight python %}
>>> distances_france = []
>>> for origin in tqdm.tqdm_notebook(cities_france):
...     distances_france.append([])
...     for destination in tqdm.tqdm_notebook(cities_france, leave=None):
...         distances_france[-1].append(get_distance(origin, destination))
{% endhighlight %}

{% highlight python %}
>>> distances_italy = []
>>> for origin in tqdm.tqdm_notebook(cities_italy):
...     distances_italy.append([])
...     for destination in tqdm.tqdm_notebook(cities_italy, leave=None):
...         distances_italy[-1].append(get_distance(origin, destination))
{% endhighlight %}

{% highlight python %}
>>> distances_usa = []
>>> for origin in tqdm.tqdm_notebook(cities_usa):
...     distances_usa.append([])
...     for destination in tqdm.tqdm_notebook(cities_usa, leave=None):
...         distances_usa[-1].append(get_distance(origin, destination))
{% endhighlight %}

# Get Networks

{% highlight python %}
>>> import numpy as np
{% endhighlight %}

{% highlight python %}
>>> all_dists_fr = sorted(list(set([d for row in distances_france for d in row])))
>>> all_dists_it = sorted(list(set([d for row in distances_italy for d in row])))
>>> all_dists_us = sorted(list(set([d for row in distances_usa for d in row])))
{% endhighlight %}

{% highlight python %}
>>> for cutoff in all_dists_fr:
...     D = [[1 if d < cutoff else 0 for d in row] for row in distances_france]
...     G = nx.from_numpy_matrix(np.matrix(D))
...     l = nx.number_connected_components(G)
...     if l == 1:
...         print(cutoff)
...         break
152.0

{% endhighlight %}

{% highlight python %}
>>> for cutoff in all_dists_it:
...     D = [[1 if d < cutoff else 0 for d in row] for row in distances_italy]
...     G = nx.from_numpy_matrix(np.matrix(D))
...     l = nx.number_connected_components(G)
...     if l == 1:
...         print(cutoff)
...         break
218.0

{% endhighlight %}

{% highlight python %}
>>> for cutoff in all_dists_us:
...     D = [[1 if d < cutoff else 0 for d in row] for row in distances_usa]
...     G = nx.from_numpy_matrix(np.matrix(D))
...     l = nx.number_connected_components(G)
...     if l == 1:
...         print(cutoff)
...         break
635.0

{% endhighlight %}

{% highlight python %}
>>> D_fr = [[1 if d < 160 else 0 for d in row] for row in distances_france]
>>> G_fr = nx.from_numpy_matrix(np.matrix(D_fr))
{% endhighlight %}

{% highlight python %}
>>> D_it = [[1 if d < 300 else 0 for d in row] for row in distances_italy]
>>> G_it = nx.from_numpy_matrix(np.matrix(D_it))
{% endhighlight %}

{% highlight python %}
>>> D_us = [[1 if d < 700 else 0 for d in row] for row in distances_usa]
>>> G_us = nx.from_numpy_matrix(np.matrix(D_us))
{% endhighlight %}

# Plot

{% highlight python %}
>>> import geopandas as gpd
>>> import matplotlib.pyplot as plt
>>> %matplotlib inline
{% endhighlight %}

{% highlight python %}
>>> world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
{% endhighlight %}

{% highlight python %}
>>> fig, ax = plt.subplots(1)
>>> world[world['name']=='France'].plot(ax=ax, linewidth=2, edgecolor='black', color='lawngreen', alpha=0.35)
>>> ax.set_xlim(-6, 10)
>>> ax.set_ylim(41, 52)
>>> xs = [r[1] for r in locations_france]
>>> ys = [r[0] for r in locations_france]
>>> nx.draw_networkx(G_fr, pos=[(r[1], r[0]) for r in locations_france], with_labels=False, node_size=30, node_color='midnightblue', edge_color='darkgreen', ax=ax)
>>> ax.get_xaxis().set_visible(False)
>>> ax.get_yaxis().set_visible(False)
>>> plt.savefig('../../assets/france_map.pdf')
<matplotlib.figure.Figure at 0x1181c8390>
{% endhighlight %}

{% highlight python %}
>>> fig, ax = plt.subplots(1)
>>> world[world['name']=='Italy'].plot(ax=ax, linewidth=2, edgecolor='black', color='lawngreen', alpha=0.35)
>>> ax.set_xlim(3, 22)
>>> ax.set_ylim(36, 48)
>>> xs = [r[1] for r in locations_italy]
>>> ys = [r[0] for r in locations_italy]
>>> nx.draw_networkx(G_it, pos=[(r[1], r[0]) for r in locations_italy], with_labels=False, node_size=30, node_color='midnightblue', edge_color='darkgreen', ax=ax)
>>> ax.get_xaxis().set_visible(False)
>>> ax.get_yaxis().set_visible(False)
>>> plt.savefig('../../assets/italy_map.pdf')
<matplotlib.figure.Figure at 0x11b161048>
{% endhighlight %}

{% highlight python %}
>>> fig, ax = plt.subplots(1)
>>> world[world['name']=='United States'].plot(ax=ax, linewidth=2, edgecolor='black', color='lawngreen', alpha=0.35)
>>> ax.set_xlim(-130, -65)
>>> ax.set_ylim(22, 53)
>>> xs = [r[1] for r in locations_usa]
>>> ys = [r[0] for r in locations_usa]
>>> ax.get_xaxis().set_visible(False)
>>> ax.get_yaxis().set_visible(False)
>>> nx.draw_networkx(G_us, pos=[(r[1], r[0]) for r in locations_usa], with_labels=False, node_size=30, node_color='midnightblue', edge_color='darkgreen', ax=ax)
>>> plt.savefig('../../assets/usa_map.pdf')
<matplotlib.figure.Figure at 0x101ff5748>
{% endhighlight %}

# Solving

{% highlight python %}
>>> dominating_fr = list(nx.dominating_set(G_fr))
>>> for c in dominating_fr:
...     print(cities_france[c])
Amiens
Avignon
Biarritz
Brest
Dijon
La Rochelle
Le Mans
Nice
Stranbourg
Toulouse

{% endhighlight %}

{% highlight python %}
>>> fig, ax = plt.subplots(1)
>>> world[world['name']=='France'].plot(ax=ax, linewidth=2, edgecolor='black', color='lawngreen', alpha=0.35)
>>> ax.set_xlim(-6, 10)
>>> ax.set_ylim(41, 52)
>>> xs = [r[1] for r in locations_france]
>>> ys = [r[0] for r in locations_france]
>>> nx.draw_networkx(G_fr, pos=[(r[1], r[0]) for r in locations_france], with_labels=False, node_size=30, node_color='midnightblue', edge_color='darkgreen', ax=ax, alpha=0.25)
>>> ax.scatter([locations_france[c][1] for c in dominating_fr], [locations_france[c][0] for c in dominating_fr], c='midnightblue', zorder=10, s=70)
>>> ax.get_xaxis().set_visible(False)
>>> ax.get_yaxis().set_visible(False)
>>> plt.savefig('../../assets/france_map_sol.pdf')
<matplotlib.figure.Figure at 0x11b14d978>
{% endhighlight %}

{% highlight python %}
>>> dominating_it = list(nx.dominating_set(G_it))
>>> for c in dominating_it:
...     print(cities_italy[c])
Bari
Bologna

{% endhighlight %}

{% highlight python %}
>>> fig, ax = plt.subplots(1)
>>> world[world['name']=='Italy'].plot(ax=ax, linewidth=2, edgecolor='black', color='lawngreen', alpha=0.35)
>>> ax.set_xlim(3, 22)
>>> ax.set_ylim(36, 48)
>>> xs = [r[1] for r in locations_italy]
>>> ys = [r[0] for r in locations_italy]
>>> nx.draw_networkx(G_it, pos=[(r[1], r[0]) for r in locations_italy], with_labels=False, node_size=30, node_color='midnightblue', edge_color='darkgreen', ax=ax, alpha=0.25)
>>> ax.scatter([locations_italy[c][1] for c in dominating_it], [locations_italy[c][0] for c in dominating_it], c='midnightblue', zorder=10, s=70)
>>> ax.get_xaxis().set_visible(False)
>>> ax.get_yaxis().set_visible(False)
>>> plt.savefig('../../assets/italy_map_sol.pdf')
<matplotlib.figure.Figure at 0x11b52c240>
{% endhighlight %}

{% highlight python %}
>>> dominating_us = list(nx.dominating_set(G_us))
>>> for c in dominating_us:
...     print(cities_usa[c])
Albuquerque
Atlanta
Boston
Seattle
Chicago
Houston
Los Angeles

{% endhighlight %}

{% highlight python %}
>>> fig, ax = plt.subplots(1)
>>> world[world['name']=='United States'].plot(ax=ax, linewidth=2, edgecolor='black', color='lawngreen', alpha=0.35)
>>> ax.set_xlim(-130, -65)
>>> ax.set_ylim(22, 53)
>>> xs = [r[1] for r in locations_usa]
>>> ys = [r[0] for r in locations_usa]
>>> ax.get_xaxis().set_visible(False)
>>> ax.get_yaxis().set_visible(False)
>>> nx.draw_networkx(G_us, pos=[(r[1], r[0]) for r in locations_usa], with_labels=False, node_size=30, node_color='midnightblue', edge_color='darkgreen', ax=ax, alpha=0.25)
>>> ax.scatter([locations_usa[c][1] for c in dominating_us], [locations_usa[c][0] for c in dominating_us], c='midnightblue', zorder=10, s=70)
>>> plt.savefig('../../assets/usa_map_sol.pdf')
<matplotlib.figure.Figure at 0x11b6f8358>
{% endhighlight %}

# Save to files

{% highlight python %}
>>> with open('../../assets/french_cities.txt', 'w') as f:
...     f.write('\n'.join(cities_france))
{% endhighlight %}

{% highlight python %}
>>> with open('../../assets/italian_cities.txt', 'w') as f:
...     f.write('\n'.join(cities_italy))
{% endhighlight %}

{% highlight python %}
>>> with open('../../assets/american_cities.txt', 'w') as f:
...     f.write('\n'.join(cities_usa))
{% endhighlight %}

{% highlight python %}
>>> with open('../../assets/french_distances.csv', 'w') as f:
...     for row in D_fr[:-1]:
...         f.write(','.join([str(x) for x in row]) + '\n')
...     f.write(','.join([str(x) for x in D_fr[-1]]))
{% endhighlight %}

{% highlight python %}
>>> with open('../../assets/italian_distances.csv', 'w') as f:
...     for row in D_it[:-1]:
...         f.write(','.join([str(x) for x in row]) + '\n')
...     f.write(','.join([str(x) for x in D_it[-1]]))
{% endhighlight %}

{% highlight python %}
>>> with open('../../assets/american_distances.csv', 'w') as f:
...     for row in D_us[:-1]:
...         f.write(','.join([str(x) for x in row]) + '\n')
...     f.write(','.join([str(x) for x in D_us[-1]]))
{% endhighlight %}

{% highlight python %}

{% endhighlight %}

