from textblob import TextBlob
import re

file = open(r'F:/lenovo.txt', 'r')

original_text = file.read()
# print(original_text)

review_list = original_text.split('\n')
# print(review_list)

review_list = review_list[1:]
# print(len(review_list)) === 1353

for i in review_list:
	if(i == ''):
		review_list.remove(i)

# print(len(review_list)) === 1190

individual_reviews = []
temp = ''
c = 0
for i in review_list:
	if(re.match(r'[\d]\?', i)):
		individual_reviews.append(temp)
		temp = '' + i
	elif(i == 'Certified Buyer'):
		c+=1
	else:
		temp = temp + ' ' + i

# print(individual_reviews)

individual_reviews = individual_reviews[1:]
# print(len(individual_reviews), c) === 119 119

individual_reviews = []
date = []
temp = ''
for i in review_list:
	if(re.match(r'[\d]\?', i)):
		individual_reviews.append(temp)
		temp = '' + i
	elif(re.match(r'\d{1,2} (jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)', i.lower())):
		date.append(i.lower())
	elif(i == 'Certified Buyer'):
		continue
	elif(re.match(r'\d{1,2}(\. | [a-z]+)', i)):
		temp = temp + ' ' + i.lower()
	elif(re.match(r'\d{1,5}', i)):
		continue
	else:
		temp = temp + ' ' + i.lower()
# print(individual_reviews[1])
# print(date[1])
individual_reviews = individual_reviews[1:]
# print(len(individual_reviews), len(date)) === 119 119

ratings = []
reviews = []
for i in individual_reviews:
	ratings.append(i[0])
	reviews.append(i[3:])
# print(len(ratings), len(reviews)) === 119 119

from nltk.corpus import stopwords
sw = set(stopwords.words('english'))

words = []
for i in reviews:
	i = i.lower()
	alpha = re.sub('[^a-zA-Z]', ' ', i)
	alpha_list = alpha.split()
	temp = []
	for j in alpha_list:
		if(j not in sw):
			temp.append(j)
	string = " ".join(temp)
	words.append(string)
# print(words)
# print(len(words)) === 119

temp = " ".join(words)
blob = TextBlob(temp)
tokens = blob.words
'''for i in tokens:
	a = TextBlob(i)
	b = a.tags
	print(b[0][0], "   ", b[0][1])'''

import matplotlib.pyplot as plt
from wordcloud import WordCloud

cloud = WordCloud(background_color = '#000000').generate(temp)
plt.imshow(cloud, interpolation = 'bilinear')
plt.axis('off')
plt.show()

sentiment = []
'''for i in reviews:
	a = TextBlob(i)
	b = a.sentiment.polarity
	sentiment.append(b)
# print(len(sentiment)) === 119
print(sentiment)'''

'''from sklearn.neighbors import KNeighborsClassifier

training_set_x = sentiment[:99]
testing_set_x = sentiment[99:]
training_set_y = ratings[:99]
testing_set_x = ratings[99:]

clf = KNeighborsClassifier()
clf.fit(training_set_x, training_set_y)

for i in range(99, 119):
	a = TextBlob(reviews[i])
	b = a.sentiment.polarity
	print(clf.predict(b), ratings[i])'''
