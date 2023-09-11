print("welcome to the rockstar games quiz")

score = 0
playing = input("Do you want to play? ").lower()

if playing != "yes":
    print("have a nice day!")
    quit()
    
answer = input("what is the full form of GTA? ").lower()
if answer == "grand theft auto":
    #print("correct!")
    score += 1

answer = input("what is the latest installment from rockstar games? ").lower()
if answer == "red dead redemption 2":
    #print("correct!")
    score += 1

answer = input("how many playable characters are there in GTA V? ").lower()
if answer == "3":
    #print("correct!")
    score += 1

answer = input("What fictional city does GTA 5 primarily take place in? ").lower()
if answer == "los santos":
    #print("correct!")
    score += 1  

answer = input("What is the name of the protagonist in Red Dead Redemption 2? ").lower()
if answer == "arthur morgan":
    #print("correct!")
    score += 1  
  
answer = input("In GTA 5, which of the three main characters is an ex-military pilot? ").lower()
if answer == "trever phillips":
    #print("correct!")
    score += 1  
    
answer = input("What is the name of the gang that the player character, Arthur Morgan, belongs to in Red Dead Redemption 2? ").lower()
if answer == "van der linde gang":
    #print("correct!")
    score += 1    
    
answer = input("What is the name of the fictional vehicle manufacturer in GTA 5 known for producing high-end cars? ").lower()
if answer == "grotti":
    #print("correct!")
    score += 1    
answer = input("What year was Rockstar Games founded? ").lower()
if answer == "1998":
    #print("correct!")
    score += 1  
    
answer = input("What is the name of the main character you play as in GTA San Andreas? ").lower()
if answer == "cj" or answer == "carl johnson":
    #print("correct!")
    score += 1 
    
print(f"thanks for playing the quiz, you got {score} out of 10")