#--------------------------
#-- TIAGO PIRES / N89544 --
#-------------------------- 

#////////\\\\\\\\\
#// x = palavra \\
#////////\\\\\\\\\


def artigo_def(x):
    if x == 'A' or x == 'O':
        return True
    else:
        return False

def vogal_palavra(x):
    if len(x) == 1 and ( artigo_def(x) or x == 'E'):
        return True
    else:
        return False

def vogal(x):
    if x == 'I' or x == 'U' or vogal_palavra(x):
        return True
    else:
        return False

def ditongo_palavra(x):
    if x == 'AI' or x == 'AO' or x == 'EU' or x == 'OU':
        return True
    else:
        return False
    
def ditongo(x):
    if x == 'AE' or x == 'AU' or x == 'EI' or x == 'OE' or x == 'OI':
        return True
    elif x == 'IU' or ditongo_palavra(x):
        return True
    else:
        return False

def par_vogais(x):
    if ditongo(x) or x == 'IA' or x == 'IO':
        return True
    else:
        return False
    
def consoante_freq(x):
    if x == 'D' or x == 'L' or x == 'M' or x == 'N' or x == 'P' or x == 'R':
        return True
    elif x == 'S' or x == 'T' or x == 'V':
        return True
    else:
        return False
    
def consoante_terminal(x):
    if x == 'L' or x == 'M' or x == 'R' or x == 'S' or x == 'X' or x == 'Z':
        return True
    else:
        return False
    
def consoante_final(x):
    if x == 'N' or x == 'P' or consoante_terminal(x):
        return True
    else:
        return False
    
def consoante(x):
    if x == 'B' or x == 'C' or x == 'D' or x == 'F' or x == 'G' or x == 'H':
        return True
    elif x == 'J' or x == 'L' or x == 'M' or x == 'N' or x == 'P' or x == 'Q':
        return True
    elif x == 'R' or x == 'S' or x == 'T' or x == 'V' or x == 'X' or x == 'Z':
        return True
    else:
        return False
    
def par_consoantes(x):
    if x == 'BR' or x == 'CR' or x == 'FR' or x == 'GR' or x == 'PR' or x == 'PL': 
        return True
    elif x == 'TR' or x == 'VR' or x == 'BL' or x == 'CL' or x == 'FL' or x == 'GL':
        return True
    else:
        return False
    
def monossilabo_2(x):
    if len(x) == 2:
        if x == 'AR' or x == 'IR' or x == 'EM' or x == 'UM':
            return True
        elif vogal_palavra(x[0]) and x[1] == 'S':
            return True
        elif consoante_freq(x[0]) and vogal(x[1]):
            return True
        elif ditongo_palavra(x):
            return True
        else:
            return False
    else:
        return False

def monossilabo_3(x):
    if len(x) == 3:
        if consoante(x[0]) and vogal(x[1]) and consoante_terminal(x[2]):
            return True
        elif consoante(x[0]) and ditongo(x[1:3]):
            return True
        elif par_vogais(x[0:2]) and consoante_terminal(x[2]):
            return True
        else:
            return False
    else:
        return False
    
def e_monossilabo(x):
    '''A Funcao recebe uma cadeia de caracteres e retorna um booleano
    A funcao verifica se o argumento inserido e' uma cadeia de caracteres, 
    se nao for, gera um ValueError, se a cadeia de caracteres formar uma 
    palavra valida de acordo com a gramatica dada e contiver apenas uma silaba, 
    ou seja, se satisfizer a regra monossilabo, a funcao devolve True, 
    senao devolve False'''         
    if not isinstance (x, str):
        raise ValueError('e_monossilabo:argumento invalido')
    elif vogal_palavra(x) or monossilabo_2(x) or monossilabo_3(x):
        return True
    else:
        return False
    


def silaba_2(x):
    if len(x) == 2:
        if par_vogais(x) or consoante(x[0]) and vogal(x[1]):
            return True
        elif vogal(x[0]) and consoante_final(x[1]):
            return True
        else:
            return False                
    else:
        return False
    
def silaba_3(x):
    if len(x) == 3:
        if x == 'QUA' or x == 'QUE' or x == 'QUI' or x == 'GUE':
            return True
        elif x == 'GUI' or vogal(x[0]) and x[1:3] == 'NS':
            return True
        elif consoante(x[0]) and par_vogais(x[1:3]):
            return True
        elif consoante(x[0]) and vogal(x[1]) and consoante_final(x[2]):
            return True
        elif par_vogais(x[0:2]) and consoante_final(x[2]):
            return True
        elif par_consoantes(x[0:2]) and vogal(x[2]):
            return True
        else:
            return False                
    else:
        return False

def silaba_4(x):
    if len(x) == 4:
        if par_vogais(x[0:2]) and x[2:4] == 'NS':
            return True
        elif consoante(x[0]) and vogal(x[1]) and x[2:4] == 'NS':
            return True
        elif consoante(x[0]) and vogal(x[1]) and x[2:4] == 'IS':
            return True     
        elif par_consoantes(x[0:2]) and par_vogais(x[2:4]):
            return True
        elif consoante(x[0]) and par_vogais(x[1:3]) and consoante_final(x[3]):
            return True 
        else:
            return False 
    else:
        return False
    
def silaba_5(x):
    if len(x) == 5 and (par_consoantes(x[0:2]) and vogal(x[2]) and x[3:5] == 'NS'):
        return True
    else:
        return False

def silaba_final(x):
    if monossilabo_2(x) or monossilabo_3(x) or silaba_4(x) or silaba_5(x):
        return True
    else:
        return False

def e_silaba(x):
    '''A Funcao recebe uma cadeia de caracteres e retorna um booleano
    A funcao verifica se o argumento inserido e' uma cadeia de caracteres, 
    se nao for, gera um ValueError, se a cadeia de caracteres formar uma 
    silaba valida de acordo com a gramatica dada, ou seja, se satisfizer a 
    regra silaba, a funcao devolve True, senao devolve False'''        
    if not isinstance (x, str):
        raise ValueError('e_silaba:argumento invalido')    
    elif vogal(x) or silaba_2(x) or silaba_3(x) or silaba_4(x) or silaba_5(x):
        return True
    else:
        return False

def palavra(x):
    def palavra_auxilar(x):
        if x == '' or e_silaba(x):
            return True

        for i in range(1, len(x)):
            if e_silaba(x[:i]) and palavra_auxilar(x[i:]):
                return True

    if e_monossilabo(x) or silaba_final(x):
        return True

    for i in range(len(x)-5, len(x) - 1):
        if silaba_final(x[i:]) and palavra_auxilar(x[:i]):
            return True
    return False

def e_palavra(x):
    '''A Funcao recebe uma cadeia de caracteres e retorna um booleano
    A funcao verifica se o argumento inserido e' uma cadeia de caracteres, 
    se nao for, gera um ValueError, se a cadeia de caracteres formar uma 
    palavra valida de acordo com a gramatica dada, ou seja, se satisfizer 
    a regra palavra, a funcao devolve True, senao devolve False'''
    if not isinstance (x, str):
        raise ValueError('e_palavra:argumento invalido')
    return palavra(x)

       