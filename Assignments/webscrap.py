
import requests
from bs4 import BeautifulSoup


# Question 1
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

#Qestion 2
soup = BeautifulSoup(page.content, "html.parser")

#Question 3
results = soup.find(id="ResultsContainer")

#Question 4
# a)
job_elements = results.find_all("div", class_="card-content")
for job_element in job_elements:

	# a)
	title_element = job_element.find("h2", class_="title")
	if "Ship broker" in title_element:
		print(title_element)

	# b)
	company_element = job_element.find("h3", class_="company")
	print(company_element)


	# c)
	paragraph_element = job_element.find("p")
	print(paragraph_element)

	# Question 5
	subtitle = job_element.find("h3", class_="subtitle is-6 company")
	if "Hughes-Williams" in subtitle:
		print(subtitle.text.strip())




