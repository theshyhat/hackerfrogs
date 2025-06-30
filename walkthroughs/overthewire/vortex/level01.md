# username
vortex1
```
ssh vortex1@vortex.labs.overthwire.org -p 2228
```
# password
Gq#qu3bF3
# objective
* We are looking for a specific value in ptr. You may need to consider how bash handles EOF..
* We are provided with the following source code:
```
#define _GNU_SOURCE
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <stdio.h>

#define e(); if(((unsigned int)ptr & 0xff000000)==0xca000000) { setresuid(geteuid(), geteuid(), geteuid()); execlp("/bin/sh", "sh", NULL); printf("%p %p\n", &ptr,ptr); }

void print(unsigned char *buf, int len)
{
	int i;

	printf("[ ");
	for(i=0; i < len; i++) printf("%x ", buf[i]); 
	printf(" ]\n");
}

int main()
{
	unsigned char buf[512];
	unsigned char *ptr = buf + (sizeof(buf)/2);
	unsigned int x;

	while((x = getchar()) != EOF) {
		switch(x) {
			case '\n': print(buf, sizeof(buf)); continue; break;
			case '\\': ptr--; break; 
			default: e(); if(ptr > buf + sizeof(buf)) continue; ptr++[0] = x; break;
		}
	}
	printf("All done\n");
	return 0;
}
```
# method of solve


