odd_count=0
even_count=0
for i in range(1,11):
    if(i%2!=0):
        odd_count=odd_count+1
    else:
        even_count=even_count+1
print("the count of odd is :",odd_count)
print("The count of even is:",even_count)
