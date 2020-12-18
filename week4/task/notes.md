## ssh shortcut
Execute a command with ssh, and create a short-cut for ssh.

### Add pub key to remote server
The should be a public key in your remote server, in the `~/.ssh/authorized_keys` file.

Note: `fenghe` is my username, and also used to name the shortcut for the remote connection.

### Config shortcut locally
In your local `~/.ssh/config` file, add the remote connection config in the following format

```bash
Host fenghe
  HostName 192.168.2.245 
  User fenghe
  IdentityFile ~/.ssh/key
```

If configured correctly, you are now able to login to the server with the shortcut.

```ssh
$ ssh fenghe
```

### References
1. https://scotch.io/tutorials/how-to-create-an-ssh-shortcut

## `journalctl`

```console
$ ssh fenghe journalctl
$ ssh fenghe journalctl | grep sshd
$ ssh fenghe 'journalctl | grep sshd | grep "Disconnected from"' | less
```

To make it more efficient, write to a log file directly.

```console
$ ssh fenghe 'journalctl | grep sshd | grep "Disconnected from"' > ssh.log
```
## `sed`
- `sed`: stream editor
- `s/REGEX/SUBSTITUTION/`

```console
$ ssh fenghe journalctl | grep sshd | grep "Disconnected from" | sed "s/.*Disconnected from //"
user fenghe 10.181.150.39 port 51518
user fenghe 10.190.66.94 port 62265
user fenghe 10.190.64.242 port 60504
user fenghe 192.168.2.231 port 55468
user fenghe 192.168.2.231 port 55493
user fenghe 192.168.2.231 port 54101
user fenghe 192.168.2.231 port 57772
user fenghe 192.168.2.231 port 59209
user fenghe 192.168.2.231 port 59907
```

```console
$ cat ssh.log | sed 's/.*Disconnected from //' | head -n 5
user turtle 10.100.123.231 port 50200
user turtle 10.100.123.231 port 50045
user turtle 10.100.123.231 port 50041
user turtle 10.100.123.231 port 50218
user turtle 10.100.123.231 port 50219
```

## Regular Expressions
- `.`: means "any single character" except newline
- `*`: zero or more of the preceding match
- `+`: one or more of the preceding match
- `[abc]`: any one character of `a`, `b` and `c`
- `(RX1|RX2)`: either something that matches `RX1` or `RX2`
- `^`: the start of the line
- `&`: the end of the line

### `g`
Regular expressions by default only match once, to match globally, add the g option.
```console
$ # replace a or be with nothing
$ echo 'aba' | sed 's/[ab]//' 
ba
$ # repalce a or be with nothing(gloabally)
$ echo 'aba' | sed 's/[ab]//g'
(nothing)
$ echo 'abac' | sed 's/[ab]//g'
c
$ echo 'abcaba' | sed 's/\(ab\)*//g'
ca
$ # equivalent to(a new syntax without )
$ echo 'abcaba' | sed -E 's/(ab)*//g'
```

### Capture group

Anything inside parentheses is a capturing group.

Get the usernames:
```console
$ cat ssh.log | sed -E 's/^.*Disconnected from (invalid |authenticating )?user (.*) [0-9.]+ port [0-9]+$/\2/' | head -n 5
turtle
turtle
turtle
turtle
turtle
```
This captures the contents in the frist capture group and by using `\1` i the substitution part replaces the lines with the content in the capturing group.


## `wc`
Count the lines of log:
```console
$ cat ssh.log | sed -E 's/^.*Disconnected from (invalid |authenticating )?user (.*) [0-9.]+ port [0-9]+$/\2/' | wc -l
273090
```

## `uniq`
Use unique to remove the duplicates:
```console
cat ssh.log | sed -E 's/^.*Disconnected from (invalid |authenticating )?user (.*) [0-9.]+ port [0-9]+$/\2/' | sort | uniq
dorsey
turtle
```

Show the counts:
```console
$ cat ssh.log | sed -E 's/^.*Disconnected from (invalid |authenticating )?user (.*) [0-9.]+ port [0-9]+$/\2/' | sort | uniq -c
  43253 dorsey
 229837 turtle
 ```

## `sort`
 Sort he results by column,
 ```console
$ cat ssh.log | sed -E 's/^.*Disconnected from (invalid |authenticating )?user (.*) [0-9.]+ port [0-9]+$/\2/' | sort | uniq -c | sort -nk1,1
 ```

Sort by default will sort by the first line, so `-k` is not necessary.
 
- `n`: numeric sort
- `k`: columns are separated by spaces
- `1,1`: starts at the first column and ends at the first column

## `tail`
Only want the last 10 lines
```console
$ cat ssh.log | sed -E 's/^.*Disconnected from (invalid |authenticating )?user (.*) [0-9.]+ port [0-9]+$/\2/' | sort | uniq -c | sort -nk1,1 | tail -n10
```

## `awk`
```console
$ cat ssh.log | sed -E 's/^.*Disconnected from (invalid |authenticating )?user (.*) [0-9.]+ port [0-9]+$/\2/' | sort | uniq -c | sort -nk1,1 | tail -n20 | awk '{print $2}' | paste -sd,
dorsey,turtle
```

- `awk` is a column based text editor.
- `paste` pastes the things with the separator specified, which is comma here.


```console
$ cat ssh.log | sed -E 's/^.*Disconnected from (invalid |authenticating )?user (.*) [0-9.]+ port [0-9]+$/\2/' | sort | uniq -c | awk '$1 > 1 && $2 ~ /^t.*e$/ {print $0}'
 229837 turtle
```

Count the lines with `awk` instead of `wc -l`:
```console
$ cat ssh.log | sed -E 's/^.*Disconnected from (invalid |authenticating )?user (.*) [0-9.]+ port [0-9]+$/\2/' | sort | uniq -c | awk 'BEGIN { rows = 0 } $1 > 1 && $2 ~ /^t.*e$/ {rows = rows + 1} END { print rows }'
```

## `bc`

```console
$ echo "1 + 2" | bc -l
```

```console
$ cat ssh.log | sed -E 's/^.*Disconnected from (invalid |authenticating )?user (.*) [0-9.]+ port [0-9]+$/\2/' | sort | uniq -c | awk '{print $1}' | paste -sd+ | bc -l
273090
```

## `R`
```console
$ apt install r-base-core
```


```console
$ cat ssh.log | sed -E 's/^.*Disconnected from (invalid |authenticating )?user (.*) [0-9.]+ port [0-9]+$/\2/' | sort | uniq -c | awk '{print $1}' | R --slave -e 'x <- scan(file="stdin", quiet=TRUE); summary(x)'
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
  43253   89899  136545  136545  183191  229837 
```