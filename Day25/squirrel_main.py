import pandas as pd

data = pd.read_csv(
    "https://raw.githubusercontent.com/svrohith9/100-days-python/main/Day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])


print(
    f"Red : {red_squirrels}\nBlack : {black_squirrels}\nGray : {grey_squirrels}")

# creating a dataframe for above extracted data
data_dict = {
    "Fur": ["Red", "Black", "Gray"],
    "Count": [red_squirrels, black_squirrels, grey_squirrels]
}
df = pd.DataFrame(data_dict)
# save it as a csv file
# df.to_csv("extracted_data.csv")
print(df)
