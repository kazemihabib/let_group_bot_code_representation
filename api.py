#!/usr/bin/env python
import sys
from google import search as google_search
from requests import get
from bs4 import BeautifulSoup 

def search(query):
	google_response = google_search(query + ' site:www.metrolyrics.com', stop=10)
	result = []
	for url in google_response:
		result.append(url)
	return result

def lyric(url):
	html = get(url).content
	soup = BeautifulSoup(html, 'html.parser')
	lyric_body= soup.select_one('#lyrics-body-text')
	soup = BeautifulSoup(str(lyric_body), 'html.parser')
	text = soup.get_text()	
	return text

if __name__ == "__main__":
	if len(sys.argv) > 1:
		query = ' '.join(sys.argv[1: ])
		links = search(query)
		lyric(links[0])
