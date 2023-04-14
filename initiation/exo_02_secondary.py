def min_max_avg(elements):

    dict = {}

    # max_value = None
    # min_value = None

    # for number in range(len(elements)):
    #     if min_value == None or min_value < elements[number]:
    #       min_value = elements[number]  
        
    #     elif max_value == None or max_value > elements[number]: 
    #         max_value = elements[number]

    # dict["min"] = min_value
    # dict["max"] = max_value

    dict["min"] = min(elements)
    dict["max"] = max(elements)
    
    # total = 0

    # for number in elements:
    #     total = total + number
    
    # moyenne = total / len(elements)
    # dict["avg"] = moyenne

    dict["avg"] = sum(elements)/len(elements)

    return dict