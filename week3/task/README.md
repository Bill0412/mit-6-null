1. Complete `vimtutor`. Note: it looks best in a 80x24 (80 columns by 24 lines) terminal window.


For lesson 4.4, firstly find out the line by using, and then replace for the whole line.
```
CTRL-G
:564,564s/thee/the/g
```

- `CTRL-G`: displays your location
- `G`: goes to the end of the file
- `gg`: goes to the bottom of the file
- `number G`: goes to that line
- Typing  `%`  while the cursor is on a (,),[,],{, or } goes to its match
- `:s/old/new`: substitute the first **in a line**
- `:s/old/new/g`: substitute all **in a line**
- `:#,#s/old/new/g`: substitute between the line range specified(by `#`)
- `:%s/old/new/g`: substitute all occurrences in the file
- `:%s/old/new/gc`: to ask for confirmation for each substitution

2. Download our basic vimrc and save it to ~/.vimrc. Read through the well-commented file (using Vim!), and observe how Vim looks and behaves slightly differently with the new config.

Done

3. Install and configure a plugin: ctrlp.vim.

    1. Create the plugins directory with `mkdir -p ~/.vim/pack/vendor/start`

    2. Download the plugin: `cd ~/.vim/pack/vendor/start; git clone https://github.com/ctrlpvim/ctrlp.vim`

    3. Read the documentation for the plugin. Try using CtrlP to locate a file by navigating to a project directory, opening Vim, and using the Vim command-line to start :CtrlP.

    4. Customize CtrlP by adding configuration to your ~/.vimrc to open CtrlP by pressing Ctrl-P.

Done


4. To practice using Vim, re-do the Demo from lecture on your own machine.

Here is a broken fizz buzz implementation:
```python
def fizz_buzz(limit):
    for i in range(limit):
        if i % 3 == 0:
            print('fizz')
        if i % 5 == 0:
            print('fizz')
        if i % 3 and i % 5:
            print(i)

def main():
    fizz_buzz(10)
```

We will fix the following issues:

- Main is never called
- Starts at 0 instead of 1
- Prints “fizz” and “buzz” on separate lines for multiples of 15
- Prints “fizz” for multiples of 5
- Uses a hard-coded argument of 10 instead of taking a command-line argument

See the lecture video for the demonstration. Compare how the above changes are made using Vim to how you might make the same edits using another program. Notice how very few keystrokes are required in Vim, allowing you to edit at the speed you think.

5. Use Vim for all your text editing for the next month. Whenever something seems inefficient, or when you think “there must be a better way”, try Googling it, there probably is. If you get stuck, come to office hours or send us an email.

I will!

