import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset
df = pd.read_csv('C:\Users\MOKKA HEMA SAI\Downloads\Movie_List.csv')

# Fill missing values in 'genre' with an empty string
df['genre'] = df['genre'].fillna('')

# Create a CountVectorizer to vectorize the genre strings
count_vectorizer = CountVectorizer(tokenizer=lambda x: x.split('|'))
genre_matrix = count_vectorizer.fit_transform(df['genre'])

# Compute the cosine similarity matrix
cosine_sim = cosine_similarity(genre_matrix, genre_matrix)

# Function to get movie recommendations based on genre similarity
def get_recommendations(title, cosine_sim=cosine_sim):
    # Check if the title exists in the DataFrame
    if title not in df['title'].values:
        return "Movie not found in the dataset."
    
    # Get the index of the movie that matches the title
    idx = df.index[df['title'] == title].tolist()[0]

    # Get the pairwise similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 5 most similar movies
    sim_scores = sim_scores[1:6]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 5 most similar movies
    return df['title'].iloc[movie_indices]

# Example usage
user_input_title = input("Enter a movie title: ")
recommended_movies = get_recommendations(user_input_title)
print("Recommended movies:")
print(recommended_movies)
