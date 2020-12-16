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
- `s/REGEX/SUBSTITUTION`

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

cat ssh.log | sed 's/.*Disconnected from //' | head -n 5
user fenghe 10.181.150.39 port 51518
user fenghe 10.190.66.94 port 62265
user fenghe 10.190.64.242 port 60504
user fenghe 192.168.2.231 port 55468
user fenghe 192.168.2.231 port 55493

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