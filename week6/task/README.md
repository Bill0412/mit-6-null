1. If you don’t have any past experience with Git, either try reading the first couple chapters of Pro Git or go through a tutorial like Learn Git Branching. As you’re working through it, relate Git commands to the data model.

I'm relatively experienced in Git.

2. Clone the [repository for the class website](https://github.com/missing-semester/missing-semester).
Explore the version history by visualizing it as a graph.
Who was the last person to modify README.md? (Hint: use git log with an argument)

```console
$ git log -1
Merge: 58959df a6b0e39
Author: Anish Athalye <me@anishathalye.com>
Date:   Thu Dec 31 17:22:45 2020 -0500

    Merge branch 'WWRS/WWRS-lineprofiler-pyutils'
```
So Anish Athalye is the last person to modify.

What was the commit message associated with the last modification to the `collections`: line of `_config.yml`? (Hint: use `git blame` and `git show`)

```console
$ git blame _config.yml
^112ddbd (Anish Athalye 2019-01-04 22:00:31 -0500  1) # Setup
d4412ead (Anish Athalye 2019-12-01 21:26:19 -0500  2) title: 'the missing semester of your cs education'
d4412ead (Anish Athalye 2019-12-01 21:26:19 -0500  3) url: https://missing.csail.mit.edu
^112ddbd (Anish Athalye 2019-01-04 22:00:31 -0500  4) 
^112ddbd (Anish Athalye 2019-01-04 22:00:31 -0500  5) # Settings
^112ddbd (Anish Athalye 2019-01-04 22:00:31 -0500  6) markdown: kramdown
^112ddbd (Anish Athalye 2019-01-04 22:00:31 -0500  7) kramdown:
^112ddbd (Anish Athalye 2019-01-04 22:00:31 -0500  8)   input: GFM
^112ddbd (Anish Athalye 2019-01-04 22:00:31 -0500  9)   hard_wrap: false
^112ddbd (Anish Athalye 2019-01-04 22:00:31 -0500 10) highlighter: rouge
^112ddbd (Anish Athalye 2019-01-04 22:00:31 -0500 11) permalink: /:title/
^112ddbd (Anish Athalye 2019-01-04 22:00:31 -0500 12) future: true
^112ddbd (Anish Athalye 2019-01-04 22:00:31 -0500 13) # safe: true # breaks local rendering if enabled
^112ddbd (Anish Athalye 2019-01-04 22:00:31 -0500 14) timezone: America/New_York
^112ddbd (Anish Athalye 2019-01-04 22:00:31 -0500 15) analytics:
d4412ead (Anish Athalye 2019-12-01 21:26:19 -0500 16)   tracking_id: UA-53167467-11
^112ddbd (Anish Athalye 2019-01-04 22:00:31 -0500 17) 
a88b4eac (Anish Athalye 2020-01-17 15:26:30 -0500 18) collections:
a88b4eac (Anish Athalye 2020-01-17 15:26:30 -0500 19)   '2019':
a88b4eac (Anish Athalye 2020-01-17 15:26:30 -0500 20)     output: true
a88b4eac (Anish Athalye 2020-01-17 15:26:30 -0500 21)   '2020':
a88b4eac (Anish Athalye 2020-01-17 15:26:30 -0500 22)     output: true
a88b4eac (Anish Athalye 2020-01-17 15:26:30 -0500 23) 
^112ddbd (Anish Athalye 2019-01-04 22:00:31 -0500 24) # Excludes
^112ddbd (Anish Athalye 2019-01-04 22:00:31 -0500 25) exclude:
^112ddbd (Anish Athalye 2019-01-04 22:00:31 -0500 26)   - README.md
^112ddbd (Anish Athalye 2019-01-04 22:00:31 -0500 27)   - Gemfile
^112ddbd (Anish Athalye 2019-01-04 22:00:31 -0500 28)   - Gemfile.lock
fa309f93 (Anish Athalye 2020-05-16 11:13:27 -0400 29)   - vendor
$ git show fa309f93
commit fa309f93162654a5a4993df8b151a1efc26ceb5c
Author: Anish Athalye <me@anishathalye.com>
Date:   Sat May 16 11:13:27 2020 -0400

    Fix Travis CI build
...
```

So the message is `Fix Travis CI build`


3. One common mistake when learning Git is to commit large files that should not be managed by Git or adding sensitive information. Try adding a file to a repository, making some commits and then deleting that file from history (you may want to look at this).