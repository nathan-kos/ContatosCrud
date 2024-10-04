from Contact import Contact

class Management:
    def __init__(self):
        self.contacts = [];

    def createContact(self, name, phone, email):
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

    def updateContactByIndex(self, index, name, phone, email):
        
        if(name != ""):
            self.contacts[index].setName(name);
        
        if(phone != ""):
            self.contacts[index].setPhone(phone);
        
        if(email != ""):
            self.contacts[index].setEmail(email);
