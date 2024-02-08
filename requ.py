import requests
import subprocess


url = "http://52.79.237.243/attend"
r = requests.post(url)
print(r)
data = r.json()
print(data)
try:
    ids = data['id']
    pwd = data['pwd']
    subprocess.run(["python3", "shoot.py",ids,pwd])
except:
    pass