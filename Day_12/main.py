#Namespaces
#Local vs Global Scope


########## SCOPE ##########

#Local Scope

#Local Scope exist within the Functions
#We can have a access of it outside of the function
 
#let see a example of local scope

def print_amount():
    amount = 2
    print(amount)

#Now if we call that function we will get the value of 2 because we print that 
#variable inside the function

#But if i try to print that variable outside of the function it will not work
print_amount()  

# print(amount)
#It will show me error of amount undefined