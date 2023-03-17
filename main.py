import requests
from datetime import datetime

USERNAME = "mariamai"
TOKEN = "Just started"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_parameters)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Reading Graph",
    "unit": "Book",
    "type": "int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

#today = datetime.now()
today = datetime(year=2022, month=12, day=18)
formatted_today = today.strftime("%Y%m%d")

# To add value:
# pixel_data = {
#     "date": formatted_today,
#     "quantity": input("How many book did you read today?: ")
# }
# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)

# To replace value:
# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_today}"
# new_pixel_data = {
#     "quantity": "2"
# }
# requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)

# To delete value:
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_today}"
requests.delete(url=delete_endpoint, headers=headers)