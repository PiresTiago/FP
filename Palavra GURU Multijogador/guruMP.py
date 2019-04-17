#--------------------------
#-- TIAGO PIRES / N89544 --
#-------------------------- 

from guru import e_palavra
import itertools

#    ///////////\\\\\\\\\\\
#   //        TAD         \\
#  //   Palavra Potencial  \\
# //////////////\\\\\\\\\\\\\\                       

def cria_palavra_potencial(palavra,conj):
    '''
    cad. caracteres x tuplo de letras -> palavra_potencial
    '''    
    if isinstance(palavra,str) and isinstance(conj, tuple):
        for elem in conj:
            if not isinstance(elem,str) or not 'A'<=elem<='Z':
                raise ValueError('cria_palavra_potencial:argumentos invalidos.')       
        lista_conjunto=list(conj)
        for elem in palavra:
            if not 'A'<=elem<='Z': #Se todos os caracteres da palavra nao forem\
                                  #letras maiusculas, o programa origina um erro
                raise ValueError('cria_palavra_potencial:argumentos invalidos.')
            elif elem not in lista_conjunto:
                raise ValueError('cria_palavra_potencial:a palavra nao e valida.')       
            else:
                lista_conjunto.remove(elem)
        return palavra                    
    else:
        raise ValueError('cria_palavra_potencial:argumentos invalidos.')
        

def palavra_tamanho(dados):
    '''
    palavra_potencial -> inteiro
    '''
    return len(dados)

def e_palavra_potencial(dados):
    '''
    universal -> logico
    '''
    if not isinstance(dados,str):
        return False
    for elem in dados:
        if not 'A'<=elem<='Z':
            return False
    return True
    
    
def palavras_potenciais_iguais(dados1,dados2):
    '''palavra_potencial x palavra_potencial -> logico'''
    return dados1 == dados2

def palavra_potencial_menor(dados1,dados2):
    '''palavra_potencial x palavra_potencial -> logico'''
    return dados1<dados2
    
def palavra_potencial_para_cadeia(dados):
    '''palavra_potencial -> cad. caracteres'''
    return str(dados)


#    ///////////\\\\\\\\\\\
#   //        TAD         \\
#  //   Conjunto Palavras  \\
# //////////////\\\\\\\\\\\\\\  

def cria_conjunto_palavras():
    '''-> conjunto_palavras'''
    return []

def numero_palavras(c):
    '''conjunto_palavras -> inteiro'''
    return len(c)

def subconjunto_por_tamanho(c,n):
    '''conjunto_palavras x inteiro -> lista'''
    lista_tamanho=[]             #criacao de uma lista que vai conter palavras \
                                 #potenciais com o mesmo tamanho
    for elem in c:
        if len(elem) == n:  
            lista_tamanho.append(elem)        
    return lista_tamanho
    
def acrescenta_palavra(c,p):
    '''conjunto_palavras x palavra_potencial ->'''
    if e_palavra_potencial(p) and e_conjunto_palavras(c):
        for elem in p:
            if not 'A'<=elem<='Z':
                raise ValueError('acrescenta_palavra:argumentos invalidos.')
        if p not in c:
            c.append(p)
    else:
        raise ValueError('acrescenta_palavra:argumentos invalidos.')
    
def e_conjunto_palavras(c):
    '''universal -> logico'''
    if isinstance(c,list):
        for elem in c:
            if not e_palavra_potencial(elem):
                return False     
        return True
    return False
        
    
def conjuntos_palavras_iguais(c1,c2):
    '''conjunto_palavras x conjunto_palavras -> logico'''
    return c1 == c2
    
