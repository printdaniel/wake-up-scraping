from indices.indice import Indices_economicos
from cine.cine import Cine

indices = Indices_economicos()
cine = Cine()

opciones_dict = {
        "dolares": indices.dolares,
        "bonos": indices.bonos,
        "riesgo": indices.riesgo_pais,
        "populares": cine.peliculas_populares,
        "lanzamientos":cine.lanzamientos,
        "taquilleras": cine.taquilleras
        }

