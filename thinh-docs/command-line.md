# *COMMAND LINE*

## - FILE AND DIRECTORY

> **`cd`** *change directory*
>> *Ex:* **`cd dir1/dir2`**
>
> **`cd ..`** or  **`cd -`** *change to previous directory*
>
> **`cd ~`** *change directory to home*
>
> **`mkdir`** *create new directories (make directory)*
>
> **`mkdir -p`** *create parent/nested directory*
>> *Ex:* **`mkdir -p dir1/dir2/dir3`**
>
> **`pwd`** *print working directory*
>
> **`ls`** *list files and directories in working directory*
>> **`ls -a`** *do not ignore entries starting with .*
>> **`ls -R`** *list subdirectories recursively*
>
> **`touch [FILE_NAMEs]`** *create new empty files*
>> *Ex:* **`touch file1 file2`**
>
> **`> [FILE_NAME]`** *or* **`cat > [FILE_NAME]`** *create new files*
>
> **`cat [FILE_NAMEs]`** *show content of file*
>> *Ex:* **`cat file1 file2 file3`**
>
> **`cp [FILEs] [DESTINATION]`** *copy files to directory*
>> *Ex:* **`cp file1 file2 dir`**
>
>**`cp -r [SOURCEs] [DESTINATION]`** *copy files or directories (and all child content) to directory*
>> *Ex:* **`cp -r dir1 dir2 file1 file2 dir`**
>
> **`mv [SOURCEs] [DESTINATION]`** *move files or directories (and all child content) to directory*
>> *Ex:* **`mv file1 file2 dir1 dir2 dir`**
>
> **`rm`** *remove files*
>> *Ex:* **`rm file1 file2`**
>
>**`rm -r`** *remove files or directories (and all child content)*
>> *Ex:* **`rm -r file1 file2 dir1 dir2`**
>
> ***NOTE:***  *remove files and directories safely with trash-cli*
>> **`sudo apt-get install trash-cli -y`** *install trash-cli*
>>
>> **`~/.local/share/Trash`** *path trash is located in*
>>> **`trash-put`** *remove files or directories safely (move to trash)*
>>>
>>> **`trash-list`** *display the contents in trash*
>>>
>>> **`trash-rm`** *remove specified trashed file or directory from trash*
>>>
>>> **`trash-empty`** *remove all content in trash*
>>>
>>> **`trash-restore`** *Restore the specified file or directory in trash*
>
> **`vi [FILE_NAME]`** *or* **`vim [FILE_NAME]`** *or* **`nano [FILE_NAME]`** *edit file using nano / vi / vim text editor*
>
> **`grep`**
>
> **`find`**
>
> **`source`**
>
> **`which`**
>
> **`echo`**
>