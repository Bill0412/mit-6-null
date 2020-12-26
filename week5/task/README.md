## Job control
1. From what we have seen, we can use some `ps aux | grep` commands to get our jobs’ pids and then kill them, but there are better ways to do it. Start a `sleep 10000` job in a terminal, background it with `Ctrl-Z` and continue its execution with bg. Now use `pgrep` to find its pid and pkill to kill it without ever typing the pid itself. (Hint: use the `-af` flags).

```console
$ sleep 10000
^Z
[1]+  Stopped                 sleep 10000
$ jobs
[1]+  Stopped                 sleep 10000
$  bg %1
[1]+ sleep 10000 &
$ pgrep -f "sleep 10000"
1782277
$ pkill -f "sleep 10000"
[1]+  Terminated              sleep 10000
```

2. Say you don’t want to start a process until another completes, how you would go about it? In this exercise our limiting process will always be sleep 60 &. One way to achieve this is to use the wait command. Try launching the sleep command and having an ls wait until the background process finishes.

However, this strategy will fail if we start in a different bash session, since wait only works for child processes. One feature we did not discuss in the notes is that the kill command’s exit status will be zero on success and nonzero otherwise. kill -0 does not send a signal but will give a nonzero exit status if the process does not exist. Write a bash function called pidwait that takes a pid and waits until the given process completes. You should use sleep to avoid wasting CPU unnecessarily.(TODO)

## Terminal multiplexer
1. Follow this tmux tutorial and then learn how to do some basic customizations following these steps.
done.

## Aliases
1. Create an alias `dc` that resolves to cd for when you type it wrongly.

```bash
alias dc="cd"
```

2. Run `history | awk '{$1="";print substr($0,2)}' | sort | uniq -c | sort -n | tail -n 10` to get your top 10 most used commands and consider writing shorter aliases for them. Note: this works for Bash; if you’re using ZSH, use history 1 instead of just history.

```console
$ history 1 | awk '{$1="";print substr($0,2)}' | sort | uniq -c | sort -n | tail -n 10
  11 git diff
  12 vim fizzbuzz.py
  14 ssh root@192.168.2.1
  25 bash random.sh
  25 cd ..
  29 git add .
  33 git push origin master
  34 git status
  69 bash benchmark.sh
 162 ls
```

Well, I will consider make alias for all of them, especially the `ls` command, I will make `sl` the alias for `ls`.

## Dotfiles
Let’s get you up to speed with dotfiles.

1. Create a folder for your dotfiles and set up version control.
2. Add a configuration for at least one program, e.g. your shell, with some customization (to start off, it can be something as simple as customizing your shell prompt by setting $PS1).
3. Set up a method to install your dotfiles quickly (and without manual effort) on a new machine. This can be as simple as a shell script that calls ln -s for each file, or you could use a specialized utility.
4. Test your installation script on a fresh virtual machine.
5. Migrate all of your current tool configurations to your dotfiles repository.
6. Publish your dotfiles on GitHub.

My dotfile repository is available at [here](https://github.com/Bill0412/dotfiles).

## Remote Machines
Done. Since I'm quite familiar with this part. I think I can safely skip this exercise.

