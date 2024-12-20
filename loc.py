import requests

# Get public IP address
ip_request = requests.get('https://get.geojs.io/v1/ip.json')
ipAdd = ip_request.json()['ip']

# Get geolocation data
url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
geo_request = requests.get(url)
geo_data = geo_request.json()

# Construct formatted output
s ="help! I am in danger\n"
s += "IP: {}\n".format(ipAdd)
s += "Latitude: {}\n".format(geo_data['latitude'])
s += "Longitude: {}\n".format(geo_data['longitude'])
s += "City: {}\n".format(geo_data['city'])
s += "Region: {}\n".format(geo_data['region'])
s += "Country: {}\n".format(geo_data['country'])
s += "Timezone: {}\n".format(geo_data['timezone'])

print(s)
