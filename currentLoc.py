import geocoder

def getLocation():
	g = geocoder.ip('me')
	return g.latlng
