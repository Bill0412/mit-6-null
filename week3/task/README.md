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
