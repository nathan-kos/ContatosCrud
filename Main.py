from Management import Management

#initializing management class
system = Management();

#####################################################
#functions
#####################################################
def createContact():    
    name = input("Digite o nome do contato: ");
    email = input("Digite o email do contato: ");
    phone = input("Digite o telefone do contato (Apenas números): ");
    try:
        system.createContact(name, phone, email);
        print("Contato criado com sucesso");
    except ValueError as e:
        print("Erro ao criar contato: ", e);

def findContactByName():
    name = input("Insira o nome para busca: ");
    try:
        contact = system.findByName(name);
        print("Nome: ", contact.name, " Email: ", contact.email, " Telefone: ", contact.phone);
    except ValueError as e:
        print("Erro ao buscar contato: ", e);

def deleteContactByName():
    name = input("Insira o nome para remoção: ");
    try:
        system.deleteByName(name);
    except ValueError as e:
        print("Erro ao remover contato: ", e);

def listContacts():
    contacts = system.listContacts();
    i = 1;
    for contact in contacts:
        print("Contato - ", i, "Nome: ", contact.name, " Email: ", contact.email, " Telefone: ", contact.phone);
        i += 1;

def updateContact():
    listContacts();
    index = input("Qual número do contato você deseja atualizar?");
    name = input("Digite o nome do contato (Mantenha em branco caso não queira atualizar): ");
    email = input("Digite o email do contato (Mantenha em branco caso não queira atualizar): ");
    phone = input("Digite o telefone do contato (Apenas números)(Mantenha em branco caso não queira atualizar): ");
    try:
        system.updateContactByIndex(int(index) - 1, name, phone, email);
        print("Contato atualizado com sucesso");
    except ValueError as e:
        print("Erro ao atualizar contato: ", e);
 


def main():
    while True:
        print("\n");
        print("Bem vindo ao sistema de gerenciamento de contatos");
        print("Escolha uma opção: ");
        print("1 - Adicionar contato");
        print("2 - Atualizar contato");
        print("3 - Encontrar contato pelo nome");
        print("4 - Remover contato");
        print("5 - Listar contatos");
        print("6 - Sair");
    
        option = input();

        if(option == "1"):
            createContact();
        elif(option == "2"):
            updateContact();
        elif(option == "3"):
            findContactByName();
        elif(option == "4"):
            deleteContactByName();
        elif(option == "5"):
            listContacts();
        elif(option == "6"):
            break;
        else:
            print("Insira uma opção válida");

main();
