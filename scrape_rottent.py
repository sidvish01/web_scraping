import bs4
from urllib.request import urlopen


def remove_extra(string):

	l =[]
	l2 = []
	l = string.split(' ')
	for i in l:
		if i!='\n':
			l2.append(i)

		return (' '.join(l2))	


url = 'https://www.rottentomatoes.com/m/aquaman_2018'

html = urlopen(url)

markup = (html.read())

soup = bs4.BeautifulSoup(markup, 'html.parser')


movie_name = soup.find('h1', attrs={'class':'title hidden-xs'})

print(movie_name.text)

critic_con = soup.find('p', attrs={'class':'critic_consensus superPageFontColor'})

print(critic_con.text)

tomatometer = soup.find('span', attrs={'class':'meter-value superPageFontColor'})

print(tomatometer.text)

audience_score = soup.find('div', attrs={'class':'meter-value'})

print(audience_score.text)

critic_review = soup.find_all('div', attrs={'class':'quote_bubble top_critic pull-left cl'})



for review in critic_review:
	review_body = review.find('p')
	review_name = review.find('a', attrs={'class':'unstyled articleLink fgm'})
	review_org = review.find('a', attrs={'class':'subtle small'})
	review_rat = review.find('div', attrs={'class':'pull-right smaller'})

	print(review_body.text)
	if review.rat!=None:
		print(review_rat.text)
	print(review_name.text)
	print(review_org.text)	
