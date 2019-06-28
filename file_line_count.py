# file name is mbox.txt

fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1
    print('Line count:', count)
print('Total line', count)
