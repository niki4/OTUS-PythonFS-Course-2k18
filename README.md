# py_literal
Simple words (literals) analyzer created as part of OTUS Python Full Stack Developer course.

The script helps to define statistic for words (verbs) usage in your (or someones) source code.

# Usage
Either run the script without any params, in that case it will just scan for subdirs placed in the same directory as the script. 

It's convenient when you don't know yet which folders you're need to scan, or you have lot of them to specify explicitly
```
G:\py_literal>python analyzer.py
[nltk_data] Downloading package averaged_perceptron_tagger to
[nltk_data]     C:\Users\User\AppData\Roaming\nltk_data...
[nltk_data]   Package averaged_perceptron_tagger is already up-to-
[nltk_data]       date!
No projects to analyze specified.
Going over current dir: ['.git', '.gitignore', '.idea', 'flask', 'libs', 'requests', '
__pycache__']
...
total 22 words, 22 unique
('get', 59) 1
('add', 36) 1
('is', 18) 1
('run', 17) 1
('make', 16) 1
('find', 8) 1
('handling', 8) 1
('has', 6) 1
('tearing', 6) 1
('using', 6) 1
('get', 7) 1
('is', 1) 1
('get', 48) 1
('is', 22) 1
('are', 13) 1
('add', 5) 1
('encoded', 5) 1
('encoding', 5) 1
('failed', 3) 1
('allow', 3) 1
('matching', 3) 1
('does', 3) 1
```

Another way is to specify path(s) to folders with source code you are need to go through using the script.
```
G:\py_literal>python analyzer.py ./flask ./requests
[nltk_data] Downloading package averaged_perceptron_tagger to
[nltk_data]     C:\Users\User\AppData\Roaming\nltk_data...
[nltk_data]   Package averaged_perceptron_tagger is already up-to-
[nltk_data]       date!
Analyzing these projects: ['./flask', './requests']
total 77 files
trees generated 77
functions extracted 1228
...
```

In fact, the script may consume parameters in different formats (relative or absolute), plus you may specify as many projects dirs as you want:

E.g., this also works:
```
G:\py_literal>python analyzer.py flask requests
[nltk_data] Downloading package averaged_perceptron_tagger to
[nltk_data]     C:\Users\User\AppData\Roaming\nltk_data...
[nltk_data]   Package averaged_perceptron_tagger is already up-to-
[nltk_data]       date!
Analyzing these projects: ['flask', 'requests']
total 77 files
trees generated 77
functions extracted 1228
...
```
