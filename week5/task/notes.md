
## Overview
- Job Control
- Terminal Multiplexer
- Dot Files
- Remote Machines


## Job Control
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