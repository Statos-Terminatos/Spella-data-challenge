# This is my dictionary with id wines as keys, the value of the key is a dictionary

reveiews = {
    14263:{
        "reveiws": 10,
        "score": 10
    },
    29847867:{
        "reveiws": 30,
        "score": 15
    }
}

# the method keys returns a set(list of unique values)
b = reveiews.keys()
b = [14263, 29847867, 753562]

# It is saver to use get than just dict[key], because if there is no value to return it will give you an error 
for k in b:
    print reveiews[k].get('score')

# The loop will return me this 
10
15

Why to use dictionary. Because function get is optimized. if I use table i will loop through all values. 

I cannot loop throught the dictionary. I need to call the function keys that returns me the keys and then I can loop through the keys. 