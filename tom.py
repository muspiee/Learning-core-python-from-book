import turtle as t
nonte = t.Turtle()
fonte = t.Turtle()
nonte.shape("circle")
nonte.shape("square")
nonte.left(30)
nonte.forward(100)
fonte.backward(50)
monte = t.Turtle()
monte.setpos(-100, -100)
monte.forward(30)
monte.clear()
nonte.clear()
fonte.clear()
fonte.shape("triangle")
monte.shape("square")
t.done()