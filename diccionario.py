from indices.indice import Indices_economicos
from cine.cine import Cine
from noticias.noticias import Noticias
from clima.clima import Clima

indices = Indices_economicos()
cine = Cine()
noticas = Noticias()
clima = Clima()

opciones_dict = {
        "dolares": indices.dolares,
        "bonos": indices.bonos,
        "riesgo": indices.riesgo_pais,
        "populares": cine.peliculas_populares,
        "lanzamientos":cine.lanzamientos,
        "taquilleras": cine.taquilleras,
        "pagina": noticas.pagina,
        "infobae": noticas.info_bae,
        "tiempo": noticas.tiempo_titulos,
        "meteored": clima.meteored
        }

