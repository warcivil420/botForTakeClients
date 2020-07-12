import vk_api

def logpass():
	login, password = 'xxxxxx', 'xxxxxxx'
	vk_session = vk_api.VkApi(login, password)
	return vk_session