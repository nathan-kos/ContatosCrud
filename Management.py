from Contact import Contact

class Management:
    def __init__(self):
        self.contacts = [];

    def createContact(self, name, phone, email):
        if(len(phone) != 11):
            raise ValueError("Telefone inválido");
        if("@" not in email):
            raise ValueError("Email inválido");
        
        self.contacts.append(Contact(name, phone, email));
    
    def findByName(self, name):
        for contact in self.contacts:
            if(contact.name == name):
                return contact;
        raise ValueError("Contact não encontrado");

    def deleteByName(self, name):
        for contact in self.contacts:
            if(contact.name == name):
                self.contacts.remove(contact);
    
    def listContacts(self):
        return self.contacts;