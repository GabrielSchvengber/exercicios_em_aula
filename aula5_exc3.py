from math import radians
from math import tan
from math import cos
from math import sin
from tarfile import CompressionError

angulo=float(input('Digite um angulo: '))

seno=sin(radians(angulo))
cosseno=cos(radians(angulo))
tangente=tan(radians(angulo))


print(' Seu angulo de {:.2f}. \n Seno = {:.2f}. \n Cosseno= {:.2f}. \n Tangente= {:.2f}.'.format(angulo,seno,cosseno,tangente))