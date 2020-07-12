import vk_api
from vk_api import VkUpload
import saver
import time
import random
import logpass
# Авторизация по логину/паролю (если нужно по токену, заполнять параметр token)
login, password = '+89197106221', 'UDokTiHeObaphz5'
vk_session = vk_api.VkApi(login, password)
vk_session.auth()
vi_Ar = []
while True:
    a = ''
    smile_id = ['&#128064;', '&#128123;',
                '&#128520;', '&#128126;', '&#128572;']
    upload = VkUpload(vk_session)  # Для загрузки изображений
    posttime = saver.saver()

    text = posttime[1]
    need_id = str(posttime[2]).replace('-', '')
    print(need_id, 'need_id')

    print(posttime, 'posttime')

    photos = ['1.jpg']

    print('text', text)

    # Или:
    # photos = [open('1.jpg', 'rb'), open('2.jpg', 'rb')]
    photo_list = upload.photo_wall(photos)
    print('vi_Ar', vi_Ar)
    attachment = ','.join('photo{owner_id}_{id}'.format(**item)
                          for item in photo_list)
    for item in photo_list:
        if (saver.saver() not in vi_Ar) and (posttime[0] != ''):
            vk_session.method('wall.post', {
                'owner_id': -180493846,
                'attachment': attachment,
                'from_group': 1,
                'message': text
            })
        elif (saver.saver() not in vi_Ar) and (posttime[0] == ''):
            vk_session.method('wall.post', {
                'owner_id': -180493846,
                'from_group': 1,
                'message': text
            })
        vi_Ar.append(posttime[0])
        vi_Ar.append(posttime[1])
        print(
            '--------------------скрипт отработал успешно--------------------------------')
    time.sleep(random.randint(100 * 60, 150 * 60))
