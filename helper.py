# Helper functions for Blackfoot project
# CMPT 120 
# Nov. 12, 2020

import wave
import time
import random
import replit
import cmpt120image
from replit import audio

def concat(infiles,outfile):
  """
  Input: 
  - infiles: a list containing the filenames of .wav files to concatenate,
    e.g. ["hello.wav","there.wav"]
  - outfile: name of the file to write the concatenated .wav file to,
    e.g. "hellothere.wav"
  Output: None
  """
  data = []
  for infile in infiles:
      w = wave.open(infile, 'rb')
      data.append( [w.getparams(), w.readframes(w.getnframes())] )
      w.close()    
  output = wave.open(outfile, 'wb')
  output.setparams(data[0][0])
  for i in range(len(data)):
      output.writeframes(data[i][1])
  output.close()

#### SELF MADE Functions###
# Playsound function
def playsound(word):
  stripped = word.lower().strip()
  final = stripped.replace(' ', '_')
  audio.play_file("sounds/"+final+".wav")

# Creates the dictionary
dictionary = {}
dictionary_blackfoot = {}
valid_words = []
file = open("Dictionary.docx")
for data in file:
  line = data.split(":")
  dictionary[line[0]] = line[1]
  dictionary_blackfoot[line[0]] = line[1]
  valid_words.append(line[0])

# Translates the words 
def translate(word):
  word = (dictionary[word])
  return word

def translateb(word):
  word = (dictionary_blackfoot[word])
  return word


# Check whether the word is a valid input
def linear_search(input_list, item):
  for x in input_list:
    if x == item:
      return True
  else: 
    return False
   
def test(topic):  
  town_word = ["cinema","store","night club","cafe","house","tipi"]
  home_word = ["bathroom","window","kitchen","door","car","dog","elevator"]
  restaurant_word = ["fish","water","oranges","apples","potatoes","fries","burger","dessert","bread","tea","coffee"]
  greetings_word = ["No","Yes","Let's go","Not too bad","I'm doing good. You?","How are you?","Hello friend","Hello"]
  family_word =["Man","Woman","Girl","Boy","Mother","Father"]
# If the user asked to be tested about town
  if topic.lower() == "town":
    score = 0
    TownX = 0
    total = 0
    if TownX != 10:
      for x in range(10):
        TownX += 1
        replit.clear()
        word = random.choice(town_word) # WORD IN ENGLISH
        question = ("What is "+ word) # What is (englishword)
        answer1 = input(question +"?"+"\n"+"Answer:") # User must type the translation
        answer = answer1.lower()
        non_key = dictionary[word] # The correct answer translated
        answer_key = non_key.lower().strip()
        if answer  == answer_key: # If the answer and the answer key matches it's correct
          print("Correct!")
          resume = input("Press enter to continue..")
          replit.clear()
          total += 1
        if answer != answer_key:
          print("Incorrect.. The correct answer is "+answer_key)
          resume = input("Press enter to continue..")
          replit.clear()
      else:
        replit.clear()
        result = (str(total) +"/"+ str(TownX))
        return result
# If the user asked to be tested about home
  if topic.lower() == "home":
    score = 0
    HomeX = 0
    total = 0
    if HomeX != 10:
      for x in range(10):
        HomeX += 1
        replit.clear()
        word = random.choice(home_word) # WORD IN ENGLISH
        question = ("What is "+ word) # What is (englishword)
        answer1 = input(question +"?"+"\n"+"Answer:") # User must type the translation
        answer = answer1.lower()
        non_key = dictionary[word] # The correct answer translated
        answer_key = non_key.lower().strip()
        if answer  == answer_key: # If the answer and the answer key matches it's correct
          print("Correct!")
          resume = input("Press enter to continue..")
          replit.clear()
          total += 1
        if answer != answer_key:
          print("Incorrect.. The correct answer is "+answer_key)
          resume = input("Press enter to continue..")
          replit.clear()
      else:
        replit.clear()
        result = (str(total) +"/"+ str(HomeX))
        return result
# If the user asked to be tested about restaurant
  if topic.lower() == "restaurant":
    score = 0
    RestaurantX = 0
    total = 0
    if RestaurantX != 10:
      for x in range(10):
        RestaurantX += 1
        replit.clear()
        word = random.choice(restaurant_word) # WORD IN ENGLISH
        question = ("What is "+ word) # What is (englishword)
        answer1 = input(question +"?"+"\n"+"Answer:") # User must type the translation
        answer = answer1.lower()
        non_key = dictionary[word] # The correct answer translated
        answer_key = non_key.lower().strip()
        if answer  == answer_key: # If the answer and the answer key matches it's correct
          print("Correct!")
          resume = input("Press enter to continue..")
          replit.clear()
          total += 1
        if answer != answer_key:
          print("Incorrect.. The correct answer is "+answer_key)
          resume = input("Press enter to continue..")
          replit.clear()
      else:
        replit.clear()
        result = (str(total) +"/"+ str(RestaurantX))
        return result
# If the user asked to be tested about greetings
  if topic.lower() == "greetings":
    score = 0
    GreetingsX = 0
    total = 0
    if GreetingsX != 10:
      for x in range(10):
        GreetingsX += 1
        replit.clear()
        word = random.choice(greetings_word) # WORD IN ENGLISH
        question = ("What is "+ word) # What is (englishword)
        answer1 = input(question +"?"+"\n"+"Answer:") # User must type the translation
        answer = answer1.lower()
        non_key = dictionary[word] # The correct answer translated
        answer_key = non_key.lower().strip()
        if answer  == answer_key: # If the answer and the answer key matches it's correct
          print("Correct!")
          resume = input("Press enter to continue..")
          replit.clear()
          total += 1
        if answer != answer_key:
          print("Incorrect.. The correct answer is "+answer_key)
          resume = input("Press enter to continue..")
          replit.clear()
      else:
        replit.clear()
        result = (str(total) +"/"+ str(GreetingsX))
        return result
