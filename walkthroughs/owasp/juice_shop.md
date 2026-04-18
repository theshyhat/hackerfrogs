# OWASP Juice Shop "Pentesting" Notes
# Initial Scans
Nmap reports ports 22 (SSH) and 80 (HTTP) are open
# Endpoints found
## Via Regular Browsing
* `/register` <-- for user registration
* `/search` <-- for product search
* `/privacy-security/privacy-policy` <-- read the privacy policy
* `/order-history` <-- order history
* `/basket` <-- user's shopping basket
* `/recycle` <-- to order a recycling container
* `/address/saved` <-- view / input addresses
* `/saved-payment-methods` <-- view / input new credit card info
* `/wallet` <-- view / update digital wallet info
* `/wallet-web3` <-- view / update crypto wallet info
* `/privacy-security/data-export` <-- export user data in various formats
* `/dataerasure` <-- supposed to be for erasing user data
* `/privacy-security/change-password` <-- for changing the user's password
* `/privacy-security/two-factor-authentication` <-- for setting up 2FA
* `/privacy-security/last-login-ip` <-- displays the IP address of your last login
* `/contact` <-- customer feedback form
* `/complain` <-- customer complain form (can upload files)
* `/chatbot` <-- chat with the bot
* `/ftp/legal.md` <-- the legal info for the company
* `/ftp` <-- a general file repository that shouldn't be public
* `/photo-wall` <-- an endpoint where you can upload photos
* `/deluxe-membership` <-- page where you can pay for deluxe membership
* `/score-board` <-- keeps track of the vulns you've found
* `/security.txt` <-- security information for responsible disclosure
* `/robotst.txt` <-- which points us to a insecure endpoint `/ftp`
* `/.well-known/csaf` <-- contains a lot of files regarding the csaf (Common Security Advisory Framework)
## Observations
* the application uses security questions, most likely for password reset, and security questions are no longer recommended as a valid factor in password reset functions
* the application allows username re-registration, which means you can register the same user with a different password
