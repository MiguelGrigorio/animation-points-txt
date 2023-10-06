import matplotlib.pyplot as plt
import matplotlib.animation as animation

txtPontos = 'pontos.txt'
with open(txtPontos) as file:
    points = file.read()
points = points.split('\n')
del points[-1]
Px = []
Py = []
for i in range(len(points)):
    if i % 2 == 0:
        Px.append(float(points[i]))
    else:
        Py.append(float(points[i]))
fig, ax = plt.subplots()

linha = ax.plot(Px[0], Py[0])[0]
ax.set(xlim=[-1, 1.1], ylim=[-1, 1])


def update(frame):
    linha.set_xdata(Px[:frame])
    linha.set_ydata(Py[:frame])
    return linha


ani = animation.FuncAnimation(fig=fig, func=update, frames=len(Px), interval=5)
plt.show()
