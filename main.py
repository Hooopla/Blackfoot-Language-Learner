# Gabriel Bello
# CMPT 120
# CMPT Final Project
# Blackfoot Translator
# December 7 2020

# Imports
import replit  # Allows to clear the screen
import time  # Allows for the time function
import helper  # Allows for helper.py
import cmpt120image  # Allows for images
import random  # Allows for random
from replit import audio

# Load all IMGS
restaurant_img = cmpt120image.getImage("photos/restaurant.jpg")
town_img = cmpt120image.getImage("photos/town.jpg")
home_img = cmpt120image.getImage("photos/home.jpg")
greetings_img = cmpt120image.getImage("photos/greetings.jpg")
family_img = cmpt120image.getImage("photos/family.jpg")
challenge_img = cmpt120image.getImage("photos/challenge.jpg")

# When online is true app is will run if not true will end
Online = True

#Sets the highscore to 0
town_highscore = "0/10"
restaurant_highscore = "0/10"
home_highscore = "0/10"
family_highscore = "0/10"
greetings_highscore = "0/10"
challenge_highscore = "0/10"

# Town Scene
Town = True
learninTown = False
testinTown = False
moveinTown = False

# Restaurant Scene
Restaurant = False
learninRestaurant = False
testinRestaurant = False
moveinRestaurant = False

# Home Scene
Home = False
learninHome = False
testinHome = False
moveinHome = False

# Family Scene
Family = False
learninFamily = False
testinFamily = False
moveinFamily = False

# Greetings Scene
Greetings = False
learninGreetings = False
testinGreetings = False
moveinGreetings = False

# Challenge Scene
Challenge = False
testinChallenge = False
moveinChallenge = False
learninChallenge = False

while Online:
  command = input(
      "Press Enter to continue / Type in Highscore to check your scores: \n")
  if command.lower() == "highscore":
    print("Town Highscore: " + (town_highscore))
    print("Restaurant Highscore: " + (restaurant_highscore))
    print("Home Highscore: " + (home_highscore))
    print("Family Highscore: " + (family_highscore))
    print("Greetings Highscore: " + (greetings_highscore))
    print("Challenge Highscore:" + (challenge_highscore))
    pause = input("Press Enter to conitnue")
    replit.clear()
  else:
    replit.clear()

##### SCENE 1 // Town ####
# While in town
  while Town:
    # Loads the image
    cmpt120image.showImage(town_img, "town")
    print("Oki(Hello!) Welcome to Brocket, Alberta!", "\n"
          "I can teach you some Blackfoot!", "\n"
          "Want to learn words? Type(Learn)", "\n"
          "Want to move? Type(Move)", "\n"
          "Want me to test you? Type(Test)", "\n"
          "Want to leave?... Type(Exit)")
    command = input("Enter Command:")
    # If the user types exit
    if command.lower() == "exit":
      print("Good bye!")
      Online = False
      Town = False
      replit.clear
      time.sleep(3)
    # If the user types learn
    elif command.lower() == "learn":
      learninTown = True
      Town = False
      replit.clear()
    # If the user types test
    elif command.lower() == "test":
      testinTown = True
      Town = False
      replit.clear()
    # If the user types move
    elif command.lower() == "move":
      moveinTown = True
      Town = False
      replit.clear()
    # If the uer's command did not register
    else:
      print("I don't seem to understand...")
      pause = input("Press Enter to continue")
      replit.clear()
# While learning in town
  while learninTown:
    # Asks the user for a word
    command = input(
        "HINT: Type in DONE to end learning \nWhat word would you like to learn?"
    )
    word = command.lower()
    # Searches if the word is in the dictionary
    valid = (helper.linear_search(helper.valid_words, word))
    # If the user says done end learn program
    if word == "done":
      learninTown = False
      Town = True
      replit.clear()
    # If the user's word is in the dictionary translate
    elif valid == True:
      print(helper.translate(word))
      audio = helper.playsound(word)
      pause = input("Press Enter to continue..")
      replit.clear()
    # If the user's word was not found False
    elif valid == False:
      pause = input("Error.. Try again.. Press Enter to continue")
