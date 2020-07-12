import vk_api
import requests
import random
access_token = '8a536957451aa7981bfbc779242caacd5b3707942d3d1147b916316dc187ae8029390c7419af5a00d2cc5'

def fuck():

	b = True
	max1 = 0
	mas_url = []
	information = ''
	appex = [-53845179,-57846937,-12382740,-45745333, -31234561, -51016572, -78543917, -114086029, -52537634, -40800148, -25554967, -139923997, -96591297, -103083994, -70147321, -138191691]
	next1 = appex[random.randint(0, 15)]
	print(next1, 'id группы')
	r = requests.get("https://api.vk.com/method/wall.get", params={"owner_id":next1, "offset":10, "count": 40, "access_token": access_token, "v": "5.94"})
	response = r.json()
	for i in range (30):
		mas_url = []
		likes_v = response['response']['items'][i]['views']['count']
		likes_l = response['response']['items'][i]['likes']['count']
	
		if likes_l/likes_v > max1:	
			max1 = likes_l/likes_v
			text = response['response']['items'][i]['text']
			ty = i
	try:
		information += response['response']['items'][ty]['attachments'][0]['photo']['sizes'][4]['url']
	except:
		pass
	return information+'::$' + text + '::$' + str(next1)