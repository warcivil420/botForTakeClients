import vk_api
import time
import random

vk = vk_api.VkApi(login='89197106221', password='rootprava12')
vk.auth()
f = open('lavos.txt', 'r')
mes = f.read()

id_club = [-51095782, -8398919, -10521881, -76335378]
while True:
	for i in range(4):
		try:
			vk.method('wall.post', {
				'owner_id':id_club[i],
				'message':mes
				})
		except:
			print(id_club[i])
		time.sleep(random.randint(44, 122))
	time.sleep(7200)
