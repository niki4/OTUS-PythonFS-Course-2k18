# py_literal
Simple words (literals) analyzer created as part of OTUS Python Full Stack Developer course.

The script helps to define statistic for words (verbs) usage in your (or someones) source code.

# Installation
Just clone this repository using your favourite Git client or Download and unpack zip archive at your PC (hint: use green button 'Clone or download' at the top right corner of this Github page), e.g.:
```
git clone https://github.com/niki4/py_literal.git
```
That's it. Now follow to the "Usage" section.

# Usage
```
usage: analyzer.py [-h] [-p [PROJECT [PROJECT ...]]]

optional arguments:
  -h, --help            show this help message and exit
  -p [PROJECT [PROJECT ...]], --project [PROJECT [PROJECT ...]]
                        Project folder name(s) or path(s) to analyze
```

Another way is to specify path(s) or folder names with source code you are need to go through using the script.
```
G:\py_literal>python analyzer.py --project ./flask ./requests
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
G:\py_literal>python analyzer.py -p flask requests
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

You also may run the script without any params.
In that case it will just scan for subdirs placed in the same directory as the script.
