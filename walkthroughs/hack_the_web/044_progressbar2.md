# URL
https://hack.arrrg.de/challenge/44
# Category
* programming
* cryptography
# Concept
* JavaScript reverse engineering
# Method of solve
* the code on the webpage that runs the progress bar countdown is this:
```
<script>
        const bar = document.getElementById('44_bar')
        const valueDiv = document.getElementById('value')
        const status = document.getElementById('status')
        
        const string = "SQNLPZWYVNYLZZ"
        const steps = 100000

        let step = -steps
        let value = string

        function forward() {
          const i = (((step + 1) % string.length) + string.length) % string.length
          const chars = value.split('')
          chars[i] = String.fromCharCode(65 + ((chars[i].charCodeAt(0) - 65 + 1) % 26))
          value = chars.join('')
          step++
          return value
        }
        
        function work(noTimeout) {
          if (step >= 0) {
            bar.style.width = '100%'
          } else {
            bar.style.width = (((steps+step)/steps) * 98.9 + 1) + '%'
            valueDiv.innerHTML = forward(valueDiv.innerHTML)
            status.innerHTML = '(' + (step+steps) + '/' + steps + ')'
            if (!noTimeout) {
              setTimeout(work, 1000)
            }
          }
        }
        
        window.onkeydown = () => {
          work(true)
        }
        
        setTimeout(work, 2000)
      </script>
```


This Python script will simulate the JavaScript code:
```
# Initial values
string = "SQNLPZWYVNYLZZ"
steps = 100000

value = list(string)
length = len(value)

step = -steps

def forward(step, value):
    i = (((step + 1) % len(value)) + len(value)) % len(value)
    # Rotate this character +1 through A–Z
    value[i] = chr(65 + ((ord(value[i]) - 65 + 1) % 26))
    return value

# Run all iterations
while step < 0:
    value = forward(step, value)
    step += 1

final_string = "".join(value)
print("Final string:", final_string)

```