# While test in town
  while testinTown:
    # Sets the topic to town
    topic = "town"
    # Saves the top score
    town_highscore = helper.test(topic)
    # Prints the top score
    print(town_highscore)
    pause = input("Press Enter to continue")
    testinTown = False
    Town = True
    replit.clear()
# While moveinTown
  while moveinTown:
    # Shows user available moving areas
    move = input(
        "Where would you like to go?\n(Town/Restaurant/Home/Family/Greetings/Challenge)"
    )
    if move.lower() == "restaurant":
      replit.clear()
      moveinTown = False
      Town = False
      Restaurant = True
    elif move.lower() == "town":
      print("We are already here!")
      replit.clear()
    elif move.lower() == "home":
      replit.clear()
      moveinTown = False
      Town = False
      Home = True
    elif move.lower() == "family":
      replit.clear()
      moveinTown = False
      Town = False
      Family = True
    elif move.lower() == "greetings":
      replit.clear()
      moveinTown = False
      Town = False
      Greetings = True
    elif move.lower() == "challenge":
      replit.clear()
      moveinTown = False
      Town = False
      Challenge = True
    else:
      print("I don't understand.. try again..")
      time.sleep(1)
      replit.clear()
#### SCENE 2 // Restaurant ####
# While in Restaurant
  while Restaurant:
    cmpt120image.showImage(restaurant_img, "restaurant")
    print("Want to learn words? Type(Learn)", "\n"
          "Want to move? Type(Move)", "\n"
          "Want me to test you? Type(Test)", "\n"
          "Want to leave?... Type(Exit)")
    command = input("Enter Command:")
    # If the user types exit
    if command.lower() == "exit":
      print("Good bye!")
      Online = False
      Restaurant = False
      time.sleep(3)
    # If the user types learn
    elif command.lower() == "learn":
      learninRestaurant = True
      Restaurant = False
      replit.clear()
    # If the user types test
    elif command.lower() == "test":
      testinRestaurant = True
      Restaurant = False
      replit.clear()
    # If the user types move
    elif command.lower() == "move":
      moveinRestaurant = True
      Restaurant = False
      replit.clear()
    # If the user's command did not register
    else:
      print("I don't seem to understand...")
      time.sleep(1)
      replit.clear
      pause = input("Press Enter to continue")
# While learn in restaurant
  while learninRestaurant:
    # Asks the user for a word
    command = input(
        "HINT: Type in DONE to end learning \nWhat word would you like to learn?"
    )
    word = command.lower()
    # Searches if the word is in the dictionary
    valid = (helper.linear_search(helper.valid_words, word))
    # If the user says done end learn program
    if word == "done":
      learninRestaurant = False
      Restaurant = True
      replit.clear()
    # If the user's word is in the dictionary translate
    elif valid == True:
      print(helper.translate(word))
      audio = helper.playsound(word)
      pause = input("Press Enter to continue..")
      replit.clear()
    # If the user's word was not found False
    elif valid == False:
      pause = input("Error.. Try again.. Press Enter to continue")
# While test in Restaurant
  while testinRestaurant:
    # Sets the topic to Restaurant
    topic = "restaurant"
    # Saves the top score
    restaurant_highscore = helper.test(topic)
    # Prints the top score
    print(restaurant_highscore)
    pause = input("Press Enter to continue")
    testinRestaurant = False
    Restaurant = True
    replit.clear()
# While movein restaurant
  while moveinRestaurant:
    # Shows the user available moving sections
    move = input(
        "Where would you like to go? (Town/Restaurant/Home/Family/Greetings/Challenge)"
    )
    if move.lower() == "restaurant":
      print("We are already here!")
      replit.clear()
    elif move.lower() == "town":
      moveinRestaurant = False
      Restaurant = False
      Town = True
      replit.clear()
    elif move.lower() == "home":
      moveinRestaurant = False
      Restaurant = False
      Home = True
      replit.clear()
    elif move.lower() == "family":
      moveinRestaurant = False
      Restaurant = False
      Family = True
      replit.clear()
    elif move.lower() == "greetings":
      moveinRestaurant = False
      Restaurant = False
      Greetings = True
      replit.clear()
    elif move.lower() == "challenge":
      replit.clear()
      moveinRestaurant = False
      Restaurant = False
      Challenge = True
    else:
      print("I don't understand.. try again..")
      time.sleep(1)
      replit.clear()
