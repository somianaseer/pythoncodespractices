word_dict={
    "Ephemeral":"lasting for a very short time",
    "Ubiquitous":"present,appearing,or found everywhere.",
    "Quintessential":"Representing the most perfect or typical example of a qualityor class",
    "Serendipity":"the occurrence of events by chance in a happy or beneficial way",
    "Ebullient":"cheerful and full of energy."
    }

def add_word(word,definition):
    word_dict[word]=definition 
    print(f"Word {word} added successsfully.")

def remove_word(word):
    if word in word_dict:
        del word_dict[word]
        print(f"word {word} removed successfully.")
    else:
        print(f"word {word} not found.")
        
def get_definition(word):
    return word_dict.get(word,"word not found")

def list_words():
    return list(word_dict.keys())

def update_definition(word, new_definition):
    if word in word_dict:
        word_dict[word] = new_definition
        print(f"Definition of '{word}' updated successfully.")
    else:
        print(f"Word '{word}' not found in the dictionary.")

def main():
    while True:
       print("\nDictionary menu")
       print("1. Add a word")
       print("2. Remove a word")
       print("3. Get definition")
       print("4. List all words")
       print("5. Update word definition")
       print("6. Exit")
       choice=input("Enter your choice(1-5).")
       if choice=='1':
           word=input("Enter the word to add:")
           definition=input("Enter the definition:")
           add_word(word,definition)
       
       elif choice=='2':
           word=input("Enter the word to remove")
           remove_word(word)
           
       elif choice=='3':
           word=input("Enter the word to get the definition of:")
           print(f"Definition of {word}: {get_definition(word)}")
       
       elif choice=='4':
           words=list_words()
           if words:
               print("Words in the dictionary:")
               for word in words:
                   print(f"-{word}")
           else:
               print("The dictionary is empty.")
               
       elif choice =='5':
            word = input("Enter the word to update: ")
            new_definition = input("Enter the new definition: ")
            update_definition(word, new_definition)        
       
       elif choice=='6':
           print("Exiting the dictionary.")
           break
       
       else:
           print("Invalid choice.please select a number between 1 and 5.")
if __name__=="__main__":
    main()           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           