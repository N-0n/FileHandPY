'''
File handling
1-read
>file must be existing
>default mode
>cursor will be placed before the first byte
> 'r' is used for read

2-write
>if file is existing then that will be opened otherwise a new file will be created
>existing content will be removed and new will be written
>'w' is used for write

3-append
>if file is existing then that will be opened otherwise a new file will be created
>existing content will not be removed and new content will be added at the end of it
>the cursor will be placed at the end
>'a' is used for append


fo=open("f1.txt")
s=fo.read(9)
print(s)
fo.close

fo=open('f11.txt','a')
fo.write(" is a veryyyy imp conceptt ;)")
fo.close

'''
#1) read the content till the first space
fo=open("f1.txt")
ch=fo.read(1)
print(ch,end='')
while ch:
    if ch==' ':
        break
    ch=fo.read(1)
   

#2)count total no. of charac. in file
fo=open("f1.txt")
ch=fo.read(1)
c=0
while ch:
    c=c+1
    ch=fo.read(1)
print("Total no. of characters in file : ",c)

#3)count total no. of vowels and consonents in file
fo=open("f1.txt")
ch=fo.read(1)
c=0
v=0
while ch:
    if ch in ['a','e','i','o','u','A','E','I','O','U']:
        v=v+1
    else:
        c=c+1
    ch=fo.read(1)
print("Total no. of vowels in file : ",v)
print("Total no. of consonents in file : ",c)

#4)count total no. of lines in a file
fo=open("f1.txt")
ch=fo.read(1)
c=0
while ch:
    if ch=='\n':
        c=c+1
    ch=fo.read(1)
print("Total no. of lines in file : ",c)