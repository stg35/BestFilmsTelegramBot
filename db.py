from pymongo import MongoClient
from secret_data import db_connect

client = MongoClient(db_connect)
db = client['BestFilmsBot']

def addUser(id):
    """
    Function by id finds a selection of the user's films and his blacklist

    Returns: wishlist,blacklist

    """
    if db['users'].find_one({'_id': id}):
        return
    db['users'].insert_one({'_id': id,
                            'wishlist': None,
                             'blacklist': None})

def addMovieToWishlist(userId, movieId):
    """
    Function sends the movie to the collection

    Returns:None

    """
    if not db['users'].find_one({'_id': userId})['wishlist']:
        db['users'].update_one({'_id': userId}, {'$set': {'wishlist': [movieId]}})
    elif movieId not in db['users'].find_one({'_id': userId})['wishlist']:
        array = db['users'].find_one({'_id': userId})['wishlist']
        array.append(movieId)
        db['users'].update_one({'_id': userId}, {'$set': {'wishlist': array}})

def addMovieToBlacklist(userId, movieId):
    """
    Function sends the movie to the blacklist

    Returns: None

    """
    if not db['users'].find_one({'_id': userId})['blacklist']:
        db['users'].update_one({'_id': userId}, {'$set': {'blacklist': [movieId]}})
    elif movieId not in db['users'].find_one({'_id': userId})['blacklist']:
        array = db['users'].find_one({'_id': userId})['blacklist']
        array.append(movieId)
        db['users'].update_one({'_id': userId}, {'$set': {'blacklist': array}})

def viewWishlist(userId):
    """
    User id function shows selection of movies

    Returns: Selection movies

    """
    return db['users'].find_one({'_id': userId})['wishlist']

def getSelection(id):
    """
    Function by id finds and displays the name of the movie

    Returns: Name movie

    """
    return {
        'selection_name': db['selections'].find_one({'_id': id})['name'],
        'selection_films': db['selections'].find_one({'_id': id})['films']
    }