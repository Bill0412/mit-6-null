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