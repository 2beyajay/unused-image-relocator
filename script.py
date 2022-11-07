import os, re
from bs4 import BeautifulSoup # this is our html parser.

allImgTags = [] # this will store all the image tags in all HTML files found in adobe folder. But it will be a list of lists. Not ideal.
allImageFileNames = [] # this will store all image sources that are in use in the HTML

direc = "adobe_campaign" # saving directory as a variable for future global exec potential

for filename in os.listdir(direc):
	if filename.lower().endswith('.html'): # only working with html files. lowercasing them so all cases match.
		fname = os.path.join(direc, filename)
		with open(fname, 'r') as f:
			doc = BeautifulSoup(f, "html.parser")
			allImgTags.append(doc.findAll('img'))

def traverse(o, tree_types=(list, tuple)): # generator function to untangle the list of lists to just be a list.
	if isinstance(o, tree_types):
		for value in o:
			for subvalue in traverse(value, tree_types):
				yield subvalue
	else:
		yield o

regex = "[\w-]+\.(jpg|jpeg|png|gif)" # regex used to extract filename from a url. Might change later on if any issues arise.
for value in traverse(allImgTags):
	allImageFileNames.append(re.search(regex, str(value['src'])).group(0)) # re.search dishes out an object. Tragetting group(0) to get the string of the match
