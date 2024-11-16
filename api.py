import csv
import json
import requests
import pandas as pd

# Parameters
location = '61231'
radius = '20'
doctortype = 'H'

# Location
url = 'https://arztsuchehessen.de/api/suggestPlzAndOrt'
header = {
    'accept': 'application/json',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
}
form_data = {'q': location}

response = requests.post(url=url, headers=header, data=form_data)
if response.status_code == 200:
    data = json.loads(response.content.decode('utf-8'))
    lat = data[0]['lat'] or "No Lat Found"
    lon = data[0]['lon']  or "No Lon Found"
    loc = f'{data[0]['plz']} {data[0]['ort']}'  or "No Loc Found"
else:
    print(f"Failed to retrieve location with status code: {response.status_code}")
    exit()

# Doctors
url = 'https://arztsuchehessen.de/api/suche'
header = {
    'accept': 'application/json',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary8AFRlRdv4BNgsr1e'
}
form_data = f'------WebKitFormBoundary8AFRlRdv4BNgsr1e\r\nContent-Disposition: form-data; name=\"doctorType\"\r\n\r\n{doctortype}\r\n------WebKitFormBoundary8AFRlRdv4BNgsr1e\r\nContent-Disposition: form-data; name=\"location[lat]\"\r\n\r\n{lat}\r\n------WebKitFormBoundary8AFRlRdv4BNgsr1e\r\nContent-Disposition: form-data; name=\"location[lon]\"\r\n\r\n{lon}\r\n------WebKitFormBoundary8AFRlRdv4BNgsr1e\r\nContent-Disposition: form-data; name=\"location[value]\"\r\n\r\n{loc}\r\n------WebKitFormBoundary8AFRlRdv4BNgsr1e\r\nContent-Disposition: form-data; name=\"radius\"\r\n\r\n{radius}\r\n------WebKitFormBoundary8AFRlRdv4BNgsr1e--\r\n'
files = {'file': form_data}

response = requests.post(url=url, headers=header, files=files)
if response.status_code == 200:
    data = json.loads(response.content.decode('utf-8'))
    df = pd.json_normalize(data["items"])

    df.to_csv('data/out/Doctors_api.csv', encoding='utf-8', index=False, quoting=csv.QUOTE_ALL, quotechar='"', sep=';')
else:
    print(f"Failed to retrieve doctors with status code: {response.status_code}")
    exit(1)
