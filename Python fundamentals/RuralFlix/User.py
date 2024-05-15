class User:
    def __init__(self, name='Null', email='Null', password='Null', adress='Null', card=0):
        self.name = name
        self.email = email
        self.password = password
        self.adress = adress
        self.card = card
        self.signature = False   
        self.plan = 'No plan'
        self.first_name = self.name.split(' ')
            
    def verifyBilling(self, billing = 35):
        
        if self.card < billing:
            print(f'Dear {self.first_name[0]}, your signature is not available')
        else:
            print(f'Welcome, {self.first_name[0]}!')
            self.card -= billing
            self.plan = 'Basic'
            self.signature = True        
        
        return self.signature

    def changePlan(self, billing = 20):
        if self.card < billing:
            print(f'Dear {self.first_name[0]}, it was impossible complete the payment')
        else:
            print(f'Dear {self.first_name[0]}, your plan has been updated')
            self.card -= billing
            self.plan = 'Advanced'   
        

