from helpers.db import select_all_query, insert_query;

def get_blockwords():
    query = "SELECT blockword FROM blockwords"
    return select_all_query(query)

def get_blocklines():
    query = "SELECT blockline FROM blocklines"
    return select_all_query(query)

def get_blockmessages():
    query = "SELECT blockmessage FROM blockmessages"
    return select_all_query(query)

blockmessages = get_blockmessages()
blocklines = get_blocklines()
blockwords = get_blockwords()

def update_blockwords():
    global blockwords
    blockwords = get_blockwords()
    
def update_blocklines():
    global blocklines
    blocklines = get_blocklines()

def update_blockmessages():
    global blockmessages
    blockmessages = get_blockmessages()

def add_blockword(word):
    query = "INSERT INTO blockwords (blockword) VALUES (%s);"
    return insert_query(query, (word,))

def add_blockline(word):
    query = "INSERT INTO blocklines (blockline) VALUES (%s);"
    return insert_query(query, (word,))

def add_blockmessage(word):
    query = "INSERT INTO blockmessages (blockmessage) VALUES (%s);"
    return insert_query(query, (word, ))