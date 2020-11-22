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

4. Use `touch` to create a new file called `semester` in missing.

5. Write the following into that file, one line at a time:
```console
#!/bin/sh
curl --head --silent https://missing.csail.mit.edu
```
The first line might be tricky to get working. It’s helpful to know that # starts a comment in Bash, and ! has a special meaning even within double-quoted (") strings. Bash treats single-quoted strings (') differently: they will do the trick in this case. See the Bash quoting manual page for more information.

6. Try to execute the file, i.e. type the path to the script (`./semester`) into your shell and press enter. Understand why it doesn’t work by consulting the output of ls (hint: look at the permission bits of the file).

Though it does not work by executing it directly, the following command will help.
```console
$ chmod u+x semester
```

- `u`: user, owner of the file
- `g`: group
- `o`: other users

7. Run the command by explicitly starting the sh interpreter, and giving it the file semester as the first argument, i.e. sh semester. Why does this work, while ./semester didn’t?

`sh semester` does work. Since `sh` is executable for all users, and the semester file is readable for all user groups. The `sh` program reads the semester file, and executes the program it reads in.

8. Look up the chmod program (e.g. use man chmod).

As I have stated in the solution to the 6th problem, `chmod u+x semester` also does the work.

The following command will also work.
```console
$ chmod 744 semester
```

9. Use chmod to make it possible to run the command ./semester rather than having to type sh semester. How does your shell know that the file is supposed to be interpreted using sh? See this page on the shebang line for more information.

The shell determines which interpreter to use by looking at the Shebang line in the `semester` file. In our case, the Shebang line indicates that the shell should use `/bin/sh` to execute the program.

10. Use | and > to write the “last modified” date output by semester into a file called last-modified.txt in your home directory.

(For checkin convenience, all the files will be in our `missing` directory)

```console
$ ls -l | grep semester | cut -c 35-46 > last-modified.txt
```

11. Write a command that reads out your laptop battery’s power level or your desktop machine’s CPU temperature from /sys. Note: if you’re a macOS user, your OS doesn’t have sysfs, so you can skip this exercise.

I'm using macOS, so this can be skipped.