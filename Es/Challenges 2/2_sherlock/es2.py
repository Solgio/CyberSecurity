# Apri il file in modalità lettura
with open("C:\\Users\\loren\\OneDrive\\Desktop\\Uni\\2° anno\\CyberSecurity\\Es\\Challenges\\2_sherlock\\challenge.txt", "r") as file:
    contenuto = file.read()  # Leggi il contenuto del file

# Inizializza la stringa di output
output = ""
counter=0

# Cicla attraverso ogni carattere del contenuto del file
for char in contenuto:
    if char == 'Z':
        output += '0'
        counter+=1
    elif char == 'N':
        output += '1'
        counter+=1


    if counter == 8:
        output += " "
        counter = 0



# Stampa la stringa di output
print(output)
