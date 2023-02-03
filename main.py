import time

import sys


def typingPrint(text, sleep):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(sleep)


typingPrint("Welcome back, Mr. Anderson", 0.22)
typingPrint(".....", 0.3)

USER_MENU = "\nType list to list movies, type add to add movies to the list, search database or type q to quit the program\n"

movies = [{
    "name": "Avatar", "genre": "Sci-Fi", "director": "James Cameron"
},
    {
        "name": "Avatar 2", "genre": "Sci-Fi", "director": "James Cameron"
    },
    {
        "name": "The Dark Knight Rises", "genre": "Action", "director": "Christopher Nolan"
    }]


def movie_to_list():
    add_movie = input("What is the name of the movie you want to add?\n")
    genre_movie = input("What is the genre of the movie?\n")
    movie_director = input("Who is the movie director?\n")
    new_movie = {"name": add_movie, "genre": genre_movie, "director": movie_director}
    movies.append(new_movie)
    print(f"{add_movie} was added to the list.")
    time.sleep(1)
    print(f"Updated movie list: {movies}")


def list_movies():
    for _ in movies:
        print(_["name"], _["genre"], _["director"], sep=", ")


def find_movies():
    search = input("You can search with Name of the movie, Genre or Director(Case Sensetive):\n")
    for _ in movies:
        if search in _.values():
            print(search + " Is in the list ", _)


# list movies
selection = input(USER_MENU)
while selection != "q":
    # list movies
    if selection.lower() == "list":
        list_movies()

    # add movies
    elif selection.lower() == "add":
        movie_to_list()
    # find movies
    elif selection.lower() == "search":
        find_movies()
    elif selection.lower() == "quit":
        quit()
    else:
        print("Invalid input")



    selection = input(USER_MENU)

## Sava Barbarov
