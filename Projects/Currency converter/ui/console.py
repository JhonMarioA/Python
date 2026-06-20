
def get_user_input():

    print("Enter the next parameters:\n")

    amount = float(input("Enter the amount: "))
    from_currency = input("From currency (e.g USD): ").upper()
    to_currency = input("To currency (e.g EUR): ").upper()

    return amount, from_currency, to_currency



def show_result(result: dict):  

    rate = list(result["rates"].values())[0]
    to_currency = list(result["rates"].keys())[0]
    print(f"{result['amount']} {result['base']} = {rate} {to_currency}") 
