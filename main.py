from src.widget import mask_account_card

a = 'Visa Platinum 7000792289606361'
if __name__ == "__main__":
    print(mask_account_card('isaplatinum 7000792289606361'))
    print(mask_account_card('maestro7000792289606361'))
    print(mask_account_card('73654108430135874305'))
    print(len(a))
    print(a.split())
