# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

mcount = dict()
for mail in handle:
    if mail.startswith('From '):
        mail = mail.rstrip()
        lst = mail.split()
        sender = lst[1]
        mcount[sender] = mcount.get(sender, 0) + 1


bigsender = None
bigcount = None
for key, value in mcount.items():
    if bigsender == None or value > bigcount:
        bigsender = key
        bigcount = value

print(bigsender, bigcount)
