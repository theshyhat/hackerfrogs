# Tool URL
https://github.com/rhinosecuritylabs/pacu
# Setting Up Pacu
* you probably want to setup Pacu in a virtual environment:
```
python -m venv myenv
virtualenv myenv
cd myenv
source bin/activate
pip install -U pacu
```
# Starting Pacu
```
pacu
```
# Common Checks
## Checking Account Permissions
```
run iam__bruteforce_permissions
```
