import requests
from bs4 import BeautifulSoup
import pandas as pd

company_list = []

url = 'https://www.inc.com/inc5000/2020'
r = requests.get(url)
page_soup = BeautifulSoup(r.text, "html.parser")
companies = page_soup.find_all("div", class_="sc-fzooss iGhmwn franchise-row")

for item in companies:
    company = {
        'rank': item.find("div", class_="rank").text,
        'company': item.find("div", class_="company").text,
        'link': 'https://www.inc.com' + item.find("div", class_="description").a['href'],
        'growth': item.find("div", class_="growth").text,
        'industry': item.find("div", class_="industry").text,
        'state': item.find("div", class_="state").text,
        'city': item.find("div", class_="city").text,
        }
    company_list.append(company)

df = pd.DataFrame(company_list)
df.to_excel('inc5000_list.xlsx', index=False)

print(f'Data of {len(companies)} companies successfully exported !!')