def rock_paper_scissors():
    import random

    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''

    def game():
        game_images = [rock, paper, scissors]

        user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
        print(game_images[user_choice])

        computer_choice = random.randint(0, 2)
        print("Computer chose:")
        print(game_images[computer_choice])

        if user_choice >= 3 or user_choice < 0:
            print("You typed an invalid number, you lose!")
        elif user_choice == 0 and computer_choice == 2:
            print("You win!")
        elif computer_choice == 0 and user_choice == 2:
            print("You lose")
        elif computer_choice > user_choice:
            print("You lose")
        elif user_choice > computer_choice:
            print("You win!")
        elif computer_choice == user_choice:
            print("It's a draw")

    game_continue = True

    while game_continue == True:
        game()
        user_contine = input("Do you like to continue?Type 'y' for yes and 'n' for no. ").lower()
        if user_contine == "y":
            game_continue == True
        elif user_contine == "n":
            game_continue == False
            print("Goodbye!")
        else:
            print("Please type n or y please")

def min_max_mean():
    def find_min_max_median(numbers):
        if len(numbers) == 0:
            print("Oops! The list is empty. Please enter some numbers.")
            return
        min_value = None
        max_value = None
        median_value = None

        for num in numbers:
            if min_value is None or num < min_value:
                min_value = num
            if max_value is None or num > max_value:
                max_value = num
        sorted_numbers = sorted(numbers)
        mid_index = len(sorted_numbers) // 2

        if len(sorted_numbers) % 2 == 0:
            median_value = (sorted_numbers[mid_index - 1] + sorted_numbers[mid_index]) / 2
        else:
            median_value = sorted_numbers[mid_index]


        print(f"Minimum: {min_value}")
        print(f"Maximum: {max_value}")
        print(f"Median: {median_value}")
    try:
        numbers = [float(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
        find_min_max_median(numbers)
    except ValueError:
        print("Oops! It seems you entered something other than numbers. Please try again.")


def csv_analysis():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt


    def load_dataset():
        while True:
            try:
                file_path = input("Enter the path to the CSV file: ")
                data = pd.read_csv(file_path)
                return data
            except FileNotFoundError:
                print("File not found. Please provide a valid file path.")


    def analyze_data(data):

        data = data.dropna()


        summary_stats = data.describe()


        mean_column = data['Column_Name'].mean()


        data['Column_Name'].hist()
        plt.title('Histogram of Column_Name')
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.show()

        unique_values_count = data['Categorical_Column'].nunique()


        group_mean = data.groupby('Category_Column')['Value_Column'].mean()


        plt.scatter(data['Numerical_Column1'], data['Numerical_Column2'])
        plt.title('Scatter Plot')
        plt.xlabel('Numerical_Column1')
        plt.ylabel('Numerical_Column2')
        plt.show()


        data.boxplot(column='Numerical_Column3')
        plt.title('Box Plot')
        plt.ylabel('Numerical_Column3')
        plt.show()

        return summary_stats, mean_column, unique_values_count, group_mean

    if __name__ == "__main__":

        dataset = load_dataset()


        summary_stats, mean_column, unique_values_count, group_mean = analyze_data(dataset)


        print("\nSummary Statistics:")
        print(summary_stats)
        print(f"Mean of Column_Name: {mean_column:.2f}")

        print(f"Number of unique values in Categorical_Column: {unique_values_count}")
        print("\nGrouped mean by Category_Column:")
        print(group_mean)

def word_checker():

    sentence = input("Enter a sentence: ")

    word_list = sentence.split()
    num_words = len(word_list)

    print(f"Number of words in the sentence: {num_words}")


    unique_words = list(set(word_list))
    print("Unique words in the sentence:")
    for word in unique_words:
        print(word)


    search_word = input("Enter a word to check if it's in the sentence: ")

    if search_word in word_list:
        print(f"'{search_word}' is in the sentence.")
    else:
        print(f"'{search_word}' is not in the sentence.")

def average_list():

    def average_of_list(numbers):
        if not numbers:
            return 0
        total = sum(numbers)
        return total / len(numbers)

    input_numbers = input("Enter a list of numbers separated by spaces: ")
    number_list = [float(num) for num in input_numbers.split()]

    average = average_of_list(number_list)
    print(f"The average of the numbers is: {average:.2f}")

def personal_info():
    import re
    import json

    class PersonalInfo:
        def __init__(self, name, birthdate, address):
            self.name = name
            self.birthdate = birthdate
            self.address = address

        def to_dict(self):
            return {
                "Name": self.name,
                "Birthdate": self.birthdate,
                "Address": self.address
            }


    def validate_input(prompt, validation_func):
        while True:
            user_input = input(prompt).strip()
            if validation_func(user_input):
                return user_input
            else:
                print("Invalid input. Please try again.")


    def validate_birthdate(birthdate):
        if re.match(r'^\d{4}-\d{2}-\d{2}$', birthdate):
            try:
                year, month, day = map(int, birthdate.split('-'))
                if 1900 <= year <= 2100 and 1 <= month <= 12 and 1 <= day <= 31:
                    return True
            except ValueError:
                pass
        return False


    def save_personal_info(info, filename):
        with open(filename, 'w') as file:
            json.dump(info.to_dict(), file)
            print("Personal information saved to 'personal_info.json'")


    def load_personal_info(filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                return PersonalInfo(data["Name"], data["Birthdate"], data["Address"])
        except (FileNotFoundError, json.JSONDecodeError):
            return None


    personal_info = None

    print("Welcome to the Personal Information Program.")


    load_option = input("Do you want to load existing personal information? (yes/no): ").lower()
    if load_option == 'yes':
        personal_info = load_personal_info('personal_info.json')
        if personal_info:
            print("Loaded Personal Information:")
            print("Name:", personal_info.name)
            print("Birthdate:", personal_info.birthdate)
            print("Address:", personal_info.address)
        else:
            print("No personal information file found or invalid data in the file.")
    else:

        print("Please enter your personal information:")

        name = validate_input("Name: ", lambda x: len(x) > 0)
        birthdate = validate_input("Birthdate (YYYY-MM-DD): ", validate_birthdate)
        address = input("Address: ")  # No specific validation for address

        personal_info = PersonalInfo(name, birthdate, address)

    print("\nPersonal Information:")
    print("Name:", personal_info.name)
    print("Birthdate:", personal_info.birthdate)
    print("Address:", personal_info.address)

    save_option = input("Do you want to save this information to a file? (yes/no): ").lower()
    if save_option == 'yes':
        save_personal_info(personal_info, 'personal_info.json')

def average():
    def average_of_list(numbers):
        return sum(numbers) / len(numbers) if numbers else 0

    user_input = input("Enter a list of numbers separated by spaces: ")
    number_list = [float(num) for num in user_input.split()]

    average = average_of_list(number_list)
    print(f"The average of the numbers is: {average:.2f}")

print("Hello,welcome to task generator!\n")
user_input = input("Type 'personal info' if you want to get access to code.\n"
      "Type 'word checker' if you want to get access to code.\n"
      "Type 'data analysis' if you want to get access to code.\n"
      "Type 'average of list' if you want to get access to code.\n"
      "Type 'max min mean' if you want to get access to code.\n"
      "Type 'rock paper scissors' if you want to get access to code.\n")
if user_input == 'personal info':
    personal_info()
elif user_input == 'word checker':
    word_checker()
elif user_input == 'data analysis':
    csv_analysis()
elif user_input == 'rock paper scissors':
    rock_paper_scissors()
elif user_input == 'max min mean':
    min_max_mean()
elif user_input == 'average of list':
    average()
else:
    print("Please enter valid names!")


