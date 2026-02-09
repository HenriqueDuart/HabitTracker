import requests
import datetime as dt


END_POINT = 'https://pixe.la/v1/users'
PIXELA_PARAMS = {
    'token':'kjshdyuejknapsoodj',
    'username':'ararar337',
    'agreeTermsOfService':'yes',
    'notMinor':'yes'
}

# Setting up a user account
# response = requests.post(url=END_POINT, json=PIXELA_PARAMS)
# print(response.text)

# Create a new graph
END_POINT_GRAPH = END_POINT + '/' + PIXELA_PARAMS['username'] + '/graphs'
GRAPH_PARAMS = {
    'id':'graph1',
    'name':'Programming routine',
    'unit':'commit',
    'type':'int',
    'color':'shibafu'
}

headers = {
    'X-USER-TOKEN':PIXELA_PARAMS['token']
}

# response = requests.post(url=END_POINT_GRAPH, json=GRAPH_PARAMS, headers=headers)
# print(response.text)
# You can visualise the tracker here:  https://pixe.la/v1/users/ararar337/graphs/graph1.html

# Post a pixel
# adjusting the date format
now = dt.datetime.now().strftime('%Y%m%d')
END_POINT_PIXEL = END_POINT_GRAPH + '/' + GRAPH_PARAMS['id']
PIXEL_PARAMS = {
    'date':now,
    'quantity':'5'
}

response = requests.post(url=END_POINT_PIXEL, json=PIXEL_PARAMS, headers=headers)
print(response)

# We can also do put (to update) and delete (to delete) requests
# same logic as above, via request.put() and requests.delete()