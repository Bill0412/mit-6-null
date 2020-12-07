## Modes

- `i`: insertion mode
- `r`: replace mode
- `v`: visual
- `Shift-V`: visual line
- `Ctrl-V`: block visual mode
- `:`: command-line mode

### Normal Mode

- `w`; move one word foreward
- `b`: move one word backward
- `e`: end of the word
- `$`: end of line
- `0`: beginning of the line
- `^`: first none-empty character of the line
- `~`: toggle the case of the character, can be used in visual mode
- `G`: move all the way down
- `gg`: move all the way up
- `f{character}`: goes to the first occurence of the `character`
foreward in current line.
- `F{character}`: goes to the first occurence of the `character`
backward in current line.

- `t{character}` and `T{character}`: similar to `f` and `F`, but moves one less character.

#### Insert Newline
- `o`: opens a newline below and enters insert mode
- `O`: opens a newline below and enters insert mode

#### Delete & Modify
- `d{move key}`: `hjklwe` etc can be combined following `d`
- `dw`: delete the entire word
- `de`: delete until the end of the word
- `c{move key}`: deletes and enters change mode(insert mode)
- `dd`: deletes the entire line
- `cc`: deletes the entire line and enters insertion


#### Undo & Redo
- `u`: undo
- `CTRL-R`: redo

#### Move to Lines in the Scope
- `L`: lowest line in current view scope
- `M`: middle line
- `H`: highest line
- `x`: delete a single character
- `r{character}`: replace the original character by the new one

#### Copy & Paste
- `y{character}`: `y` is short for **yank**, i.e., copy 
- `yy`: copy the whole line
- `yw`: copy a single word
- `p`: paste

### Visual Mode
To enter visual mode
- `v`: visual
- `Shift-V`: visual line, select by line
- `Ctrl-V`: block visual mode. select by block

### Commands

- `:w`“ Write
- `:help`: `:help :w` show the manual page for write
- `:e{name of file}`: open file to edit

## Settings
### Line numbers
- Show line number: `:set number`
- Turn of line numbering: `:set nonumber`

#### Relative line number
- `:set relativenumber`