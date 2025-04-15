sentence = input("ENTER THE SENTENCE: ") # User se input lene keliye ek variable liya 
words = sentence.split() # fhir user joh input diya uske harek word ko ek alag alag string ki using 
                        #split attribute
longest_word = "" # fhir ek empty string banayi
max_length = 0 # or ek or variable liya jisko 0 se initialize kiya

for word in words: # fhir for loop use kiya taaki voh harek word ki length loop me check kare
      if len(word)>max_length: # fhir if condition use kiya ki agar joh user ne input diya usme ek 
                               #particular string ki length agar zero se badi rahi toh
          max_length = len(word) # joh max_length variable 0 the uski length sabse badi 
                                 #string jitni ho jayegi
          longest_word = word    # fhir joh sabse badi string mili hai usko voh empty string 
                                 #me shift karenge
          
print("The longest word is:",longest_word) # atlast print