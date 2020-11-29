1. Read [man ls](https://www.man7.org/linux/man-pages/man1/ls.1.html) and write an ls command that lists files in the following manner

```console
$ ls -laGth  
```

- `-l`: List files with details
- `-a`: List all the files, including hidden files
- `-h`: In human readable format(i.e. 454M instead of 454279954)
- `-t`: Order file by recency
- `-G`: Enable colorized output

2. Write bash functions `marco` and `polo` that do the following. Whenever you execute `marco` the current working directory should be saved in some manner, then when you execute `polo`, no matter what directory you are in, `polo` should cd you back to the directory where you executed `marco`. For ease of debugging you can write the code in a file `marco.sh` and (re)load the definitions to your shell by executing `source marco.sh`.

`marco.sh`:
```bash
#!/bin/bash
echo $(pwd) > /tmp/marco.tmp
```

`polo.sh`:
```bash
#!/bin/bash
cd "$(cat /tmp/marco.tmp)"
```

A small demo:
```console
foo/ $ ls
marco.sh polo.sh
foo/ $ bash marco.sh
foo/ $ chmod +x polo.sh
foo/ $ mkdir test
foo/test $ cd test
foo/test $ . ../polo.sh
foo/ $
```

3. Say you have a command that fails rarely. In order to debug it you need to capture its output but it can be time consuming to get a failure run. Write a bash script that runs the following script until it fails and captures its standard output and error streams to files and prints everything at the end. Bonus points if you can also report how many runs it took for the script to fail.

```bash
 #!/usr/bin/env bash

 n=$(( RANDOM % 100 ))

 if [[ n -eq 42 ]]; then
    echo "Something went wrong"
    >&2 echo "The error was using magic numbers"
    exit 1
 fi

 echo "Everything went according to plan"
 ```


`>&2` redirects the output to `stderr`(standard error). 

`>name` means redirect output to file `name`.
`>&number` means redirect output to file descriptor `number`, in this case `2`, i.e., `stderr`.

- `0`: stdin
- `1`: stdout
- `2`: stderr

`random.sh` in the following script refers to the script given above.
```bash
#!/usr/bin/env bash

tmp_stderr=stderr.tmp
tmp_stdout=stdout.tmp
rm -f $tmp_stderr
rm -f $tmp_stdout

while :
do
    bash random.sh 2>> $tmp_stderr >> $tmp_stdout
    if $(grep -q "error" $tmp_stderr); then
        echo "$(cat $tmp_stdout | wc -l)"
        break
    fi
done
```

4. As we covered in the lecture `find`’s `-exec` can be very powerful for performing operations over the files we are searching for. However, what if we want to do something with **all** the files, like creating a zip file? As you have seen so far commands will take input from both arguments and STDIN. When piping commands, we are connecting STDOUT to STDIN, but some commands like tar take inputs from arguments. To bridge this disconnect there’s the [xargs](https://www.man7.org/linux/man-pages/man1/xargs.1.html) command which will execute a command using STDIN as arguments. For example `ls | xargs rm` will delete the files in the current directory.
Your task is to write a command that recursively finds all HTML files in the folder and makes a zip with them. *Note that your command should work even if the files have spaces* (hint: check `-d` flag for `xargs`).
If you’re on macOS, note that the default BSD find is different from the one included in [GNU coreutils](https://en.wikipedia.org/wiki/List_of_GNU_Core_Utilities_commands). You can use -print0 on find and the -0 flag on xargs. As a macOS user, you should be aware that command-line utilities shipped with macOS may differ from the GNU counterparts; you can install the GNU versions if you like by [using brew](https://formulae.brew.sh/formula/coreutils).

From `tldr`:
- Package and compress multiple directories and files:
    `zip -r compressed.zip path/to/directory1 path/to/directory2 path/to/file`
- Delete all files with a `.backup` extension (`-print0` uses a null character to split file names, and `-0` uses it as delimiter):
    `find . -name '*.backup' -print0 | xargs -0 rm -v`

```console
$ find . -name "*.html" -print0 | xargs -0 zip -9 htmls.zip
```
