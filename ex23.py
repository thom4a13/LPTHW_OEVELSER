import sys
script, encoding, error = sys.argv

def main(language_file, encoding, errors): 
    line = language_file.readline()
    
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip() #Fjerne alle whitespaces fra variablen "line" fra linje 5. Det bliver gemt i "next_lang" 
    raw_bytes = next_lang.encode(encoding, errors=errors) #Her "omkodes" next_lang til bytes vua "encode" og assigner det til  "raw_bytes"
    cooked_string = raw_bytes.decode(encoding, errors=errors) #raw_bytes "decodes" og gemmes i en variable 

    print(raw_bytes, "<===>", cooked_string) #De to variabler sættes overfor hinanden på hver side af "<===>" 


languages = open("languages.txt", encoding="utf-8") #Her åbnes .txt filen og encoder med utf-8. 

main(languages, encoding, error)


'''
Samlet set læser denne kode en fil, der indeholder en liste over programmeringssprog, koder hvert sprog som bytes ved hjælp af en specificeret kodning og afkoder 
derefter bytes tilbage til en streng. Programmet udskriver derefter både de rå bytes og den afkodede streng til konsollen. 
ovedfunktionen læser hver linje i filen og kalder print_line-funktionen for at udskrive hver linjes rå bytes og afkodede streng. 
'''