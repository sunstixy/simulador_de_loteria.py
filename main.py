from random import sample

print ( "Simulador De Loteria\n\n" )

palpites = [ ]
acertos = 0
sorteados = sample ( range ( 1, 61 ) , 11 )
sorteados.sort ( )

valor_da_aposta = float ( input ( "Digite O Valor Da Aposta : " ) )

while len ( palpites ) < 11 :
    palpite = int ( input ( "Digite Um Palpite : " ) )
    if palpite in palpites :
        print ( "Palpite Já Feito !!!" )
    elif palpite < 1 or palpite > 60 :
        print ( "Palpite Dever Estar Entre 1 E 60 !!!" )
    else :
        palpites.append ( palpite )

palpites.sort ( )

acertos = len ( set ( palpites ).intersection ( set ( sorteados ) ) )

premio = valor_da_aposta * acertos

print ( f"Números Sorteados : {sorteados}" )
print ( f"Seus Palpites : {palpites}" )
print ( f"Acertos : {acertos}" )
print ( f"Premio : R$ {premio:,.2f}" )
