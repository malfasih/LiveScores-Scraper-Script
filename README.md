# Soccer livescores scrapper written in Python

Python webscrapper that gets the scores from livescores.com.

## Requirements:
> BeautifulSoup. urllib.request.

## Usage:
To execute the script, simply type in the console:

1. **No parameter**
* Prints all the listed games in the website:
	<p>ex: </p>

	> python livescores.py 

2. **With parameter (--active or --not_active)** 
* --active -> only games that had begun or are finished. 
* --not_active -> games that did not begin yet.

	<p>ex: </p>

	>python livescores.py --active

	<p>or</p>

	>python livescores.py --not_active
