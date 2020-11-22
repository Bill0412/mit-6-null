1. For this course, you need to be using a Unix shell like Bash or ZSH. If you are on Linux or macOS, you don’t have to do anything special. If you are on Windows, you need to make sure you are not running cmd.exe or PowerShell; you can use Windows Subsystem for Linux or a Linux virtual machine to use Unix-style command-line tools. To make sure you’re running an appropriate shell, you can try the command echo $SHELL. If it says something like /bin/bash or /usr/bin/zsh, that means you’re running the right program.

I am using macOS, so no extra work for this problem.

2. Create a new directory called missing under /tmp.

Created it under this directory.

3. Look up the touch program. The man program is your friend.

Before reading the man page for `touch`, I only know that this command is for creating files. For example, to create a file named `foo.txt`,
```console
$ touch foo.txt
```
- `-A` option: changes the timestamp by a difference

More options are remained to be exlored, `touch` is good at modifying some of the meta data of files.