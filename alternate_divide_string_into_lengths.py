s=input()
t=int(input())
for i in range(0,len(s),t):
 print (''.join(s[i:i+t]))