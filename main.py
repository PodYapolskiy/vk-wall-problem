"""
VK_Wall_Problem

"""
import vk_api
from config import login, password


def delete_posts(offset=0):
	"""
	:param offset: Отступ от последней записи на стене. Удаление будет происходить, начиная с `offset` + 1 записи.
	:type offset: int
	"""
	posts = vk.wall.get(count=100, offset=offset)['items']

	while posts:
	    for post in posts:
	        vk.wall.delete(post_id=post['id'])
	    posts = vk.wall.get(count=100, offset=offset)['items']


if __name__ == '__main__':

	# Authentification
	try:
		vk_session = vk_api.VkApi(login, password)
		vk_session.auth()
		vk = vk_session.get_api()

		delete_posts(offset=15)
	
	except Exception as e:
		print("Ошибка аунтефикации: ", e)
