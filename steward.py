from crew import Crew

class Steward(Crew):
    def __init__(self, name, birthday, cpf, role, cms):
        super().__init__(name, birthday, cpf, role)
        self._cms = cms

    @property
    def cms(self):
        return self._cms

    @cms.setter
    def cms(self, value):
        self._cms = value 
        
    def to_dict(self):
        return {'Name': self.name, 
                'Birthday': self.birthday,
                'CPF':self.cpf,
                'CMS':self.cms,
                'Role':self.role}
        
    def __str__(self):
        return (f'Name:{self.name}, Birthday:{self.birthday}, CPF:{self.cpf}'
                f'cms:{self.cms}, Role:{self.role}')