#### SCENE 3 // Home ####
# While in Home
  while Home:
    cmpt120image.showImage(home_img, "home")
    print("Want to learn words? Type(Learn)", "\n"
          "Want to move? Type(Move)", "\n"
          "Want me to test you? Type(Test)", "\n"
          "Want to leave?... Type(Exit)")
    command = input("Enter Command:")
    # If the user types exit
    if command.lower() == "exit":
      print("Good bye!")
      Online = False
      Home = False
      replit.clear
      time.sleep(3)
    # If the user types learn
    elif command.lower() == "learn":
      learninHome = True
      Home = False
      replit.clear()
    # If the user types test
    elif command.lower() == "test":
      testinHome = True
      Home = False
      replit.clear()
    # If the user types move
    elif command.lower() == "move":
      moveinHome = True
      Home = False
      replit.clear()
    # If the uer's command did not register
    else:
      print("I don't seem to understand...")
      pause = input("Press Enter to continue")
      replit.clear()
# While learn in Home
  while learninHome:
    #Asks the user for a word
    command = input(
        "HINT: Type in DONE to end learning \nWhat word would you like to learn?"
    )
    word = command.lower()
    valid = (helper.linear_search(helper.valid_words, word))
    if word == "done":
      learninHome = False
      Home = True
      time.sleep(2)
      replit.clear()
    elif valid == True:
      print(helper.translate(word))
      audio = helper.playsound(word)
      command = input("Press Enter to continue..")
      replit.clear()
    elif valid == False:
      command = input("Error.. Try again.. Press Enter to continue")
# While movein Home
  while moveinHome:
    # Shows user avaiable moving sections
    move = input(
        "Where would you like to go? (Town/Restaurant/Home/Family/Greetings/Challenge)"
    )
    if move.lower() == "home":
      print("We are already here!")
      replit.clear()
    elif move.lower() == "town":
      moveinHome = False
      Home = False
      Town = True
      replit.clear()
    elif move.lower() == "greetings":
      moveinHome = False
      Home = False
      Greetings = True
      replit.clear()
    elif move.lower() == "restaurant":
      moveinHome = False
      Home = False
      Restaurant = True
      replit.clear()
    elif move.lower() == "family":
      moveinHome = False
      Home = False
      Family = True
      replit.clear()
    elif move.lower() == "challenge":
      replit.clear()
      moveinHome = False
      Home = False
      Challenge = True
    else:
      print("I don't understand.. try again..")
      time.sleep(1)
      replit.clear()
# While test in Home
  while testinHome:
    # Sets the topic to Home
    topic = "home"
    # Saves the top score
    home_highscore = helper.test(topic)
    # Prints the top score
    print(home_highscore)
    pause = input("Press Enter to continue")
    testinHome = False
    Home = True
    replit.clear()
#### SCENE 4 // Family ####
# While in Family
  while Family:
    cmpt120image.showImage(family_img, "family")
    print("Want to learn words? Type(Learn)", "\n"
          "Want to move? Type(Move)", "\n"
          "Want me to test you? Type(Test)", "\n"
          "Want to leave?... Type(Exit)")
    command = input("Enter Command:")
    # If the user types exit
    if command.lower() == "exit":
      print("Good bye!")
      Online = False
      Family = False
      replit.clear
      time.sleep(3)
    # If the user types learn
    elif command.lower() == "learn":
      learninFamily = True
      Family = False
      replit.clear()
    # If the user types test
    elif command.lower() == "test":
      testinFamily = True
      Family = False
      replit.clear()
    # If the user types move
    elif command.lower() == "move":
      moveinFamily = True
      Family = False
      replit.clear()
    # If the uer's command did not register
    else:
      print("I don't seem to understand...")
      pause = input("Press Enter to continue")
      replit.clear()
