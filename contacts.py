
class Contact:
    def  __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.fullInfo = [firstName,lastName]

    def print_Contact(self):
        pass
        print(self.fullInfo)

class emailContact(Contact):
    def __init__(self, firstName, lastName, email):
        super().__init__(firstName,lastName)
        self.email = email
        self.fullInfo = [firstName,lastName,email]
