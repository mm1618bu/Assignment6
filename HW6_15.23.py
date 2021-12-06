def displayPermutation(s):
   #print all possible permutations
   return ''.join(s)

#recursively generates permutations
def displayPermutationHelper(li, start , end):
   #string is of length 1, just display that single letter as permutation
  
   if (start==end):
       print (displayPermutation(li))
   else:
       #iterate over whole string
      
       for i in range(start,end+1):
           temp = li[start]
           li[start] = li[i]
           li[i] = temp
           displayPermutationHelper(li, start+1, end)
          
           temp = li[start]
           li[start] = li[i]
           li[i] = temp


#here we will take input from the user
input("Enter three letters: ")
s = "ABC"
str_len = len(s)
str_l = list(s)
displayPermutationHelper(str_l, 0, str_len-1)
