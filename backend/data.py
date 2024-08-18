from src.models import Game, Review, Player


GAMES_A = [
    Game(name='The_Legend_of_Zelda:_Breath_of_the_Wild', calification=4.9, description='Un juego de acción y aventura en un mundo abierto.'),
    Game(name='Red_Dead_Redemption_2', calification=4.8, description='Juego de acción y aventura con un entorno de mundo abierto en el Salvaje Oeste.'),
    Game(name='The_Witcher_3:_Wild_Hunt', calification=4.9, description='Juego de rol y acción en un mundo de fantasía.'),
    Game(name='Minecraft', calification=4.7, description='Juego de construcción, exploración y supervivencia en un mundo de bloques.'),
    Game(name='Super_Mario_Odyssey', calification=4.8, description='Juego de plataformas en 3D protagonizado por Mario en una aventura global.'),
    Game(name='Cyberpunk_2077', calification=3.5, description='Juego de rol y acción en un futuro distópico.'),
    Game(name='Fortnite', calification=4.4, description='Juego de batalla real en línea con construcción y supervivencia.')
]

GAMES_B = [
    Game(name='God_of_War', calification=4.9, description='Juego de acción y aventura mitológica.'),
    Game(name='The_Last_of_Us_Part_II', calification=4.8, description='Juego de acción y aventura con una narrativa emocional.'),
    Game(name='Grand_Theft_Auto_V', calification=4.8, description='Juego de acción y aventura en un mundo abierto.'),
    Game(name='Overwatch', calification=4.5, description='Juego de disparos en primera persona en equipo.'),
    Game(name='Dark_Souls_III', calification=4.6, description='Juego de rol de acción con alta dificultad.'),
    Game(name='Horizon_Zero_Dawn', calification=4.7, description='Juego de rol y acción en un futuro post-apocalíptico.'),
    Game(name='Doom_Eternal', calification=4.7, description='Juego de disparos en primera persona con acción intensa.')
]

GAMES_C = [
    Game(name='Assassins_Creed_Valhalla', calification=4.5, description='Juego de rol y acción ambientado en la era vikinga.'),
    Game(name='Call_of_Duty:_Modern_Warfare', calification=4.6, description='Juego de disparos en primera persona con una campaña intensa.'),
    Game(name='Resident_Evil_2_Remake', calification=4.7, description='Juego de survival horror con gráficos modernizados.'),
    Game(name='Sekiro:_Shadows_Die_Twice', calification=4.8, description='Juego de acción y aventura con combates desafiantes.'),
    Game(name='Apex_Legends', calification=4.4, description='Juego de batalla real con personajes únicos y habilidades.'),
    Game(name='Control', calification=4.3, description='Juego de acción y aventura con elementos sobrenaturales.'),
    Game(name='Stardew_Valley', calification=4.9, description='Juego de simulación de granja con muchas actividades y relaciones.')
]





REVIEWS_A = [
    Review(title='Impresionante_libertad_en_Breath_of_the_Wild', description='Breath of the Wild ofrece una libertad sin precedentes y un mundo abierto lleno de sorpresas y desafíos.', calification=4.9),
    Review(title='Una_obra_maestra_del_Salvaje_Oeste', description='Red Dead Redemption 2 es una experiencia narrativa y visual que define una generación.', calification=4.8),
    Review(title='El_pináculo_del_RPG_moderno', description='The Witcher 3: Wild Hunt combina una narrativa profunda con un vasto mundo abierto lleno de aventuras.', calification=4.9),
    Review(title='Creatividad_sin_límites', description='Minecraft permite a los jugadores desatar su creatividad en un mundo infinito de bloques.', calification=4.7),
    Review(title='Una_aventura_global_con_Mario', description='Super Mario Odyssey es un juego de plataformas encantador y repleto de imaginación.', calification=4.8),
    Review(title='Un_lanzamiento_complicado_pero_prometedor', description='Cyberpunk 2077 ofrece una experiencia de rol futurista con algunos problemas técnicos.', calification=3.5),
    Review(title='Diversión_constante_en_cada_partida', description='Fortnite es un juego adictivo que combina construcción y combate en un entorno de batalla real.', calification=4.4)
]

REVIEWS_B = [
    Review(title='Épico_viaje_mitológico_en_God_of_War', description='God of War redefine la serie con una emocionante aventura mitológica.', calification=4.9),
    Review(title='Emocional_y_brutal_en_The_Last_of_Us_Part_II', description='The Last of Us Part II es una montaña rusa emocional con una jugabilidad excelente.', calification=4.8),
    Review(title='Libertad_y_crimen_en_GTA_V', description='Grand Theft Auto V ofrece un vasto mundo abierto lleno de actividades y una historia intrigante.', calification=4.8),
    Review(title='Acción_en_equipo_en_Overwatch', description='Overwatch es un juego de disparos en equipo con personajes únicos y una jugabilidad adictiva.', calification=4.5),
    Review(title='Desafío_incesante_en_Dark_Souls_III', description='Dark Souls III ofrece una experiencia desafiante y gratificante en un mundo oscuro y peligroso.', calification=4.6),
    Review(title='Futuro_apocalíptico_en_Horizon_Zero_Dawn', description='Horizon Zero Dawn combina una narrativa fascinante con una jugabilidad impresionante.', calification=4.7),
    Review(title='Acción_intensa_en_Doom_Eternal', description='Doom Eternal es pura adrenalina con combates intensos y un diseño de niveles excepcional.', calification=4.7)
]

