We are given two sets of credentials, one for our account, `wiener:peter` and one for the account we want to break into `carlos:montoya`
1) Login normally with the first set of credentials.
2) Note that we are directed to a `login2` endpoint, but at this point we're actually already logged in.
3) Use the email client page to get the 2FA code and enter it to get to your user homepage. Copy this endpoint address.
4) Login as with the second set of credentials.
5) When we reach the `login2` endpoint, manually paste in the homepage URL, but replace the URL parameter with the carlos user
> Finis
