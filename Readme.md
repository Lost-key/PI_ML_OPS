# Proyecto 1 MLOps

Se nos pide desarrollar un MVP, una API que retorne información específica en base a un dataset de la plataforma STEAM.

Se requieren las siguientes funciones para los endpoints que se consumirán en la API:

- `def PlayTimeGenre(genero: str)`: Debe devolver el año con más horas jugadas para dicho género.
- `def UserForGenre(genero:str)`: Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.
- `def UsersRecommend(año: int)`: Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado (reviews.recommend = True y comentarios positivos/neutrales).
- `def UsersWorstDeveloper(año: int)`: Devuelve el top 3 de desarrolladoras con juegos MENOS recomendados por usuario para el año dado (reviews.recommend = False y comentarios negativos).
- `def sentiment_analysis(empresa_desarrolladora: str)`: Según la empresa desarrolladora, se devuelve un diccionario con el nombre de la desarrolladora como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor.

Tecnologías Utilizadas
Visual Studio Code Jupyter Notebook Python NumPy Pandas Matplotlib scikit-learn FastAPI Render

Diccionario de datos para el proyecto

partimos de un dataset de 3 json:

output_steam_games.json 
contiene datos relacionados con los juegos, las variables que contiene son:

- publisher: 		empresa publicadora/desarrolladora del juego.
- genres: 			género del juego, formado por una lista de uno o mas géneros por cada registro.
- app_name: 		nombre del juego.
- title: 			título del juego.
- url: 				url del juego.
- release_date: 	fecha de lanzamiento del juego en formato YYYY-MM-DD.
- tags: 			etiqueta del contenido, formado por una lista de uno o mas tags por registro.
- reviews_url: 		url donde se encuentra el review de ese juego.
- specs: 			son especificaciones de cada juego. Es una lista con uno o mas especificaciones.
- price: 			es el precio del item.
- early_access: 	indica acceso temprano con un True/False.
- id: 				identificador único del contenido.
- developer: 		desarrollador del juego, suele duplicar el campo publisher (taen casi siempre los mismos datos).

-----------------------------------------------------------------------------------------------------------------------------------------------------------

australian_user_reviews.json 
contiene los comentarios que los usuarios realizaron sobre los juegos que consumen, 
además de datos adicionales como si recomiendan o no ese juego, emoticones, etc 
y estadísticas de si el comentario fué útil o no para otros usuarios. 
También presenta el id del usuario que comenta con su url del perfil y el id del juego que comenta.
Las variables que contiene son:

- user_id: 	identificador único para el usuario.  
- user_url: url del perfil del usuario en streamcommunity.  
- reviews: 	contiene una lista de diccionarios, para cada usuario se tiene uno o mas diccionarios con el review. 
		Cada diccionario contiene:
						- funny: 		indica si alguien puso emoticón de gracioso al review.  
						- posted: 		fecha de posteo del review en formato Posted April 21, 2011.  
						- last_edited: 	fecha de la última edición.  
						- item_id: 		identificador único del item, es decir, del juego.  
						- helpful: 		estadística donde otros usuarios indican si fue útil la información.  
						- recommend: 	booleano que indica si el usuario recomienda o no el juego.  
						- review: 		comentarios sobre el juego.
						
----------------------------------------------------------------------------------------------------------------------------------------------------------
	
australian_users_items.json 

contiene información sobre los juegos que juegan todos los usuarios, así como el tiempo acumulado que cada usuario jugó a un determinado juego.
Las variables que contiene son:

- user_id: 			identificador único del usuario.
- items_count: 		número entero que indica la cantidad de juegos que ha consumido el usuario.
- steam_id: 		es un número único para la plataforma.
- user_url: 		es la url del perfil del usuario
- items: 			contiene una lista de uno o mas diccionarios de los items que consume cada usuario. 
				Cada diccionario tiene las siguientes claves:
						- item_id: 			es el identificados del item, es decir, del juego.
						- item_name: 		nombre del contenido que consume (juego).
						- playtime_forever: tiempo acumulado que un usuario jugó a un juego.
						- playtime_2weeks: 	tiempo acumulado que un usuario jugó a un juego en las últimas dos semanas.
