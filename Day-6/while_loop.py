# With the while loop we can execute a set of statements as long as a condition is true.

i = 1
while i < 6: # It will continously return the value, until the condition is true.
  print(i)
  i += 1

######### BREAK #########
# With the break statement we can stop the loop even if the while condition is true:

a = 1
while a < 10:
  print(a)
  if a == 7: 
    break     # It will break the loop as soon as a becomes equal to 7.
  a += 1

######### CONTINUE #########
# With the continue statement we can stop the current iteration, and continue with the next:

a = 0
while a < 10:
  a += 1
  if a == 7:
    continue # It will skip 7 and continue printing after it.
  print(a)

######### ELSE #########
# With the else statement we can run a block of code once when the condition no longer is true:

a = 1
while a < 10:
  print(a)
  a += 1
else:
  print("i is no longer less than 10")

######### REBORG HURDLE-2 CHALLENGE #########
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json

######### REBORG HURDLE-3 CHALLENGE #########
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

######### REBORG HURDLE-4 CHALLENGE #########
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.jsonvv

######### REBORG MAZE CHALLENGE #########
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
  
# def jump():
#     turn_left()
    
#     while wall_on_right():
#         move()
        
#     turn_right()
#     move()
#     turn_right()
    
#     while front_is_clear():
#         move()
        
#     turn_left()
        
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()