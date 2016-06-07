import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import urllib2
import bs4
import string
import math
import json
def get_text_title(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    print response.read()

    ## get text
    soup = bs4.BeautifulSoup(response, "html.parser")
    content = bs4.BeautifulSoup(str(soup.find_all(id = 'Content')),"lxml")
    text = ''
    for x in content.find_all('p'):
        text = text+x.string
    text = "".join([c  if c not in string.punctuation else ' ' for c in text])
    title = bs4.BeautifulSoup(str(soup.find_all(id = 'title')),"lxml")
    print title
    return text,title

def count_tf(text):
    word_dict = {}
    count = 0
    for word in text.split() :
        if word in word_dict:
            word_dict[word] =  word_dict[word]  + 1
        else:
            word_dict[word] = 1.0
        count = count + 1
    for word in word_dict:
        word_dict[word] =  word_dict[word]/count
    return word_dict

def count_idf(word_dicts):
    big_word_dict = {}
    for word_dict in word_dicts:
        for word in word_dict:
            if word in big_word_dict:
                big_word_dict[word] =  big_word_dict[word]  + 1
            else:
                big_word_dict[word] = 1.0
    for word in big_word_dict:
        big_word_dict[word] =  math.log(len(url_list)/big_word_dict[word])+0.000000001
        #big_word_dict[word] =  math.log(10/float(big_word_dict[word]))+0.000000001
    return big_word_dict

#response = urllib2.urlopen("http://www.chinadaily.com.cn")
#request = urllib2.Request("http://www.baidu.com")
url_list = ['http://www.bbc.com/news/world-asia-china-36457453',
            'http://www.chinadaily.com.cn/china/2016-04/20/content_24700746.htm',
            ]

word_dicts = []
titles = []
for url in url_list:
    text,title = get_text_title(url)
    titles.append(title)
    word_dict = count_tf(text)
    word_dicts.append(word_dict)

big_word_dict = count_idf(word_dicts)

words = []
for word_dict in word_dicts:
    for word in word_dict:
        #print word,word_dict[word],big_word_dict[word]
        word_dict[word] =  word_dict[word]*big_word_dict[word]
    word_dict= sorted(word_dict.iteritems(), key=lambda d:d[1], reverse = True)
    words.append(str(word_dict[:10]))
data = [title+':'+word for title,word in zip(titles,words)]
data = '\n'.join(data)
with open('data1.json', 'w') as f:
    json.dump(data, f)