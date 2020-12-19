1. Take this [short interactive regex tutorial](https://regexone.com/).

    0. Match `['abcdefg', 'abcde', 'abc']`: `abc.*`
    2. Match `['abc123xyz', 'define "123"', 'var g = 123;']`: `.*\d\d\d.*`
    2. Match `['cat.', '896.', '?=+.']`, skip `['abc1']`: `.*\.`
    2. Match `['can', 'man', 'fan']`, skip `['dan', 'ran', 'pan']`: `[cmf]an`
    2. Match `['hog', 'dog', 'bog']`: `[^b]og` 
    2. Match `['Ana', 'Bob', 'Cpc']`, skip `['aax', 'bby', 'ccz']`: `[A-Z][a-z]*`
    2. Match `['wazzzzzup', 'wazzzup']`, skip `['wazup']`: `waz{3,5}up`: `waz{3,5}up`
    2. Match `['aaaabcc', 'aabbbbc', 'aacc']`, skip `['a']`: `aa+b*c*`
    2. Match `['1 file found?', '2 files found?', '24 files found?']`, skip `['No files found.']`: `[0-9]+ files? found\?`
    2. Match `['1.   abc', '2.	abc', '3.           abc']`, skip `[2.abc]`: `[123]\.\s+abc`
    2. Match `['Mission: successful', 'Last Mission: unsuccessful', 'Next Mission: successful upon capture of target']`: `^M.*`
    2. Capture `['file_record_transcript', 'file_07241999']` from `['file_record_transcript.pdf', 'file_07241999.pdf']` respectively, skip `['testfile_fake.pdf.tmp']`: `(.*).pdf$`
    2. Capture `[['Jan 1987', '1987'], ['May 1969', '1969'], ['Aug 2011', '2011']]` from `['Jan 1987', 'May 1969', 'Aug 2011']` respectively: `(\w+\s(\d+))`
    2. Capture `[['1280', '720'], ['1920', '1600'], ['1024', '768']]` from `['1280x720', '1920x1600', '1024x768']` respectively: `(\d*)x(\d*)`
    2. Match `['I love cats', 'I love cats']`, skip `['I love logs', 'I love cogs']`: `I\slove\s(cat|dog)s`
    2. Match `['The quick brown fox jumps over the lazy dog.', 'There were 614 instances of students getting 90.0% or above.', 'The FCC had to censor the network for saying &$#*@!.']`: `The(re)?\s((\w+)\s)+(dog|90\.0%((\s\w+))+|\W+).`

2. Find the number of words (in `/usr/share/dict/words`) that contain at least three `a`s and don’t have a `'s` ending. What are the three most common last two letters of those words? `sed`’s `y` command, or the `tr` program, may help you with case insensitivity. How many of those two-letter combinations are there? And for a challenge: which combinations do not occur?