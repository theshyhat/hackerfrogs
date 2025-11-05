# username
aura
# password
TiqpedAFjwmVyBlYpzRh
# mission contents
User aegle has a good memory for numbers.
# method of solve
* This challenge requires you to input a string of numbers into the `numbers binary`
* `1 2 3 1 2 3 9 1 1 1 1 2 6`
* We're workshopping a Python script to automate the process..
```
#!/usr/bin/env python3
from pwn import ssh

# SSH Parameters
ssh_host = "hades.hackmyvm.eu"
ssh_user = "aura"
ssh_password = "TiqpedAFjwmVyBlYpzRh"
ssh_port = 6666
remote_binary = "/pwned/aura/numbers"

known_numbers = ["1"]
all_numbers = ["1","2","3","4","5","6","7","8","9","0"]
position = 0

# Global connection objects
s = None
p = None

def connect():
    """Establish SSH connection and start process"""
    global s, p
    
    if p:
        try:
            p.close()
        except:
            pass
    
    if not s:  # Only create SSH connection once
        s = ssh(host=ssh_host, user=ssh_user, password=ssh_password, port=ssh_port)
    
    p = s.process([remote_binary])
    return p

def get_response():
    try:
        response = p.recv(timeout=1).decode(errors='ignore')
        return response
    except EOFError:
        return "[EOF - Process closed]"
    except Exception as e:
        return f"[Error: {e}]"

def send_known_numbers(known_numbers):
    print(f"[*] Sending sequence: {known_numbers}")
    for i in known_numbers:
        try:
            p.sendline(i.encode('utf-8'))
            resp = get_response()
            if "[EOF" in resp or "[Error" in resp:
                return False  # Signal that connection died
            print(f"    → {resp.strip()}")
        except:
            return False
    return True

def restart_binary():
    print("[*] Restarting binary...")
    connect()
    # Skip initial output
    try:
        p.recv(timeout=1)
    except:
        pass

def test_numbers():
    global known_numbers, position
    
    while True:
        # Send known sequence
        if not send_known_numbers(known_numbers):
            print("[!] Connection died during sequence send")
            restart_binary()
            continue
        
        # Test next number
        test_num = all_numbers[position]
        print(f"[+] Guessing: {test_num}")
        
        try:
            p.sendline(test_num.encode('utf-8'))
        except:
            print("[!] Failed to send, restarting...")
            restart_binary()
            continue
        
        test_resp = get_response()
        
        # Check if connection died
        if "[EOF" in test_resp or "[Error" in test_resp:
            print(f"[!] Process died: {test_resp}")
            restart_binary()
            continue
        
        print(f"    Response: {test_resp.strip()}")
        
        if "Number OK" in test_resp or "Correct" in test_resp:
            print(f"[✓] New number found: {test_num}")
            known_numbers.append(test_num)
            position = 0
            restart_binary()
            
        elif "NO :_(" in test_resp or "Wrong" in test_resp or "Incorrect" in test_resp:
            print(f"[✗] Wrong guess")
            position += 1
            if position >= len(all_numbers):
                print("[!] Exhausted all numbers at this position")
                print(f"[!] Known sequence so far: {known_numbers}")
                break
            restart_binary()
            
        else:
            print(f"[?] Unexpected response: {test_resp}. Is this the flag?")
            # Try to continue or decide to break
            break

def main():
    try:
        connect()  # Initial connection
        
        initial_output = p.recv(timeout=2).decode(errors='ignore')
        print("=== Initial Output ===")
        print(initial_output)
        print("======================")
        
        test_numbers()
        
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user")
    finally:
        # Cleanup
        print("[*] Cleaning up...")
        if p:
            try:
                p.close()
            except:
                pass
        if s:
            try:
                s.close()
            except:
                pass

if __name__ == "__main__":
    main()
```
