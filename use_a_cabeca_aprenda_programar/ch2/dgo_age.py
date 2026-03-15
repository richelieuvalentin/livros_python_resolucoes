# Pergunta ao usuário o nome e idade do cachorroe guarda em variavéis
dog_name = input("What is your dog's name? ")
dog_age = int(input("What is your dog's age? "))

# Converte para anos humanos
human_age = dog_age * 7

# Output para o usuário
print(f"Your dog's age is {human_age}, years old in human years")