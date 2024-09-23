import requests
from datetime import datetime

USERNAME = "<Username>"
TOKEN = "<Token>"
GRAPH_ID = "graph1"


### Creating User
user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
pixela_endpoint = "https://pixe.la/v1/users"


# response = requests.post(url = pixela_endpoint, json=user_parameters)
# print(response.text)

### Creating Graph

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_parameters = {
    "id": GRAPH_ID,
    "name": "Workout Graph",
    "unit": "hr",
    "type": "float",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url = graph_endpoint, json = graph_parameters, headers = headers)
# print(response.text)

### POST-ing

today = datetime.now()

pixel_parameters = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you go to the gym?: "),
}

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# response = requests.post(url = pixel_endpoint, json = pixel_parameters, headers = headers)
# print(response.text)

### Updating a Pixel

day_to_update = today.strftime("%Y%m%d")
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{day_to_update}"

new_pixel_parameter = {
    "quantity" : "1.2",
}

response = requests.put(url = update_endpoint, json= new_pixel_parameter, headers=headers)
print(response.text)


### Deleting a Pixel
day_to_delete = today.strftime("%Y%m%d")
delete_enpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{day_to_delete}"

# response = requests.delete(url = delete_enpoint, headers= headers)
# print(response.text)