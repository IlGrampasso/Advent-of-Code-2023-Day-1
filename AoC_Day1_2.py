import re

# Dizionario per la mappatura dei numeri in forma di stringa ai numeri reali
word_to_num = {
    "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
    "six": "6", "seven": "7", "eight": "8", "nine": "9"
}


# Funzione per trovare il primo e l'ultimo numero in una stringa
def find_first_and_last_number(s):
    digits = []
    # Sostituisci i numeri in forma di stringa con le loro rappresentazioni numeriche
    i = 0
    while i < len(s):
        if s[i].isdigit():
            digits.append(s[i])
            i += 1
        else:
            matched = False
            for word, num in word_to_num.items():
                if s[i:i + len(word)] == word:
                    digits.append(num)
                    i += len(word)
                    matched = True
                    break
            if not matched:
                i += 1

    if len(digits) >= 1:
        return int(digits[0] + digits[-1])
    else:
        return 0  # Nessun numero trovato


# Apri il file e leggi le righe
with open("input1.txt", "r") as file:
    rows = file.readlines()

total_sum = 0

# Itera su ogni riga per trovare i numeri e calcolare la somma
for row in rows:
    combined_number = find_first_and_last_number(row.strip())
    total_sum += combined_number
    print(f"Row: {row.strip()}, Combined number: {combined_number}")

print("\nTotal sum:", total_sum)
