translation_table = str.maketrans("12345","aeiou") 

my_string ="Th3s 3s 1 str3ng"

translated = my_string.translate(translation_table)
print(translated)
