from bs4 import BeautifulSoup
from requests.compat import quote_plus
import requests

class Indeed_Scraper:
    def scrape(self):
        for url in self.pages:
            page = requests.get(url)

            soup = BeautifulSoup(page.text, 'html.parser')
            if (soup.find('div', class_='no_results')):
                self.results = False
                return

            for title in soup.find_all('h2'):
                self.titles.append(title.getText()[2:-6])
                temp = title.findChild("a", recursive=False).get('href')
                link = "https://be.indeed.com{}".format(temp)
                self.links.append(link)

            for location in soup.find_all('div', class_='recJobLoc'):
                self.locations.append(location.get('data-rc-loc'))

            for date in soup.find_all('span', class_="date"):
                self.dates.append(date.getText())

            for company in soup.find_all('span', {'class': "company"}):
                self.companys.append(company.text[1:])

    def __init__(self,search, location, pages_to_scape):
        self.pages = []
        self.titles = []
        self.locations = []
        self.companys = []
        self.links = []
        self.dates = []
        self.results = True

        for i in range(1, pages_to_scape + 1):
            url = ("https://be.indeed.com/jobs?q={}&l={}&sort=date&start={}0").format(quote_plus(search), location, i)
            self.pages.append(url)
        self.scrape()

