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
    # If those three attributes are truthy, then return a dictionary
    # This dictionary should have three key-value pairs, with specific keys
    # The three keys should be "title", "genre", and "rating"
    # The values of these key-value pairs should be appropriate values
    if title and genre and rating:
        movie_dict["title"] = title
        movie_dict["genre"] = genre
        movie_dict["rating"] = rating
        return movie_dict
    else: # If title is falsy, genre is falsy, or rating is falsy, this function should return None
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
    # An empty list represents that the user has no movies in their watchlist
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
        if title in movie.values(): # If the title is in a movie in the user's watchlist:
            user_data["watchlist"].remove(movie) # remove that movie from the watchlist
            user_data["watched"].append(movie) # add that movie to watched
            return user_data # return the user_data
    
    # If the title is not a movie in the user's watchlist:
    return user_data # return the user_data
# -----------------------------------------


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






# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

