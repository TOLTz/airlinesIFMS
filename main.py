from flight import Flight
from plane import *
from passenger import Passenger
from pilot import Pilot
from steward import Steward
from crew import CrewType
import random
from utils import *
from datetime import timedelta, datetime


if __name__ == '__main__':
    list_models = list(Models)
    names = random.sample(list_models, 10)
    airplanes = []

    for name in names:
        scope = random.choice(list(Scope))
        airplane_obj = Plane(name.value, scope.value)

        airplane_dict = airplane_obj.to_dict()
        airplanes.append((airplane_obj, airplane_dict))

    for airplane_obj, airplane in airplanes:
        print('\n--- NOVO VOO ---')
        print(f'Modelo da aeronave: {airplane_obj.model}')

        # Criar tripulação
        pilot = Pilot(generate_name(), generate_birthday(), generate_cpf(),
                      CrewType.PILOT, generate_code())
        copilot = Pilot(generate_name(), generate_birthday(), generate_cpf(),
                        CrewType.COPILOT, generate_code())
        stewards = [
            Steward(generate_name(), generate_birthday(), generate_cpf(),
                    CrewType.STEWARD, generate_code(prefix='CMS'))
            for _ in range(5)
        ]
        crewmates = {
            'Pilot': pilot.to_dict(),
            'Copilot': copilot.to_dict(),
            'Stewards': [s.to_dict() for s in stewards]
        }

        # Criar voo

        origin, destination, price, flight_code = generate_flight_info(scope.value)
        flight = Flight(airplane, origin, destination, price)
        num_connections = random.randint(0, 2)
        if num_connections > 0:
            all_possible_stops = [
                'Fortaleza', 'Natal', 'Madrid', 'Miami', 'Londres', 'Lima',
                'Cidade do México', 'Amsterdam', 'Dakar', 'Roma', 'Frankfurt'
            ]
            used_stops = set([origin, destination])
            for _ in range(num_connections):
                stop = random.choice([s for s in all_possible_stops if s not in used_stops])
                conn = {
                    'stop': stop
                }
                flight.add_connection(conn)
                used_stops.add(stop)

        flight.add_crewmate(crewmate=crewmates)

        # ==== MENU DE ESCOLHA DO USUÁRIO ====
        while True:
            print('\nComo deseja cadastrar os passageiros?')
            print('[1] Manualmente')
            print('[2] Preencher automaticamente')
            option = input('Escolha: ').strip()
            if option == '1':
                assentos_disponiveis = list(range(1, airplane_obj.max_seat + 1))
                while True:
                    print('\n--- Assentos disponíveis ---')
                    print(assentos_disponiveis)
                    try:
                        seat = int(input('Digite o número do assento desejado (ou 0 para sair): '))
                        if seat == 0:
                            break
                        if seat not in assentos_disponiveis:
                            print('Assento inválido ou já ocupado.')
                            continue

                        name = input('Nome do passageiro: ')
                        birthday = input('Data de nascimento (dd/mm/aaaa): ')
                        cpf = input('CPF: ')
                        passport = input('Número do passaporte: ')
                        loyalty = input('Número do programa de fidelidade: ')
                        special = input('Possui necessidades especiais? (s/n): ').lower() == 's'

                        passenger = Passenger(name, birthday, cpf, passport, loyalty, special)
                        flight.add_passenger({seat: passenger.to_dict()})
                        assentos_disponiveis.remove(seat)
                        print(f'Passageiro {name} cadastrado no assento {seat} com sucesso.')

                    except Exception as e:
                        print(f'Erro ao cadastrar passageiro: {e}')

            elif option == '2':
                passengers = {}
                for seat in range(1, airplane_obj.max_seat + 1):
                    p = Passenger(
                        generate_name(), generate_birthday(), generate_cpf(),
                        generate_passport_number(), generate_loyalty_number(),
                        random_bool()
                    )
                    passengers[seat] = p.to_dict()
                flight.add_passenger(passengers)
                break
            else:
                print('Opção inválida. Tente novamente.')
                continue
            break  # Sai do menu após cadastro manual também

        # ==== INFORMAÇÕES DO VOO ====
        print('\n========================')
        print(f'VOO {origin[:3].upper()}-{destination[:3].upper()}-{flight_code}')
        print(f'Origem: {origin} → Destino: {destination}')
        print(f'Avião: {airplane_obj.model}')
        print(f'Alcance: {airplane_obj.alcance} | Preço da passagem: R$ {flight.price:.2f}\n')
        print(f'Preço da passagem: R$ {flight.price:.2f}\n')

        print('--- Tripulação ---')
        print(f'Piloto: {pilot.name}')
        print(f'Copiloto: {copilot.name}')
        print('Comissários:')
        for s in stewards:
            print(f' - {s.name}')

        print('\n--- 10 Passageiros Aleatórios ---')
        if flight.passengers:
            sample_seats = random.sample(list(flight.passengers.keys()), min(10, len(flight.passengers)))
            for seat in sample_seats:
                p = flight.passengers[seat]
                print(f'Assento {seat}: {p["name"]}')
        else:
            print('Nenhum passageiro registrado neste voo.')

        # ==== OPÇÃO FINAL ====
        while True:
            choice = input('\nDigite [1] para ver todos os passageiros ou [2] liberar o voo: ')
            if choice == '1':
                print('\n--- Lista completa de passageiros ---')
                for seat, p in sorted(flight.passengers.items()):
                    print(f'Assento {seat}: {p["name"]}')
                input("\nPressione Enter para continuar...")
                break
            elif choice == '2':
                flight.liberate_plane()
                alcance = airplane_obj.alcance
                if alcance == Scope.NACIONAL.value:
                    duration = timedelta(hours=2)
                elif alcance == Scope.INTERNACIONAL.value:
                    duration = timedelta(hours=6)
                elif alcance == Scope.GLOBAL.value:
                    duration = timedelta(hours=12)
                else:
                    duration = timedelta(hours=1)  # fallback
                
                flight.arrival_date = flight.departure_date + duration

                print(f"\n✈️ Partida registrada em: {flight.departure_date.strftime('%d/%m/%Y %H:%M')}")
                print(f"🛬 Chegada estimada em: {flight.arrival_date.strftime('%d/%m/%Y %H:%M')}")
                break
            else:
                print('Opção inválida. Tente novamente.')
