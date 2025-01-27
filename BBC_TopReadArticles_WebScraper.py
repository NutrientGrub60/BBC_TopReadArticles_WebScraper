from requests_html import HTMLSession

s = HTMLSession()
r = s.get("https://www.bbc.co.uk/news")
most_read = r.html.find("ol.ssrcss-1020bd1-Stack.e1y4nx260", first=True)

if most_read:
    headlines = most_read.find("li")
    for article, headline in enumerate(headlines[:10], start=1):
        print(f"{article}. {headline.text}")
