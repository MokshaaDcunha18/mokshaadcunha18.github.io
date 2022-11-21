'''fhand=open('mbox.txt')
print(fhand)'''

'''stuff='hello\nworld!'
print(stuff)'''

'''fhand=open('mbox-short.txt')
inp=fhand.read()
print(len(inp))
print(inp[:20])'''

'''fhand=open('mbox-short.txt')
print(len(fhand.read()))
print(len(fhand.read()))'''

'''fhand=open('mbox-short.txt')
count=0
for line in fhand:
    if line.startswith('from:'):
        print(line)'''

'''hand=open('mbox-short.txt')
for line in fhand:
    line=line.rstrip()
    if line.startswith('From: '):
        print(line)'''

'''fhand=open('mbox-short.txt')
for line in fhand:
    line=line.rstrip() #skip 'uninteresting lines'
    if not line.startswith('From:'):
        continue  #process pur 'intersting' line
    print(line)'''

'''fhand=open('mbox-short.txt')
    for line in fhand:
        line=line.rstrip()
        if line.find('@uct.ac.za') == -1: continue
        print(line)'''

'''fname=input('enetr the file name:')
fhand=open(fname)
count=0
for line in fhand:
    if line.startswith('subject:'):
        count=count+1
print('there were' , count, 'suject lines in', fname)'''

'''fname=input('enter the file name:')
try:
    fhand=open(fname)
except:
    print('file cannot be opened:',fname)
    excit()
count=0
for line in fhand:
    if line.startswith('subject'):
        count=count+1
print('there were', count, 'subject lines in', fname)'''

'''fout=open('output.txt','w')
print(fout)
line1="this here's the wattle,\n"
print(fout.write(line1))
line2='the emblem of our land.\n'
print(fout.write(line2))'''

'''s='1 2\t 3\n 4'
print(s):
print(repr(s))'''

'''fname= input('enter the file name')
try:
    fhand = open(fname)
except:
     print('file name cannot be opened:', fname)
     exit()
count=0
for line in fhand:
    line =line.rstrip()
    print(line.upper())'''

'''fname=input('Enter the file name: ')
try:
    fhand=open(fname)
except:
    print('Fine cannot be opened:)', fname)
    exit()
count=0
total=0
for line in fhand:
    if not line.startswith('X-DSPAM-Confidence:'):continue
    t= line.find('0')
    number=float(line[t:])
    count=count+1
    total=total+number
average=total/count
print('Average spam confidence:',average)'''

'''fname=input('enter the file name:')
try:
    fhand=open(fname)
except:
    if fname == "naa naa boo boo":
        print("you jack ass")
    else:
        print("file cannot be opened:",fname)
    exit()
count = 0
for line in fhand:
    if line.startswith("subject:"):
        count = count + 1
print("There were", count, "subject lines in", fname)'''        

 


 
 

     
     
    




        
        
        
    




