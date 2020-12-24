
## Overview
- Job Control
- Terminal Multiplexer
- Dot Files
- Remote Machines


## Job Control
Running he [`sigint.py`](./sigint.py) program:
```console
$ python3 sigint.py
215^C
I got a SIGINT, but I am not stopping
443^C
I got a SIGINT, but I am not stopping
448^C
I got a SIGINT, but I am not stopping
456^\Quit (core dumped)
```

Use CTRL-Z to suspend a job
```console
$ sleep 1000
^Z
zsh: suspended  sleep 1000
```

Use `&`(ampersand) to run a job in background.

```console
$ sleep 2000 &
```

To view the jobs
```console
$ jobs
[1]  + suspended  sleep 1000
[2]  - running    sleep 2000
```

To proceed the first one(`bg` for backgound running, `fg` for foreground running),
```console
$ bg %1
$ jobs
[1]  - running    sleep 1000
[2]  + running    sleep 2000
```

To send a signal
```console
$ kill -STOP %1
$ jobs
[1]  + suspended (signal)  sleep 1000
[2]  - running    sleep 2000
```

```console
$ kill -HUP %1
[1]  + hangup     sleep 1000     
$ jobs
[2]  + running    sleep 2000   
$ kill -KILL %2
[2]  + killed     sleep 2000      
```

## Terminal Multiplexer
- Sessions
    - Windows
        - Panes


### `tmux`
Install `tmux` on macOS
```console
$ brew install tmux
```
#### Sessions

- `tmux`: Starts a new session
- `tmux new -s NAME`: Start it with that name
- `tmux ls`: Lists the current sessions
- within `tmux` type `<Ctrl-b> d`: Detach the current session
- `tmux a`: Attatch the last session
- `tmux a -t <session name>`: Attach the specified session(by name)

#### Windows
Inside `tmux`
- `<Ctrl-b> c`: Create a new window, use `<Ctrl-d>` to close it
- `<Ctrl-b> i`: Go to the i-th window, star means the current window*(`[2] 0:bash  1:bash- 2:bash  3:bash*`)
- `<Ctrl-b> p`: Go to the previous window
- `<Ctrl-b> n`: Go to the next window
- `<Ctrl-b> ,`: Rename the current window
- `<Ctrl-b> w`: List current windows

#### Panes
- `<Ctrl-b> "`: Split the current pane horizontally
- `<Ctrl-b> %`: Split the current pane vertically
- `<Ctrl-b> <direction>`: Move to the pange in the specified direction. Direction here means arrow keys
- `<Ctrl-b> z`: Toggle zoom for the current pane
- `<Ctrl-b> x`: Kills the current pane
- `<Ctrl-b> [`: Start scrollback
- `<Ctrl-b> <space>`: Cycle throught pane arrangements

## Aliases
```console
alias alias_name="command_to_alias arg1 arg2"
```

```console
# Make shorthands for common flags
alias ll="ls -lh"

# Save a lot of typing for common commands
alias gs="git status"
alias gc="git commit"
alias v="vim"

# Save you from mistyping
alias sl=ls

# Overwrite existing commands for better defaults
alias mv="mv -i"           # -i prompts before overwrite
alias mkdir="mkdir -p"     # -p make parent dirs as needed
alias df="df -h"           # -h prints human readable format

# Alias can be composed
alias la="ls -A"
alias lla="la -l"

# To ignore an alias run it prepended with \
\ls
# Or disable an alias altogether with unalias
unalias la

# To get an alias definition just call it with alias
alias ll
# Will print ll='ls -lh'
```

## Remote Machines
### Copy files over SSH
```console
$ cat localfile | ssh remote_server tee serverfile
```

- `ssh+tee`
- `scp`
- `rsync`

### Remote Mount via SSH
- [Mosh](https://mosh.org/): for mobile use, when network environment changes a lot.
- [sshfs](https://github.com/libfuse/sshfs): mount a remote folder.