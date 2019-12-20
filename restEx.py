import requests
#https://www.dataquest.io/blog/python-api-tutorial/------->URL
#response = requests.get("http://api.open-notify.org/iss-now.json")
#print response.status_code--------> 200

#response1 = requests.get("http://api.open-notify.org/iss-pass")
#print response.status_code--------> 404

#response2 = requests.get("http://api.open-notify.org/iss-pass.json")
#print response1.status_code-------->400

'''
parameters = {"lat":40.71 , "lon":-74}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
print response.content
print "Same as ---------------------------------------------------------------->"
response = requests.get("http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74")
print response.content   '''

'''
best_food_chains = ["Taco Bell","Shake-Shack","Chipotle"]
print type(best_food_chains)
print best_food_chains
import json
best_food_chains_strings = json.dumps(best_food_chains)
print type(best_food_chains_strings)
print best_food_chains_strings
best_food_chains_strings_lists = json.loads(best_food_chains_strings)
print type(best_food_chains_strings_lists)
print best_food_chains_strings_lists
fast_food_franchise = {
    "Subway": 24722,
    "McDonalds": 14098,
    "Starbucks": 10821,
    "Pizza Hut": 7600
}
fast_food_franchise_string = json.dumps(fast_food_franchise)
print type(fast_food_franchise_string)
print fast_food_franchise_string    '''

'''
# Make a list of fast food chains.
best_food_chains = ["Taco Bell", "Shake Shack", "Chipotle"]

# This is a list.
print(type(best_food_chains)) 

# Import the json library
import json

# Use json.dumps to convert best_food_chains to a string.
best_food_chains_string = json.dumps(best_food_chains)

# We've successfully converted our list to a string.
print(type(best_food_chains_string))

# Convert best_food_chains_string back into a list
print(type(json.loads(best_food_chains_string)))

# Make a dictionary
fast_food_franchise = {
    "Subway": 24722,
    "McDonalds": 14098,
    "Starbucks": 10821,
    "Pizza Hut": 7600
}

# We can also dump a dictionary to a string and load it.
fast_food_franchise_string = json.dumps(fast_food_franchise)
print(type(fast_food_franchise_string))   '''
 
'''
parameters = {"lat": 37.78, "lon": -122.41}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# Get the response data as a python object.  Verify that it's a dictionary.
data = response.json()
print(type(data))
print(data)  '''

'''
response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()

# 9 people are currently in space.
print(data["number"])
print(data)      '''
#https://realpython.com/api-integration-in-python/------->URL
task = {"summary": "Take out trash", "description": "" }
resp = requests.post('https://todolist.example.com/tasks/', json=task)
if resp.status_code != 201:
    raise ApiError('POST /tasks/ {}'.format(resp.status_code))
print('Created task. ID: {}'.format(resp.json()["id"]))


