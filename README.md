# Matching With Your Soulmate

## Description

This project is a Python-based matchmaking system that helps users find their ideal partner based on criteria such as age, zodiac sign, occupation, personality, love language, and hobbies. It calculates compatibility scores using various factors and suggests the best matches.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/kronos-optimize/G1_T2_Project.git
   ```
   
2. Navigate to the project directory:

   ```bash
   cd G1_T2_Project/G1_T2_Code
   ```

3. Install dependencies:

To Run our code you need to have colorama library 
we use colorama for coloring our text in code (terminal output)
   
   ```bash
   pip install colorama
   ```

## Usage
To run the matchmaking system, please stay in folder G1_T2_Project 

so after install colorama library

execute:

```bash
cd ..
```

```bash
python G1_T2_Code/main.py
```

The program will guide users through:

- Creating a profile (for new users)

- Logging in (for returning users)

- Finding matches based on compatibility

- Accepting or rejecting suggested matches

## Features

- User profile creation (name, age, zodiac sign, occupation, etc.)

- Preference-based matchmaking

- Compatibility scoring system:

  - Age (+12%)

  - Height (+10%)

  - Occupation (+10%)

  - Love Language (+16%)

  - Personality (+18%)

  - Zodiac Sign Compatibility (+10%)

  - Shared Hobbies (+4% each)

- Accept/reject match suggestions

- Personalized responses for accepted/rejected matches

## Configuration

- User data is stored in `text_files/men.txt` and `text_files/women.txt`

- Zodiac compatibility scores are predefined in the system

## File Structure
```
G1_T2_Project/

│-- documents/

│ ├── G1_T2_Report.pdf # Our report for this project

│ ├── G1_T2_Slide.pptx # Slide presentation (PowerPoint format)

│ ├── G1_T2_Slide.pdf # Slide presentation (PDF format)

│

│-- G1_T2_Code/

│ ├── main.py # Main program logic

│ ├── test.py # Checks if each line in text files has 20 columns

│ ├── text_files/

│ │ ├── men.txt # Male user data

│ │ ├── women.txt # Female user data

│

│-- README.md # Project documentation
```

## Contributing

We are a group of students from CADT majoring in Computer Science, and this is our project for the OOP (python) course.

Lecturer: Han Leangsiv

Group Members

1: Chum Palla

2: Soeun Sokchetra

3: Khy Pichsereyvathanak



