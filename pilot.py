from crew import Crew

class Pilot(Crew):
    def __init__(self, name, birthday, cpf, role, cht, traning=False):
        super().__init__(name, birthday, cpf, role)
        self._cht = cht
        self._training = traning

    @property
    def training(self):
        return self._training

    @training.setter
    def training(self, value):
        self._training = value

    @property
    def cht(self):
        return self._cht

    @cht.setter
    def cht(self, value):
        self._cht = value

    def to_dict(self):
        """
            Função que transforma o objeto em dicionario
        Returns:
            dict: dicionario com as informações
        """
        return {'Name': self.name, 
                'Birthday': self.birthday,
                'CPF':self.cpf,
                'CHT':self.cht,
                'Role':self.role.value,
                'In training': self.training}
        
    def __str__(self):
        return (f'Name:{self.name}, Birthday:{self.birthday}, CPF:{self.cpf}'
                f'CHT:{self.cht}, Role:{self.role}, In training:{self.training}')