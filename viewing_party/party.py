def create_movie(title, genre, rating):
    """Create a movie dictionary.
    
    Return a dictionary with keys "title", "genre" and "rating",
    or None if any parameter is falsy
    
    Parameters:
        title,
        genre,
        rating,
    
    Returns: a dictionary in this format:
        {
            "title": "Title A",
            "genre": "Horror",
            "rating": 3.5
        }
    """

    movie_dict = {}

    if not (title and genre and rating):
        return None
    
    movie_dict["title"] = title
    movie_dict["genre"] = genre
    movie_dict["rating"] = rating
    return movie_dict


def add_to_watched(user_data, movie):
    """Add the movie to the "watched" list inside of user_data
    
    Parameters: 
        user_data: dict, 
            {"watched": [{}, {}, {}]}
        movie: dict
            {
                "title": "Title A",
                "genre": "Horror",
                "rating": 3.5
            }

    Returns:
        user_data
    """
    
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    """Add the movie to the "watchlist" list inside of user_data
    
    Parameters: 
        user_data: dict, 
            {"watchlist": [{}, {}, {}]}
        movie: dict
            {
                "title": "Title A",
                "genre": "Horror",
                "rating": 3.5
            }

    Returns:
        user_data
    """

    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    """Move a movie from the "watchlist" list to the "watched" list inside of user_data.
    
    Parameters: 
        user_data: dict, 
            {"watchlist": [{}, {}, {}], "watched": [{}, {}, {}]}
        title: str
            The title of the movie the user has watched

    Returns:
        user_data
    """
    for movie in user_data["watchlist"]:
        if movie.get("title") == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie) 
            return user_data
    return user_data


def get_watched_avg_rating(user_data):
    """Calculate the average rating of the movies in the user's watched list.

    Parameters:
        user_data (dict): A dictionary containing user information.
            Expected to have a key "watched", whose value is a list of 
            movie dictionaries. Each movie dictionary must contain a 
            "rating" key with a numeric value.

    Returns:
        float: The average rating of all movies in the "watched" list.
            Returns 0.0 if the list is empty.
    """
    num_of_movies = len(user_data["watched"])
    rating_total = 0
    if not user_data["watched"]:
        return 0.0
    for movie in user_data["watched"]:
        rating_total += movie["rating"]
    rating_avg = rating_total / num_of_movies
    return rating_avg


def get_most_watched_genre(user_data):
    """Determine the most frequently watched genre for a user.

    Parameters:
        user_data (dict): A dictionary containing user information.
            Expected to have a key "watched", whose value is a list of 
            movie dictionaries. Each movie dictionary must contain 
            a "genre" key with a string value.

    Returns:
        str: The genre that appears most frequently in the "watched" list.
        None: If the "watched" list is empty.
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
    for genre, count in frequently_watched_genre.items():
        if count > max_num:
            max_num = count
            most_watched_genre = genre
    return most_watched_genre


def get_unique_watched(user_data):
    """Determine which movies the user has watched, but none of their friends have watched
    
    Parameters: 
        user_data: dict, 
            {
                "watched": [{}, {}, {}], 
                "friends": ["watched": [{"title": }, {}, {}]}, {"watched": [{}, {}, {}]}]
            }
    Returns: 
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
    """Determine which movies at least one of the user's friends have watched,
        but the user has not watched
    
    Parameters: 
        user_data: dict, 
            {
                "watched": [{}, {}, {}], 
                "friends": ["watched": [{"title": }, {}, {}]}, {"watched": [{}, {}, {}]}, {"watched": [[{}, {}, {}]}]
            }
    Returns: 
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


def get_available_recs(user_data):
    """Create a list of recommended movies for a user based on their subscriptions and friends' watched movies.

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
    
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_data["watched"] and movie["host"] in user_data["subscriptions"]:
                if movie not in recommended_movies:
                    recommended_movies.append(movie)
                        
    return recommended_movies


def get_new_rec_by_genre(user_data):
    """Determine a list of recommended movies

    Parameters:
        user_data (dict): 
            A dictionary containing:
            - "watched": list of movies the user has already watched
            - "friends": list of friends, each with their own "watched" list

    Returns:
        list: list of recommended movies
    """

    most_watched_genre = get_most_watched_genre(user_data)
    recommended_movies = []
    for friend in user_data["friends"]:
        for friend_movie in friend["watched"]:
            if friend_movie not in user_data["watched"] and friend_movie["genre"] == most_watched_genre:
                if friend_movie not in recommended_movies:
                    recommended_movies.append(friend_movie)
    return recommended_movies


def get_rec_from_favorites(user_data):
    """Determine a list of the user's favorite movies that none of the friends have watched
    Parameters:
        user_data (dict): 
            A dictionary containing:
            - "watched": list of movies the user has already watched
            - "friends": list of friends, each with their own "watched" list
            - "favorites": list of movie dictionaries

    Returns:
        list: list of recommended movies
    """

    rec_from_favorites = []
    friend_titles_set= set()

    if not user_data["friends"]:
        return user_data["favorites"]
    else:
        for friend in user_data["friends"]:
            for friend_movie in friend["watched"]:
                friend_titles_set.add(friend_movie["title"])   
        
        for user_fav_movie in user_data["favorites"]:
            if user_fav_movie["title"] not in friend_titles_set:
                            rec_from_favorites.append(user_fav_movie)

    return rec_from_favorites