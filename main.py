# curl -X POST https://pixe.la/v1/users -d '{"token":"thisissecret", "username":"a-know", "agreeTermsOfService":"yes", "notMinor":"yes"}'
# {"message":"Success.","isSuccess":true}
from pip._vendor import requests
import datetime

END_POINTS_PIXE = "https://pixe.la/v1/users"
# GET_GRAPH_END = "https://pixe.la/v1/"
USERNAME = "badar"
TOKEN = "badardani11"
day = datetime.datetime.now()
date_str = str(day.year) + str(day.month) + str(day.day)
quantity = "5"

# param = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
graph_id_config = {
    "date":date_str,
    "quantity": quantity,
}
# Account Has been created, use only for account creation
# response = requests.post(url = END_POINTS_PIXE, json = param)
# print(response.text)


graph_end_point = f"{END_POINTS_PIXE}/{USERNAME}/graphs"
# print(graph_end_point)
graph_config = {
    "id": "graph1",
    #     "name": "Programing",
    #     "unit": "commit",
    #     "type": "int",
    #     "color": "kuro",
}

header = {
    "X-USER-TOKEN": TOKEN
}
# Graph Creation
# response = requests.post(url=graph_end_point, json=graph_config, headers=header)
# print(response.text)
response = requests.post(url=graph_end_point + f"/{graph_config['id']}", json=graph_id_config, headers=header)
print(response.text)
