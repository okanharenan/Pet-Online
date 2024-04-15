from django.core.management.base import BaseCommand
import random
from reservas.models import PetShop

class Command(BaseCommand):
    def list_petshop(self):
        return PetShop.objects.all().values_list('pk', flat = True)
    
    def add_arguments(self,parser):
        parser.add_argument(
            'quantity',
            nargs = '?',
            default = 5,
            type = int,
            help = 'how many persons should be participate in the contest',
        )

        parser.add_argument(
            '-petshop',
            required = True,
            type = int,
            choices = self.list_petshop(),
            help = 'Petshop ID to execute the contest',

        )

    
    def escolher_reservas(self, banhos, quantidade):
        banho_list = list(banhos)
        if quantidade > len(banho_list):
            quantidade = len(banho_list)
        
        return random.sample(banho_list, quantidade)

    def imprimir_informacoes_do_petshop(self, petshop):
        self.stdout.write(self.style.HTTP_INFO('Dados do petshop que realizou o sorteio: '))
        self.stdout.write(f'nome do petshop: {petshop.nome}')
        self.stdout.write(f'Endereço: {petshop.rua}, {petshop.numero}, {petshop.bairro}')

    def imprimir_reserva_sorteada(self,reserva):
        self.stdout.write( self.style.HTTP_INFO('=' *35))
        self.stdout.write(self.style.HTTP_INFO('Dados das pessoas e animais sorteados'))
        for reservas in reserva:
            self.stdout.write(f'Animal: {reservas.nome_pet}')
            self.stdout.write(f'Tutor: {reservas.nome}')
            self.stdout.write(self.style.HTTP_INFO(
                '=' *35
            )) 

    def handle(self, *args, **options):
        quantity  = options['quantity']
        petshop_id = options['petshop']
        petshop = PetShop.objects.get(pk = petshop_id)
        reservas = petshop.reservas.all()

        banhos_escolhidos = self.escolher_reservas(reservas,quantity)
        '''for reserva in banhos_escolhidos:
        self.stdout.write(str(reservas))'''
        self.stdout.write(self.style.SUCCESS('Sorteio concluido!'))
        self.imprimir_informacoes_do_petshop(petshop)
        self.imprimir_reserva_sorteada(banhos_escolhidos)