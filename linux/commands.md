# Linux commands basic

## file and directory
* `ls` : list all files and folders in current directory
  * `ls -a` : view all files started with .
  * `ls -l` : view more information of files 
* `mkdir` : make directory
  * `mkdir <dir_name>`
  * `mkdir -p <dir_name>/<dirname>` : create directory nested
* `pwd` : print working directory
* `cd` : change directory
* `rmdir` : remove directory
* `rm` : remove file, you can use `rm -r` to remove directory
* `cp` : copy file, you can use `cp -r` to copy directory
* `mv` : move file or directory, this command can rename file.
* `cat` : read and print files
* `tail` : read and print last 10 line in a file. you can use `tail -n N <fileName>` to print N line
* `less` : read and print file 
* `grep` : `grep <string> <file name>` to search string in file
* `find` : `find <directory> -name <filename>` to search file in directory
* `tar` :
  * `tar -cvf <finename.tar> <filename>` : create file .tar from file
  * `tar -tvf <filename.tar>` : view content of filename.tar
  * `tar -xvf <filename.tar>` : unzip file .tar
* `gzip` :
  * `gzip <filename>` : to zip a file with .gz
  * `gzip <filename.gz>` : to unzip a file.gz
* `unzip` "
  * `unzip <file.zip>` : to unzip a file.zip
  * `unzip -l <file.zip>` : to view content of file.zip

## system
* `help` : view information and config of a command
  * `<command> --help` or `<command> -h`
* `whatis` : view description of a command
  * `whatis <command>`
* `man` : view a document of constructor of a command
  * `man <command>`
* `exit` : exit of current session
* `ping <host>` : check ping of a remote server
* `who` : view list of user are logging into system
* `su` : switch to another user
  * `su <username>`
* `uname` : view system information : kernel, host, ..
  * `uname -a`
* `free` : view memory used in system
  * `free -m` : KBs
  * `free -g` : GBs
* `df` : view disk space free
* `ps` : view processes are running
* `shutdown` : shutdown system in next 1 minute, use `shutdown -r` to reboot system