from colorama import Fore, Back, Style
import random
import os
from abc import ABC, abstractmethod

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

class Person(ABC):
    def __init__(self, id, username, gender, age, height, occupation, zodiac, personality, 
                 lovelang, h1, h2, h3, h4, h5, h6, p_age, p_height, p_occupation, p_personality, 
                 p_lovelang):
        self.__id = id
        self.__username = username
        self.__gender = gender
        self.__age = int(age)
        self.__zodiac = zodiac
        self.__height = height
        self.__occupation = occupation
        self.__personality = personality
        self.__lovelang = lovelang
        self.__hobbies = [h1, h2, h3, h4, h5, h6]
        self.__preference = {
            "age": p_age,
            "height": p_height,
            "occupation": p_occupation,
            "personality": p_personality,
            "lovelang": p_lovelang
        }

    @abstractmethod
    def get_profile(self):
        pass

    @abstractmethod
    def match_criteria(self):
        pass
    
    #magic method 
    def __str__(self):
        return f"{self.__username} ({self.__gender}, {self.__age} years old)"

    def __repr__(self):
        return f"Person(id={self.__id}, username={self.__username}, gender={self.__gender}, age={self.__age})"

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.__id == other.__id and self.__username == other.__username
        return False

    # Getter methods
    def get_id(self):
        return self.__id

    def get_username(self):
        return self.__username

    def get_gender(self):
        return self.__gender

    def get_age(self):
        return self.__age

    def get_zodiac(self):
        return self.__zodiac

    def get_height(self):
        return self.__height

    def get_occupation(self):
        return self.__occupation

    def get_personality(self):
        return self.__personality

    def get_lovelang(self):
        return self.__lovelang

    def get_hobbies(self):
        return self.__hobbies

    def get_preference(self):
        return self.__preference

class Man(Person):
    def get_profile(self):
        hobbies = ', '.join(self.get_hobbies())  # Use getter
        return (f"Man: {self.get_username()}\nAge: {self.get_age()}\nHeight: {self.get_height()}\n"
                f"Zodiac Sign: {self.get_zodiac()}\nOccupation: {self.get_occupation()}\nPersonality: {self.get_personality()}\n"
                f"Love Language: {self.get_lovelang()}\nHobbies: {hobbies}")
    
    def match_criteria(self):
        return self.get_preference()  # Use getter

class Woman(Person):
    def get_profile(self):
        hobbies = ', '.join(self.get_hobbies())  # Use getter
        return (f"Woman: {self.get_username()}\nAge: {self.get_age()}\nHeight: {self.get_height()}\n"
                f"Zodiac Sign: {self.get_zodiac()}\nOccupation: {self.get_occupation()}\nPersonality: {self.get_personality()}\n"
                f"Love Language: {self.get_lovelang()}\nHobbies: {hobbies}")
    
    def match_criteria(self):
        return self.get_preference()  # Use getter


