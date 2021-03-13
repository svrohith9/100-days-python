# Dictionaries
sample = {
    "one": 1,
    "two": 2,
    "three": 3
}
print(sample)

key = {
    "key1": [1, 2, sample],
    "key2": sample
}
print(key)

print("************************")

trips_dic = [
    {
        "country": "England",
        "visited": 10,
        "places": ["Big Ben", "London Eye", "Diagon Alley"]
    },
    {
        "country": "South Africa",
        "visited": 2,
        "places": ["Durham", "Cape Town"]
    }
]


def add_data():
    country = input("Enter the Country: ")
    visited = input("Enter the no of times you visited: ")
    places = input(
        "Enter the places visited comma(,) separated: ").lower().split(",")
    temp = {}
    temp["country"] = country
    temp["places"] = places
    temp["visited"] = visited
    trips_dic.append(temp)


add_data()
print(trips_dic)
