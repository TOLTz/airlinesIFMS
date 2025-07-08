from flight import Flight
from plane import *
from passenger import Passenger
from pilot import Pilot
from steward import Steward
from crew import CrewType
import random
from utils import *

if __name__ == '__main__':
    list_models = list(Models)
    names = random.sample(list_models, 10)
    airplanes = []

    for name in names:
        airplane_obj = Plane(name.value, Scope.GLOBAL.value)
        airplane_dict = airplane_obj.to_dict()
        airplanes.append((airplane_obj, airplane_dict))  # Guarda objeto e dicionário

    for airplane_obj, airplane in airplanes:
        input('\nPressione Enter para iniciar o próximo voo...')

        # Criar piloto
        pilot = Pilot(
            generate_name(), generate_birthday(), generate_cpf(),
            CrewType.PILOT, generate_code()
        )

        # Criar copiloto
        copilot = Pilot(
            generate_name(), generate_birthday(), generate_cpf(),
            CrewType.COPILOT, generate_code()
        )

        # Criar comissários
        stewards = [
            Steward(
                generate_name(), generate_birthday(), generate_cpf(),
                CrewType.STEWARD, generate_code(prefix='CMS')
            )
            for _ in range(5)
        ]

        crewmates = {
            'Pilot': pilot.to_dict(),
            'Copilot': copilot.to_dict(),
            'Stewards': [s.to_dict() for s in stewards]
        }

        # Criar passageiros
        passengers = {}
        for seat in range(1, 251):
            p = Passenger(
                generate_name(), generate_birthday(), generate_cpf(),
                generate_passport_number(), generate_loyalty_number(),
                random_bool()
            )
            passengers[seat] = p.to_dict()

        # Criar voo
        flight = Flight(airplane, 'Guarulhos', 'Paris', 5000)
        flight.add_crewmate(crewmate=crewmates)
        flight.add_passenger(passengers)

        # ==== PRINTAR INFORMAÇÕES ====
        print(f'\n--- ✈️ VOO DE {flight.origin.upper()} PARA {flight.destination.upper()} ---')
        print(f'Nome do Avião: {airplane_obj.model}\n')

        print('--- Tripulação ---')
        print(f'Piloto: {pilot.name}')
        print(f'Copiloto: {copilot.name}')
        print('Comissários:')
        for s in stewards:
            print(f' - {s.name}')
        
        print('\n--- 10 Passageiros Aleatórios ---')
        sample_seats = random.sample(list(flight.passengers.keys()), 10)
        for seat in sample_seats:
            p = flight.passengers[seat]
            print(f'Assento {seat}: {p["name"]}')

        # ==== INTERAÇÃO COM O USUÁRIO ====
        while True:
            choice = input('\nDigite [1] para ver todos os passageiros ou [2] para o próximo voo: ')
            if choice == '1':
                print('\n--- Todos os passageiros ---')
                for seat, p in flight.passengers.items():
                    print(f'Assento {seat}: {p["name"]}')
                input("\nPressione Enter para seguir...")
                break
            elif choice == '2':
                break
            else:
                print('Opção inválida. Tente novamente.')