class MatchmakingSystem:
    def __init__(self):
        self.__men_file = "G1_T2_Code/text_files/men.txt"
        self.__women_file = "G1_T2_Code/text_files/women.txt"
        self.__load_users()
        self.__zodiac_scores = {
            "Aries": {
                "Best": ["Aries", "Leo", "Sagittarius"],
                "Good": ["Gemini", "Libra", "Aquarius"],
                "Average": ["Taurus", "Virgo", "Pisces", "Scorpio"],
            },
            "Taurus": {
                "Best": ["Taurus", "Virgo", "Capricorn"],
                "Good": ["Cancer", "Scorpio", "Pisces"],
                "Average": ["Aries", "Gemini", "Libra", "Sagittarius"],
            },
            "Gemini": {
                "Best": ["Gemini", "Libra", "Aquarius"],
                "Good": ["Aries", "Leo", "Sagittarius"],
                "Average": ["Taurus", "Cancer", "Scorpio", "Capricorn"],
            },
            "Cancer": {
                "Best": ["Cancer", "Scorpio", "Pisces"],
                "Good": ["Taurus", "Virgo", "Capricorn"],
                "Average": ["Gemini", "Leo", "Sagittarius", "Aquarius"],
            },
            "Leo": {
                "Best": ["Aries", "Leo", "Sagittarius"],
                "Good": ["Gemini", "Libra", "Aquarius"],
                "Average": ["Cancer", "Virgo", "Pisces", "Capricorn"],
            },
            "Virgo": {
                "Best": ["Virgo", "Taurus", "Capricorn"],
                "Good": ["Cancer", "Scorpio", "Pisces"],
                "Average": ["Aries", "Leo", "Libra", "Aquarius"],
            },
            "Libra": {
                "Best": ["Gemini", "Libra", "Aquarius"],
                "Good": ["Aries", "Leo", "Sagittarius"],
                "Average": ["Taurus", "Virgo", "Scorpio", "Pisces"],
            },
            "Scorpio": {
                "Best": ["Scorpio", "Cancer", "Pisces"],
                "Good": ["Taurus", "Virgo", "Capricorn"],
                "Average": ["Aries", "Gemini", "Libra", "Sagittarius"],
            },
            "Sagittarius": {
                "Best": ["Aries", "Sagittarius", "Leo"],
                "Good": ["Gemini", "Libra", "Aquarius"],
                "Average": ["Taurus", "Cancer", "Scorpio", "Capricorn"],
            },
            "Capricorn": {
                "Best": ["Taurus", "Virgo", "Capricorn"],
                "Good": ["Cancer", "Scorpio", "Pisces"],
                "Average": ["Gemini", "Sagittarius", "Aquarius", "Leo"],
            },
            "Aquarius": {
                "Best": ["Gemini", "Libra", "Aquarius"],
                "Good": ["Aries", "Leo", "Sagittarius"],
                "Average": ["Cancer", "Capricorn", "Pisces", "Virgo"],
            },
            "Pisces": {
                "Best": ["Cancer", "Scorpio", "Pisces"],
                "Good": ["Taurus", "Virgo", "Capricorn"],
                "Average": ["Aries", "Leo", "Aquarius", "Libra"],
            },
        }

    def __load_users(self):
        self.__men = self.__load_data(self.__men_file)
        self.__women = self.__load_data(self.__women_file)

    def __load_data(self, filename):
        users = []
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                next(file)  # Skip header
                #read file line by line
                for line in file:
                    data = line.strip().split('|')
                    if len(data) != 20:  # Ensure data length matches Person constructor
                        print(f"Error: Incorrect data format in {filename}: {data}")
                        continue  # Skip invalid entries

                    if filename == self.__men_file:
                        users.append(Man(*data))
                    else:
                        users.append(Woman(*data))
        except FileNotFoundError:
            print(f"File {filename} not found.")
        return users
    
    def __range(self, str):
        if '-' in str:
            min_val, max_val = map(int, str.split('-'))
            return min_val, max_val
        return None
    
    def __zodiac_match(self, user_zodiac, partner_zodiac):
        if user_zodiac not in self.__zodiac_scores:
            return 3  # Default score for unknown zodiac signs
    
        if partner_zodiac in self.__zodiac_scores[user_zodiac]["Best"]:
            return 10  # Best match
        elif partner_zodiac in self.__zodiac_scores[user_zodiac]["Good"]:
            return 7  # Good match
        elif partner_zodiac in self.__zodiac_scores[user_zodiac]["Average"]:
            return 5  # Average match
        return 3  # No match

    def __calculate_match_score(self, user, partner):
        score = 0
        preferences = user.match_criteria()

        #check height preference
        height_range = self.__range(preferences["height"])
        if height_range:
            min_height, max_height = height_range
            if min_height <= float(partner.get_height()) <= max_height:    
                score += 10
        
        #check age preference
        min_age, max_age = self.__range(preferences["age"])
        if min_age <= partner.get_age() <= max_age:
            score += 12

        #check occupation pref.
        if preferences["occupation"] == partner.get_occupation():
            score += 10
        
        #check love language pref.
        if preferences["lovelang"] == partner.get_lovelang():
            score += 16

        #check zodiac compatibility
        score += self.__zodiac_match(user.get_zodiac(), partner.get_zodiac())

        #check shared hobbies
        shared_hobbies_count = sum(1 for hobby in user.get_hobbies() if hobby in partner.get_hobbies())
        score += shared_hobbies_count * 4

        return score
    
    def suggest_match(self, user):
        potential_matches = self.__women if isinstance(user, Man) else self.__men
        matches = []
        for partner in potential_matches:
            score = self.__calculate_match_score(user, partner)
            if score >= 50:
                matches.append((partner, score))
        #sort from highest to lowest percentage
        matches.sort(key=lambda x: x[1], reverse=True)
        return matches

#function to welcome user when they first running our code
def welcome():
    print(Fore.CYAN + "=" * 50)
    print(Fore.LIGHTRED_EX + "WELCOME TO MATCHING WITH YOUR SOULMATE".center(50))
    print(Fore.CYAN +"=" * 50)
    print(Fore.MAGENTA + "Finding your perfect match has never been easier!")
    print(Fore.GREEN + "Let's get started.... \n"+ Style.RESET_ALL)

    # Ask if they want to know about matching rule and how to use our program
    while True:
        # Remove white space and change input to lowercase
        inform_of_program = input(Fore.LIGHTBLUE_EX + Style.BRIGHT +"Wanna learn more about US before starting the program? (yes/no): " + Style.RESET_ALL).strip().lower()
        if inform_of_program == 'yes':
            display_inform()
            break
        elif inform_of_program == 'no':
            print(Fore.GREEN + "\n Alright! Let's continue. \n")
            break
        else:
            print("\n Invalid input! Please enter 'yes' or 'no'. \n")
    
    # Ask if User is a NewUser or OldUser
    while True:
        print(Fore.CYAN + Style.BRIGHT + "Are you a new user or an existing user?" + Style.RESET_ALL)
        print(Fore.YELLOW + "1. New User (Register)")
        print(Fore.GREEN +"2. Existing User (confirm Username and ID)")
        print(Fore.RED + "3. Exit")

        choice = int(input(Fore.CYAN + Style.BRIGHT +"Please enter your choice (1 | 2 | 3): ").strip())

        if choice == 1:
            print(Fore.YELLOW + "Let's create your profile together. \n")
            new_user()
            break
        elif choice == 2:
            print(Fore.MAGENTA +"Welcome back! Let's verify with us to make sure that it's YOU. \n")
            old_user()
            break
        elif choice == 3:
            print(Fore.YELLOW +"Thanks for visiting us! Have a great day. \n")
            print(Fore.GREEN + "Exiting...")
            exit()
        else:
            print(Fore.RED + "Invalid INPUT! Please enter number 1, 2, or 3 \n")

