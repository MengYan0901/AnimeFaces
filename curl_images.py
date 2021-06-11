import requests
from tqdm import tqdm
import traceback

def curl1():
	# curl "https://media.kitsu.io/characters/images/[1-99000]/original.jpg" -o "#1.jpg"
	for i in tqdm(range(50000, 99001)):
		url = f'https://media.kitsu.io/characters/images/{i}/original.jpg'
		try:
			respone = requests.get(url)
			try:
				with open(f'./anime_planet/{i}.jpg', 'wb') as wp:
					wp.write(respone.content)
			except:
				traceback.print_exc()
		except:
			print('http request wrong!')

def curl2():
	#http://www.anime-planet.com/images/characters/i-[1-60000].jpg
	for i in tqdm(range(1, 60001)):
		url = f'http://www.anime-planet.com/images/characters/i-{i}.jpg'
		try:
			respone = requests.get(url)
			try:
				with open(f'./anime_planet/i-{i}.jpg', 'wb') as wp:
					wp.write(respone.content)
			except:
				traceback.print_exc()
		except:
			print('http request wrong!')

if __name__ == '__main__':
	curl1()
	curl2()