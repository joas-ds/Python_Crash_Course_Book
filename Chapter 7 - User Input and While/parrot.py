# #Os laços For executam um bloco de código uma vez para cada item na coleção
# #Os laços WHILE são executados enquanto uma certa condição é verdadeira:
# current_number = 1
# while current_number <= 5:
#     print(f"Counting number {current_number}.")
#     current_number += 1

# #Letting the USER choose when to quit:
# prompt = "\nTell me something, and I will repeat it back to you:" \
#          "\nEnter 'quit' to end the program. "
# #We need to assing an empty variable message so python can check the while block for the 1st time.
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     #Removing the 'quit' from output:
#     if message != 'quit':
#         print(message)

# #Using a FLAG
# active = True #Essa é a variável flag
#
# prompt = "\nTell me something, and I will repeat it back to you:" \
#          "\nEnter 'quit' to end the program. "
#
# while active:
#     message = input(prompt)
#
#     if message.lower() == 'quit':
#         active = False  #Aqui o programa se encerra porque o While está considerando rodar com o valor True
#     else:
#         print(message)

# #Using BREAK to exit a loop:
# #O break pode ser usado em qualquer tipo de loop
# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.) "
#
# while True:     #Um loop While True rodará pra sempre até encontrar um break.
#     city = input(prompt)
#
#     if city.lower() == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}.")

# #Using Continue in a loop:
# #   imprimindo apenas números ímpares
# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue                #Se o número FOR divisível por 2, o programa IGNORA e continua.
#
#     print(current_number)
