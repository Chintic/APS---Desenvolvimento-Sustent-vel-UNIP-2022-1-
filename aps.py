import random
#Random é uma biblioteca matemática

#chaves = ["6Zi27$", "f!69P9", "2Wj!13", "0!13Il"]
#chave = random.choice(chaves)

chave_user = int(input("Insira uma chave númerica para ser sua criptografia: "))

def criptografar(frase_criptografada):
#def é como criamos uma função em python e criptografar é o nome dela
    mensagem_digitada = ""
    #variável vazia, criada para recebe um valor, no caso, a mensagem criptografada
    #print("Sua chave é: ", chave_user)
    #print, comando para exibir algo na tela, combinação de um texto e uma variável

    for letra in frase_criptografada:
    #estrutura de for/in onde letra é a variável que irá percorrer
    #cada índice dentro da variável frase_criptografada
        mensagem_digitada = mensagem_digitada + chr(ord(letra) + chave_user)
        #chr
        #ord
        #mensagem_digitada é a variável vazia, aqui ela irá receber um valor após
        #após atribuição de uma cifra semelhante à de Cesar
    return mensagem_digitada
    #return, irá exibir na tela a variável mensagem_digitada


def descriptografar(mensagem_digitada):
#def, cria função, com o nome descriptografar a mensagem_digitada
#aqui iremos fazer a lógica inversa da primeira função, percorrendo
#o índice da mensage_digitada subtraindo as posições ao invés de somar
    frase_criptografada = ""
    #variável vazia, irá receber o valor depois de percorrer o índice da mensagem_digitada novamente
    #verificador_chave = input("Digite a chave: ")
    #if verificador_chave == chave:
    for letra in mensagem_digitada:
        frase_criptografada = frase_criptografada + chr(ord(letra) - chave_user)
    return frase_criptografada
    #else:
        #print("\nChave errada, fechando programa.")
    return mensagem_digitada


msg1 = criptografar(input("Mensagem: "))
print("\nMensagem: ", msg1)
#print("\nMensagem: ", descriptografar(msg1))