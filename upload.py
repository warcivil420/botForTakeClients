import vk_api
from vk_api import VkUpload
import time
import random
from logpass import logpass
import text as txt


# Авторизация по логину/паролю (если нужно по токену, заполнять параметр token)
vk_session = logpass()
vk_session.auth()
vi_Ar = []
while True:

	top_com = (((open('top_comments.txt', 'r')).read()).split(':'))
	text = top_com[random.randint(0, len(top_com)-1)]
	print('text', text)
	# Или:
	# photos = [open('1.jpg', 'rb'), open('2.jpg', 'rb')]
	vk_session.method('wall.post', {
		'owner_id':-180493846,
		'from_group':1,
		'message':text
	})
	print('--------------------скрипт отработал успешно--------------------------------')
	time.sleep(random.randint(80*60, 130*60))

