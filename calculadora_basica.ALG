Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 22/02/2025
Var
   // Seção de Declarações das variáveis
   x,y,resultado : inteiro
   operacao : caractere

Inicio
   // Seção de Comandos, procedimento, funções, operadores, etc...
   escreval("informe o número 1:")
   leia(x)
   escreval("informe o número 2:")
   leia(y)

   escreval("Informe a operação: (+, -, *, /)")
   leia(operacao)

   se operacao = "+" entao
      resultado <- x+y
      escreva(resultado)
   senao
      se operacao = "-" entao
         resultado <- x-y
         escreva(resultado)
      senao
         se operacao = "*" entao
            resultado <- x*y
            escreva(resultado)
         senao
            se operacao = "/" entao
               resultado <- x/y
               escreva(resultado)
            senao
               escreva("operacao invalida")
            fimse
         fimse
      fimse
   fimse


Fimalgoritmo