# While learn in Family
  while learninFamily:
    # Asks the user for a word
    command = input(
        "HINT: Type in DONE to end learning \nWhat word would you like to learn?"
    )
    word = command.capitalize()
    # Searches if the word is in the dictionary
    valid = (helper.linear_search(helper.valid_words, word))
    # If the user says done end learn program
    if word == "Done":
      learninFamily = False
      Family = True
      replit.clear()
    # If the user's word is in the dictionary translate
    elif valid == True:
      print(helper.translate(word))
      audio = helper.playsound(word)
      pause = input("Press Enter to continue..")
      replit.clear()
    # If the user's word was not found False
    elif valid == False:
      pause = input("Error.. Try again.. Press Enter to continue")
# While testin Family
  while testinFamily:
    # Sets the topic to Family
    topic = "family"
    # Saves the top score
    family_highscore = helper.test(topic)
    # Prints the top score
    print(family_highscore)
    pause = input("Press Enter to continue")
    testinFamily = False
    Family = True
    replit.clear()
# While movein Family
  while moveinFamily:
    # Shows user all the available moving sections
    move = input(
        "Where would you like to go? (Town/Restaurant/Home/Family/Greetings/Challenge)"
    )
    if move.lower() == "family":
      print("We are already here!")
      replit.clear()
    elif move.lower() == "town":
      moveinFamily = False
      Family = False
      Town = True
      replit.clear()
    elif move.lower() == "greetings":
      moveinFamily = False
      Family = False
      Greetings = True
      replit.clear()
    elif move.lower() == "restaurant":
      moveinFamily = False
      Family = False
      Restaurant = True
      replit.clear()
    elif move.lower() == "home":
      moveinFamily = False
      Family = False
      Home = True
      replit.clear()
    elif move.lower() == "challenge":
      replit.clear()
      moveinFamily = False
      Family = False
      Challenge = True
    else:
      print("I don't understand.. try again..")
      time.sleep(1)
      replit.clear()
#### SCENE 5 // Greetings ####
# While in Greetings
  while Greetings:
    cmpt120image.showImage(greetings_img, "greetings")
    print("Want to learn words? Type(Learn)", "\n"
          "Want to move? Type(Move)", "\n"
          "Want me to test you? Type(Test)", "\n"
          "Want to leave?... Type(Exit)")
    command = input("Enter Command:")
    # If the user types exit
    if command.lower() == "exit":
      print("Good bye!")
      Online = False
      Greetings = False
      replit.clear
      time.sleep(3)
    # If the user types learn
    elif command.lower() == "learn":
      learninGreetings = True
      Greetings = False
      replit.clear()
    # If the user types test
    elif command.lower() == "test":
      testinGreetings = True
      Greetings = False
      replit.clear()
    # If the user types move
    elif command.lower() == "move":
      moveinGreetings = True
      Greetings = False
      replit.clear()
    # If the uer's command did not register
    else:
      print("I don't seem to understand...")
      pause = input("Press Enter to continue")
      replit.clear()
# While learn in Greetings
  while learninGreetings:
    # Asks the user for a word
    command = input(
        "HINT: Type in DONE to end learning \nWhat word would you like to learn?"
    )
    word1 = command.capitalize()
    if word1 == "I'm doing good. you?":
      word = word1.replace('y', 'Y')
    else:
      word = word1
    # Searches if the word is in the dictionary
    valid = (helper.linear_search(helper.valid_words, word))
    # If the user says done end learn program
    if word == "Done":
      learninGreetings = False
      Greetings = True
      replit.clear()
    # If the user's word is in the dictionary translate
    elif valid == True:
      print(helper.translate(word))
      audio = helper.playsound(word)
      pause = input("Press Enter to continue..")
      replit.clear()
    # If the user's word was not found False
    elif valid == False:
      pause = input("Error.. Try again.. Press Enter to continue")
