from requests_html import HTMLSession
import pandas as pd

session = HTMLSession()

r = session.get('https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNRGR6YzJNU0JXVnVMVWRDS0FBUAE?hl=en-GB&gl=GB&ceid=GB%3Aen')

r.html.render(sleep=1, scrolldown=1, timeout=10)

articles = r.html.find('article')
newList = []

for item in articles:
    try:
        all_links = item.find('a')
        
        newsitem = next((link for link in all_links if link.text.strip()), None)
        
        if newsitem:
            title = newsitem.text                  
            link = newsitem.attrs['href']          
            newssarticle = {
                'title': title,
                'link': link
            }
            newList.append(newssarticle)
    except Exception as e:
        print(f"Error processing article: {e}")

print(len(newList))

df = pd.DataFrame(newList)
df.to_csv('news_articles.csv', index=False)
print(df.head(5))
