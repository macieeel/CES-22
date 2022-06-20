import turtle   # biblioteca para usar as tartarugas

def draw_poly(t, n, sz):
    """faz uma tartaruga t desenhar um polígono de n lados de tamanho sz"""
    for i in range(n):   # repete o código n vezes
        t.forward(sz)   # desenha retas de tamanho sz
        t.left(360/n)   # faz um ângulo do tamanho do ângulo interno do polígono

wn = turtle.Screen()   # cria uma janela para as tartarugas
wn.bgcolor("lightgreen")   # muda a cor da janela para verde claro
wn.title("Lista 01 -  Exercício 02")   # define o título da janela
alex = turtle.Turtle()   # cria uma tartaruga
alex.color("HotPink")   # muda a cor da tartaruga para rosa
alex.pensize(5)   # aumenta o comprimento do traçado da tartaruga para 5

draw_poly(alex, 8, 50)   # chama a função para desenhar um polígono

wn.mainloop()   # espera o usuário fechar a janela