REVIEWS_C3 = [
    Review(title='Épica_aventura_vikinga_en_Valhalla', description='Assassin\'s Creed Valhalla ofrece una experiencia vikinga envolvente con combates épicos.', calification=4.5),
    Review(title='Intensidad_y_realismo_en_Modern_Warfare', description='Call of Duty: Modern Warfare redefine el género con su realismo y acción intensa.', calification=4.6),
    Review(title='Horror_reimaginado_en_Resident_Evil_2', description='Resident Evil 2 Remake es una reinvención magistral del clásico de survival horror.', calification=4.7),
    Review(title='Desafío_y_precisión_en_Sekiro', description='Sekiro: Shadows Die Twice es una prueba de habilidad con combates precisos y exigentes.', calification=4.8),
    Review(title='Batalla_real_con_estilo_en_Apex_Legends', description='Apex Legends ofrece una experiencia de batalla real rápida y llena de acción con personajes diversos.', calification=4.4),
    Review(title='Misterio_sobrenatural_en_Control', description='Control combina una narrativa intrigante con poderes sobrenaturales en un entorno único.', calification=4.3),
    Review(title='Vida_de_granja_en_Stardew_Valley', description='Stardew Valley es una experiencia de simulación de granja encantadora y adictiva.', calification=4.9)
]

PLAYERS_A = [
    Player(name='Faker', preference='MOBA', phone='123-456-7890'),
    Player(name='s1mple', preference='Shooter', phone='234-567-8901'),
    Player(name='N0tail', preference='MOBA', phone='345-678-9012'),
    Player(name='Ninja', preference='Battle Royale', phone='456-789-0123'),
    Player(name='Coldzera', preference='Shooter', phone='567-890-1234'),
    Player(name='Arteezy', preference='MOBA', phone='678-901-2345'),
    Player(name='Uzi', preference='MOBA', phone='789-012-3456')
]

PLAYERS_B = [
    Player(name='Cristian_Ruz', preference='Shooter', phone='123-456-7890'),
    Player(name='Moises_Retamal', preference='RPG', phone='234-567-8901'),
    Player(name='Caps', preference='MOBA', phone='765-432-1098'),
    Player(name='Xyp9x', preference='Shooter', phone='654-321-0987'),
    Player(name='Perkz', preference='MOBA', phone='543-210-9876'),
    Player(name='Mongraal', preference='Battle Royale', phone='432-109-8765'),
    Player(name='kennyS', preference='Shooter', phone='321-098-7654')
]

PLAYERS_C = [
    Player(name='ZywOo', preference='Shooter', phone='456-789-1230'),
    Player(name='Chovy', preference='MOBA', phone='567-890-2341'),
    Player(name='Bjergsen', preference='MOBA', phone='678-901-3452'),
    Player(name='FalleN', preference='Shooter', phone='789-012-4563'),
    Player(name='Ropz', preference='Shooter', phone='890-123-5674'),
    Player(name='Rekkles', preference='MOBA', phone='901-234-6785'),
    Player(name='TenZ', preference='Shooter', phone='012-345-7896')
]




WRONG_GAMES = [
    Game(name='', calification='', description='Un juego de acción y aventura en un mundo abierto.'),
    Game(name='Red_Dead_Redemption_2', calification='', description=''),
    Game(name='The_Witcher_3:_Wild_Hunt', calification=4.9, description=''),
    Game(name='Minecraft', calification=4.7, description='Juego de construcción, exploración y supervivencia en un mundo de bloques.'),
    Game(name='', calification=4.8, description='Juego de plataformas en 3D protagonizado por Mario en una aventura global.')
]

WRONG_REVIEWS = [
    Review(title='', description='Breath of the Wild ofrece una libertad sin precedentes y un mundo abierto lleno de sorpresas y desafíos.', calification=4.9),
    Review(title='Una_obra_maestra_del_Salvaje_Oeste', description='', calification=4.8),
    Review(title='El_pináculo_del_RPG_moderno', description='The Witcher 3: Wild Hunt combina una narrativa profunda con un vasto mundo abierto lleno de aventuras.', calification=0.0),
    Review(title='', description='Minecraft permite a los jugadores desatar su creatividad en un mundo infinito de bloques.', calification=4.7),
    Review(title='Una_aventura_global_con_Mario', description='', calification=4.8)
]

WRONG_PLAYERS = [
    Player(name='', preference='Shooter', phone='123-456-7890'),
    Player(name='s1mple', preference='', phone='234-567-8901'),
    Player(name='N0tail', preference='MOBA', phone=''),
    Player(name='', preference='', phone='456-789-0123'),
    Player(name='Coldzera', preference='Shooter', phone='567-890-1234')
]