import ipinfo
import pprint
access_token = 'd26467ba90b0fe'
handler = ipinfo.getHandler(access_token)
ip_address = '172.118.204.89'
details = handler.getDetails(ip_address)
details.city
'Mountain View'
details.loc
'37.3861,-122.0840'
pprint.pprint(details.city)
pprint.pprint(details.all)
