S = input()
T = ""
while S!="":
	i=(len(S)-1)//2
	T+=S[i]
	S=S[:i]+S[i+1:]
print(S)