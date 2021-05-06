"""
VK_Wall_Problem

"""
import vk_api


def main():

    #Authentification
    vk_session = vk_api.VkApi('***', '***')#login, password
    vk_session.auth()
    vk = vk_session.get_api()


    #delete posts, exept first 10
    posts = vk.wall.get(count=100, offset=10)['items']
    while posts:
        for post in posts:
            print(post['id'])
            vk.wall.delete(post_id=post['id'])
        posts = vk.wall.get(count=100, offset=10)['items']


if __name__ == '__main__':
	main()
