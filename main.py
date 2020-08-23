print("welcome to my first game")
name=input("what is your name?")
print(name)
age=int(input("what is ur age:"))
#print("hello",name,"you are",age,"years old")

Health =10 #is_older=age>=18
print("you are starting with ",Health,"Health")
if age>=18:
  print("you are old enough!")
  wants_to_play=input("Do you want to play?").lower()
  if wants_to_play=="yes":
    print("Let's play!")
    left_or_right=input("First choice...Left or left_or_right(left/right)?")
    if left_or_right=="left":   # and weapon=="":hare
      ans=input("Nice,You follow the path and reach a lake....Do you swim across or go around (across/around)?")

      if ans=="around":
        print("You went around and reach the other side of lake")

      elif ans=="across":
        print("you manage to get across, but were bit by a fish and lost 5 health")
        Health-=5
      ans=input("You notice a house and a river.Which do you go to (river/house)?")
      if ans=="house":
        print("you go to the house and are greted by the owner...He doent like you and you lose 5 health")
        Health-=5
        if Health<=0:
          print("you now have 0 health and you lose the game...")
        else:
          print("you have survived....You win!") 
      else:
        print("you fell in river and lost")
 
    else:
      print("you fall down and lost...")
  else:
    print("cya...")

#elif age>=14:     #if its not true skip rest
  #print("you can play with supervision")
else:
  print("you are not old enough to play...")


#print(is_older)
'''
5==5 and 7==8->True



x=9
y=8
x+=y,x=x+y
z=x**(y+y)  x raise to power of y + y
z=x%y->1 How many times 8 goes to y, whats the remainder
Division
x=5,y=2, z=x//y   gives 2, how many times y is in 5
others,  <,>,<=,>=,==,!=




hello_world=9
yes="hello"
hello=hello_world+9







string "hello","hi",'89'
int 23,55,-584,099090
float 6.0,100.0
bool True, False
'''

