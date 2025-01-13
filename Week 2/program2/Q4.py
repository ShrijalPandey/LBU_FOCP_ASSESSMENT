'''
4. A kindly teacher wishes to distribute a tub of sweets between her pupils. 
She will first count the sweets and then divide them according to how many pupils 
attend that day. Write a program that will tell the teacher how many sweets to give to 
each pupil, and how many she will have left over. 
'''
total_sweets=int(input("Enter the number of sweets ")) 
pupils=int(input("Enter the number of pupils "))
how_many_sweets=int(input("How many sweets you want to give to each "))
sweets=pupils *how_many_sweets
left_over=total_sweets-sweets
if sweets>total_sweets:
    print("You can't give that many sweets to each pupil")
else:
    print (f"You have given {sweets} sweets and you have {left_over} sweets left over")