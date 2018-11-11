import geocoder
g = geocoder.ip('me')
print(g.latlng)
l = geocoder.google(g, method='reverse')
l.city
l.state
l.state_long
l.country
l.country_long