def display_inform():
    print(Fore.GREEN + "About US ".center(50))
    print(Fore.CYAN +"-" * 50)
    print(Fore.BLUE + "We are a team of students dedicated to creating a platform where you can find your soulmate.")
    print("Please note that this is a prototype of our project and still requires further development.")
    print("Thank you for being a part of our journey!" +Style.RESET_ALL)
    print(Fore.MAGENTA +'=' * 50)

    print(Fore.BLUE +"\nOur system suggests a match based on the following criteria:")
    print(Fore.BLUE +"Your prefernce: ")
    print(Fore.RED + "- Height (+10%)")
    print("- Occupation (+10%)")
    print("- Age (+12%)")
    print("- Love Language (+16%)")
    print("- Personality (+18%)")
    print(Fore.BLUE +"Matching: ")
    print(Fore.RED +"- Zodiac sign compatibility (+10%) base on website")
    print("- Shared same hobbies (+4% for one)")
    print("\nThe match score must be at least 50% for a suggestion.")
    print(Fore.BLUE + " You will have the option to accept or reject each suggestion.")
    print(Fore.MAGENTA + "-" * 50)
    print(Fore.GREEN + "Now, let's begin! \n" + Style.RESET_ALL)

#randomly display message one of it using random
def display_reject_message():
    #when ppl reject the match
    reject_message = ["Thank you for your time! This match is not the right fit for you, but do not worry—we will keep searching for someone more compatible!"
    ,"Not every match is meant to be, and that is okay! We will find someone who truly clicks with you. Stay tuned for your next potential match!"
    ,"We understand that this match was not the right fit. Your preferences matter, and we will continue working to find a better match for you."
    ,"This one was not the one,' but don't worry—your perfect match could be just around the corner! Lets keep the search going!"
    ,"Got it! We'll keep looking for someone who better matches your vibe. Stay patient—the right match is out there!"]
    print(Fore.YELLOW +random.choice(reject_message))
def display_accept_message():
    #when ppl accept the match
    accept_message = ["It is a match!Looks like you both are interested in each other. Start a conversation and see where it goes!"
    ,"Nice choice!You and your match are on the same page—go ahead and break the ice!" 
    ,"Great news! Your match is in—now it's time to get to know each other. Who's making the first move?"
    ,"You've accepted the match! We hope this leads to a great connection. Start chatting and see where things go!"
    ,"Matched! Now it's time to chat and see if sparks fly!"]
    print(Fore.GREEN + random.choice(accept_message))


