import csv 


def save_to_csv(HISTORYFILE: str, result: dict):

    to_currency, rate = list(result["rates"].items())[0]

    with open(HISTORYFILE, mode="a", newline="") as file:
        writer = csv.writer(file)

        if file.tell() == 0:
            writer.writerow(["amount", "base", "date", "to_currency", "rate"])
            writer.writerow([result["amount"], result["base"], result["date"], to_currency, rate])


