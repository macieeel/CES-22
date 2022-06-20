import turtle   # biblioteca para usar as tartarugas

def draw_square(t, sz):   # faz uma tartaruga t desenhar um quadrado de tamanho sz
    for i in range(4):
        t.forward(sz)   # tartaruga faz um risco de tamanho sz
        t.left(90)   # tartaruga vira para a esquerda em 90 graus

def reposition(t, sz):  
    """ faz a tartaruga se reposicionar para desenhar um novo quadrado sem desenhar na janela"""
    t.penup()   # faz os próximos movimentos da tartaruga não desenharem na tela
    t.backward(sz)
    t.right(90)
    t.forward(sz)
    t.left(90)
    t.pendown()   # faz os próximos movimentos da tartaruga voltarem a desenhar na tela

wn = turtle.Screen()      # cria uma janela para as tartarugas
wn.bgcolor("lightgreen")   # muda a cor da janela para verde claro
wn.title("Lista 01 -  Exercício 01")   # define o título da janela
alex = turtle.Turtle()   # cria uma tartaruga
alex.color("HotPink")   # muda a cor da tartaruga para rosa
alex.pensize(5)   # aumenta o comprimento do traçado da tartaruga para 5

for i in range(20, 100, 20):   # para i = 20, 40, 60 e 80
    draw_square(alex, i)   # chama a função para desenhar um quadrado de tamanho i
    reposition(alex, 10)   # chama a função para reposicionar a tartaruga

wn.mainloop()   # espera o usuário fechar a janela