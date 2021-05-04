arr = input('Enter Array\n')
A = list(map(int,arr.split(' ')))

size_subseq = int(input("Enter size of subsequence\n"))
if size_subseq <= 0:
    size_subseq = int(input("Subsequence length cannot be Zero or less\nEnter size of subsequence\n"))
if len(A) < size_subseq:
    size_subseq = int(input("Subsequence length cannot be less than length of array\nEnter size of subsequence\n"))

count = 0

for i in range(len(A)-size_subseq+1):
    temp = 0
    for j in range(size_subseq):
        temp += A[i+j]
    if temp<=1000:
        count += 1

print(count)