def conjunto_palavras_para_cadeia(c):
    '''conjunto_palavras -> cad. caracteres'''
    if c == []:               #\
        return '[]'           # >Casos que sao excepcao
    elif c == ['']:           #/
        return '[0->[]]'
    cadeia='['
    c=ordenar(c)    
    for n in range(1, len(c[-1])+1):
        variavel_len=conjunto_palavras_para_cadeia_aux(c,n) 
        if variavel_len != '[]':
            if n == len(c[-1]):      #se for o ultimo ja nao leva o caracter ';'
                cadeia += str(n) + '->' + str(variavel_len)
            else:
                cadeia += str(n) + '->' + str(variavel_len) + ';'
    return cadeia +']'
    
def conjunto_palavras_para_cadeia_aux(c,n):
    '''conjunto_palavras x inteiro -> cad. caracteres
    Funcao auxiliar'''
    string = ''
    for elem in c:
        if  len(elem) == n:
            if string == '':
                string+= elem
            else: 
                string += ',' + elem
    return '[' + string + ']'
    
def ordenar(c):
    '''conjunto -> conjunto
    Funcao que ordena um conjunto de palavras por ordem crescente 
    do seu tamanho, e para cada tamanho sao ordenadas alfabeticamente'''
    sorted(c)
    c.sort(key=len)
    return c

#    ///////////\\\\\\\\\\\
#   //        TAD         \\
#  //        Jogador       \\
# //////////////\\\\\\\\\\\\\\  

def cria_jogador(nome):
    '''cad. caracteres -> jogador'''
    if isinstance(nome,str):
        return {'JOGADOR':nome, 'PONTOS':0, 'VALIDAS':cria_conjunto_palavras(),\
                'INVALIDAS':cria_conjunto_palavras()}
    raise ValueError('cria_jogador:argumento invalido.')
       
def jogador_nome(jogador):
    '''jogador -> cad. caracteres'''
    return jogador['JOGADOR']

def jogador_pontuacao(jogador):
    '''jogador -> inteiro'''
    return jogador['PONTOS']

def jogador_palavras_validas(jogador):
    '''jogador -> conjunto_palavras'''
    return jogador['VALIDAS']

def jogador_palavras_invalidas(jogador):
    '''jogador -> conjunto_palavras'''
    return jogador['INVALIDAS']
    
def adiciona_palavra_valida(jogador,palavra):
    '''jogador x palavra_potencial ->'''
    adiciona_palavra(jogador,palavra,'valida')
    
def adiciona_palavra_invalida(jogador,palavra):
    '''jogador x palavra_potencial ->'''
    adiciona_palavra(jogador,palavra,'invalida')

def adiciona_palavra(jogador,palavra,validade):
    '''jogador x palavra_potencial ->'''
    if e_jogador(jogador) and e_palavra_potencial(palavra):
        if validade == 'valida':
            if palavra not in jogador_palavras_validas(jogador):
                acrescenta_palavra(jogador_palavras_validas(jogador),palavra)
                jogador['PONTOS'] += palavra_tamanho(palavra)
        else:
            if palavra not in jogador_palavras_invalidas(jogador):
                acrescenta_palavra(jogador_palavras_invalidas(jogador),palavra)
                jogador['PONTOS'] -= palavra_tamanho(palavra)
    else:
        if validade == 'valida':
            raise ValueError('adiciona_palavra_valida:argumentos invalidos.') 
        else:           
            raise ValueError('adiciona_palavra_invalida:argumentos invalidos.')    

def e_jogador(jogador):
    '''universal -> logico'''
    return isinstance(jogador,dict) and 'JOGADOR' in jogador and 'PONTOS' \
           in jogador and 'VALIDAS' in jogador and 'INVALIDAS' in jogador and \
           isinstance(jogador['JOGADOR'],str) and isinstance(jogador['PONTOS'],int)\
           and e_conjunto_palavras(jogador['VALIDAS']) and \
           e_conjunto_palavras(jogador['INVALIDAS'])

def jogador_para_cadeia(jogador):
    '''jogador -> cad. caracteres'''
    cadeia = 'JOGADOR '+jogador['JOGADOR']+' PONTOS='+str(jogador['PONTOS'])+\
        ' VALIDAS='+conjunto_palavras_para_cadeia(jogador['VALIDAS'])+\
        ' INVALIDAS='+conjunto_palavras_para_cadeia(jogador['INVALIDAS'])
    return cadeia


