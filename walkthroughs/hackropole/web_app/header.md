# URL
https://hackropole.fr/en/challenges/web/fcsc2022-web-header/
# Concept
* source code analysis (Node JS)
* sending custom headers
# Method of solve
* navigate to the landing page
* note that there is a button on the page with a tab labeled "Source"
* click on that tab and we see there is Node JS code, which we assume is the app's code
```javascript
const fs = require('fs');
const express = require('express');
const escape = require('escape-html')
var favicon = require('serve-favicon');
const app = express();

app.use(favicon('favicon.ico'));
app.set('view engine', 'ejs');
app.use(express.static('public'));

app.get('/', async (req, res) => {
    var verif = req.header("X-FCSC-2022");
    if (verif == "Can I get a flag, please?") {
        var flag = fs.readFileSync("flag.txt");
        res.status(200);
        res.render("pages/index", {
            type: "success",
            msg: "Here it is: " + flag,
        });
        return res.end();
    } else {
        res.status(200);
        res.render("pages/index", {
            type: "warning",
            msg: "No flag for you. Want a meme instead?",
        });
        return res.end();
    }
});

app.get('/source', async (req, res) => {
    const source = fs.readFileSync(__filename);
    res.render("pages/source", {
        source: escape(source),
    });
    return res.end();
});

app.listen(8000);
```
* there is a section of this code which specifies how the flag is returned:
```javascript
var verif = req.header("X-FCSC-2022");
    if (verif == "Can I get a flag, please?") {
        var flag = fs.readFileSync("flag.txt");
        res.status(200);
        res.render("pages/index", {
            type: "success",
            msg: "Here it is: " + flag,
```
* so we need to send a custom header `X-FCSC-2022` with the value `Can I get a flag, please?`
```
curl -v -H "X-FCSC-2022: Can I get a flag, please?" http://localhost:8000/
```
