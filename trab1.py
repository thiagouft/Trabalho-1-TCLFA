def transicao_estendida(estado, valor):
    #print(valor)
    if valor == '&':
        return 'q0'
    i = len(valor)
    e = transicao_estendida(estado,valor[:len(valor)-1])
    #print(e)
    return trasicao_afd(e,valor[i-1])

def trasicao_afd(estado, palavra):
    if estado == 'q0':
        if (palavra == 'a'):
            print("q0 entrou \"" + palavra + "\"")
            return 'q2'
        else:
            return 'q1'

    if estado == 'q1':
        if (palavra == 'a'):
            return 'q4'
        else:
            return 'q3'

    if estado == 'q2':
        if (palavra == 'a'):
            return 'q6'
        else:
            return 'q5'

    if estado == 'q3':
        if (palavra == 'a'):
            return 'q8'
        else:
            return 'q7'

    if estado == 'q4':
        if (palavra == 'a'):
            return 'q8'
        else:
            return 'q9'

    if estado == 'q5':
        if (palavra == 'a'):
            return 'q8'
        else:
            return 'q10'

    if estado == 'q6':
        if (palavra == 'a'):
            return 'q8'
        else:
            return 'q11'

    if estado == 'q7':
        if (palavra == 'a'):
            return 'q12'
        else:
            return 'q7'

    if estado == 'q8':
        if (palavra == 'a'):
            return 'q8'
        else:
            return 'q8'

    if estado == 'q9':
        if (palavra == 'a'):
            return 'q13'
        else:
            return 'q10'

    if estado == 'q10':
        if (palavra == 'a'):
            return 'q12'
        else:
            return 'q7'

    if estado == 'q11':
        if (palavra == 'a'):
            return 'q13'
        else:
            return 'q10'

    if estado == 'q12':
        if (palavra == 'a'):
            return 'q14'
        else:
            return 'q9'

    if estado == 'q13':
        if (palavra == 'a'):
            return 'q14'
        else:
            return 'q9'

    if estado == 'q14':
        if (palavra == 'a'):
            return 'q15'
        else:
            return 'q11'

    if estado == 'q15':
        if (palavra == 'a'):
            return 'q15'
        else:
            return 'q11'

'''palavra = input("Digite uma palavra do alfabeto (a,b) minusculo")
estado = ['q0']
i = 0
tam_palavra = len(palavra)

while tam_palavra >  0:
    if estado[i] == 'q0':
        if(palavra[i] == 'a'):
            estado.append('q2')
            tam_palavra -= 1
        else:
            estado.append('q1')
            tam_palavra -= 1

    if estado[i] == 'q1':
        if(palavra[i] == 'a'):
            estado.append('q4')
            tam_palavra -= 1
        else:
            estado.append('q3')
            tam_palavra -= 1

    if estado[i] == 'q2':
        if(palavra[i] == 'a'):
            estado.append('q6')
            tam_palavra -= 1
        else:
            estado.append('q5')
            tam_palavra -= 1

    if estado[i] == 'q3':
        if(palavra[i] == 'a'):
            estado.append('q8')
            tam_palavra -= 1
        else:
            estado.append('q7')
            tam_palavra -= 1

    if estado[i] == 'q4':
        if(palavra[i] == 'a'):
            estado.append('q8')
            tam_palavra -= 1
        else:
            estado.append('q9')
            tam_palavra -= 1

    if estado[i] == 'q5':
        if(palavra[i] == 'a'):
            estado.append('q8')
            tam_palavra -= 1
        else:
            estado.append('q10')
            tam_palavra -= 1

    if estado[i] == 'q6':
        if(palavra[i] == 'a'):
            estado.append('q8')
            tam_palavra -= 1
        else:
            estado.append('q11')
            tam_palavra -= 1

    if estado[i] == 'q7':
        if(palavra[i] == 'a'):
            estado.append('q12')
            tam_palavra -= 1
        else:
            estado.append('q7')
            tam_palavra -= 1

    if estado[i] == 'q8':
        if(palavra[i] == 'a'):
            estado.append('q8')
            tam_palavra -= 1
        else:
            estado.append('q8')
            tam_palavra -= 1

    if estado[i] == 'q9':
        if(palavra[i] == 'a'):
            estado.append('q13')
            tam_palavra -= 1
        else:
            estado.append('q10')
            tam_palavra -= 1

    if estado[i] == 'q10':
        if(palavra[i] == 'a'):
            estado.append('q12')
            tam_palavra -= 1
        else:
            estado.append('q7')
            tam_palavra -= 1

    if estado[i] == 'q11':
        if(palavra[i] == 'a'):
            estado.append('q13')
            tam_palavra -= 1
        else:
            estado.append('q10')
            tam_palavra -= 1

    if estado[i] == 'q12':
        if(palavra[i] == 'a'):
            estado.append('q14')
            tam_palavra -= 1
        else:
            estado.append('q9')
            tam_palavra -= 1

    if estado[i] == 'q13':
        if(palavra[i] == 'a'):
            estado.append('q14')
            tam_palavra -= 1
        else:
            estado.append('q9')
            tam_palavra -= 1

    if estado[i] == 'q14':
        if(palavra[i] == 'a'):
            estado.append('q15')
            tam_palavra -= 1
        else:
            estado.append('q11')
            tam_palavra -= 1

    if estado[i] == 'q15':
        if(palavra[i] == 'a'):
            estado.append('q15')
            tam_palavra -= 1
        else:
            estado.append('q11')
            tam_palavra -= 1

    print("Entrou \"" + palavra[i] + "\" estado " +estado[i+1])
    i += 1
if estado[-1] == 'q7' or estado[-1] == 'q9' or estado[-1] == 'q12' or estado[-1] == 'q14':
    print("Palavra \"" + palavra + "\" do alfabeto \"a,b\" Reconhecida com sucesso")
else:
    print("Palavra \"" + palavra + "\" do alfabeto \"a,b\" Não reconhecida")'''

palavra = input("Digite uma palavra do alfabeto (a,b) em minusculo")

palavra_com_vazio = "&"+palavra
aux = transicao_estendida('q0',palavra_com_vazio)
if aux == 'q7' or aux == 'q9' or aux == 'q12' or aux == 'q14':
    print("Palavra \""+ palavra+"\" " + "Reconhecida com Sucesso.")
else:
    print("Palavra \"" + palavra + "\" " + "Não Reconhecida.")