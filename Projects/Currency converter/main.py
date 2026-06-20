from api.exchange import convert_currency
from ui.console import get_user_input, show_result
from utils.storage import save_to_csv

HISTORY_FILE = "history.csv"

def main():
    amount, from_currency, to_currency = get_user_input()
    result = convert_currency(amount, from_currency, to_currency)
    show_result(result)
    save_to_csv(HISTORY_FILE, result)

main()