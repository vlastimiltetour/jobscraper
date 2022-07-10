from bs4 import BeautifulSoup
import requests


def extract(role, location):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    url = f'https://cz.indeed.com/jobs?q={role}&l={location}&from=searchOnHP&vjk=467caa405e7501e3'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup

def transform(soup):
    divs = soup.find_all('div', class_="job_seen_beacon")
    for item in divs:
        title = item.find('span').text
        company = item.find('span', class_="companyName").text
        try:
            salary = item.find('div', class_='attribute_snippet').text.strip()
        except:
            salary = 'N/A'

        summary = item.find("div", class_="job-snippet").text.replace("\n", '')
        portal = 'Indeed'

        job = {
            'title': title,
            'company': company,
            'salary': salary,
            'summary': summary,
            'portal': portal
        }


        joblist.append(job)

    return


joblist = []

def next_page(soup):
    pass
    #next = soup.find('a', {'aria-label':2}).get('href')
    #print(next)
        #https://www.youtube.com/watch?v=eN_3d4JrL_w&list=LL&index=3&ab_channel=IzzyAnalytics
        #19.05

s = extract('Python', 'Praha')
transform(s)
#print(joblist)



