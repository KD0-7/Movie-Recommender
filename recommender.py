import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



movies = pd.read_csv("data/movies.csv")



movies["genres"] = movies["genres"].fillna("")
movies["rating"] = movies["rating"].fillna(0)



vectorizer = TfidfVectorizer()

genre_vectors = vectorizer.fit_transform(movies["genres"])



similarity = cosine_similarity(genre_vectors)


def recommend(movie_name, number=10):

    
    movie_index = movies[
        movies["title"].str.lower() == movie_name.lower()
    ].index

    
    if len(movie_index) == 0:
        return []

    movie_index = movie_index[0]

    
    scores = list(
        enumerate(similarity[movie_index])
    )

    
    results = []

    for index, similarity_score in scores:

        
        if index == movie_index:
            continue

        rating = movies.iloc[index]["rating"]

       
        rating_score = rating / 10

        
        final_score = (
            0.7 * similarity_score +
            0.3 * rating_score
        )

        results.append(
            (index, final_score)
        )

    
    results.sort(
        key=lambda x: x[1],
        reverse=True
    )

    
    recommendations = []

    for index, score in results[:number]:

        recommendations.append({
            "movieId": int(movies.iloc[index]["movieId"]),
            "title": movies.iloc[index]["title"],
            "genres": movies.iloc[index]["genres"],
            "rating": float(movies.iloc[index]["rating"]),
            "score": round(score, 3)
        })

    return recommendations



if __name__ == "__main__":

    movie_name = input(
        "Enter movie name: "
    )

    recommendations = recommend(movie_name)

    if recommendations:

        print("\nRecommended Movies:\n")

        for movie in recommendations:

            print(
                f"{movie['title']} | "
                f"Rating: {movie['rating']} | "
                f"Score: {movie['score']}"
            )

    else:

        print("\nMovie not found.")