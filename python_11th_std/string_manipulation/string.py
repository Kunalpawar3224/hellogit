name = "superb"

for ch in name:
    print(ch,'-',end=' ')

string1 = input("Enter a string:")
print("The",string1,"in reverse order is:")
length=len(string1)

for a in range(-1,(-length-1),-1):
    print(-length-1)
    print(string1[a] )    

print('1'+'1')    
print(1+1)
print('abc'*3)
print(3*3)

print("ku" in "kunal")
print("ku" in "KUNAL")
print("ku" not in "kunal")
print("ku" not in "KUNAL")

print('a'<'A')
print('a'>'A')
print('abc'>'ab')

print(ord('B'))
print(ord('b'))
print(chr(66))
print(chr(107))

word = "amazing"
print(word[3:],word[:5])
print(word[1:-1])
print(word[1:6:2])

string='#'
pattern=''
for a in range(5):
    pattern += string
    print(pattern)

print("kunal".capitalize())    #first character will be capatalized

game = 'the times of india'
sub = 'of'
print(game.find(sub))
print(game.find(sub,12))