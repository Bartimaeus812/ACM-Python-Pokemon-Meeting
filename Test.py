import poke_mod
import pandas as pd
import plotly.express as px

pokemon = poke_mod.loadPokemon(100)

egg_groups = {}

arrX = []
arrY = []
stringarr = []

id = 0

for i in pokemon:
    for j in i['egg_groups']:
        name = j['name']
        try:
            egg_groups[name]
        except KeyError as error:
            egg_groups[name] = id
            arrX.append(id)
            stringarr.append(name)
            id += 1
            arrY.append(0)
        arrY[egg_groups[name]] += 1

df = pd.DataFrame(dict(
    x = arrX,
    y = arrY
))

fig = px.line(df,'x','y')
fig.show()

for i in range(len(arrX)):
    print(arrX[i],'=',stringarr[i],'\n')