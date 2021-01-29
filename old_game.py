#outer while loop to make sure that the game can be repeated even when  
#one of the storylines has been completed.
while True:
#a loop to make the code repeat if the input to the first decision is invalid
  while True:
    #Game created by Moaz and Thomas, this choice game is a satire game where 
    #unexpected choices bring forth unexpected outcomes. this may not be funny to most, 
    #but it was funny to us. 
    #displaying the title and storing the players' name
    print("BORING SATURDAY")
    #empty print statements to space out the console a bit 
    print()
    player_name = input("Enter Your Name: ")
    print()
    print("Man, I'm bored today. I need something to do.")
    print("1.Go to the kitchen")
    print("2.Go on a walk")
    #loop and try/except to make sure a player cannot proceed without 
    #entering a proper input. these smaller loops are repeated everytime there is
    #a new input. keeping inputs simple with numbers instead of words
    while True:  
      try:
        print()
        decision = int(input("What do you choose to do: "))
        break
      except ValueError:
        print()
        print("That is not a valid option. Try Again")
    #branching off different possible story paths.
    if decision == 1:
      print()
      print("You go down to the kitchen... there are some rummaging noises when all of a sudden you see a raccoon and a bush-like creature raiding your fridge. what do you choose to do?")
      print("1.Escape")
      print("2.Chase them")
      #branching off within branches 
      while True:
        try:
          print()
          decision_2 = int(input("What do you choose to do:  "))
          break
        except ValueError:
          print()
          print("That is not a valid option. Try Again")  
      if decision_2 == 1:
        #f string for efficiency in calling upon variables in print statements
        print()
        print(f"The invader realizes {player_name} is a beta and they beat {player_name} to death for being a wuss")
        print()
        print("GAME OVER")
        #this break statement is repeated after most if statements in this
        #program so that it doesnt automatically loop once the if statement
        #is completed
        break
      #repeat all of the elements accordingly for all the other story paths
      elif decision_2 == 2:
        print()
        print(f"{player_name} chases them outside where they split up. which one will you chase?  ")
        print()
        print("1.Bush creature")
        print("2.Raccoon")
        decision_3 = int(input("What do you choose to do:  "))
        if decision_3 == 1:
          print()
          print(f"{player_name} chases the creature into the woods where it gathers with a child-sized ferret and a statue of George Washington. They're discussing something about a coup. {player_name} can't believe it.")
          print()
          print("1.Take a photo")
          print("2.Escape")
          print("3.Join them")
          while True:
            try:
              print()
              decision_4 = int(input("What do you choose to do:  "))
              break
            except ValueError:
              print()
              print("That is not a valid option. Try Again")
          if decision_4 == 1:
            print()
            print(f"{player_name} takes a photo. but they saw the flash so you were caught and beat to death. it's 1pm. what do you have flash on for? you deserved that, you dirty snitch.")
            print()
            print("GAME OVER")
            break
          elif decision_4 == 2:
            print()
            print(f"{player_name} attempts to escape but snaps a stick on the way out. look where you're going next time genius lol. you obviously get beat to death.")
            print()
            print("GAME OVER")
            break
          elif decision_4 == 3:
            print()
            print(f"{player_name} accepts defeat due to incompetence and join the mysterious gang. {player_name} is accepted into the group.")
            print()
            print("YOU WIN!")
            break
          #else statements used to stop players from entering undesired inputs
          else:
            print()
            print("invalid option")
            #continue statements used to automatically repeat the immediate
            #loop so that players cannot advance without the proper inputs
            continue
        if decision_3 == 2:
          print()
          print(f"{player_name} chases the raccoon a few houses down where it ends in a standoff. What will they do?")
          print()
          print("1.Throw something at it")
          print("2.Let it be")
          print("3.Grab it")
          while True:
            try:
                print()
                decision_5 = int(input("What do you choose to do: "))
                break
            except ValueError:
                print()
                print("That is not a valid option. Try Again")
          if decision_5 == 1:
              print()
              print(f"{player_name} threw a stick at the raccoon.")
              print(f"the raccoon hit it back at {player_name} with the force of 1000 suns. {player_name} incinerates and dies instantly.")
              print()
              print("GAME OVER")
              break
          elif decision_5 == 2:
              print()
              print(f"John Quiñones, host of What Would You Do appears. 'Congratulations, {player_name}. I'm John Quiñones,host of What Would You Do, and this raccoon is a paid actor. You did well.'")
              print()
              print("YOU WIN!")
              break
          elif decision_5 == 3:
              print()
              print("{player_name} tries to grab the raccoon, but is bitten by it. {player_name} transforms into a were-raccoon and wreaks havoc on everyone in town.")
              print()
              print("YOU WIN!")
              break
          else:
            print()
            print("invalid option")
            continue
            #the 'go to kitchen' potential storylines end here
    #this is what happens if the player chooses to go on a walk
    elif decision == 2:
        print()
        print(f"{player_name} is out on the street when they spot a statue of George Washington head into the forest. What will they do?")
        print()
        print("1.Ignore and continue walking.")
        print("2.Follow the statue.")
        while True:
            try:
                print()
                decision_6 = int(input("What do you choose to do:  "))
                break
            except ValueError:
                print()
                print("That is not a valid option. Try Again")
        if decision_6 == 1:
          print()
          print(f"{player_name} continued walking.")
        elif decision_6 == 2:
          print()
          print(f"{player_name} was spotted and caught a mean right hook from the statue. {player_name} is out cold")
          print()
          print("GAME OVER")
          break
        else:
          print()
          print("Invalid option")
          continue
        print()
        print(f"{player_name} reaches a crossroads. Which way will they go?")
        print()
        print("1.right")
        print("2.straight")
        print("3.left")
        while True:
          try:
            print()
            decision_i=int(input("Which way do you choose: "))
            break
          except ValueError:
            print()
            print("That is not a valid option. Try Again")
        if decision_i == 1:
          print()
          print(f"{player_name} stumbles across a vampire and a T-rex having a dance off in the middle of the street. What will you do?")
          print()
          print("1.Join in")
          print("2.Ignore them")
          while True:
            try:
              print()
              int_right=int(input("What will you do"))
              break
            except ValueError:
              print()
              print("That is not a valid option. Try Again")
          if int_right==1:
            print()
            print(f"{player_name} decides to show them why they call you the modern Micheal Jackson. They are thouroughly impressed and decide to become your buddies")
            print()
            print("YOU WIN")
            break
          elif int_right==2:
            print()
            print(f"{player_name} decided to ignore them. Unfortunately they caught you before you could leave. They decided to give you the beats because you wanted to be a lame")
            print()
            print("GAME OVER")
            break
        elif decision_i == 2:
          print()
          print(f"{player_name} decided to be foolish and went straight. You were obviously trampled by a marching band of elephants")
          print()
          print("GAME OVER")
          break
        elif decision_i == 3:
          print()
          print(f"{player_name} heads left and you are met with 2 old ladies arguing about a shared yard. What will you do?")
          print()
          print("1.Try to act as a mediator")
          print()
          print("2.Ignore them")
          while True:
            try:
              print()
              int_left=int(input("What will you do:  "))
              break
            except ValueError:
              print()
              print("That is not a valid option. Try Again")
          if int_left==1:
            print()
            print(f"{player_name} chooses to try to help them but end up getting yourself and the other lady shot because you couldn't just mind your business")
            print()
            print("GAME OVER")
            break
          elif int_left==2:
            print()
            print(f"{player_name} decides to mind your business(as you should) and you make it home safely")
            print()
            print("YOU WIN")
            break
          else:
            print()
            print("Invalid option")
            continue
        else:
            print()
            print("Invalid option")
    else:
      print()
      print("invalid option")
      
#placed inside the outermost while loop, this allows players to decide whether or 
#not they would like to repeat
  print()
  play_again = input("Would you like to play again (yes/no): ")
  if play_again.lower() == "yes":
    print()
    print()
    print()
    print()
    continue
  elif play_again.lower() == "no":
    print()
    print("Thank you for playing.")
    break      