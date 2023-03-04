import turtle

# Cria a janela de desenho
janela = turtle.Screen()

# Cria uma caneta
caneta = turtle.Turtle()

# Define a cor da caneta para vermelho
caneta.color("red")

# Desenha o corpo
caneta.forward(100)
caneta.left(90)
caneta.forward(50)
caneta.left(90)
caneta.forward(100)
caneta.left(90)
caneta.forward(50)

# Vira a caneta para desenhar a cabeça
caneta.right(90)
caneta.forward(50)
caneta.right(90)
caneta.forward(30)
caneta.right(90)
caneta.forward(40)
caneta.right(90)
caneta.forward(30)

# Desenha a teia
caneta.penup()
caneta.goto(20, 70)
caneta.pendown()
caneta.goto(20, 90)
caneta.goto(40, 90)
caneta.goto(40, 70)

# Move a caneta para longe do desenho
caneta.penup()
caneta.goto(200, 200)

# Mantém a janela de desenho aberta
janela.mainloop()
