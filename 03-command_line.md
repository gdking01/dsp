# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path: `ls`
* creating a directory `mkdir DIRECTORY_NAME`
* deleting a directory `rm DIRECTORY_NAME`
* creating a file using `touch` command `touch FILE_NAME`
* deleting a file `rm FILE_NAME`
* renaming a file `mv OLD_NAME NEW_NAME`
* listing hidden files `ls -a`
* copying a file from one directory to another `cp OLD_DIR/OLD_NAME NEW_DIR/NEW_NAME`

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

* Search a file for a keyword: `grep FILE_NAME KEYWORD`
* print a file to the screen: `echo FILE_NAME`

---

### Q2.  List Files in Unix   

What do the following commands do:  
* `ls`  Lists non-hidden files in directory
* `ls -a`  Lists all files in directory
* `ls -l`  Lists non-hidden files, giving user, permission, and size info for each
* `ls -lh`  As above, but replace byte size with, for example, "4MB"
* `ls -lah`  As `ls lh` but also include hidden files
* `ls -t`  as  `ls` but sort by timestamp, newest first
* `ls -Glp`  list non-hidden files in long form but omit group listing and add a / to directory names


---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

* `ls -L` follows symbolic links instead of giving the info for the link itself
* `ls -mQ` outputs entries enclosed in quotes, separated by commas, for easy machine reading
* `ls -R` lists an entire document tree at once
* `ls --group-directories-first` groups directories first in the listing

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

`xargs` takes its input and breaks it into arguments suitable for piping into another command. For example, to search all files in the active directory for the word "fish", we could do

`ls -1 | xargs grep "fish"`

 

