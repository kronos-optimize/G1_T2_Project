class Person():
    def __init__(self, id, username, gender, age, height, occupation, zodiac, personality, 
                 lovelang, h1, h2, h3, h4, h5, h6, p_age, p_height, p_occupation, p_personality, 
                 p_lovelang):
        self.id = id
        self.username = username
        self.gender = gender
        self.age = int(age)
        self.zodiac = zodiac
        self.height = height
        self.occupation = occupation
        self.personality = personality
        self.lovelang = lovelang
        self.hobbies = [h1, h2, h3, h4, h5, h6]
        self.preference = {
            "age": p_age,
            "height": p_height,
            "occupation": p_occupation,
            "personality": p_personality,
            "lovelang": p_lovelang
        }

class Man(Person):
    pass

class Woman(Person):
    pass

class MatchmakingSystem:
    def __init__(self):
        self.men_file = "men.txt"
        self.women_file = "women.txt"
        self.load_users()
        self.zodiac_scores = {
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

    def load_users(self):
        self.men = self.load_data(self.men_file)
        self.women = self.load_data(self.women_file)

    def load_data(self, filename):
        users = []
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                next(file)  # Skip header
                for line in file:
                    data = line.strip().split('|')
                    if len(data) != 20:  # Ensure data length matches Person constructor
                        print(f"Error: Incorrect data format in {filename}: {data}")
                        continue  # Skip invalid entries

                    if filename == self.men_file:
                        users.append(Man(*data))
                    else:
                        users.append(Woman(*data))
        except FileNotFoundError:
            print(f"File {filename} not found.")
        return users

# Create an instance of MatchmakingSystem
match_making = MatchmakingSystem()