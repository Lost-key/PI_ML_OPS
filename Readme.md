# Proyecto 1 MLOps

Se nos pide desarrollar un MVP, una API que retorne información específica en base a un dataset de la plataforma STEAM.

Se requieren las siguientes funciones para los endpoints que se consumirán en la API:

- `def PlayTimeGenre(genero: str)`: Debe devolver el año con más horas jugadas para dicho género.
- `def UserForGenre(genero:str)`: Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.
- `def UsersRecommend(año: int)`: Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado (reviews.recommend = True y comentarios positivos/neutrales).
- `def UsersWorstDeveloper(año: int)`: Devuelve el top 3 de desarrolladoras con juegos MENOS recomendados por usuario para el año dado (reviews.recommend = False y comentarios negativos).
- `def sentiment_analysis(empresa_desarrolladora: str)`: Según la empresa desarrolladora, se devuelve un diccionario con el nombre de la desarrolladora como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor.

**Deployment:** Render