import re
from validate_docbr import CPF

def cpf_valido(numero_do_cpf):
    # cpf = CPF()
    # return cpf.validate(numero_do_cpf)
    modelo ='(^\d{3}\.\d{3}\.\d{3}\-\d{2}$)|(^\d{2}\.\d{3}\.\d{3}\/\d{4}\-\d{2}$)'
    resposta = re.findall(modelo, numero_do_cpf)
    return resposta
    # 908.148.430-34
    # 48.191.722/0001-05
def nome_valido(nome ):
    modelo = r"(^[a-z ,.'-]+$)"
    resposta = re.findall(modelo, nome)
    return resposta
    # nÃO PODE NUMEROS 

def rg_valido(rg):
    return len(rg) == 9
# TEM QUE SER DE 9 DIGITOS

def celular_valido(numero_celular):
    modelo = '(^1\d\d(\d\d)?$|^0800 ?\d{3} ?\d{4}$|^(\(0?([1-9a-zA-Z][0-9a-zA-Z])?[1-9]\d\) ?|0?([1-9a-zA-Z][0-9a-zA-Z])?[1-9]\d[ .-]?)?(9|9[ .-])?[2-9]\d{3}[ .-]?\d{4}$)'
    resposta = re.findall(modelo, numero_celular)
    print(modelo, resposta)
    return resposta