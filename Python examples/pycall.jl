using PyCall
math = pyimport("math")
math.sin(math.pi / 4) # returns ≈ 1/√2 = 0.70710678...



plt = pyimport("matplotlib.pyplot")
x = range(0;stop=2*pi,length=1000); y = sin.(3*x + 4*cos.(2*x));
plt.plot(x, y, color="red", linewidth=2.0, linestyle="--")
plt.show()

so = pyimport("scipy.optimize")
so.newton(x -> cos(x) - x, 1)


plot1 = pyimport("einsteinpy")
plot = pyimport("einsteinpy.plotting")
a = plot.StaticGeodesicPlotter()
a.animate


pyversion
PyCall.libpython
PyCall.conda
