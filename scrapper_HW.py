import requests
from bs4 import BeautifulSoup

url = "https://www.indeed.com/jobs?q=python&limit=50&vjk=91ac3fcf406a26e9"
LIMIT = 50


def extract_pages():
	data = requests.get(url)
	indeed_result = BeautifulSoup(data.text, "html.parser")
	pagination = indeed_result.find("div", {'class' : 'pagination'})
	links = pagination.find_all("a")
	pages = []
	for link in links[:-1]:
		pages.append(int(link.string))
	max_page = pages[-1]
	return max_page


def title_extract(last_page):
	jobs = []
	result = requests.get(f"{url}&start={0*LIMIT}")
	soup = BeautifulSoup(result.text, "html.parser")
	job_titles = soup.find_all("div", {'class' : 'jobsearch-SerpJobCard'})

	for job_title in job_titles:
		title = job_title.find('h2', {'class' : 'title'})
		anchor = (title.find('a')["title"])
		print(anchor)
	return jobs

last_page = extract_pages()
title_extract(last_page)