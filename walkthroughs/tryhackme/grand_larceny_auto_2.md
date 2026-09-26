# URL
https://tryhackme.com/room/grandlarcenyautoii
# Concept
* reverse engineering  
* dot-net binary reversing
# Code
```Python
import requests
import json
import hashlib
import hmac
from time import sleep

URL = "http://gla2.thm/"

secret_key = "gla2_crew_sign_v1_2f9b6c8ad14e".encode('utf-8')

checkpoint_ep = "checkpoint"
session_ep = "session"
claim_ep = "claim"

# Initial Request to Session
initial_res = requests.post(URL+session_ep)
sleep(6)
res_dict = initial_res.json() 
print(res_dict)
sess_id = res_dict["session_id"]
stash_ord = res_dict["stash_order"]
token = res_dict["token"]
step = "heat5"
final_list = ["heat5"]
# Series of Requests to Checkpoint

# create a test signature 
while True:
        sig_str = f"{sess_id}|{step}|{token}".encode('utf-8')
        sig = hmac.new(secret_key,sig_str,hashlib.sha256)
        sig_digest = sig.hexdigest()
        payload = {"session_id":sess_id, "step":step, "token":token, "sig":sig_digest}
        check_res = requests.post(URL+checkpoint_ep,json=payload)
        sleep(6)
        res_dict = check_res.json()
        step = res_dict["next"]
        final_list.append(step)
        token = res_dict["token"]
        print(res_dict)

        # Final Request to Claim
        if step == None:
                sleep(6)
                step = "claim"
                sig_str = f"{sess_id}|{step}|{token}".encode('utf-8')
                sig = hmac.new(secret_key,sig_str,hashlib.sha256)
                sig_digest = sig.hexdigest()
                final_list.pop()
                final_string = "_".join(final_list)
                final_bytes = final_string.encode('utf-8')
                staff_role = hashlib.sha1(final_bytes).hexdigest()
                final_payload = {"session_id":sess_id,"role":staff_role, "token":token, "sig":sig_digest}
                last_res = requests.post(URL+claim_ep,json=final_payload)
                print(last_res.json())
                break
```
