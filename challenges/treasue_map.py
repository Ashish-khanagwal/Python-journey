row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# after entering the value in position, we know that it will going to be an string.
# to get hold of this value, we have to store this value in varaible.
horizontal = int(position[0])
vertical = int(position[1])

# now we have to use this value to get the treasure in the map and for this we have to plot the values.
selected_row = map[vertical-1]
selected_row[horizontal-1] = "X"

print(f"{row1}\n{row2}\n{row3}")