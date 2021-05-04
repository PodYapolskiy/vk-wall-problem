"""
VK_Wall_Problem

"""
import vk_api
from config import token  # Main token


vk = vk_api.VkApi(token=token).get_api()


def main():
	print(token)


if __name__ == '__main__':
	main()
