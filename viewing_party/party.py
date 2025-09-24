# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    """ This function will create a movie dictionary with three keys: title, genre, and rating.
    If any of the parameters are falsy, return None.
    
    Parameters:
        title, 
        genre, 
        rating, 
    
    Output: a dictionary in this format:
        {
            "title": "Title A",
            "genre": "Horror",
            "rating": 3.5
        }
    """

    movie_dict = {}

    if title and genre and rating:
        movie_dict["title"] = title
        movie_dict["genre"] = genre
        movie_dict["rating"] = rating
        return movie_dict
    else:
        return None

def add_to_watched(user_data, movie):
    """ This function will add the movie to the "watched" list inside of user_data
    
    Parameters: 
        user_data: dict, 
            {"watched": [{}, {} , {}]} the value of user_data will be a dictionary with a key "watched", and a value which is a list of dictionaries representing the movies the user has watched
        movie: dict
            {
                "title": "Title A",
                "genre": "Horror",
                "rating": 3.5
            }

    Output:
        user_data
    """
    
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    """ This function will add the movie to the "watchlist" list inside of user_data
    
    Parameters: 
        user_data: dict, 
            {"watchlist": [{}, {} , {}]} the value of user_data will be a dictionary with a key "watchlist", and a value which is a list of dictionaries representing the movies the user wants to watch
        movie: dict
            {
                "title": "Title A",
                "genre": "Horror",
                "rating": 3.5
            }

    Output:
        user_data
    """

    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    """ This function will move a movie from the "watchlist" list to the "watched" list inside of user_data.
    
    Parameters: 
        user_data: dict, 
            {"watchlist": [{}, {} , {}], "watched": [{}, {} , {}]} the value of user_data will be a dictionary with a "watchlist" and a "watched", this represents that the user has a watchlist and a list of watched movies
        title: str
            The title of the movie the user has watched

    Output:
        user_data
    """
    for movie in user_data["watchlist"]:
        if title in movie.values():
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie) 
            return user_data
    return user_data

# ------------- WAVE 2 --------------------
def get_watched_avg_rating(user_data):
    
    """
    Calculate the average rating of the movies in the user's watched list.

    Args:
        user_data (dict): A dictionary containing user information.
            Expected to have a key "watched", whose value is a list of 
            movie dictionaries. Each movie dictionary must contain a 
            "rating" key with a numeric value.

    Returns:
        float: The average rating of all movies in the "watched" list.
               Returns 0.0 if the list is empty.
    
    Example:
        user_data = {
            "watched": [
                {"title": "Movie A", "genre": "Horror", "rating": 3.5},
                {"title": "Movie B", "genre": "Comedy", "rating": 4.0}
            ]
        }
        get_watched_avg_rating(user_data)  # Returns 3.75
    """
    num_of_movies = len(user_data["watched"])
    rating_avg = 0
    rating_total = 0
    if not user_data["watched"]:
        return 0.0
    for movie in user_data["watched"]:
        rating_total += movie["rating"]
    rating_avg = rating_total / num_of_movies
    return rating_avg

def get_most_watched_genre(user_data):
    """
    Determine the most frequently watched genre for a user.

    Args:
        user_data (dict): A dictionary containing user information.
            Expected to have a key "watched", whose value is a list of 
            movie dictionaries. Each movie dictionary must contain 
            a "genre" key with a string value.

    Returns:
        str: The genre that appears most frequently in the "watched" list.
        None: If the "watched" list is empty.
    
    Example:
        user_data = {
            "watched": [
                {"title": "Movie A", "genre": "Horror", "rating": 3.5},
                {"title": "Movie B", "genre": "Comedy", "rating": 4.0},
                {"title": "Movie C", "genre": "Horror", "rating": 4.2}
            ]
        }
        get_most_watched_genre(user_data)  # Returns "Horror"
    """

    frequently_watched_genre = {}
    max_num = 0
    most_watched_genre = ""
    if not user_data["watched"]:
        return None
    for movie in user_data["watched"]:
        genre = movie["genre"]
        if genre in frequently_watched_genre:
            frequently_watched_genre[genre] += 1
        else:
            frequently_watched_genre[genre] = 1
    for genre , count in frequently_watched_genre.items():
        if count > max_num:
            max_num = count
            most_watched_genre = genre
    return most_watched_genre


# ------------- WAVE 3 --------------------
def get_unique_watched(user_data):
    """This function determine which movies the user has watched, but none of their friends have watched
    
    Parameters: 
        user_data: dict, 
            {
                "watched": [{}, {} , {}], 
                "friends": ["watched": [{"title": }, {}, {}]}, {"watched": [{}, {}, {}]}, {"watched": [[{}, {}, {}]}]
            }
    Output: 
        list: [{}, {}, {}] Return a list of dictionaries, that represents a list of movies
    """
    user_movies_list = set()
    friend_movies_list = set()
    only_user_watched = []

    for movie in user_data["watched"]:
        user_movies_list.add(movie["title"])
        for friend in user_data["friends"]:
            for friend_movie in friend["watched"]:
                friend_movies_list.add(friend_movie["title"])
    only_user_watched_set = user_movies_list.difference(friend_movies_list)

    for movie in user_data["watched"]:
        if movie["title"] in only_user_watched_set:
            only_user_watched.append(movie)

    return only_user_watched

def get_friends_unique_watched(user_data):
    """This function determine which movies at least one of the user's friends have watched, but the user has not watched
    
    Parameters: 
        user_data: dict, 
            {
                "watched": [{}, {} , {}], 
                "friends": ["watched": [{"title": }, {}, {}]}, {"watched": [{}, {}, {}]}, {"watched": [[{}, {}, {}]}]
            }
    Output: 
        list: [{}, {}, {}] Return a list of dictionaries, that represents a list of movies
    """
    user_movies_list = set()
    friend_movies_list = set()
    only_friends_watched = []

    for movie in user_data["watched"]:
        user_movies_list.add(movie["title"])
        for friend in user_data["friends"]:
            for friend_movie in friend["watched"]:
                friend_movies_list.add(friend_movie["title"])
    only_friends_watched_set = friend_movies_list.difference(user_movies_list)

    for friend in user_data["friends"]:
        for friend_movie in friend["watched"]:
            if friend_movie["title"] in only_friends_watched_set and friend_movie not in only_friends_watched:
                only_friends_watched.append(friend_movie)

    return only_friends_watched

# ------------- WAVE 4 --------------------
def get_available_recs(user_data):

    """
    Create a list of recommended movies for a user based on their subscriptions and friends' watched movies.

    Parameters:
        user_data (dict): 
            A dictionary containing:
            - "watched": list of movies the user has already watched
            - "friends": list of friends, each with their own "watched" list
            - "subscriptions": list of streaming services the user is subscribed to

    Returns:
        list: Movies that the user hasn't watched, that at least one friend has watched,
              and are hosted on a service in the user's subscriptions.
    """
    
    recommended_movies = []
    
    for movie in user_data["watched"]:
        for friend in user_data["friends"]:
            for movie in friend["watched"]:
                if movie not in user_data["watched"] and movie["host"] in user_data["subscriptions"]:
                    if movie not in recommended_movies:
                        recommended_movies.append(movie)
                        
    return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
# 1. Create a function named  `get_new_rec_by_genre`. This function should...
def get_new_rec_by_gen(user_data):
# - take one parameter: `user_data`
# - Consider the user's most frequently watched genre. Then, determine a list of recommended movies. A movie should be added to this list if and only if:
#   - The user has not watched it
#   - At least one of the user's friends has watched
#   - The `"genre"` of the movie is the same as the user's most frequent genre
# - Return the list of recommended movies

    most_watched_genre = get_most_watched_genre(user_data)
    recommended_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_data["watched"] and movie["genre"] == most_watched_genre:
                recommended_movies.append("genre")
    return recommended_movies


