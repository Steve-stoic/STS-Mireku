import random
import string
print("You are welcome to the Ultimate Password Generator!")

#from numpy import character
while True:
    

    adjectives = [
        'happy', 'sad', 'angry', 'excited', 'tired', 'brave', 'kind', 'generous', 'smart', 'creative',
        'funny', 'serious', 'silly', 'intelligent', 'curious', 'friendly', 'shy', 'energetic', 'calm', 'proud',
        'honest', 'loyal', 'ambitious', 'confident', 'patient', 'responsible', 'organized', 'thoughtful', 'charming',
        'determined', 'gentle', 'hardworking', 'helpful', 'optimistic', 'passionate', 'polite', 'sincere', 'talented',
        'wise', 'courageous', 'grateful', 'imaginative', 'independent', 'resourceful', 'sympathetic', 'trustworthy',
        'adventurous', 'cheerful', 'compassionate', 'cooperative', 'flexible'
    ]


    nouns = [
        'apple', 'dog', 'cat', 'car', 'house', 'book', 'computer', 'friend', 'teacher', 'student',
        'pencil', 'tree', 'flower', 'river', 'mountain', 'ocean', 'city', 'country', 'university', 'hospital',
        'restaurant', 'movie', 'song', 'artist', 'actor', 'actress', 'writer', 'scientist', 'doctor', 'engineer',
        'musician', 'chef', 'athlete', 'business', 'money', 'dream', 'goal', 'adventure', 'journey', 'challenge',
        'success', 'failure', 'love', 'hope', 'faith', 'joy', 'peace', 'freedom', 'knowledge', 'wisdom'
    ]   

    adjectives = random.choice(adjectives)
    nouns = random.choice(nouns)
    numbers = random.randrange(1,100)
    special_character = random.choice(string.punctuation)

    password = adjectives + nouns + str(numbers) + special_character

    print(f"The generated password is {password}")

    another_one = input("Do you want another password to be generated? Enter y for yes and n for no")

    if another_one.lower() == "n":
        print("Alright, no new password would be generated")
        break

    




