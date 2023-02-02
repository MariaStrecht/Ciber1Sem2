#include <stdio.h>
#include <fcntl.h>

void bar(void) {
        printf("Hello");
}

void foo(void){
        printf("World");
        int fd = open("a.txt", O_RDONLY);
        close(fd);
}

int main(int argc, char **argv){
        foo();
        return 0;
}
