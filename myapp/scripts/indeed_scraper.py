from bs4 import BeautifulSoup
from requests.compat import quote_plus
import requests

class Indeed_Scraper:
    def makeFinal_postings(self):
        for i in range(len(self.titles)):
            self.final_postings.append((self.titles[i],self.locations[i],self.companys[i],
                                        self.links[i],self.dates[i]))

    def scrape(self):
        for url in self.pages:
            page = requests.get(url)

            soup = BeautifulSoup(page.text, 'html.parser')
            if (soup.find('div', class_='no_results')):
                self.results = False
                return

            for title in soup.find_all('a', class_='jobtitle'):
                self.titles.append(title.text)
                link = "https://be.indeed.com{}".format(title.get('href'))
                self.links.append(link)

                # new_page = requests.get(link)
                # soup = BeautifulSoup(new_page.text, 'html.parser')
                # if(soup.find('div', class_='jobsearch-IndeedApplyButton-buttonWrapper')):
                #     self.links.append(link)
                # else:
                #     new_link = soup.find('a',{'rel':'noopener'})
                #     self.links.append(new_link.get('href'))

            for location in soup.find_all('div', class_='recJobLoc'):
                self.locations.append(location.get('data-rc-loc'))

            for date in soup.find_all('span', class_="date"):
                self.dates.append(date.getText())

            for company in soup.find_all('span', {'class': "company"}):
                self.companys.append(company.text[1:])

            self.makeFinal_postings()

    def __init__(self,search, location,radius, pages_to_scape):
        self.pages = []
        self.titles = []
        self.locations = []
        self.companys = []
        self.links = []
        self.dates = []
        self.results = True

        self.final_postings=[]

        for i in range(1, pages_to_scape + 1):
            url = ("https://be.indeed.com/jobs?q={}&l={}&radius={}&sort=date&start={}0").format(quote_plus(search), location,radius, i)
            self.pages.append(url)
        self.scrape()