# While testin Greetings
  while testinGreetings:
    # Sets the topic to Family
    topic = "greetings"
    # Saves the top score
    greetings_highscore = helper.test(topic)
    # Prints the top score
    print(greetings_highscore)
    pause = input("Press Enter to continue")
    testinGreetings = False
    Greetings = True
    replit.clear()
# While trying to Move in Greetings
# Shows user all the available sections
  while moveinGreetings:
    move = input(
        "Where would you like to go? (Town/Restaurant/Home/Family/Greetings/Challenge)"
    )
    if move.lower() == "greetings":
      print("We are already here!")
      replit.clear()
    elif move.lower() == "town":
      moveinGreetings = False
      Greetings = False
      Town = True
      replit.clear()
      print("Press Enter to continue")
    elif move.lower() == "family":
      moveinGreetings = False
      Greetings = False
      Family = True
      replit.clear()
      print("Press Enter to continue")
    elif move.lower() == "restaurant":
      moveinGreetings = False
      Greetings = False
      Restaurant = True
      replit.clear()
      print("Press Enter to continue")
    elif move.lower() == "home":
      moveinGreetings = False
      Greetings = False
      Home = True
      replit.clear()
      print("Press Enter to continue")
    elif move.lower() == "challenge":
      replit.clear()
      print("Press Enter to continue")
      moveinGreetings = False
      Greetings = False
      Challenge = True
    else:
      print("I don't understand.. try again..")
      time.sleep(1)
      replit.clear()
#### Scene 6 // Challenge ####
# While in Challenge
  while Challenge:
    # Loads the image
    cmpt120image.showImage(challenge_img, "challenge")
    print("Oki(Hello!) Welcome to Brocket's Challenge!", "\n"
          "Want to move? Type(Move)", "\n"
          "Want me to test you? Type(Test)", "\n",
          "Want to learn challenging sentences? Type(Learn)", "\n"
          "Want to leave?... Type(Exit)")
    command = input("Enter Command:")
    # If the user types exit
    if command.lower() == "exit":
      print("Good bye!")
      Online = False
      Challenge = False
      replit.clear
      time.sleep(3)
    # If the user types learn
    elif command.lower() == "learn":
      learninChallenge = True
      Challenge = False
      replit.clear()
    # If the user types test
    elif command.lower() == "test":
      testinChallenge = True
      Challenge = False
      replit.clear()
    # If the user types move
    elif command.lower() == "move":
      moveinChallenge = True
      Challenge = False
      replit.clear()
    # If the uer's command did not register
    else:
      print("I don't seem to understand...")
      pause = input("Press Enter to continue")
      replit.clear()
# While movein Challenge
  while moveinChallenge:
    move = input(
        "Where would you like to go? (Town/Restaurant/Home/Family/Greetings/Challenge)"
    )
    if move.lower() == "challenge":
      replit.clear()
      print("We are already here!")
    elif move.lower() == "town":
      moveinChallenge = False
      Challenge = False
      Town = True
      replit.clear()
      print("Press Enter to continue")
    elif move.lower() == "family":
      moveinChallenge = False
      Challenge = False
      Family = True
      replit.clear()
      print("Press Enter to continue")
    elif move.lower() == "restaurant":
      moveinChallenge = False
      Challenge = False
      Restaurant = True
      replit.clear()
      print("Press Enter to continue")
    elif move.lower() == "home":
      moveinChallenge = False
      Challenge = False
      Home = True
      replit.clear()
      print("Press Enter to continue")
    elif move.lower() == "greetings":
      replit.clear()
      print("Press Enter to continue")
      moveinChallenge = False
      Challenge = False
      Greetings = True
    else:
      print("I don't understand.. try again..")
      time.sleep(1)
      replit.clear()
