'''
-----------------------------------------------------------------------
MADE BY: github.com/sankalpsagar
DESCRIPTION: Unofficial MAL console client made using Jikan, an Unofficial MyAnimeList API.
			 Jikian Link: https://jikan.moe/
DEVELOPED USING: Python3 and SublimeText3
FUTURE MILESTONES: Better representation of data and better looking client

Feel free to modify and share.
-----------------------------------------------------------------------
'''

#getting it all ready
import json
import time
from datetime import datetime
from jikanpy import Jikan
jikan = Jikan()

#making stuff pretty
print("-"*80)
print("\t\t\tWelcome to Anime Console\t\t\t")
print("-"*80)

#starting menu
while True:
	print("\n 1. Anime Airing today \n 2. Top Anime \n 3. Search for Anime \n 4. Exit")
	choice = int(input("Enter your choice: "))
	if choice == 1:
		#getting dict
		scheduled = jikan.schedule()

		#getting anime for day
		print("\nAnime airing today: ")

		#print(scheduled)
		#printing anime airing today
		day = datetime.today().strftime('%A').lower()
		for items in scheduled[day]:
			print("\nTitle: ", items['title'])
			print("Score: ", items['score'])
			print("Synopsis: ", items['synopsis'])

	elif choice == 2:
		print("\nTop Animes: ")

		#getting dict
		top_anime = jikan.top(type='anime')

		#printing all the stuff
		for items in top_anime['top']:
			print("\nRank: ", items['rank'])
			print("Title: ", items['title'])
			print("Score: ", items['score'])
			print("Type: ", items['type'])
			print("Episodes: ", items['episodes'])

	elif choice == 3:
		#search anime
		print("\nEnter search term: ")
		search = input();

		#getting dict
		search_result = jikan.search('anime', search)

		#to weedout unneccessary animes
		count = 0

		#printing results (only top 10)
		for items in search_result['results']:
			#display only 10 animes
			if count == 10:
				break
			print("\nTitle: ", items['title'])
			print("Episodes: ", items['episodes'])
			print("Score: ", items['score'])
			print("Synopsis: ", items['synopsis'])
			count+=1


	elif choice == 4:
		break
	else:
		print("\nInvalid choice, please enter again.")

#congratulations for making it all the way to the end
print("\nDeveloped with <3 by Sankalp")
print("Checkout my GitHub: github.com/sankalpsagar")