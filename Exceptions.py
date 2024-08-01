actor = {"name": "John McClane", "rank": "awesome"}

def get_last_name(): 
    try:
        return actor["last_name"]
    except:
        return actor["name"].split()[1]
