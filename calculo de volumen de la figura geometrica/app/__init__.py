from abc import abstractmethod
class Figura(object):
    def __init__(self,radio,altura,pi,volumen):
        self.radio = radio
        self.altura=altura


    @abstractmethod
    def tipo_figura(self):
        pass

class Leer(object):
    def leer(self):
        print("hola te ayudare a calcular el volumen de una figura geometrica\n")
        opc=input("¿Que figura es? cilindro,  cono o esfera\n ")
        return opc









class Cono(Figura):


    def cal_vol(self):
        radio = int(input("escriba cual es el radio \n"))
        altura = int(input("escriba cual es la altura \n"))
        radio= radio*radio
        volumen = (3.14*radio*altura)/3

        return volumen




    def tipo_figura(self):
        return 'cono'


class cilindro(Figura):
    def cal_vol(self):
        radio=int(input("escriba cual es el radio \n"))
        altura=int(input("escriba cual es la altura \n"))


        radio= radio*radio
        volumen = (3.14*radio*altura)
        return volumen



    def tipo_figura(self):
        return 'cono'



class esfera(Figura):
    def cal_vol(self):
        radio=int(input("escriba cual es el radio \n"))


        radio= radio*radio*radio
        volumen = (3.14*radio)/3
        return volumen



    def tipo_figura(self):
        return 'cono'






if __name__ == '__main__':
    print(Leer , ' \n')
    opc = Leer.leer(str)
    if 'cono' in opc:
        a = Cono.cal_vol(int)
        print("El volumen del cono es: " + str(a))
    elif 'esfera' in opc:
        a=esfera.cal_vol(int)
        print("El volumen de la esfera es: " + str(a))
    elif 'cilindro' in opc:
        a=cilindro.cal_vol(int)
        print("El volumen del cilindro es: " + str(a))
