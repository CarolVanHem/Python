def max_key_in_dict(dict):
    
    max_key = None
    max_value = None

    for key, value in dict.items():
        if max_value == None or max_value < value :
            max_key = key
            max_value = value
        
    return max_key
        
