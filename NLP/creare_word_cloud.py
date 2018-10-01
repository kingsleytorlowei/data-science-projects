import sys
from os import path
import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS

# get path to script's directory
currdir = path.dirname(__file__)

f = open('constitution.txt', 'r')
text = f.read()


def create_wordcloud(text_file):
	# create numpy araay for wordcloud mask image
	mask = np.array(Image.open(path.join(currdir, "cloud.png")))

	# create set of stopwords	
	stopwords = set(STOPWORDS)

	# create wordcloud object
	wc = WordCloud(background_color="white",
					max_words=200, 
					mask=mask,
	               	stopwords=stopwords)
	
	# generate wordcloud
	wc.generate(text)

	# save wordcloud
	wc.to_file(path.join(currdir, "wc.png"))


if __name__ == "__main__":
	
	# generate wordcloud
	create_wordcloud(text)