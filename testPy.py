#!/usr/bin/python

# To ignore the warnings
import warnings
warnings.filterwarnings("ignore")
warnings.simplefilter("ignore")
import logging
logging.getLogger().setLevel(logging.ERROR)
import getopt, sys

try:
    t1 = sys.argv[1]
    print("t1 ", t1)

    if t1 != "--title":
        raise ValueError('Invalid Format')
    title = sys.argv[2]
    print("title ",title)
    d1 = sys.argv[3]
    print("d1 ",d1)
    if d1 != "--description":
        raise ValueError('Invalid Format')
    desc = sys.argv[4]
    print("desc ", desc)
except:
    print(11)
    print("Please execute in the following format: python.exe movie_classifier.py --title (or --t) 'Forrest Gump' --description (or --d) 'A man with a low IQ has accomplished great'")
    sys.exit(2)

print("Start Script!")
import os
import time
start_time = time.time()
pwd = os.getcwd()
try:
    import pip
except:
    try:
        print('Installing pip to install other required packages, please wait')
        os.system('python get_pip.py')
    except:
        print('please install pip')

#fuzzywuzzy - to do the string matching
try:
    from fuzzywuzzy import fuzz
    from fuzzywuzzy import process
except ImportError:
    print("trying to install module: fuzzywuzzy")
    os.system('pip install fuzzywuzzy')
    from fuzzywuzzy import fuzz
    from fuzzywuzzy import process
# ast
try:
    import ast
except ImportError:
    print("trying to install module: ast")
    os.system('pip install ast')
    import ast

# Pandas
try:
    import pandas as pd
except ImportError:
    print("trying to install module: pandas")
    os.system('pip install pandas')
    import pandas as pd
# Numpy
try:
    import numpy as np
except ImportError:
    print("trying to install module: numpy")
    os.system('pip install numpy')
    import numpy as np

print("Importing the required libraries/packages successful! ")

#read the csv
df = pd.read_csv(pwd+'/moviesList-preprocessed.csv')
dff = df[['id','genres','original_language','original_title','overview','title']].copy() # Considering only the required columns
#dff['genres'] = dff['genres'].fillna('[]').apply(ast.literal_eval).apply(lambda x: [i['name'] for i in x] if isinstance(x, list) else []) # Converting the metadata into a list

print("\nSubset of the full dataset with required columns: ")
print(dff.head())
print("\n")

#Function to check the string similarity
def checker(wrong_options,correct_options):
  names_array=[]
  print("....")
  for wrong_option in wrong_options:
      if wrong_option in correct_options:
          names_array.append(wrong_option)
      else:
          x=process.extract(wrong_option,correct_options,scorer=fuzz.token_set_ratio)
          names_array.append(x[0])
  return names_array

# First compare the match the tile and make a subset of of the dataframe
strOptions = dff.title.tolist()
title1=[]
title1.append(title)
print("Matching the given title with the movie database\n")
a = checker(title1,strOptions)
# dataframe with title matches
dff1 = dff[dff['title']==a[0]]

# Now from the subset of the dataframe with title matches, check the best matching description
strOptions1 = dff1.overview.tolist()
print("Matching the given description with the movie database\n")
a1 = checker(desc,strOptions1)
titleO, descriptionO, genreO = dff1[dff1['overview']==a1[0][0]]['title'], dff1[dff1['overview']==a1[0][0]]['overview'], dff1[dff1['overview']==a1[0][0]]['genres']
print("\n        --------------------------------- Final Result ---------------------------------")
#print('title: ',titleO.values)
#print('description: ',descriptionO.values)
#print('genre: ',genreO.values)

res = {"Title":titleO.values[0], "Description":descriptionO.values[0], "Genre":genreO.values[0]}
print(res)
print("--- %s seconds ---" % (time.time() - start_time))
