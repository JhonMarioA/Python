from api.petitions import search_by_category, search_by_keyword
from utils.filter_and_save_in_dataframe import filter_and_save

def format_response(response):
    if response.status_code == 200:
        data = response.json()
        for i, article in enumerate(data.get("articles", []), start=1):
            print(f"\n{i}. {article['title']}")
            print(article['url'])
    else:
        print("Error:", response.status_code, response.text)


def menu():

    print("Welcome to the News API!!!\n")
    print("Options:\n1) Search by category.\n2) Search by keyword.\n3) Filter and save in a DataFrame with Pandas.")
    option = int(input("Enter the option: "))

    if option == 1:
        category = input("Enter the category: ")
        response = search_by_category(category)
        format_response(response)
 
    elif option == 2:
        key_word = input("Enter the keyword: ")
        response = search_by_keyword(key_word)
        format_response(response)
        
    elif option == 3:
        category = input("Enter the category: ")
        response = search_by_category(category)
        df = filter_and_save(response)
        print(df.head())
        
    else:
        print("Wrong option!!!")

