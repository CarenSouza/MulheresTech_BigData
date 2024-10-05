print("String") #comando para exibir meu conteúdo no terminal.

'''
Dentro dos tipos de arquivo em Python,
temos os tipo texto que são conhecidos
como STRINGS; no exemplo acima, eu utilizei
o comando PRINT para exibir uma String no meu
terminal Python
'''

print('morango', '    banana') #string
print(123) #1 int
print(37438,23534) #2 int
print('2963.44') #float
print(True) # Boolean
print(False)
print(None) #none
print(['string']) #listas
print(['string']) #dupla
print({'string':'texto'}) #dicicionário



idade=17
if idade<16:
    print("Você é menor de idade.")
elif idade >16 and idade<18:
    print("Você é menor de idade")
else:
    print('Você é maior de idade')

    
    
    
fruta1='jambo'
fruta2='maçã'
fruta3='uva'
fruta4='maçã'
num1=67
num2=12
num3=12.0
num4=67.1

print(fruta1==fruta3)
fruta1=fruta3
print(fruta1)

print(fruta1==fruta4)
print(fruta2==fruta4)
print(fruta3==fruta4)
print(num1==num2)
print(num1!=num2)
print(num1>num2)
print(num1<num2)
print(num2==num3)
print(num1!=num4)