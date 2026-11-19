# This script has been written to solve the Overthewire Bandit levels in a programatic way, which is required because the Bandit levels passwords are reset every few months
import paramiko

hostname = "bandit.labs.overthewire.org"
port = "2220"

user_pass = {}

for i in range(34):
  base_name = "bandit"
  combined_name = base_name + str(i)
  user_pass[combined_name] = ""

user_pass["bandit0"] = "bandit0"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Level 0
print("Level 0")
ssh_client.connect(hostname=hostname,port=port,username="bandit0",password=user_pass["bandit0"])
std_in,std_out,std_err = ssh_client.exec_command("cat readme")
output = std_out.readlines()
user_pass["bandit1"] = output[-2].split()[-1]

# Level 1
print("Level 1")
ssh_client.connect(hostname=hostname,port=port,username="bandit1",password=user_pass["bandit1"])
std_in,std_out,std_err = ssh_client.exec_command("cat ./-")
output = std_out.readlines()
user_pass["bandit2"] = output[0].strip()

# Level 2
print("Level 2")
ssh_client.connect(hostname=hostname,port=port,username="bandit2",password=user_pass["bandit2"])
std_in,std_out,std_err = ssh_client.exec_command("cat './--spaces in this filename--'")
output = std_out.readlines()
user_pass["bandit3"] = output[0].strip()

# Level 3
print("Level 3")
ssh_client.connect(hostname=hostname,port=port,username="bandit3",password=user_pass["bandit3"])
std_in,std_out,std_err = ssh_client.exec_command("cat inhere/...Hiding-From-You")
output = std_out.readlines()
user_pass["bandit4"] = output[0].strip()

# Level 4
print("Level 4")
ssh_client.connect(hostname=hostname,port=port,username="bandit4",password=user_pass["bandit4"])
std_in,std_out,std_err = ssh_client.exec_command("file /home/bandit4/inhere/* | grep ASCII")
output = std_out.readlines()
file_path = output[0].split(":")[0]
std_in,std_out,std_err = ssh_client.exec_command("cat " + file_path)
output = std_out.readlines()
user_pass["bandit5"] = output[0].strip()

# Level 5
print("Level 5")
ssh_client.connect(hostname=hostname,port=port,username="bandit5",password=user_pass["bandit5"])
std_in,std_out,std_err = ssh_client.exec_command("find inhere -size 1033c -not -executable -print0 | xargs -0 file | grep ASCII | cut -d ':' -f 1 | xargs cat")
output = std_out.readlines()
file_path = output[0].split(":")[0]
user_pass["bandit6"] = output[0].strip()

# Level 6
print("Level 6")
ssh_client.connect(hostname=hostname,port=port,username="bandit6",password=user_pass["bandit6"])
std_in,std_out,std_err = ssh_client.exec_command("find / -user bandit7 -group bandit6 -size 33c 2>/dev/null -print0 | xargs -0 cat")
output = std_out.readlines()
file_path = output[0].split(":")[0]
user_pass["bandit7"] = output[0].strip()

# End of script

print(user_pass)
