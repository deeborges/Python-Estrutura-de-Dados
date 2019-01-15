# Material do Curso 
#    Dominando Listas em Python
#        ministrado por Deyvison Borges 
#    
#    Contatos
#        e-mail: web.dborges@gmail.com
#        github.com/deeborges
#        nationti.blogspot.com.br
#        insta: @dee.borges

pecas = ["placa mae", "hd", "ssd", "fonte"]
print(pecas)

pecas.insert(2, "teclado")
print(pecas)


tamanho = len(pecas)

print(pecas.insert(tamanho, "fone")