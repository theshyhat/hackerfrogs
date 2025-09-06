# URL
https://training.olicyber.it/challenges#challenge-53
# Concept
* reverse engineering Ruby code
* insecure user registation
# Method of solve
* when we look at the main.rb file that is used to create the website, we see that there is a function that creates an admin user:
```
post '/admin/init' do
  username = "admin-#{SecureRandom.hex}"
  password = SecureRandom.hex
  statement = $client.prepare("INSERT INTO users (username, password, is_admin) VALUES (?, ?, ?)")
  statement.execute(username, password, 1)
  return "{\"username\":\"#{username}\"}"
end
```
* this code creates an admin-level user and returns the name of that user, but it doesn't let us know the password
* fortunately, the same code has an insecure user registration function:
```
post '/register' do
  begin
    statement = $client.prepare("INSERT INTO users (username, password) VALUES (?, ?)")
    result = statement.execute(params[:username], params[:password])
    redirect 'login.html'
  rescue Error
    redirect 'register.html?error'
  end
end
```
* this code doesn't check if the username exists or not, which means it could be used to overwrite an existing user's password
* so first, we create an admin-level user on the system:
```
curl -X POST -d "" 'http://zio-frank.challs.olicyber.it/admin/init' 
```
* after the user has been created, we can access the registration endpoint and register a user with the same name as the admin user, and set their password to whatever we want
* login as that admin user, and the new password to get the flag
* finis
