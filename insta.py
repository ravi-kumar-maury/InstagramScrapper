import urllib
import urllib.request
import os
import requests
import json
url_fashion="https://www.instagram.com/explore/tags/fashion/?hl=en"

url1 = "https://www.instagram.com/graphql/query/?query_hash=02e14f6a7812a876f7d133c9555b1151&variables=%7B%22id%22%3A%2240183604206%22%2C%22first%22%3A12%7D"
#value of variable is urlencoded and can be decoded to check the content

#nope, not the correct cookie , use your own (check yours in chrome devtools)
cookies = {
'csrftoken': '6Vlhpp5dfDvFgVgBu7stU9xd2vaH8Wedfwrjw',
'ds_user_id':'990245665526',
'fbm_124024574287414':'base_domain=.instagram.com',
'ig_did':'9Ecfve2183RUHBFVIHRFOsdc',
'mid':'XimajgAEAAH8CRa_vb5l8nYOTQ9O',
'rur':'RVA',
'sessionid':'15ir23g28b041edfv',
'shbid':'1948'
}
#this commented block is for getting random profile
# r= requests.get(url1,cookies=cookies)
# edges = r.json()['data']['user']['edge_owner_to_timeline_media']['edges']
# images= []
# for e in edges :
#     img = e['node']['display_url']
#     images.append(img)
# os.chdir('/home/rk/Instagram_Scrapper')

# for e in range(len(images)):
#     im=urllib.request.urlretrieve(images[e],str(e)+".jpg")

r =  requests.get(url_fashion , cookies=cookies)
print(r.text)


	