def new_user():
    clear_screen()
    print(Fore.BLUE + "To start our program we need some of your information and prefernce.")
    print("Some question you need to write and some are option so just choose number 1, 2, 3, or so on.")
    print("If you want to exit, please press 0."+ Style.RESET_ALL)
    print("Your Information: " )
    #create empty list to store each detail 
    data = []
    
    #Ask for name
    username = input("Name: ").strip()
    if username == '0':
        print(Fore.GREEN +"Exiting..." + Style.RESET_ALL)
        return
    data.append(username)
    clear_screen()  # Clear after name input
    
    #Ask for gender
    while True:
        print("Gender: ")
        print("0: Exit")
        print(Fore.BLUE + "1: Male")
        print(Fore.RED +"2: Female"+ Style.RESET_ALL)

        try:
            option1 = int(input("Enter: ").strip())
            if option1 == 0:
                print(Fore.GREEN +"Exiting..."+Style.RESET_ALL)
                return
            if option1 == 1:
                gender = 'Male'
                data.append(gender)
                clear_screen()
                break
            elif option1 == 2:
                gender = 'Female'
                data.append(gender)
                clear_screen()
                break
            else:
                print(Fore.RED +"Invalid INPUT! please enter 1 or 2 \n"+Style.RESET_ALL)
        except ValueError:
            print(Fore.RED +"Invalid INPUT! Please enter 1 or 2 \n" +Style.RESET_ALL)
            clear_screen()

    #Ask for age
    while True:
        try:
            age = int(input("Age (only number and must be >= 18): ").strip())
            if age == 0:
                print(Fore.GREEN +"Exiting..."+Style.RESET_ALL)
                return
            if age >= 18 and age < 50:
                data.append(age)
                clear_screen()
                break
            else:
                print(Fore.RED+"Please input a number greater than 18."+Style.RESET_ALL)
        except ValueError:
            print(Fore.RED+"Invalid Input! Please enter a valid number! \n"+Style.RESET_ALL)
            clear_screen()

    #Ask for height
    while True:
        try:
            height = int(input("Height in cm (e.g.: 150): ").strip())
            if height == 0:
                print(Fore.GREEN +"Exiting..."+Style.RESET_ALL)
                return
            if height > 140:
                data.append(height)
                clear_screen()
                break
            else:
                print(Fore.RED +"Please input number only."+Style.RESET_ALL)
        except ValueError:
            print(Fore.RED +"Invalid input! Please enter a valid number! \n"+Style.RESET_ALL)
            clear_screen()
        
    #ask if user is a student or worker
    while True:
        print("occupation: ")
        print("0: Exit")
        print(Fore.GREEN +"1: Student")
        print(Fore.BLUE +"2: Worker"+Style.RESET_ALL)
        try:
            option2 = int(input("Enter: ").strip())
            if option2 == 0:
                print(Fore.GREEN+"Exiting..."+Style.RESET_ALL)
                return
            if option2 == 1:
                occupation = 'Student'
                data.append(occupation)
                clear_screen()
                break
            elif option2 == 2:
                occupation = 'Worker'
                data.append(occupation)
                clear_screen()
                break
            else:
                print(Fore.RED +"Invalid INPUT! please enter 1 or 2 \n"+Style.RESET_ALL)
        except ValueError:
            print(Fore.RED +"Invalid input! Please enter a valid number! \n"+Style.RESET_ALL)
            clear_screen()
        
    #ask for zodiac sign
    while True:
        print("Zodiac Sign: ")
        print("0: Exit")
        print(Fore.BLUE +"1: Aries (March 21 - April 19)")
        print("2: Taurus (April 20 - May 20)")
        print("3: Gemini (May 21 - June 20)")
        print("4: Cancer (June 21 - July 22)")
        print("5: Leo (July 23 - August 22)")
        print("6: Virgo (August 23 - September 22)")
        print("7: Libra (September 23 - October 22)")
        print("8: Scorpio (October 23 - November 21)")
        print("9: Sagittarius (November 22 - December 21)")
        print("10: Capricorn (December 22 - January 19)")
        print("11: Aquarius (January 20 - February 18)")
        print("12: Pisces (February 19 - March 20)"+Style.RESET_ALL)
        try:
            option3 = int(input("Enter: ").strip())
            if option3 == 0:
                print(Fore.GREEN+"Exiting..."+Style.RESET_ALL)
                return
            if option3 == 1:
                zodiac = 'Aries'
                data.append(zodiac)
                clear_screen()
                break
            elif option3 == 2:
                zodiac = 'Taurus'
                data.append(zodiac)
                clear_screen()
                break
            elif option3 == 3:
                zodiac = 'Gemini'
                data.append(zodiac)
                clear_screen()
                break
            elif option3 == 4:
                zodiac = 'Cancer'
                data.append(zodiac)
                clear_screen()
                break
            elif option3 == 5:
                zodiac = 'Leo'
                data.append(zodiac)
                clear_screen()
                break
            elif option3 == 6:
                zodiac = 'Virgo'
                data.append(zodiac)
                clear_screen()
                break
            elif option3 == 7:
                zodiac = 'Libra'
                data.append(zodiac)
                clear_screen()
                break
            elif option3 == 8:
                zodiac = 'Scorpio'
                data.append(zodiac)
                clear_screen()
                break
            elif option3 == 9:
                zodiac = 'Sagittarius'
                data.append(zodiac)
                clear_screen()
                break
            elif option3 == 10:
                zodiac = 'Capricorn'
                data.append(zodiac)
                clear_screen()
                break
            elif option3 == 11:
                zodiac = 'Aquarius'
                data.append(zodiac)
                clear_screen()
                break
            elif option3 == 12:
                zodiac = 'Pisces'
                data.append(zodiac)
                clear_screen()
                break
            else:
                print(Fore.RED +"Invalid input! please enter number from 1-12 \n"+Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Invalid input! Please enter a valid number! \n" +Style.RESET_ALL)
            clear_screen()

    #ask for personailty
    while True:
        print("Personality: ")
        print("0: Exit")
        print("1: Introvert")
        print("2: Extrovert")
        print("3: Ambivert")
        try:
            option4 = int(input("Enter: ").strip())
            if option4 == 0:
                print(Fore.GREEN +"Exiting..."+Style.RESET_ALL)
                return
            if option4 == 1:
                personality = 'Introvert'
                data.append(personality)
                clear_screen()
                break
            elif option4 == 2:
                personality = 'Extrovert'
                data.append(personality)
                clear_screen()
                break
            elif option4 == 3:
                personality = 'Ambivert'
                data.append(personality)
                clear_screen()
                break
            else:
                print(Fore.RED +"Invalid INPUT! please enter 1 , 2 or 3\n"+Style.RESET_ALL)
        except ValueError:
            print(Fore.RED +"Invalid input! Please enter a valid number! \n"+Style.RESET_ALL)
            clear_screen()
    
    #ask for love language
    while True:
        print("Love Language (Choose one that best matches you): ")
        print("0: Exit")
        print(Fore.RED +"1: Physical Touch")
        print("2: Words of Affirmation")
        print("3: Gifting")
        print("4: Acts of Service")
        print("5: Quality Time"+Style.RESET_ALL)
        try:
            option5 = int(input("Enter: ").strip())
            if option5 == 0:
                print(Fore.Green +"Exiting..."+Style.RESET_ALL)
                return
            if option5 == 1:
                lovelang = 'Physical Touch'
                data.append(lovelang)
                clear_screen()
                break
            elif option5 == 2:
                lovelang = 'Words of Affirmation'
                data.append(lovelang)
                clear_screen()
                break
            elif option5 == 3:
                lovelang = 'Gifting'
                data.append(lovelang)
                clear_screen()
                break
            elif option5 == 4:
                lovelang = 'Acts of Service'
                data.append(lovelang)
                clear_screen()
                break
            elif option5 == 5:
                lovelang = 'Quality Time'
                data.append(lovelang)
                clear_screen()
                break
            else:
                print(Fore.RED+"Invalid INPUT! please enter 1 - 5 \n"+Style.RESET_ALL)
        except ValueError:
            print(Fore.RED +"Invalid input! Please enter a valid number! \n"+Style.RESET_ALL)
            clear_screen()

    #ask for hobby 1
    while True:
        print("Sports & Outdoor Activities (Choose one that best matches you): ")
        print("0: Exit")
        print("1: Gym & weightlifting")
        print("2: Swimming")
        print("3: Running")
        print("4: Cycling")
        print("5: Fishing")
        print("6: Camping")
        try:
            option6 = int(input("Enter: ").strip())
            if option6 == 0:
                print(Fore.GREEN+"Exiting..."+Style.RESET_ALL)
                return
            if option6 == 1:
                h1 = 'Gym & weightlifting'
                data.append(h1)
                clear_screen()
                break
            elif option6 == 2:
                h1 = 'Swimming'
                data.append(h1)
                clear_screen()
                break
            elif option6 == 3:
                h1 = 'Swimming'
                data.append(h1)
                clear_screen()
                break
            elif option6 == 4:
                h1 = 'Cycling'
                data.append(h1)
                clear_screen()
                break
            elif option6 == 5:
                h1 = 'Fishing'
                data.append(h1)
                clear_screen()
                break
            elif option6 == 6:
                h1 = 'Camping'
                data.append(h1)
                clear_screen()
                break
            else:
                print(Fore.RED+"Invalid INPUT! please enter 1 - 6 \n"+Style.RESET_ALL)
        except ValueError:
            print(Fore.RED +"Invalid input! Please enter a valid number! \n"+Style.RESET_ALL)
            clear_screen()

    #ask for hobby 2
    while True:
        print("Tech & Digital Hobbies (Choose one that best matches you): ")
        print("0: Exit")
        print("1: Coding")
        print("2: Video editing")
        print("3: Gaming")
        print("4: Robotics")
        print("5: UI/UX design")
        try:
            option7 = int(input("Enter: ").strip())
            if option7 == 0:
                print(Fore.GREEN+"Exiting..."+Style.RESET_ALL)
                return
            if option7 == 1:
                h2 = 'Coding'
                data.append(h2)
                clear_screen()
                break
            elif option7 == 2:
                h2 = 'Video editing'
                data.append(h2)
                clear_screen()
                break
            elif option7 == 3:
                h2 = 'Gaming'
                data.append(h2)
                clear_screen()
                break
            elif option7 == 4:
                h2 = 'Robotics'
                data.append(h2)
                clear_screen()
                break
            elif option7 == 5:
                h2 = 'UI/UX design'
                data.append(h2)
                clear_screen()
                break
            else:
                print(Fore.RED+"Invalid INPUT! please enter 1 - 5 \n"+Style.RESET_ALL)     
        except:
            print(Fore.RED+"Invalid input! Please enter a valid number! \n"+Style.RESET_ALL)   
            clear_screen()

    #ask for hobbie 3
    while True:
        print("Intellectual & Educational Hobbies (Choose one that best matches you): ")
        print("0: Exit")
        print("1: Reading")
        print("2: Sudoku & puzzles")
        print("3: Movies/Documentaries")
        print("4: Chess")
        try:
            option8 = int(input("Enter: ").strip())
            if option8 == 0:
                print(Fore.GREEN +"Exiting..."+Style.RESET_ALL)
                return
            if option8 == 1:
                h3 = 'Reading'
                data.append(h3)
                clear_screen()
                break
            elif option8 == 2:
                h3 = 'Sudoku & puzzles'
                data.append(h3)
                clear_screen()
                break
            elif option8 == 3:
                h3 = 'Movies/Documentaries'
                data.append(h3)
                clear_screen()
                break
            elif option8 == 4:
                h3 = 'Chess'
                data.append(h3)
                clear_screen()
                break
            else:
                print(Fore.RED+"Invalid INPUT! please enter 1 - 4 \n"+Style.RESET_ALL)
        except ValueError:
            print(Fore.RED+"Invalid input! Please enter a valid number! \n"+Style.RESET_ALL)
            clear_screen()

    #ask for hobbie 4
    while True:
        print("Food & Culinary Hobbies (Choose one that best matches you): ")
        print("0: Exit")
        print("1: Cooking")
        print("2: Food photography")
        print("3: Coffee brewing")
        try:
            option9 = int(input("Enter: ").strip())
            if option9 == 0:
                print(Fore.GREEN + "Exiting..."+Style.RESET_ALL)
                return
            if option9 == 1:
                h4 = 'Cooking'
                data.append(h4)
                clear_screen()
                break
            elif option9 == 2:
                h4 = 'Food photography'
                data.append(h4)
                clear_screen()
                break
            elif option9 == 3:
                h4 = 'Coffee brewing'
                data.append(h4)
                clear_screen()
                break
            else:
                print(Fore.RED+"Invalid INPUT! please enter 1 - 3 \n"+Style.RESET_ALL)
        except ValueError:
            print(Fore.RED+"Invalid input! Please enter a valid number! \n")
            clear_screen()

    #ask for hobbie 5
    while True:
        print("Social & Travel Hobbies (Choose one that best matches you): "+Style.RESET_ALL)
        print("0: Exit")
        print("1: Traveling")
        print("2: Vlogging")
        print("3: Volunteering")
        try:
            option10 = int(input("Enter: ").strip())
            if option10 == 0:
                print(Fore.GREEN+"Exiting..."+Style.RESET_ALL)
                return
            if option10 == 1:
                h5 = 'Traveling'
                data.append(h5)
                clear_screen()
                break
            elif option10 == 2:
                h5 = 'Vlogging'
                data.append(h5)
                clear_screen()
                break
            elif option10 == 3:
                h5 = 'Volunteering'
                data.append(h5)
                clear_screen()
                break
            else:
                print(Fore.RED+"Invalid INPUT! please enter 1 - 3 \n"+Style.RESET_ALL)
        except ValueError:
            print(Fore.RED+"Invalid input! Please enter a valid number! \n"+Style.RESET_ALL)
            clear_screen()

    #ask for hobbie 6
    while True:
        print("Creative & Artistic Hobbies (Choose one that best matches you): ")
        print("0: Exit")
        print("1: Painting")
        print("2: Photography")
        print("3: Graphic design")
        print("4: Writing (stories, poems, blogs)")
        print("5: Playing a musical instrument")
        print("6: Singing")
        print("7: Dancing")
        try:
            option11 = int(input("Enter: ").strip())
            if option11 == 0:
                print(Fore.GREEN+"Exiting..."+Style.RESET_ALL)
                return
            if option11 == 1:
                h6 = 'Painting'
                data.append(h6)
                clear_screen()
                break
            elif option6 == 2:
                h6 = 'Photography'
                data.append(h6)
                clear_screen()
                break
            elif option6 == 3:
                h6 = 'Graphic design'
                data.append(h6)
                clear_screen()
                break
            elif option11 == 4:
                h6 = 'Writing (stories, poems, blogs)'
                data.append(h6)
                clear_screen()
                break
            elif option11 == 5:
                h6 = 'Playing a musical instrument'
                data.append(h6)
                clear_screen()
                break
            elif option11 == 6:
                h6 = 'Singing'
                data.append(h6)
                clear_screen()
                break
            elif option11 == 7:
                h6 = 'Dancing'
                data.append(h6)
                clear_screen()
                break
            else:
                print(Fore.RED+"Invalid INPUT! please enter 1 - 7 \n"+Style.RESET_ALL)
        except ValueError:
            print(Fore.RED+"Invalid input! Please enter a valid number! \n"+Style.RESET_ALL)
            clear_screen()

    #preference
    print("Your Preference in Finding a Partner")    

    #ask for age range
    while True:
        print("Age: ")
        print("0: Exit")
        print("1: 18-20")
        print("2: 20-22")
        print("3: 22-24")
        print("4: 24-26")
        print("5: 26-28")
        print("6: 28-30")
        try:
            option12 = int(input("Enter: ").strip())
            if option12 == 0:
                print(Fore.GREEN+"Exiting..."+Style.RESET_ALL)
                return
            if option12 == 1:
                p_age = '18-20'
                data.append(p_age)
                clear_screen()
                break
            elif option12 == 2:
                p_age = '20-22'
                data.append(p_age)
                clear_screen()
                break
            elif option12 == 3:
                p_age = '22-24'
                data.append(p_age)
                clear_screen()
                break
            elif option12 == 4:
                p_age = '24-26'
                data.append(p_age)
                clear_screen()
                break
            elif option12 == 5:
                p_age = '26-28'
                data.append(p_age)
                clear_screen()
                break
            elif option12 == 6:
                p_age = '28-30'
                data.append(p_age)
                clear_screen()
                break
            else:
                print(Fore.RED+"Invalid INPUT! please enter 1 - 6 \n"+Style.RESET_ALL)
        except ValueError:
            print(Fore.RED+"Invalid input! Please enter a valid number! \n"+Style.RESET_ALL)
            clear_screen()

    #ask for height range
    while True:
        print("Height: ")
        print("0: Exit")
        print("1: below 150")
        print("2: 150 - 155")
        print("3: 155 - 160")
        print("4: 160 - 165")
        print("5: 165 - 170")
        print("6: 170 - 175")
        print("7: 175 - 180")
        print("8: 180 - 185")
        print("9: 185 - 190")
        print("10: 190 +")
        try:
            option13 = int(input("Enter: ").strip())
            if option13 == 0:
                print(Fore.GREEN+"Exiting..."+Style.RESET_ALL)
                return
            if option13 == 1:
                p_height = 'below 150'
                data.append(p_height)
                clear_screen()
                break
            elif option13 == 2:
                p_height = '150 - 155'
                data.append(p_height)
                clear_screen()
                break
            elif option13 == 3:
                p_height = '155 - 160'
                data.append(p_height)
                clear_screen()
                break
            elif option13 == 4:
                p_height = '160 - 165'
                data.append(p_height)
                clear_screen()
                break
            elif option13 == 5:
                p_height = '165 - 170'
                data.append(p_height)
                clear_screen()
                break
            elif option13 == 6:
                p_height = '170 - 175'
                data.append(p_height)
                clear_screen()
                break
            elif option13 == 7:
                p_height = '175 - 180'
                data.append(p_height)
                clear_screen()
                break
            elif option13 == 8:
                p_height = '180 - 185'
                data.append(p_height)
                clear_screen()
                break
            elif option13 == 9:
                p_height = '185 - 190'
                data.append(p_height)
                clear_screen()
                break
            elif option13 == 10:
                p_height = '190 +'
                data.append(p_height)
                clear_screen()
                break
            else:
                print(Fore.RED+"Invalid INPUT! please enter 1 - 10 \n"+Style.RESET_ALL)
        except ValueError:
            print(Fore.RED+"Invalid input! Please enter a valid number! \n"+Style.RESET_ALL)
            clear_screen()
    
    #ask if user is a student or worker
    while True:
        print("occupation: ")
        print("0: Exit")
        print("1: Student")
        print("2: Worker")
        try:
            option14 = int(input("Enter: ").strip())
            if option14 == 0:
                print(Fore.GREEN+"Exiting..."+Style.RESET_ALL)
                return
            if option14 == 1:
                p_occupation = 'Student'
                data.append(p_occupation)
                clear_screen()
                break
            elif option14 == 2:
                p_occupation = 'Worker'
                data.append(p_occupation)
                clear_screen()
                break
            else:
                print(Fore.RED+"Invalid INPUT! please enter 1 or 2 \n"+Style.RESET_ALL)
        except ValueError:
            print(Fore.RED+"Invalid input! Please enter a valid number! \n"+Style.RESET_ALL)
            clear_screen()

    #ask for personailty
    while True:
        print("Personality: ")
        print("0: Exit")
        print("1: Introvert")
        print("2: Extrovert")
        print("3: Ambivert")
        try:
            option15 = int(input("Enter: ").strip())
            if option15 == 0:
                print(Fore.GREEN+"Exiting..."+Style.RESET_ALL)
                return
            if option15 == 1:
                p_personality = 'Introvert'
                data.append(p_personality)
                clear_screen()
                break
            elif option15 == 2:
                p_personality = 'Extrovert'
                data.append(p_personality)
                clear_screen()
                break
            elif option15 == 3:
                p_personality = 'Ambivert'
                data.append(p_personality)
                clear_screen()
                break
            else:
                print(Fore.RED+"Invalid INPUT! please enter 1 , 2 or 3\n"+Style.RESET_ALL)
        except ValueError:
            print(Fore.RED+"Invalid input! Please enter a valid number! \n"+Style.RESET_ALL)
            clear_screen()
    
    #ask for love language
    while True:
        print("Love Language (Choose one that best matches you): ")
        print("0: Exit")
        print(Fore.RED+"1: Physical Touch")
        print("2: Words of Affirmation")
        print("3: Gifting")
        print("4: Acts of Service")
        print("5: Quality Time"+Style.RESET_ALL)
        try:
            option16 = int(input("Enter: ").strip())
            if option16 == 0:
                print(Fore.GREEN+"Exiting..."+Style.RESET_ALL)
                return
            if option16 == 1:
                p_lovelang = 'Physical Touch'
                data.append(p_lovelang)
                clear_screen()
                break
            elif option16 == 2:
                p_lovelang = 'Words of Affirmation'
                data.append(p_lovelang)
                clear_screen()
                break
            elif option16 == 3:
                p_lovelang = 'Gifting'
                data.append(lovelang)
                clear_screen()
                break
            elif option16 == 4:
                p_lovelang = 'Acts of Service'
                data.append(p_lovelang)
                clear_screen()
                break
            elif option16 == 5:
                p_lovelang = 'Quality Time'
                data.append(p_lovelang)
                clear_screen()
                break
            else:
                print(Fore.RED+"Invalid INPUT! please enter 1 - 5 \n"+Style.RESET_ALL)
        except ValueError:
            print(Fore.RED+"Invalid input! Please enter a valid number! \n"+Style.RESET_ALL)
            clear_screen()

    # we store detail of that person as a list in 'data'
    # after success complete every needed 
    # we will check a file to append into men or women file
    if gender == 'Male':
        filename = "G1_T2_Code/text_files/men.txt"
        with open(filename, 'r', encoding='utf-8') as  file:
            lines = file.readlines()
            #since we have header so id of that new user equal to number of line
            find_id = len(lines)
            id = 'm' + str(find_id)
        format_data = '\n' + id + '|' + '|'.join(map(str, data))
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(format_data)
        user = Man(id, *data)

    if gender == 'Female':
        filename = "G1_T2_Code/text_files/women.txt"
        with open(filename, 'r', encoding='utf-8') as  file:
            lines = file.readlines()
            #since we have header so id of that new user equal to number of line
            find_id = len(lines)
            id = 'f' + str(find_id)
        format_data = '\n' + id + '|' + '|'.join(map(str, data))
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(format_data)
        user = Woman(id, *data)

    print(Fore.CYAN+"=" * 50)
    print(Fore.GREEN+"You successfully check in our program.")
    print(Fore.MAGENTA+f"Username: {data[0]}")
    print(f"ID: {id}")
    print("YOU need Username and ID for using our program next-time.")
    print(Fore.CYAN+"=" *50 +Style.RESET_ALL)
    
    #Asking if they wanna searching a match
    while True:
        print("Are you ready to find your soulmate?")
        # Remove white space and change input to lowercase
        check = input(Fore.LIGHTBLUE_EX + Style.BRIGHT + "yes/no: " + Style.RESET_ALL).strip().lower()
        if check == 'yes':
    
            #create an instance of matchmaking system
            matchmaking_system = MatchmakingSystem()
                
            #get matches
            matches = matchmaking_system.suggest_match(user)
            
            # Display matches one by one and let users accept or reject
            accepted_matches = []
            clear_screen()
            for match, score in matches:
                print(Fore.GREEN+"\nHere is a potential match:")
                print(Fore.LIGHTMAGENTA_EX+match.get_profile())
                print(f"Match Score: {score}%"+Style.RESET_ALL)

                while True:  # This loop ensures user input is valid before moving to the next match
                    try:
                        response = input(Fore.BLUE+"Do you accept or reject this person? (yes/no): "+Style.RESET_ALL).strip().lower()
                        if response == 'yes':
                            accepted_matches.append((match, score))  # Store match along with score
                            clear_screen()
                            display_accept_message()
                            break  # Move to the next match
                        elif response == 'no':
                            clear_screen()
                            display_reject_message()
                            break  # Move to the next match
                        elif response == '0':
                            clear_screen()
                            print(Fore.GREEN + "\nYou have chosen to exit. Here are your accepted matches so far:")
                            for accepted_match, accepted_score in accepted_matches:
                                print(Fore.RED + f"Username: {accepted_match.get_username()}, Score: {accepted_score}%" + Style.RESET_ALL)
                            return
                        else:
                            print(Fore.RED+"Invalid input! Please enter 'yes' or 'no'."+Style.RESET_ALL)
                    except ValueError:
                        print(Fore.RED+"Invalid input! Please enter 'yes' or 'no'."+Style.RESET_ALL)
                        clear_screen()

            # Display accepted matches after all suggestions
            if accepted_matches:
                print(Fore.GREEN+"\nHere are your accepted matches:")
                for match, score in accepted_matches:
                    print(Fore.RED+f"Username: {match.get_username()}, Score: {score}%"+Style.RESET_ALL)
            else:
                print(Fore.RED+"No matches found."+Style.RESET_ALL)

            break
            
        #if user don't want to search
        elif check == 'no':
            print(Fore.GREEN + "\nThanks for joining Us")
            print("Hope to see you again soon.")
            print("Exiting..."+Style.RESET_ALL)
            return
        else:
            print("\n Invalid input! Please enter 'yes' or 'no'. \n")


def old_user():
    while True:
        clear_screen()
        username = input(Fore.GREEN+"Please enter your Username: ").strip()
        user_id = input("ID: " +Style.RESET_ALL).strip()

        if username == '0':
            print(Fore.GREEN+"Exiting..."+Style.RESET_ALL)
            return
        
        if user_id == 0:
            print(Fore.GREEN+"Exiting..."+Style.RESET_ALL)
            return

        check = 0  # Initialize check before file reading

        if 'm' in user_id:
            filename = "G1_T2_Code/text_files/men.txt"
        elif 'f' in user_id:
            filename = "G1_T2_Code/text_files/women.txt"
        else:
            print(Fore.RED+"Invalid ID format. Please try again."+Style.RESET_ALL)
            continue  # Restart the loop

        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                data = line.strip().split('|')

                if data[0] == user_id and data[1] == username:
                    print(Fore.CYAN+"=" * 50)
                    print(Fore.MAGENTA+ "Verify account successfully.")
                    print(f"Username: {data[1]}")
                    print(f"ID: {data[0]}")
                    print("YOU need Username and ID for using our program next time."+Style.RESET_ALL)
                    user = Man(*data) if data[2].lower() == 'male' else Woman(*data)
                    check = 1
                    break  # Exit for loop since the user is verified

        if check == 1:
            break  # Exit while loop since verification is successful
        else:
            print(Fore.RED+"Username or ID is wrong. Please check again.\n"+Style.RESET_ALL)

    #display user's profile
    print(user.get_profile())

    #Asking if they wanna searching a match
    while True:
        # Remove white space and change input to lowercase
        print("Are you ready to find your soulmate?")
        check = input(Fore.LIGHTBLUE_EX + Style.BRIGHT + "yes/no: " + Style.RESET_ALL).strip().lower()
        if check == 'yes':
    
            #create an instance of matchmaking system
            matchmaking_system = MatchmakingSystem()
                
            #get matches
            matches = matchmaking_system.suggest_match(user)
            
            # Display matches one by one and let users accept or reject
            accepted_matches = []
            clear_screen()
            for match, score in matches:
                print(Fore.GREEN+"\nHere is a potential match:")
                print(Fore.LIGHTMAGENTA_EX+match.get_profile())
                print(f"Match Score: {score}%"+Style.RESET_ALL)

                while True:  # This loop ensures user input is valid before moving to the next match
                    try:
                        response = input(Fore.BLUE+"Do you accept or reject this person? (yes/no): "+Style.RESET_ALL).strip().lower()
                        if response == 'yes':
                            accepted_matches.append((match, score))  # Store match along with score
                            clear_screen()
                            display_accept_message()
                            break  # Move to the next match
                        elif response == 'no':
                            clear_screen()
                            display_reject_message()
                            break  # Move to the next match
                        elif response == '0':
                            clear_screen()
                            print(Fore.GREEN + "\nYou have chosen to exit. Here are your accepted matches so far:")
                            for accepted_match, accepted_score in accepted_matches:
                                print(Fore.RED + f"Username: {accepted_match.get_username()}, Score: {accepted_score}%" + Style.RESET_ALL)
                            return
                        else:
                            print(Fore.RED+"Invalid input! Please enter 'yes' or 'no'."+Style.RESET_ALL)
                    except ValueError:
                        print(Fore.RED+"Invalid input! Please enter 'yes' or 'no'."+Style.RESET_ALL)

            # Display accepted matches after all suggestions
            if accepted_matches:
                print(Fore.GREEN+"\nHere are your accepted matches:")
                for match, score in accepted_matches:
                    print(Fore.RED+f"Username: {match.get_username()}, Score: {score}%"+Style.RESET_ALL)
            else:
                print(Fore.RED+"No matches found."+Style.RESET_ALL)

            break

        #if user don't want to search
        elif check == 'no':
            print(Fore.GREEN + "\nThanks for joining Us")
            print("Hope to see you again soon.")
            print("Exiting..."+Style.RESET_ALL)
            return
        else:
            print("\n Invalid input! Please enter 'yes' or 'no'. \n")


# Run the welcome function when the program starts
if __name__ == "__main__":
    welcome()
