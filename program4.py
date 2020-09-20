# with open('file.txt', 'r') as f:
#     content = f.read()

# with open('file.txt', 'r') as f:
#     for line in f:
#         print(len(line))
    
    
# fname=input("enter file name")
# count=0             
# maxcount=0          
# l=[]                
# with open(fname,'r') as f:
#     with open(fname,'r') as f:
#         content=f.read()
#         words=content.split()
#     for i in range(len(words)):
#         for j in range(len(words)):
#             if(words[i]==words[j]):        
#                 count+=1
#             else:
#                 count=count
#             if(count==maxcount):          
#                 l.append(words[i])
#             elif(count>maxcount):         
#                 l.clear()
#                 l.append(words[i])
#                 maxcount=count
#             else:
#                 l=l
#             count=0
# print(count, maxcount, l)                              

f = open('file.txt', 'r')
content = f.read()

print('Content of the file: \n')
print(content)

words = content.split(' ')

dictionary = dict()

for w in words:
    if w not in dictionary.keys():
        dictionary[w.lower()] =  1
    else:
        dictionary[w.lower()] = dictionary[w.lower()] + 1

sortedList = sorted(dictionary.items(), key=lambda x: x[1], reverse = True)

i, j = sortedList[0]

print('\nMost Frequent word:',i,'\nFrequency:',j)

