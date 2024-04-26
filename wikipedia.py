from bs4 import BeautifulSoup
import requests
import pandas as pd

try:
    response = requests.get("https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue")
    print(response.status_code)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("table", class_="wikitable sortable")
        heading = table.find_all("th")
        column_heading = [data.text.strip() for data in heading]

        df = pd.DataFrame(columns=column_heading)

        row_data = table.find_all("tr")
        for row in row_data[1:]:
            record_td = row.find_all("td")
            record = [data.text.strip() for data in record_td]
            length = len(df)
            df.loc[length] = record

    df.to_csv(r'C:\Users\ARUN NIVAAS\PycharmProjects\Web_Scraping\csv\companies.csv',index=False)


except Exception as e:
    print(e)
