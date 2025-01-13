"""
Write a program that manages a list of countries and their capital cities. It should
prompt the user to enter the name of a country. If the program already "knows"
the name of the capital city, it should display it. Otherwise it should ask the user to
enter it. This should carry on until the user terminates the program (how this
happens is up to you).
Note: A good solution to this task will be able to cope with the country being entered
variously as, for example, "Wales", "wales", "WALES" and so on
"""

def manage_countries_and_capitals():
    countries_capitals = {}

    print("Type 'exit' to terminate the program.\n")

    while True:
        country = input("Enter the name of a country: ").strip()

        if country.lower() == 'exit':
            print("Exiting program. Goodbye!")
            break

        normalized_country = country.lower()

        if normalized_country in countries_capitals:
            capital = countries_capitals[normalized_country]
            print(f"The capital of {country.title()} is {capital.title()}.\n")
        else:
            capital = input(f"I don't know the capital of {country.title()}. Please enter it: ").strip()

            countries_capitals[normalized_country] = capital.lower()
            print(f"Thank you! I've stored that the capital of {country.title()} is {capital.title()}.\n")

if __name__ == "__main__":
    manage_countries_and_capitals()
