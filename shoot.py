import subprocess
import requests
import json
import time
import sys


def string_to_ascii_hex(s):
    return ''.join(f"{ord(c):02x} " for c in s)

def set_advertise_data():
    subprocess.run(["hciconfig", "hci0", "up"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.run(["hciconfig", "hci0", "leadv3"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.run(["hciconfig", "hci0", "noscan"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    cmd = [
        "hcitool", "-i", "hci0", "cmd",
        "0x08", "0x0008",
        "1B", "02", "01", "1A", "02", "0A", "07", "03", "03", "34", "12", "0F", "09",
        "5B", "45", "6E", "5D" #"39", "61", "6F", "76", "79", "56", "59"#, "5B", "31", "5D"
    ]
    url = "https://std.yu.ac.kr/atnd/jsp/std/checkLogin.jsp"

    # x-www-form-urlencoded 데이터
    #id = input('id :')
    #pwd = input('pwd :')

    id =  sys.argv[1] 
    pwd = sys.argv[2]
    data = {
        "id": id,
        "pwd": pwd
    }

    response = requests.post(url, data=data)
    data = response.json()
    name = string_to_ascii_hex(data['encUserNo'] + '[1]')
    hexname = name.split()
    #print(hexname)
    for i in hexname:
        cmd.append(i)
    #print(cmd)
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode == 0:
        print("Advertisement data set successfully!")
        time.sleep(10)
        subprocess.run(["hciconfig", "hci0", "noleadv"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Advertisement done")
    else:
        print(f"Error setting advertisement data: {result.stderr.decode()}")
    
if __name__ == "__main__":
    set_advertise_data()