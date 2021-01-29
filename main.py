from tkinter import *
root=Tk()

def game():
        print()
        print("BORING SATURDAY")
        print()
        username=input("Enter your name: ")

  def raccoon_invest():
      print()
      print(f"{username} finds a raccoon and a creature rummaging through your fridge")
      print("1. Ignore them and leave")
      print("2. Chase them outside")
      
      myButtonp=Button(root, text="Ignore them and leave", command=raccoon_beats)
      myButtont=Button(root, text="Chase them outside", command=invader_chase)

      myButtonp.pack()
      myButtont.pack()

      myButton1.pack_forget()
      myButton2.pack_forget()
      
      root.mainloop()

  
  def raccoon_beats():
      print()
      print(f"{username} was attacked because invaders realized that {username} is a dumb wuss")
      print()
      print("GAME OVER")
      game()
      




  def invader_chase():
      print()
      print("The creature and raccoon went in opposite directions...Which one will you follow?")
      print("1. The raccoon")
      print("2. The creature")

      myButton5=Button(root, text="The raccoon", command=rac_standoff)
      myButton6=Button(root, text="The creature")

      
      myButton5.pack()
      myButton6.pack()

      
      root.mainloop()
  





  def rac_standoff():
      print()
      print(f"{username} and the raccoon are in a standoff...What will you do?")
      print("1. Throw a stick")
      print("2. Leave it be")
      print("3. Grab it")

      myButton_throw=Button(root, text="Throw a stick", command=throw)
      myButton_leave=Button(root, text="Leave it be", command=leave)
      myButton_grab=Button(root, text="Grab it", command=grab)

      myButton_throw.pack()
      myButton_leave.pack()
      myButton_grab.pack()


      root.mainloop

  def picture():
      print()
      print(f"{username} took a picture")
      print("You idiot you left the flash on. They ended up beating you to death. Next time keep your flashlight off lol. Why do you even have it on it's the middle of the day, serves you right.")
      print()
      print("GAME OVER")
      game()



  def run():
      print()
      print(f"{username} tried to run away. You ended up stepping on a branch. What do you think they did after they heard you smooth head. They beat you to death. You were basically asking for it.")
      print()
      print("GAME OVER")
      game()



  def lefty_ignore():
      print()
      print(f"{username} decided to ignore them. Unfortunately they caught you before you could walk by. They decided that the best thing to do is give you the beats since you wanted to be a lame.")
      print()
      print("GAME OVER")
      game()

  def lefty_join():
      print()
      print("You decided to show them why they call you the Modern Day Micheal Jackson. You ended up making new buddies and bringing them over to your house.")
      print()
      print("WINNER")
      exit()
  
  
  
          
  def left():
      print()
      print("You decided to go left and were met with a vampire and a T-rex having a spectacular dance off. They notice you and ask you to join. What will you do?")
      print("1. Ignore them")
      print("2. Join them ")
      left_ignore=Button(root, text="Ignore them", command=lefty_ignore)
      left_join=Button(root, text="Join them", command=lefty_join)

      left_ignore.pack()
      left_join.pack()
      


  def straightup():
      print()
      print(f"{username} decided to be foolish and go straight. You were trampled by a band of marching elephants. How did you not see them coming from a mile away. Serves you right.")
      print()
      print("GAME OVER")
      game()


  def assist():
      print()
      print(f"{username} decided to try to help the ladies resolve their issue. Unfortunately the granny shot you and her neighbour because you just couldn't mind business")
      print()
      print("GAME OVER")
      game()

  def home():
      print()
      print(f"You decide to let the two ladies argue and head back home. {username} gets to their house safe and sound and decides to take a nap")
      print()
      print("WINNER")
      exit()
  
  


  
  def right():
      print()
      print("You head right and are met with 2 old ladies arguing about a shared yard. What will you do?")
      print("1. Help them")
      print("2. Go home")
      right_help=Button(root, text="Help them", command=assist)
      right_leave=Button(root, text="Go home", command=home)


      right_help.pack()
      right_leave.pack()





  def join():
      print()
      print(f"{username} realizes that they are too incompetent to plan out a successfull coup. So you decide to join them and help them plan.")
      print()
      print("After helping them you conclude that it's time to go and you head home")
      print()
      print(f"{username} reaches an intersection. Which way do you decide to go?")
      print("1. Right")
      print("2. Left")
      print("3. Straight")
      go_right=Button(root, text="Right", command=right)
      go_left=Button(root, text="Left", command=left)
      go_straight=Button(root, text="Straight", command=straightup)

      go_right.pack()
      go_left.pack()
      go_straight.pack()

      
      
  def ignore():
      print()
      print("The statue caught you trying to sneak away and hit you with a smooth falcon punch to the jaw.")
      print()
      print("GAME OVER")
      game()

  def follow():
      print()
      print(f"{username} follow the creature into the woods where it gathers with a child-sized ferret and a George Washington Statue. They’re discussing something about a coup.What will you do?!")
      print("1. Take a picture")
      print("2. Run away")
      print("3. Join them")
      coup_picture=Button(root, text="Take a picture", command=picture)
      coup_escape=Button(root, text="Run away", command=run)
      coup_join=Button(root, text="Join them", command=join)

      coup_picture.pack()
      coup_escape.pack()
      coup_join.pack()
            
      

  def throw():
      print()
      print("The raccoon hits the stick back with the strength of 1000 suns. You combust instantly.")
      print()
      print("GAME OVER")
      game()
  

  def grab():
      print()
      print(f"{username} tried to grab the raccoon. The raccoon bit you and response and you turned into were-raccoon. You then went on to destroy the whole town.")
      print()
      print("GAME OVER")

  def leave():
      print()
      print(f"John Quiñones, host of What Would You Do appears. 'Congratulations, {username}. I'm John Quiñones,host of What Would You Do, and this raccoon is a paid actor. You did well.'")
      print()
      print("You decide that since you're already out you might as well go on a short walk")
      print()
      print("You notice a statue of George Washington walking into a forest. What will you do next")
      print("1. Ignore it")
      print("2. Follow it")
      george_ignore=Button(root, text="Ignore it", command=ignore)
      george_follow=Button(root, text="Follow it", command=follow)

      george_ignore.pack()
      george_follow.pack()
      
  
  def walk():
      print()
      print("You notice a statue of George Washington walking into a forest. What will you do next")
      print("1. Ignore it")
      print("2. Follow it")
      george_ignore=Button(root, text="Ignore it", command=ignore)
      george_follow=Button(root, text="Follow it", command=follow)

      george_ignore.pack()
      george_follow.pack()
      
      


  
      
  print("Man I'm bored today. I need something to do.")
  print("1. Go to the kitchen")
  print("2. Go on a walk")

  myButton1 = Button(root, text="Go to the kitchen", command=raccoon_invest)
  myButton2= Button(root, text="Go on a walk", command=walk)

  myButton1.pack()
  myButton2.pack()


    


    
    root.mainloop()
            



    

game()

