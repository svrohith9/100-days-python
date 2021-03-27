import pandas as pd

data = pd.read_csv(
    "https://raw.githubusercontent.com/svrohith9/100-days-python/b7567b17a72663f7f056f3ffb0dcfe631af9edd1/Day26/NATO-alphabet-start/nato_phonetic_alphabet.csv"
)
user_str = input("Enter the String: ").lower()
output_str = [
    row.code
    for i in range(0, len(user_str))
    for index, row in data.iterrows()
    if row.letter.lower() == user_str[i]
]
print(output_str)