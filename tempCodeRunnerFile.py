import requests 
import json
from bs4 import BeautifulSoup
try:
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}
   
    pages=1
    quotes_list=[]
    while True:
        url=f"https://quotes.toscrape.com/page/{pages}/"
        response=requests.get(url,headers=headers,timeout=10)
        response.raise_for_status()
        html=response.text
        soup=BeautifulSoup(html,"html.parser")
        quotes=soup.find_all("div",class_="quote")
        if not quotes:
            break
    
        for quote in quotes:
            text=quote.find("span",class_="text").text
            author=quote.find("small",class_="author").text
            data={
            "quotes":text,
        "author":author
        }
            quotes_list.append(data)
       
        pages+=1
    with open("quotes.json","w" ) as file:
            json.dump(quotes_list,file,indent=4,ensure_ascii=False)
       
except requests.exceptions.ConnectionError:
    print("check connection error")
except requests.exceptions.Timeout:
    print("Timeout")
except requests.exceptions.HTTPError as e:
    print("HTTP error",e)

