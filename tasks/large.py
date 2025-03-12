def number_list(items):
    
    largest = items[0]
    for item in items:
        if item > largest:
            largest = item
    return largest
    
results = (number_list([0,2,3,4,55,6]))
print (results)



