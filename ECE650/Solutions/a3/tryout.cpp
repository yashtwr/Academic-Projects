#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<sys/types.h>
#include<string.h>
#include<sys/wait.h>
#include<iostream>
int main()
{
    int fd1[2];
    //pipe(fd1[2]);
    //close(fd1[0]);
    //dup2(fd[1],1);
    int pid = fork();
    if(pid == 0)
    {
    char *args[20];
    args[0] = (char*)"g++";
    args[1] = (char*)"rgen.cpp";
    args[2] = (char*)"-o";
    args[3] = (char*)"rgen";
    //args[4] = (char*)"&&";
    //args[5] = (char*) "./rgen";
    args[4] = NULL;
    execvp((char*)"g++",args);
    execvp((char*)"./rgen",(char*){"./rgen",NULL});
    }
    else
    {
        wait(NULL);
    }
    return 0;
}