import requests
from bs4 import BeautifulSoup

res = requests.get(r'https://news.ycombinator.com/news?p=1')
res2 = requests.get(r'https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

links = soup.select('.titlelink') + soup2.select('.titlelink')
subtext = soup.select('.subtext') + soup2.select('.subtext')


def popularHackerNews(links, subtext):
  hn = []
  for i, r in enumerate(links):
    title = links[i].getText()
    href = links[i].get('href', None)
    vote = subtext[i].select('.score')
    if len(vote):
      points = int(vote[0].getText().replace(' points', ''))
      if points > 99: hn.append(
        {'title': title, 'link': href, 'votes': points})
  return sortStoriesByVotes(hn)


def sortStoriesByVotes(hnList):
  return sorted(hnList, key=lambda x: x['votes'], reverse=True)


for h in popularHackerNews(links, subtext):
  link = h['link']
  title = h['title']
  votes = h['votes']
  print(f'<a href="{link}">{title} Votes: {votes}</a>')
