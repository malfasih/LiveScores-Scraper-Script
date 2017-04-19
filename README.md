# Soccer livescores scrapper written in Python

Python webscrapper that gets the scores from livescores.com.

Requirements:
  -BeautifulSoup. urllib.request.

Usage:
  -To execute the script, simply type in the console:
	No parameter 
	Prints all the listed games in the website:
	ex:
	python livescores.py

	With parameter    
	--active -> only games that had begun or are finished. 
	--not_active -> games that did not begin yet.
	ex:
	python livescores.py --active
	or
	python livescores.py --not_active
