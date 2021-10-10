input_string=input()
length_string=int(input())
string=list(input_string)
len_str=len(string)
times=int(len_str/length_string)
j=0
k=length_string
for i in range(times):
    word=string[j:k]
    s=""
    word=s.join(word)
    print(word)
    j=j+length_string
    k=k+length_string

k=k-length_string
if(k!=len_str):
    word=string[k:len_str]
    s=""
    word=s.join(word)    
    print(word)