#=========================================
#= Gerador de todas as palavras validas =
#=========================================

def gera_todas_palavras_validas(c):
    '''tuplo de letras -> conjunto_palavras'''
    gerador=[]       #lista que vai conter todas as palavras geradas \
                     #pelas letras do conjunto c
    conjunto=cria_conjunto_palavras()   #conjunto que vai conter todas as \ 
                                        #palavras validas,geradas pelas \ 
                                        #letras do conjunto c
    for n in range(1,len(c)+1):
        for word in itertools.permutations(c,n):
            gerador.append(''.join(word))
    for elem in gerador:
        if e_palavra(elem):
            acrescenta_palavra(conjunto,cria_palavra_potencial(elem, c))
    return conjunto

#===============================
#= Palavra Guru - MultiJogador =
#===============================
         
def guru_mj(c):
    '''tuplo de letras'''
    lista_tentativas=[]  #lista que ira' conter todas as palavras descobertas \ 
                         #que pertencem 'a lista com todas as palavras validas
    lista_jogadores=[]   #lista que contem todos os jogadores que jogam o jogo    
    empate=0             #variavel que decide se ha' empate no final do jogo        
    jogador=0            #variavel que permite introduzir os jogadores no \
                         #inicio do jogo           
    contador=0           #variavel que serve de numero para cada jogador
    contador_jogada=1    #variavel que serve para contar o numero de jogadas \ 
                         #efetuadas                                                        
    contador_palavras_restantes=numero_palavras(gera_todas_palavras_validas(c)) 
                         #'contador_palavras_restantes'-variavel que serve para\
                         # contar o numero de palavras por descobrir
    nome_jogador=0
    print ('Descubra todas as palavras geradas a partir das letras:')
    print (c)
    print ('Introduza o nome dos jogadores (-1 para terminar)...')
    while jogador != str(-1):
        contador += 1
        jogador = input('JOGADOR '+str(contador)+' -> ')
        if jogador != str(-1):
            lista_jogadores.append(cria_jogador(jogador))
    while contador_palavras_restantes != 0:
        if nome_jogador == len(lista_jogadores):
            nome_jogador=0
        print('JOGADA ' +str(contador_jogada)+' - Falta descobrir '+\
              str(contador_palavras_restantes)+' palavras')
        tentativa=cria_palavra_potencial(input('JOGADOR '+str(lista_jogadores[nome_jogador]['JOGADOR'])+' -> '),c)
        if tentativa in gera_todas_palavras_validas(c):
            if tentativa not in lista_tentativas:
                lista_tentativas.append(tentativa)
                contador_palavras_restantes -=1
                adiciona_palavra_valida(lista_jogadores[nome_jogador],tentativa)
            print(tentativa+' - palavra VALIDA')        
        else:
            adiciona_palavra_invalida(lista_jogadores[nome_jogador],tentativa)
            print(tentativa+' - palavra INVALIDA')
        contador_jogada += 1
        nome_jogador += 1
    pontuacao_maxima=jogador_pontuacao(lista_jogadores[0])
    for jogador in lista_jogadores:
        if jogador_pontuacao(jogador)>pontuacao_maxima:
            pontuacao_maxima=jogador_pontuacao(jogador)
    for jogador in lista_jogadores:
        if  jogador_pontuacao(jogador)==pontuacao_maxima:
            empate += 1
            jogador_vencedor=jogador
    if empate > 1:
        print('FIM DE JOGO! O jogo terminou em empate.')
    else:
        print('FIM DE JOGO! O jogo terminou com a vitoria do jogador '+\
              jogador_nome(jogador_vencedor)+' com '+\
              str(jogador_pontuacao(jogador_vencedor))+' pontos.')
    for jogador in lista_jogadores:
        print(jogador_para_cadeia(jogador))