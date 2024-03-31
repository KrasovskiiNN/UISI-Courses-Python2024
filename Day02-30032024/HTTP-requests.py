# pip install requests
# pip freeze

import requests as rq

response = rq("https://google.com")
print(response)

response = rq("https://google.com/type5")
print(response)

##########

getParams = {'param1':'value1', 'param2':'value2'}
response = rq.get("https://google.com", getParams)

print(response.url)

##########

getParams = {'param1':'value1', 'param2':'value2'}
responseGet = rq.get("https://google.com", getParams)

print(responseGet.url)

postParams = {'param1':'value1', 'param2':'value2'}
responsePost = rq.post("https://httpbin.org/post", postParams, timeout = 2)

print(responsePost.json()['form'])

##########

response = rq.options("https://google.com")
print(response.headers["Allow"])

##########

response = rq.head("https://google.com")
print(response.headers)

##########

putParams = {'param1':'value2', 'param2':'value2'}
responsePut = rq.put("https://google.com", data=putParams)
print(responsePut.status_code)

putParams2 = {'param1':'value2', 'param2':'value2'}
responsePut2 = rq.put("https://httpbin.org/put", data=putParams2)
print(responsePut2.status_code)

##########

putParams = {'param1':'value2', 'param2':'value2'}
responsePut = rq.put("https://httpbin.org/put", data=putParams)
print(responsePut.status_code)

patchParams = {'param1':'value2', 'param2':'value2'}
responsePatch = rq.patch("https://httpbin.org/patch", data=patchParams)
print(responsePatch.status_code)

##########

deleteParams = {'param1':'value2', 'param2':'value2'}
responseDelete = rq.delete("https://httpbin.org/delete", data=deleteParams)
print(responseDelete.status_code)