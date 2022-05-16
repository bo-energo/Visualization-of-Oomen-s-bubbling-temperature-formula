import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

mpl.use('Qt5Agg')  # Для вывода графика в окне в PyCharm

#
# ---------------------------------------------------------


def main():

    fig = plt.figure(figsize=(12, 8))
    ax_3d = Axes3D(fig)

    count = 100

    w = np.linspace(0.1, 5, count)      # x
    p = np.linspace(500, 1500, count)   # y
    g = 30

    xgrid, ygrid = np.meshgrid(w, p)

    t_bubbling = 6996.7 / (22.454 + 1.4495 * np.log(xgrid) - np.log(ygrid)) - \
                 np.exp(0.473/xgrid)*np.power(g/30, 1.585) - 273.15

    ax_3d.plot_wireframe(xgrid, ygrid, t_bubbling)

    ax_3d.set_xlabel('w')
    ax_3d.set_ylabel('p')
    ax_3d.set_zlabel('t')

    plt.show()


if __name__ == '__main__':
    main()
