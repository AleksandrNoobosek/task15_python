import os
os.system('cls')
import fractions
import logging
import argparse

FORMAT = '{levelname:} - recording time: {asctime}, function: {funcName:>12} , {msg}'
logging.basicConfig(format=FORMAT, filename='logger_frac.log', 
                    encoding='UTF-8', level=logging.INFO, 
                    filemode='w', style='{'
                )
logger = logging.getLogger(__name__)


class Fractions:
    def __init__(self, numerator: int, denominator: int) -> None:
        self.numerator = numerator
        self.denominator = denominator
#__init__  метод-конструктор, который инициализирует 
#числитель (numerator) и знаменатель (denominator) дроби
    def frac_create(self):
        logger.info(f"created fraction {self.numerator}/{self.denominator}")        
        return fractions.Fraction(self.numerator, self.denominator)
#frac_create метод создает дробь   
    def frac_mult(self, other: 'Fractions'):
       
        a = (f"{self.numerator}/{self.denominator}")
        b = (f"{other.numerator}/{other.denominator}")
        с = (f"{self.numerator * other.numerator}/{self.denominator * other.denominator}")
        logger.info(f"multiplication result {a} and {b}: {с}")
        return f'{self.numerator * other.numerator}/{self.denominator * other.denominator}'
#frac_mult  метод умножает текущую дробь на другую дробь   
    def __add__(self, other: 'Fractions'):

        a = (f"{self.numerator}/{self.denominator}")
        b = (f"{other.numerator}/{other.denominator}")
        res_add = (fractions.Fraction(self.numerator, self.denominator) 
                + fractions.Fraction(other.numerator, other.denominator))
        logger.info(f"addition result {a} и {b}: {res_add}")
        return (res_add)
#__add__метод складывает текущую дробь с другой дробью (другой)    
    def __str__(self) -> str:
        return f'{self.numerator}/{self.denominator}'
#__str__ метод возвращает строковое представление дроби.   
def parser():
    pars = argparse.ArgumentParser(prog='Fractions()')
    pars.add_argument('-ch', default=1)
    pars.add_argument('-zn', default=1)        
    args = pars.parse_args()
    return Fractions(int(args.ch), int(args.zn)) 
#parser -предназначена для разбора аргументов командной строки.
# Ожидает два аргумента: -ch для числителя и -zn для знаменателя.
# Возвращает объект Fractions с разобранными аргументами.

if __name__ == "__main__":    
    frac1 = Fractions(1, 2)
    frac2 = Fractions(1, 3)   
    frac3 = Fractions(1, 4)

    frac1 + frac2
    frac1 + frac3
    frac1.frac_mult(frac2)
    frac1.frac_mult(frac3)
