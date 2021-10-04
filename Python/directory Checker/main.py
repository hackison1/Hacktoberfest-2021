import requests as r

url = input("Enter the url: ")

# create a data.txt in same directory
with open('data.txt') as f:
    lines = f.read()

    # create a list of each lines
    a = lines.split("\n")
    found = []
    for i in range(len(a)):
       makingRequest = r.get(f"{url}{a[i]}")
       statusCode = makingRequest.status_code
       if statusCode == 200:
           found.append(url + a[i])
           print(f"Found: - {url}{a[i]}")
       else:
           print("Url not found.") 

print(f"Total url found: {len(found)}")
