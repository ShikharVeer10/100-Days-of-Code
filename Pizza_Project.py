size=input()
add_pepporoni=input()
add_extracheese=input()
bill=0 #Set the bill=0
if size=="S":
   bill+=15
elif size=="M":
     bill+=20
else:
    bill+=25
    
if add_pepporoni=="Yes":
    bill+=2
else:
    bill+=3
if add_extracheese=="Yes":
    bill+=1
print(f"Your final bill is{bill}")