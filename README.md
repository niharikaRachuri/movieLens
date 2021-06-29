# movieLens
A simple command line application: given a title and a short description, the application returns the genre(s) by performing string matching of the MovieLens Database

# Process
First I start with the https://www.kaggle.com/rounakbanik/the-movies-dataset?select=movies_metadata.csv file from the MovieLens database (from Kaggle)

The original dataset from Kaggle looks as below: 
![image](https://user-images.githubusercontent.com/34402162/123810815-fe982080-d8f2-11eb-917c-0fa2226c97e7.png)

For the current requirement, we don't need all the columns, so I made a copy of the original dataframe with the columns: **id,genres,original_language,original_title,overview,title**

The overview of the final dataset that we would work on is as follows:
![image](https://user-images.githubusercontent.com/34402162/123811300-6c444c80-d8f3-11eb-9188-2c331e1306c1.png)

As the Genre columns contains metadata with Genre and respective ID, I convert it to a list of strings (with only the genres) using the AST library, which results in the following dataframe: (This dataset is exported for easy usage as the file **moviesList-preprocessed.csv**)
![image](https://user-images.githubusercontent.com/34402162/123811547-a1509f00-d8f3-11eb-8205-48c3f250672d.png)


# Data Exploration
Considering all the records, the top genres (in descending order) has been represented using the bar chart.
![image](https://user-images.githubusercontent.com/34402162/123811941-fc829180-d8f3-11eb-8007-8b8320917687.png)

Just to see the occurrence of the most repeated titles in the full database I plotted the following word cloud.
![image](https://user-images.githubusercontent.com/34402162/123812183-29cf3f80-d8f4-11eb-992c-4e7580059f6e.png)

# String Matching - FuzzyWuzzy
As the database already contains the genre for the respective title, I use the Fuzzy Wuzzy (https://pypi.org/project/fuzzywuzzy/) Package to perform string matching for the given input arguments (title and description) to get the exact record for which the input data corrresponds to. 

Step-1: Consider the title (first input argument), perform string matching with the whole dataset (title column) to get the top matching entries

Step-2: Create a subset of the full dataset with the matching entries

Step-3: Considering the subset of the dataframe, now perform the fuzzy string matching to find the most similar description to the input argument.

Step-4: Print the final result

# Usage
1. Directly from the command line

Run: python testPy.py --title "Othello" --description "The evil Iago pretends to be friend of Othello in order to manupulate him to serve his own end in the film version of this shakespeare classic."

Assuming the required libraries are not installed, at the first run of the program, the libraries/packages are installed. 

The final result format is as follows: (this will be printed on the command line)
{'Title': 'Othello', 'Description': 'The 1965 version of the Shakespeare play.', 'Genre': "['Drama']"}

2. Using the docker file

Download the contents into a folder, along with the dockerfile (which would install the required packages/libraries), change the current working directory in the dockerfile to your current directory and run the following from the command line.

docker run -it movielensproject testPy.py --title "Othello" --description "The evil Iago pretends to be friend of Othello in order to manupulate him to serve his own end in the film version of this shakespeare classic."

3. Manual Testing

Use the ipynb file for testing. It includes all the steps followed. 
