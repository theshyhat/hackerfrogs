# URL
https://labs.hackadvisor.io/en/challenges/profilehub-idor
# Concept
* IDOR
* insecure API endpoint
# Method of Solve
* access the website in Burp Suite browser
* login with our test credentials `user@test.com / password123`
* access your own user profile by clicking on the button on the top-right of the screen and select `My profile`
* look at the Burp Suite HTTP history tab
* see that you made a request to this endpoint: `/api/users/2/profile`
* note that there's a number in the endpoint, which could be iterated over to get different users' info
* send a request in the burp Repeater with the this endpoint: `/api/users/1/profile`
* this returns the admin user's info, which includes a flag in the `private_notes` field