# While testin Challenge
  while testinChallenge:
    ChallengeX = 0
    total = 0  # User's total points
    if ChallengeX != 10:  # After 10 questions have been asked
      for x in range(10):
        category = random.choice(
            helper.advanced_category)  # Chooses the category
        layout = random.choice(
            helper.format_selection)  # Chooses the layout of the list.

        # If the category that was chosen is advanced town questions
        if category == "advanced_town":
          correct = helper.town_words
          incorrect = helper.not_town_words
          correct_word = random.choice(correct)
          incorrect1 = random.choice(incorrect)
          incorrect2 = random.choice(incorrect)
          incorrect3 = random.choice(incorrect)
          if layout == 1:
            list = [correct_word, incorrect1, incorrect2, incorrect3]
            # Uses the format of 2 [wrong,correct,wrong,wrong]
          elif layout == 2:
            list = [incorrect1, correct_word, incorrect2, incorrect3]
            # Uses the format of 3 [wrong,wrong,correct,wrong]
          elif layout == 3:
            list = [incorrect1, incorrect2, correct_word, incorrect3]
            # Uses the format of 4 [wrong,wrong,wrong,correct]
          elif layout == 4:
            list = [incorrect1, incorrect2, incorrect3, correct_word]
          print("Which word does belong in the Town category")
          print(list)
          command = input("Press Enter to hear the words (1/4)")
          audioq = helper.translateb(correct_word)
          audio = helper.playsound(audioq)
          command = input("Press Enter to hear the words (2/4)")
          audioq = helper.translateb(incorrect1)
          audio = helper.playsound(audioq)
          command = input("Press Enter to hear the words (3/4)")
          audioq = helper.translateb(incorrect2)
          audio = helper.playsound(audioq)
          command = input("Press Enter to hear the words (4/4)")
          audioq = helper.translate(incorrect3)
          audio = helper.playsound(audioq)
          answer = input("Answer:")
          if answer.lower() == correct_word.lower():
            print("Correct!")
            total += 1
            command = input("Press Enter to continue")
            replit.clear()
            total += 1
          else:
            print("Incorrect!")
            command = input("Press Enter to continue")
            replit.clear()
            total += 1
        # If the category that was chosen is advanced home questions
        elif category == "advanced_home":
          correct = helper.home_words
          incorrect = helper.not_home_words
          correct_word = random.choice(correct)
          incorrect1 = random.choice(incorrect)
          incorrect2 = random.choice(incorrect)
          incorrect3 = random.choice(incorrect)
          if layout == 1:
            list = [correct_word, incorrect1, incorrect2, incorrect3]
            # Uses the format of 2 [wrong,correct,wrong,wrong]
          elif layout == 2:
            list = [incorrect1, correct_word, incorrect2, incorrect3]
            # Uses the format of 3 [wrong,wrong,correct,wrong]
          elif layout == 3:
            list = [incorrect1, incorrect2, correct_word, incorrect3]
            # Uses the format of 4 [wrong,wrong,wrong,correct]
          elif layout == 4:
            list = [incorrect1, incorrect2, incorrect3, correct_word]
          print("Which word does belong in the Home category")
          print(list)
          command = input("Press Enter to hear the words (1/4)")
          audioq = helper.translateb(correct_word)
          audio = helper.playsound(audioq)
          command = input("Press Enter to hear the words (2/4)")
          audioq = helper.translateb(incorrect1)
          audio = helper.playsound(audioq)
          command = input("Press Enter to hear the words (3/4)")
          audioq = helper.translateb(incorrect2)
          audio = helper.playsound(audioq)
          command = input("Press Enter to hear the words (4/4)")
          audioq = helper.translate(incorrect3)
          audio = helper.playsound(audioq)
          answer = input("Answer:")
          if answer.lower() == correct_word.lower():
            print("Correct!")
            total += 1
            command = input("Press Enter to continue")
            replit.clear()
            total += 1
          else:
            print("Incorrect!")
            command = input("Press Enter to continue")
            replit.clear()
            total += 1
        # If the category that was chosen is advanced restaurant questions
        elif category == "advanced_restaurant":
          correct = helper.restaurant_words
          incorrect = helper.not_restaurant_words
          correct_word = random.choice(correct)
          incorrect1 = random.choice(incorrect)
          incorrect2 = random.choice(incorrect)
          incorrect3 = random.choice(incorrect)
          if layout == 1:
            list = [correct_word, incorrect1, incorrect2, incorrect3]
            # Uses the format of 2 [wrong,correct,wrong,wrong]
          elif layout == 2:
            list = [incorrect1, correct_word, incorrect2, incorrect3]
            # Uses the format of 3 [wrong,wrong,correct,wrong]
          elif layout == 3:
            list = [incorrect1, incorrect2, correct_word, incorrect3]
            # Uses the format of 4 [wrong,wrong,wrong,correct]
          elif layout == 4:
            list = [incorrect1, incorrect2, incorrect3, correct_word]
          print("Which word does belong in the Restaurant category")
          print(list)
          command = input("Press Enter to hear the words (1/4)")
          audioq = helper.translateb(correct_word)
          audio = helper.playsound(audioq)
          command = input("Press Enter to hear the words (2/4)")
          audioq = helper.translateb(incorrect1)
          audio = helper.playsound(audioq)
          command = input("Press Enter to hear the words (3/4)")
          audioq = helper.translateb(incorrect2)
          audio = helper.playsound(audioq)
          command = input("Press Enter to hear the words (4/4)")
          audioq = helper.translate(incorrect3)
          audio = helper.playsound(audioq)
          answer = input("Answer:")
          if answer.lower() == correct_word.lower():
            print("Correct!")
            total += 1
            command = input("Press Enter to continue")
            replit.clear()
            total += 1
          else:
            print("Incorrect!")
            command = input("Press Enter to continue")
            replit.clear()
            total += 1
        # If the category that was chosen is advanced family
        elif category == "family_home":
          correct = helper.family_words
          incorrect = helper.not_family_words
          correct_word = random.choice(correct)
          incorrect1 = random.choice(incorrect)
          incorrect2 = random.choice(incorrect)
          incorrect3 = random.choice(incorrect)
          if layout == 1:
            list = [correct_word, incorrect1, incorrect2, incorrect3]
            # Uses the format of 2 [wrong,correct,wrong,wrong]
          elif layout == 2:
            list = [incorrect1, correct_word, incorrect2, incorrect3]
            # Uses the format of 3 [wrong,wrong,correct,wrong]
          elif layout == 3:
            list = [incorrect1, incorrect2, correct_word, incorrect3]
            # Uses the format of 4 [wrong,wrong,wrong,correct]
          elif layout == 4:
            list = [incorrect1, incorrect2, incorrect3, correct_word]
          print("Which word does belong in the Family category")
          print(list)
          command = input("Press Enter to hear the words (1/4)")
          audioq = helper.translateb(correct_word)
          audio = helper.playsound(audioq)
          command = input("Press Enter to hear the words (2/4)")
          audioq = helper.translateb(incorrect1)
          audio = helper.playsound(audioq)
          command = input("Press Enter to hear the words (3/4)")
          audioq = helper.translateb(incorrect2)
          audio = helper.playsound(audioq)
          command = input("Press Enter to hear the words (4/4)")
          audioq = helper.translate(incorrect3)
          audio = helper.playsound(audioq)
          answer = input("Answer:")
          if answer.lower() == correct_word.lower():
            print("Correct!")
            total += 1
            command = input("Press Enter to continue")
            replit.clear()
            total += 1
          else:
            print("Incorrect!")
            command = input("Press Enter to continue")
            replit.clear()
            total += 1
        # If the category that was chosen is advanced greetings
        elif category == "advanced_greetings":
          correct = helper.greetings_words
          incorrect = helper.not_greetings_words
          correct_word = random.choice(correct)
          incorrect1 = random.choice(incorrect)
          incorrect2 = random.choice(incorrect)
          incorrect3 = random.choice(incorrect)
          if layout == 1:
            list = [correct_word, incorrect1, incorrect2, incorrect3]
            # Uses the format of 2 [wrong,correct,wrong,wrong]
          elif layout == 2:
            list = [incorrect1, correct_word, incorrect2, incorrect3]
            # Uses the format of 3 [wrong,wrong,correct,wrong]
          elif layout == 3:
            list = [incorrect1, incorrect2, correct_word, incorrect3]
            # Uses the format of 4 [wrong,wrong,wrong,correct]
          elif layout == 4:
            list = [incorrect1, incorrect2, incorrect3, correct_word]
          print("Which word does belong in the Greetings category")
          print(list)
          command = input("Press Enter to hear the words (1/4)")
          audioq = helper.translateb(correct_word)
          audio = helper.playsound(audioq)
          command = input("Press Enter to hear the words (2/4)")
          audioq = helper.translateb(incorrect1)
          audio = helper.playsound(audioq)
          command = input("Press Enter to hear the words (3/4)")
          audioq = helper.translateb(incorrect2)
          audio = helper.playsound(audioq)
          command = input("Press Enter to hear the words (4/4)")
          audioq = helper.translate(incorrect3)
          audio = helper.playsound(audioq)
          answer = input("Answer:")
          if answer.lower() == correct_word.lower():
            print("Correct!")
            total += 1
            command = input("Press Enter to continue")
            replit.clear()
            total += 1
          else:
            print("Incorrect!")
            command = input("Press Enter to continue")
            replit.clear()
            total += 1
    else:
      replit.clear()
      challenge_highscore = (str(total) + "/" + str(ChallengeX))
      print(challenge_highscore)
      command = input("Press Enter to continue")
      replit.clear()
      testinChallenge = False
      Challenge = True

