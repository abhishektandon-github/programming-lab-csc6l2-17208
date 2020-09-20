import sys 

n = len(sys.argv) 
print("Total arguments passed:", n-1) 

print("Arguments passed:") 

for i in range(1, n): 
    print(sys.argv[i], end = " ") 