print("Enter data to convert to morse code")
data = input()
data = data.upper()
character = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
             'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
code = ['•-', '-•••', '-•-•', '-••', '•', '••-•', '--•', '••••', '••', '•---', '-•-', '•-••', '--', '-•', '---', '•--•', '--•-', '•-•', '•••',
        '-', '••-', '•••-', '•--', '-••-', '-•--', '--••', '-----', '•----', '••---', '•••--', '••••-', '•••••', '-••••', '--•••', '---••', '----•']

for i in range(0, len(data)):
    char_index = character.index(data[i])
    morse_code = code[char_index]

print(morse_code)
