import requests
import time
import math
import os

#app data
clear = lambda: os.system('cls')
url = 'https://api.hamsterkombat.io/clicker/tap'
energy_recovery_rate = 3#скорость востановления энергии const


#your data                                        ||
energy_max = 1500#сюда нужно вставить ваши данные \/ подробней откуда можно взять данные тута: https://youtu.be/PTdUmkT-yas?si=ZG-P-aj65YB6b_Un&t=2530
authorization_data = 'Bearer 1719756772367iSeaZMRbBFGevnwGMFxCQgxgZ2aFX5fknlGphjRfAlhaOPmFVB9f6fiFLBvkIidV910022900'

#========
sleep_time : int =  math.ceil(energy_max / energy_recovery_rate)

def send_post_request():
    current_timestamp = int(time.time())
    headers = {
        'Authorization': authorization_data,
        'Content-Type': 'application/json',
    }
    payload = {
        "count": energy_max,
        "availableTaps": 0,
        "timestamp": current_timestamp
    }
    response = requests.post(url, json=payload, headers=headers)
    print(response.status_code) 

while True:  
    send_post_request()
    for i in range(sleep_time):
        progress = math.floor(i / 10)
        print(f"\r<{"=" * progress}{'-' * (int(sleep_time / 10) - progress)}>   {i}/{sleep_time}", end="")
        time.sleep(1)
    clear()
