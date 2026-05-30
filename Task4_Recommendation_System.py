import random

movies = [
    {"name": "John Wick", "genres": ["action", "thriller"], "rating": 8.2},
    {"name": "Avengers", "genres": ["action", "sci-fi"], "rating": 8.0},
    {"name": "Mad Max", "genres": ["action", "sci-fi"], "rating": 8.1},

    {"name": "Inception", "genres": ["sci-fi", "thriller"], "rating": 8.8},
    {"name": "Interstellar", "genres": ["sci-fi", "drama"], "rating": 8.6},

    {"name": "La La Land", "genres": ["romance", "drama"], "rating": 7.9},
    {"name": "Titanic", "genres": ["romance", "drama"], "rating": 7.9},

    {"name": "The Conjuring", "genres": ["horror", "thriller"], "rating": 7.5},
    {"name": "A Quiet Place", "genres": ["horror", "sci-fi"], "rating": 7.5},

    {"name": "Coco", "genres": ["animation", "family"], "rating": 8.4},
    {"name": "Finding Nemo", "genres": ["animation", "family"], "rating": 8.1},

    {"name": "Forrest Gump", "genres": ["drama", "romance"], "rating": 8.8}
]

genres = [
    "action", "romance", "sci-fi", "horror",
    "family", "animation", "drama", "thriller"
]


def show_genres():
    print("\nSelect your favorite genres:")
    for i in range(len(genres)):
        print(f"{i+1}. {genres[i]}")


def compute_similarity_score(movie, liked_genres):
    score = 0
    genre_match = False

    for genre in movie["genres"]:
        if genre in liked_genres:
            score += 10
            genre_match = True

    if genre_match:
        score += movie["rating"] * 0.5
    else:
        score = 0

    return score


def recommend_movies():
    show_genres()

    choices = input("\nEnter choice numbers (space separated): ").split()
    liked_genres = []

    for choice in choices:
        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(genres):
                liked_genres.append(genres[index])

    if not liked_genres:
        print("\nInvalid choice!")
        return

    print("\nYou selected:", liked_genres)

    recommendations = []

    for movie in movies:
        score = compute_similarity_score(movie, liked_genres)
        if score > 0:
            recommendations.append((movie, score))

    recommendations.sort(key=lambda x: x[1], reverse=True)

    print("\nTop Recommended Movies:")
    print("--------------------------------")

    if recommendations:
        for i, (movie, score) in enumerate(recommendations[:5], start=1):
            print(f"\n{i}. {movie['name']}")
            print("   Genre :", ", ".join(movie["genres"]))
            print("   Rating:", movie["rating"])
    else:
        print("No movies found!")


def show_all_movies():
    print("\nAll Available Movies 🎬")
    print("--------------------------------")

    for i, movie in enumerate(movies, start=1):
        print(f"\n{i}. {movie['name']}")
        print("   Genre :", ", ".join(movie["genres"]))
        print("   Rating:", movie["rating"])


def random_movie():
    movie = random.choice(movies)

    print("\nRandom Movie Suggestion 🎲")
    print("--------------------------------")
    print("Movie  :", movie["name"])
    print("Genres :", ", ".join(movie["genres"]))
    print("Rating :", movie["rating"])


while True:

    print("\n========== MOVIE RECOMMENDATION SYSTEM ==========")
    print("1. Recommend Movies By Genre")
    print("2. Show All Movies")
    print("3. Random Movie Suggestion")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        recommend_movies()

    elif choice == "2":
        show_all_movies()

    elif choice == "3":
        random_movie()

    elif choice == "4":
        print("\nThank you for using the Movie Recommendation System. Goodbye!")
        break

    else:
        print("\nInvalid choice! Please try again.")
