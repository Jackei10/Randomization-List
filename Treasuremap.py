Line1=[" ", " ", " "]
Line2=[" ", " ", " "]
Line3=[" ", " ", " "]
map= [Line1,Line2,Line3]
position=input("Enter location where you want to mark 'x'. ")
location1=position[0].lower()
abc=["a", "b", "c"]
letter_index=abc.index(location1)
number_index=int(position[1])-1
map[number_index][letter_index]="X"
print(f"{Line1}\n{Line2}\n{Line3}")
