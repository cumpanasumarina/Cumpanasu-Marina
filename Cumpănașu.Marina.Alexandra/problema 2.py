import matplotlib.pyplot as M
import pandas as C

df = C.read_csv("data.csv")
df.plot()
M.title("Toate valorile")
M.show()
df[:9].plot()
M.title("Primele 9 valori")
M.show()
df[-15:].plot()
M.title("Ultimele 15 valori")
M.show()