# curl -X POST https://pixe.la/v1/users -d '{"token":"thisissecret", "username":"a-know", "agreeTermsOfService":"yes", "notMinor":"yes"}'
# {"message":"Success.","isSuccess":true}
from pip._vendor import requests

END_POINTS_PIXE = "https://pixe.la/v1/users"
# GET_GRAPH_END = "https://pixe.la/v1/"
USERNAME = "badar"
TOKEN = "badardani11"

param = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Account Has been created, use only for account creation
# response = requests.post(url = END_POINTS_PIXE, json = param)
# print(response.text)


graph_end_point = f"{END_POINTS_PIXE}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Programing",
    "unit": "commit",
    "type": "int",
    "color": "kuro",
}
header = {
    "X-USER-TOKEN": TOKEN
}
# Graph Creation
# response = requests.post(url=graph_end_point, json=graph_config, headers=header)
# print(response.text)

