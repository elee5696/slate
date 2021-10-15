import http.client

#headers = {"x-api-key" : "m2DWpp8AUt2vV45KwMPJPioJ64abCjm6x39JHHid"}
conn = http.client.HTTPConnection("api.hq.dev.techscapevr.com")
conn.request("GET", "/common/sites", "", )

res = conn.getresponse()

print(res.status, res.reason)

data = res.read()

print(data)