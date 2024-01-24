import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dic = {row.letter: row.code for (index, row) in data.iterrows() }

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dic[letter] for letter in word]
    except:
        print("Sorry, only letters in the alphabt please.")
        generate_phonetic()
    else:
        print(output_list)

    print(output_list)

generate_phonetic()