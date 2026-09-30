# URL
https://tryhackme.com/room/grandlarcenyautoii
# Concept
* reverse engineering  
* dot-net binary reversing
# Method of solve
* once we've unzipped all the files we see there's a dll file named `GrandLarcenyAuto.dll`
* if we decompile that file (using decompiler.com), then download all the files
* the file with all the networking details is the `PoPClient.cs` file
* we find a lot of interesting details in here:
  * there's a signing key string
  * ```C#
    SignKey = Encoding.UTF8.GetBytes("gla2_crew_sign_v1_2f9b6c8ad14e")
    ```
  * there's also a series of endpoints that we can contact:
    * `/session`, `/checkpoint`, and `/claim`
## The Session Endpoint
* the `/session` endpoint is the start of the challenge, and we have to send a POST request to it:
```C#
public void StartSession()
        {
                Status = "opening session...";
                Post("/session", "{}");
        }
```
* the response will include our session ID, the order we need to send checkpoint headers, and our token for use with the `/checkpoint` endpoint
```C#
private void OnCompleted(long result, long code, string[] headers, byte[] body)
{
    Busy = false; // Reset the busy state
    
    if (code == 200) // If HTTP OK
    {
        string jsonText = Encoding.UTF8.GetString(body);
        
        // The IL code deserializes the JSON string and assigns it to these properties:
        // JsonParsedData data = Json.Parse(jsonText);
        
        this.sessionId = data["session_id"];
        this.token = data["token"];
        this.StashOrder = data["stash_order"]; // Updates the public int[] StashOrder
        
        Status = "Session opened successfully.";
    }
    else
    {
        Status = "Session setup failed.";
        LastError = "HTTP Error " + code;
    }
}
```
* with these three parameters, we can then move on to the `/checkpoint` endpoint
# The Checkpoint Endpoint
* the `/checkpoint` endpoint requires us to send a series of POST requests in order to finish its process
* for each POST request, we will require:
  * the `session_id`
  * the `token`
  * the `step`
  * and the `sig`
* the `sig` value is a hash of a specific string
```C#
public void ReportCheckpoint(string step)
{
        // 1. Constructs a pipe-separated string and signs it with HMAC-SHA256
        string text = Sign(sessionId + "|" + step + "|" + token);
        
        // 2. Transmits the payload to the /checkpoint endpoint via the Post helper method
        Post("/checkpoint", "{\"session_id\":\"" + sessionId + "\",\"step\":\"" + step + "\",\"token\":\"" + token + "\",\"sig\":\"" + text + "\"}");
}
```
* so each time we send a POST request to `/checkpoint`, we need to update our `sig` value with a hash derived from our parameters
* after 5 requests to `/checkpoint`, we will have the `claim` step, and we're ready to receive the flag at the `/claim` endpoint
# The Claim Endpoint
* to receive the real flag from the endpoint, we need to create a hash value from all of the other steps to create the `staff` role:
```C#
public string DeriveStaffRole()
        {
                string text = string.Concat(new string[7]
                {
                        "heat5_stash",
                        StashOrder[0].ToString(),
                        "_stash",
                        StashOrder[1].ToString(),
                        "_stash",
                        StashOrder[2].ToString(),
                        "_vault"
                });
                byte[] array = SHA1.HashData(Encoding.UTF8.GetBytes(text));
                StringBuilder val = new StringBuilder(array.Length * 2);
                byte[] array2 = array;
                foreach (byte b in array2)
                {
                        val.Append(b.ToString("x2"));
                }
                return ((object)val).ToString();
        }
```
* we send the `session_id`, `role`, `sig` and `token` to the endpoint via POST to get the final flag
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
