''' The file name is mbox.txt
$
-bash-4.1$ cat mbox.txt
This is first line
This is seocnd line
This is third line
This is fourth line
This is fifth line
This is sixth line
This is seventh line
-bash-4.1$ 
'''

fhand = open('mbox.txt')
for line in fhand:
    #to get rid off whitespace. \n newline is also a part of white spce
    line = line.rstrip()
    if line.startswith('This'):
        print(line)
