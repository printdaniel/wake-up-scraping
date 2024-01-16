from indices.indice import Indices_economicos
from cine.cine import Cine
app = Indices_economicos()
cine = Cine()

opciones = {
        "dolares": app.dolares,
        "bonos": app.bonos,
        "riesgo": app.riesgo_pais,
        "populares": cine.peliculas_populares,
        "lanzamientos": cine.lanzamientos
        }