# While learning Chllange
  while learninChallenge:
    # Key words
    Verbs = ["I will go", "I will eat"]
    Time_words = ["This morning", "Tomorrow"]
    location = ["store", "night club", "cafe", "house", "tipi"]
    food = ["fish", "oranges", "apples", "fries", "burger", "dessert", "bread"]
    command = input(
        "Type continue to learn another sentence(Continue)\nType Done to finish learning sentences(Done): "
    )
    command = command.lower()
    if command == "done":
      learninChallenge = False
      Challenge = True
      replit.clear()
    if command == "continue":
      replit.clear()
      Chosen_verb = random.choice(Verbs)
      Chosen_time_words = random.choice(Time_words)
      Translated_Chosen_verb = helper.translate(Chosen_verb)
      Translated_time_words = helper.translate(Chosen_time_words)
      if Chosen_verb == "I will go":
        vocab = random.choice(location)
        Translated_vocab = helper.translate(vocab)
        Translated_vocab = Translated_vocab.strip()
        Translated_Chosen_verb = Translated_Chosen_verb.strip()
        Translated_time_words = Translated_time_words.strip()
        print(Chosen_time_words + " " + Chosen_verb + " to the " + vocab)
        print(Translated_time_words + " " + Translated_Chosen_verb + " " +
              Translated_vocab)
        audio = helper.playsound(Chosen_time_words)
        time.sleep(1)
        audio = helper.playsound(Chosen_verb)
        time.sleep(1)
        audio = helper.playsound(vocab)
        pause = input("Press Enter to continue..")
        replit.clear()
      elif Chosen_verb == "I will eat":
        vocab = random.choice(food)
        Translated_vocab = helper.translate(vocab)
        Translated_vocab = Translated_vocab.strip()
        Translated_Chosen_verb = Translated_Chosen_verb.strip()
        Translated_time_words = Translated_time_words.strip()
        print(Chosen_time_words + " " + Chosen_verb + " the " + vocab)
        print(Translated_time_words + " " + Translated_Chosen_verb + " " +
              Translated_vocab)
        audio = helper.playsound(Chosen_time_words)
        time.sleep(1)
        audio = helper.playsound(Chosen_verb)
        time.sleep(1)
        audio = helper.playsound(vocab)
        pause = input("Press Enter to continue..")
        replit.clear()
