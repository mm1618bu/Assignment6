def displayPermutation(s):
   #this function prints
   #all the possible permutations
   return ''.join(s)

#this function will recursively generate all the permutations
def displayPermutationHelper(li, start , end):
   #if the string is of length 1 then we can
   #just display that single letter as permutation
  
   if (start==end):
       print (displayPermutation(li))
   else:
       #here we will iterate over whole string
       #and generate all the possible permutations
      
       for i in range(start,end+1):
           #here we will exchange the front and back part of the string
          
           temp = li[start]
           li[start] = li[i]
           li[i] = temp
           displayPermutationHelper(li, start+1, end)
          
           temp = li[start]
           li[start] = li[i]
           li[i] = temp


#here we will take inpute from the user and call the function
print("HELLO USER!!!")
s = "ABC"
str_len = len(s)
str_l = list(s)
displayPermutationHelper(str_l, 0, str_len-1)
