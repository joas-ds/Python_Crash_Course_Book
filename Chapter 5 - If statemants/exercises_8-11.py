# #5.8 Hello Admin:
# usernames = ['TechMaster', 'CodeWizard', 'DataGuru', 'CyberNinja', 'PixelPilot',
#              'CloudCommander', 'ScriptMaster', 'admin', 'LogicLynx', 'QuantumCoder']
#
# for username in usernames:
#     if username == 'admin':
#         print("Olá, Mestre! Bem-vindo de volta, pronto para banir alguns engraçadinhos hoje?")
#     else:
#         print(f"Bem-vindo de volta {username}, tenha um bom jogo.")
#
# #5.9 No Users
# del usernames[:0]
# if usernames:
#     print("Precisamos encontrar mais usuários!")
#
# #5.10 Checking Usernames
# current_users = ["Liam", "Olivia", "Noah", "Emma", "Elijah", "Ava", "James"]
# lower_current_users = ["liam", "olivia", "noah", "emma", "elijah", "ava", "james"]
#
# new_users = ["AVA", "JAMES", "Sophia", "William", "Isabella"]
#
# for user in new_users:
#     if user.lower() in lower_current_users:
#         print(f"O usuário {user} já está sendo utilizado, escolha outro.")
#     else:
#         print(f"O usuário {user} está disponível.")
#
#5.11 Ordinal Numbers:
numbers = list(range(1,11))
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}st")

#5.12 Styling if Statements
#Eu já faço isso.

