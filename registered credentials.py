user_credentials = {}

def signup():
    print("\n--- Signup ---")
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    
    if username in user_credentials:
        print("Username already exists. Please log in.")
        return login()
    
    user_credentials[username] = password
    print("Signup successful! Please login.\n")
    login()
    
def login():
    print("\n--- Login ---")
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    
    if user_credentials.get(username) == password:
        print("Login Successful!\nStarting the Quiz...")
        quiz()
    else:
        print("Incorrect username or password. Please try again.\n")
        login()

def quiz():
    questions = [
        ("What is the capital of Norway?", ["Bergen", "Oslo", "Stavanger", "Trondheim"], "B"),
        ("What is the currency of Norway?", ["Euro", "Pound", "Krone", "Deutsche Mark"], "C"),
        ("What is the largest city in Norway?", ["Oslo", "Stavanger", "Bergen", "Trondheim"], "A"),
        ("When is Constitution Day (the national day) of Norway?", ["7th May", "17th May", "7th April", "17th April"], "B"),
        ("What color is the background of the Norwegian flag?", ["Red", "White", "Blue", "Yellow"], "A"),
        ("How many countries does Norway border?", ["1", "2", "3", "4"], "C"),
        ("What is the name of the university in Trondheim?", ["UiS", "UiO", "NMBU", "NTNU"], "D"),
        ("How long is the border between Norway and Russia?", ["100 km", "196 km", "256 km", "300 km"], "B"),
        ("Where in Norway is Stavanger?", ["North", "South", "South-west", "South-east"], "C"),
        ("From which Norwegian city did the world famous composer Edvard Grieg come?",  
         ["Oslo", "Bergen", "Stavanger", "Tromsø"], "B"),
        ("Which Norwegian explorer was the first to reach the South Pole?", 
         ["Roald Amundsen", "Fridtjof Nansen", "Leif Erikson", "Thor Heyerdahl"], "A"),
        ("What is the name of the longest fjord in Norway?", 
         ["Hardangerfjord", "Oslofjord", "Sognefjord", "Geirangerfjord"], "C"),
        ("Which famous Viking king united Norway?", 
         ["Harald Hardrada", "Harald Fairhair", "Olaf Tryggvason", "Erik the Red"], "B"),
        ("What is the name of Norway royal family?", 
         ["Bernadotte", "Windsor", "Glücksburg", "Oldenburg"], "C"),
        ("Which Norwegian city hosted the Winter Olympics in 1994?", 
         ["Bergen", "Oslo", "Lillehammer", "Trondheim"], "C"),
        ("What is the traditional Norwegian dish made of dried fish and lye?", 
         ["Rakfisk", "Lutefisk", "Kjøttkaker", "Fårikål"], "B"),
        ("Which Norwegian playwright wrote 'A Doll’s House'?", 
         ["Henrik Ibsen", "Knut Hamsun", "Jostein Gaarder", "Bjørnstjerne Bjørnson"], "A"),
        ("What is the name of the famous Norwegian painter known for 'The Scream'?", 
         ["Edvard Munch", "Gustav Vigeland", "Hans Gude", "Harald Sohlberg"], "A"),
        ("Which Norwegian island is known for the Global Seed Vault?", 
         ["Svalbard", "Lofoten", "Jan Mayen", "Senja"], "A"),
        ("What is the name of Norway’s highest mountain?", 
         ["Galdhøpiggen", "Glittertind", "Snøhetta", "Store Skagastølstind"], "A"),
        ("Which Norwegian footballer won the Ballon d'Or in 1997?", 
         ["Ole Gunnar Solskjær", "Tore André Flo", "John Arne Riise", "Henrik Larsson"], "B"),
        ("Which city is known as the 'Gateway to the Fjords'?", 
         ["Oslo", "Bergen", "Tromsø", "Kristiansand"], "B"),
        ("What is Norway’s second-largest city?",
         ["Trondheim", "Bergen", "Stavanger", "Drammen"], "B"),
        ("Which animal is featured on Norway’s coat of arms?",
         ["Bear", "Moose", "Lion", "Wolf"], "C"),
        ("Which Norwegian company is one of the world’s largest producers of salmon?", 
         ["Mowi", "Tine", "Jotun", "Equinor"], "A"),
        ("Which Norwegian scientist developed the paperclip?", 
         ["Kristian Birkeland", "Johan Vaaler", "Thor Heyerdahl", "Trygve Haavelmo"], "B"),
        ("What is the longest road tunnel in Norway?", 
         ["Laerdal Tunnel", "Gudvanga Tunnel", "Oslofjord Tunnel", "Førde Tunnel"], "A"),
        ("What is the northernmost town in Norway?", 
         ["Tromsø", "Alta", "Hammerfest", "Longyearbyen"], "D"),
        ("Which Norwegian festival celebrates the midnight sun?", 
         ["Oslo Jazz Festival", "Nordkappfestivalen", "Riddu Riđđu", "Trondheim Viking Festival"], "B"),
        ("Which popular TV series is set in Norway’s oil industry?", 
         ["Occupied", "Skam", "Beforeigners", "State of Happiness"], "D"),
    ]
    
    correct = 0
    incorrect = 0
    incorrect_answer = []
    
    for i, (question, options, answer) in enumerate(questions, start=1):
        print(f"\nQ{i}. {question}")
        for j, option in enumerate(options, start=65):
            print(f"{chr(j)}. {option}") 
        
        user_answer = input("Enter your answer (A, B, C, D): ").strip().upper()
        
        if user_answer == answer:
            correct += 1
        else:
            incorrect += 1
            incorrect_answer.append((question, user_answer, answer)) 

    print("\nQuiz Completed")       
    print(f"Correct Answers: {correct}")
    print(f"Incorrect Answers: {incorrect}\n")   

    if incorrect_answer:
        print("Incorrect Answers Review:") 
        for q, user_ans, correct_ans in incorrect_answer:
            print(f"Question: {q}")
            print(f"Your answer: {user_ans}")
            print(f"Correct answer: {correct_ans}\n")

signup()
