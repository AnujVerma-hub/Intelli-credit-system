from newsapi import NewsApiClient
import json

def new_api(company_name):
            
            
    newsapi = NewsApiClient(api_key = "0187e26d772845bfa3db7d1420a9cce4")


    articles = newsapi.get_everything(
    q=f'{company_name} AND (litigation OR fraud OR penalty OR insolvency OR RBI OR default)',
    language="en",
    sort_by="publishedAt",
    page_size=20
)
    

    return articles
    
    


    
headings = new_api("Apple Inc")

with open("Data/news_extract.txt", "w", encoding="utf-8") as f:
    json_str = json.dumps(headings)

    f.write(json_str)