# If the user asked to be tested about family
  if topic.lower() == "family":
    score = 0
    FamilyX = 0
    total = 0
    if FamilyX != 10:
      for x in range(10):
        FamilyX += 1
        replit.clear()
        word = random.choice(family_word) # WORD IN ENGLISH
        question = ("What is "+ word) # What is (englishword)
        answer1 = input(question +"?"+"\n"+"Answer:") # User must type the translation
        answer = answer1.lower()
        non_key = dictionary[word] # The correct answer translated
        answer_key = non_key.lower().strip()
        if answer  == answer_key: # If the answer and the answer key matches it's correct
          print("Correct!")
          resume = input("Press enter to continue..")
          replit.clear()
          total += 1
        if answer != answer_key:
          print("Incorrect.. The correct answer is "+answer_key)
          resume = input("Press enter to continue..")
          replit.clear()
      else:
        replit.clear()
        result = (str(total) +"/"+ str(FamilyX))
        return result

#### ADVANCED QUESTION SECTION

format_selection = [1,2,3,4]
advanced_category = ["advanced_town"]
#advanced_category = ["advanced_town","advanced_home","advanced_restaurant","advanced_greetings","advanced_family"]

# Words that belongs in Town
town_words = ["Aisaksittoo","Itaohpomoapii","Itaisimmioapii","Itoiyo’pii","Naapoiyiss","Niitoiyiss"]

# Words that don't belong in Town
not_town_words = ["Aohkii","Mamii","aotahkoinammiksi","aipasstaamiinammiksi","paataakistsi","pikkiaaksin","pisatsoyiikan","napayin","Siksikimmii","Iitapsiksikimmii","Makapoiyiss","Itoiyo’soap","Aiksistomatomahka","Kitsim","Aisspaohpii","Ksisstsikomstan","Imitaa","Ninaa","Aakii","Aakiikoan","Saahkomaapi","Iksisst","Inn","Oki","Oki napi","Tsa niita’piiwa?","Tsikohssokopii. Kistoo?","Matohkwiikii","Okí","Aa","Saa"]

# Words that belong in Restaurant
restaurant_words =["Aohkii","mamii","aotahkoinammiksi","aipasstaamiinammiksi","paataakistsi","pikkiaaksin","pisatsoyiikan","napayin","Siksikimmii","Iitapsiksikimmii"]

# Words that don't belong in Restaurant
not_restaurant_words = ["Aisaksittoo","Itaohpomoapii","Itaisimmioapii","Itoiyo’pii","Naapoiyiss","Niitoiyiss","Makapoiyiss","Itoiyo’soap","Aiksistomatomahka","Kitsim","Aisspaohpii","Ksisstsikomstan","Imitaa","Ninaa","Aakii","Aakiikoan","Saahkomaapi","Iksisst","Inn","Oki","Oki napi","Tsa niita’piiwa?","Tsikohssokopii. Kistoo?","Matohkwiikii","Okí","Aa","Saa"]

# Words that belong in Home
home_words = ["Makapoiyiss","Itoiyo’soap","Aiksistomatomahka","Kitsim","Aisspaohpii","Ksisstsikomstan","Imitaa"]

# Words that don't belong in Home
not_home_words = ["Aisaksittoo","Itaohpomoapii","Itaisimmioapii","Itoiyo’pii","Naapoiyiss","Niitoiyiss","Aohkii","mamii","aotahkoinammiksi","aipasstaamiinammiksi","paataakistsi","pikkiaaksin","pisatsoyiikan","napayin","Siksikimmii","Iitapsiksikimmii","Ninaa","Aakii","Aakiikoan","Saahkomaapi","Iksisst","Inn","Oki","Oki napi","Tsa niita’piiwa?","Tsikohssokopii. Kistoo?","Matohkwiikii","Okí","Aa","Saa"]

# Words that belong in Family
family_words = ["Ninaa","Aakii","Aakiikoan","Saahkomaapi","Iksisst","Inn"]

# Words that don't belong in Family
not_family_words = ["Aisaksittoo","Itaohpomoapii","Itaisimmioapii","Itoiyo’pii","Naapoiyiss","Niitoiyiss","Aohkii","mamii","aotahkoinammiksi","aipasstaamiinammiksi","paataakistsi","pikkiaaksin","pisatsoyiikan","napayin","Siksikimmii","Iitapsiksikimmii","Makapoiyiss","Itoiyo’soap","Aiksistomatomahka","Kitsim","Aisspaohpii","Ksisstsikomstan","Imitaa","Oki","Oki napi","Tsa niita’piiwa?","Tsikohssokopii. Kistoo?","Matohkwiikii","Okí","Aa","Saa"]

# Words that belong in Family
greetings_words = ["Oki","Oki napi","Tsa niita’piiwa?","Tsikohssokopii. Kistoo?","Matohkwiikii","Okí","Aa","Saa"]

# Words that don't belong in Home

not_greetings_words = ["Aisaksittoo","Itaohpomoapii","Itaisimmioapii","Itoiyo’pii","Naapoiyiss","Niitoiyiss","Aohkii","mamii","aotahkoinammiksi","aipasstaamiinammiksi","paataakistsi","pikkiaaksin","pisatsoyiikan","napayin","Siksikimmii","Iitapsiksikimmii","Makapoiyiss","Itoiyo’soap","Aiksistomatomahka","Kitsim","Aisspaohpii","Ksisstsikomstan","Imitaa","Ninaa","Aakii","Aakiikoan","Saahkomaapi","Iksisst","Inn"]