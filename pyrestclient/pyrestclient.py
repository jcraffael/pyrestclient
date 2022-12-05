import requests

api_url = "http://10.1.1.2:8080/data"
try:
    response = requests.get(api_url)
#except ConnectionRefusedError:
except requests.exceptions.RequestException as e:
    print("Error: request connection")
    raise SystemExit(e)
#conn = http.client.HTTPConnection("http://127.0.0.1", 8080)
#todo = {"test" : 123}
#try:
#    conn.request("PUT", "/data", todo)
#    r1 = conn.getresponse()
#    print("code =", r1.status)
#except socket.gaierror:
#    print("Error in requesting ")
try:    
    while True:
        action = input("Please input your action among GET and PUT: ")
        if(action != "GET" and action != "PUT"):
            print("Input not valid, please try again!")
            continue
        if(action == "PUT"):
            try:
                key, value = input("Please input your data as json entrance (e.g. \"msg hello\"): ").split()
            except ValueError:
                print("Values not match")
                continue

            try:
                todo = '{' + key + ':' +  value + '}'
                response = requests.put(api_url, json=todo)
                print("res = ", response.status_code)
                #print("and ", response.json())
            except requests.exceptions.ConnectionError:
                print("Error in putting")
            continue

        try:
            response = requests.get(api_url)
            print("res = ", response.status_code)
            print(response.json())
        except:
            print("Error in getting")
except KeyboardInterrupt:
    pass
finally:
    print("Closed... BYE!")
