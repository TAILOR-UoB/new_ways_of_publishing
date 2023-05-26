import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
import pandas as pd


def matplotlib_trisurf3d_2():
    """
    Example from the Matplotlib documentation.
      source: https://matplotlib.org/stable/gallery/mplot3d/trisurf3d_2.html#sphx-glr-gallery-mplot3d-trisurf3d-2-py
      Copyright 2002–2012 John Hunter, Darren Dale, Eric Firing, Michael
      Droettboom and the Matplotlib development team; 2012–2023 The Matplotlib
      development team.
    ===========================
    More triangular 3D surfaces
    ===========================

    Two additional examples of plotting surfaces with triangular mesh.

    The first demonstrates use of plot_trisurf's triangles argument, and the
    second sets a `.Triangulation` object's mask and passes the object directly
    to plot_trisurf.
    """
    fig = plt.figure(figsize=plt.figaspect(0.5))

    # ==========
    # First plot
    # ==========

    # Make a mesh in the space of parameterisation variables u and v
    u = np.linspace(0, 2.0 * np.pi, endpoint=True, num=50)
    v = np.linspace(-0.5, 0.5, endpoint=True, num=10)
    u, v = np.meshgrid(u, v)
    u, v = u.flatten(), v.flatten()

    # This is the Mobius mapping, taking a u, v pair and returning an x, y, z
    # triple
    x = (1 + 0.5 * v * np.cos(u / 2.0)) * np.cos(u)
    y = (1 + 0.5 * v * np.cos(u / 2.0)) * np.sin(u)
    z = 0.5 * v * np.sin(u / 2.0)

    # Triangulate parameter space to determine the triangles
    tri = mtri.Triangulation(u, v)

    # Plot the surface.  The triangles in parameter space determine which x, y, z
    # points are connected by an edge.
    ax = fig.add_subplot(1, 2, 1, projection='3d')
    ax.plot_trisurf(x, y, z, triangles=tri.triangles, cmap=plt.cm.Spectral)
    ax.set_zlim(-1, 1)


    # ===========
    # Second plot
    # ===========

    # Make parameter spaces radii and angles.
    n_angles = 36
    n_radii = 8
    min_radius = 0.25
    radii = np.linspace(min_radius, 0.95, n_radii)

    angles = np.linspace(0, 2*np.pi, n_angles, endpoint=False)
    angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
    angles[:, 1::2] += np.pi/n_angles

    # Map radius, angle pairs to x, y, z points.
    x = (radii*np.cos(angles)).flatten()
    y = (radii*np.sin(angles)).flatten()
    z = (np.cos(radii)*np.cos(3*angles)).flatten()

    # Create the Triangulation; no triangles so Delaunay triangulation created.
    triang = mtri.Triangulation(x, y)

    # Mask off unwanted triangles.
    xmid = x[triang.triangles].mean(axis=1)
    ymid = y[triang.triangles].mean(axis=1)
    mask = xmid**2 + ymid**2 < min_radius**2
    triang.set_mask(mask)

    # Plot the surface.
    ax = fig.add_subplot(1, 2, 2, projection='3d')
    ax.plot_trisurf(triang, z, cmap=plt.cm.CMRmap)


    plt.show()


def pandas_table_weather():
    """
    Example from Pandas documentation
    source: https://pandas.pydata.org/docs/user_guide/style.html
    """
    weather_df = pd.DataFrame(np.random.rand(10,2)*5,
                              index=pd.date_range(start="2021-01-01", periods=10),
                              columns=["Tokyo", "Beijing"])

    def rain_condition(v):
        if v < 1.75:
            return "Dry"
        elif v < 2.75:
            return "Rain"
        return "Heavy Rain"

    def make_pretty(styler):
        styler.set_caption("Weather Conditions")
        styler.format(rain_condition)
        styler.format_index(lambda v: v.strftime("%A"))
        styler.background_gradient(axis=None, vmin=1, vmax=5, cmap="YlGnBu")
        return styler

    return weather_df.loc["2021-01-04":"2021-01-08"].style.pipe(make_pretty)


def python_function_example():
    '''This function prints 'Hello world!'
    '''
    print('Hello world!')
