#PROJECT: Inteligent Registration System (PYTHON)#

registrations =[]

while True:
    print('\n---Main Menu---')
    print('1.Register a new person: ')
    print('2.View all registrations: ')
    print('3.Filter adults only: ')
    print('4.View most common professions: ')
    print('5. Exit')
    
    option = input('Choose an option: ')
    
    if option == '1': #Variaveis da 'option 1' criadas para cadastro de nova pessoa.
        person_name = input('Write your name: ')
        person_age = int(input('Write your age: '))
        person_profession = input('Write your profession: ')
        
        person = {      #Criando um dicionario person com os dados, esse dicionario vai ser adicionado na lista registrations.
            'name': person_name,
            'age': person_age,
            'profession': person_profession
        }
        
        registrations.append(person)
        print(f'{person_name} has been succesfully registered!')
        print(registrations) #Isso mostra a lista completa e verifica o que foi armazenado.
        
    elif option == '2':
        if not registrations:
            print('No registrations found.')
        else:
            print('\n--- All Registrations ---')
            for i, person in enumerate(registrations, start=1):
                print(f"{i}. Name: {person['name']}, Age: {person['age']}, Profession: {person['profession']}")
                         
    elif option == '3':
        if not registrations:
            print('No registrations found.')
        else:
            print('\n--- Adults Only ---')
            for i, person in enumerate(registrations, start=1):
                if person['age'] >= 18:
                    print(f"{i}. Name: {person['name']}, Age: {person['age']}, Profession: {person['profession']}")
                    
    elif option == '4':
        if not registrations:
            print('No registrations found. ')
        else:
            profession_count = {} #Criando um dicionario para contar as profissoes.
            for person in registrations:
                profession = person['profession']
                if profession in profession_count:
                    profession_count[profession] += 1
                else:
                    profession_count[profession] = 1    
            sorted_professions = sorted(profession_count.items(), key = lambda x:x[1], reverse=True) #Ordenando o dicionario por valor(quantidade de pessoas) de forma decrescente.
            print('\n--- The most commom profession ---')
            for profession, count in sorted_professions:
                print(f'Profession: {profession}, Count: {count}')
                
    elif option == '5':
        print('Exiting the system. See you later!')
        break #Encerra o laco while e finaliza o programa.

    else:
        print('Invalid option. Please try again.') #Trata entradas invalidas.

