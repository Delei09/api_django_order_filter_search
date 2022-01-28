from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate(self , data) :
        print(data)
        if not cpf_valido(data['cpf']) :
            raise serializers.ValidationError({"cpf" : "O CPF deve conter 11 digitos"}) 
        if not rg_valido(data['rg']) :
            raise serializers.ValidationError({"rg" : "O rg deve contem 9 digitos"}) 
        if not nome_valido(data['nome']) :
            raise serializers.ValidationError({"nome" : "O nome nao pode conter numeros"}) 
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':" Exemplos válidos: 35997111055/ 0335997221055 /  34715265 /  03562655656"})
            # 35997111055
            # 0335997221055
            # 34715265
            # 03562655656
        return data
        
    # def validate_cpf(self, cpf):
    #     if len(cpf)  != 11:
    #         raise serializers.ValidationError("O CPF deve conter 11 digitos") 
    #     return cpf
    # def validate_nome(self , nome):
    #     if not nome.isalpha():
    #         raise serializers.ValidationError("Não incluia numero no nome")
    # def validate_rg(self, rg):
    #     if not len(rg) != 9:
    #         raise serializers.ValidationError("O Rg deve ter 9 digitos")
    # def validate_celular(self, celular):
    #     if len(celular) < 11:
    #         raise serializers.ValidationError(" O telefone deve contem mais numeros")