# Material do Curso 
#    Dominando Listas em Python
#        ministrado por Deyvison Borges 
#    
#    Contatos
#        e-mail: web.dborges@gmail.com
#        github.com/deeborges
#        nationti.blogspot.com.br
#        insta: @dee.borges

animais = ["rato", "morcego", "cachorro", "gato"]

del animais[2]
print(animais)


idade = [12, 34, 346, 7, 32, 56, 3, 6, 1, 45, 78, 12, 78, 3, 6, 89, 25, 90, 100]
posicao = idade.index(45)

del idade[posicao]
print(idade)