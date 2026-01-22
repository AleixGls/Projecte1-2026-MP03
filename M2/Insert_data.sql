USE mydb;

SET FOREIGN_KEY_CHECKS = 0;

DELETE FROM Adventures;
DELETE FROM Characters;
DELETE FROM Adventure_protagonists;
DELETE FROM Step_adventures;
DELETE FROM Step_options;
DELETE FROM Users;

SET FOREIGN_KEY_CHECKS = 1;
-- Tabla adventures
INSERT INTO Adventures (Id_adventure, `name`, Description) VALUES
(1, 'El Bosque Maldito', 'Explora un bosque lleno de misterios'),
(2, 'La Torre Oscura', 'Asciende una torre llena de peligros'),
(3, 'La Ciudad Perdida', 'Descubre una civilización olvidada'),
(4, 'El Reino Submarino', 'Aventura bajo el océano');

-- Tabla characters
INSERT INTO Characters (Id_character, `name`, Description) VALUES
(1, 'Arin el Guerrero', 'Fuerte y valiente'),
(2, 'Lyra la Maga', 'Sabia y poderosa'),
(3, 'Korin el Explorador', 'Ágil y curioso');


-- Tabla adventure_protagonists
INSERT INTO Adventure_protagonists (Id_adventure, Id_character) VALUES
(1, 1), 
(2, 2), 
(3, 3),
(4, 2); 

-- Tabla Step_adventures

INSERT INTO Step_adventures (Id_step_adventure, Id_adventure, Description, Is_final_step) VALUES

(1, 1, 'Origen', 0),

(2, 1, 'Has aceptado la misión de adentrarte en el Bosque Maldito. Nada más cruzar su límite, la luz del mundo exterior desaparece y los árboles retorcidos te rodean. Sabes que, a partir de este momento, no hay vuelta atrás.', 0),

(3, 1, 'Avanzas con decisión por el sendero principal, pero pronto el bosque parece cerrarse tras de ti. Las ramas crujen como si algo se moviera entre ellas y, de repente, escuchas pasos que no son los tuyos siguiéndote de cerca. Al girarte descubres que una masa horripilante de ojos, tentáculos (¿o dedos retorcidos?) y dientes te está siguiendo. Lo has visto, y lo sabe. Podrías enfrentarte a ese terror cósmico, pero parece que no puede moverse más rápido que tú, así que también está la posibilidad de huir.', 0),

(4, 1, 'Te internas entre los árboles, apartando ramas que rezuman savia oscura. El suelo cede bajo tus pies y durante un instante crees ver figuras humanas observándote antes de desaparecer entre la vegetación. Caes en un foso lleno de esqueletos, lo que parecía ser una trampa mortal de estacas de madera si no fuese por que esas estacas estaban podridas y la abundancia de esqueletos te acolchase la caída. Al levantarte, percibes varios reflejos de luz rutilar a tu alrededor. Un pequeño vistazo más de cerca descubre que estos esqueletos están llenos de oro, gemas y joyas con un viso de incalculable valor.', 0),

(5, 1, 'Te detienes para analizar el entorno, pero el silencio se rompe con un grito lejano. Descubres huellas que parecen aparecer y desaparecer frente a tus ojos, como si el bosque las creara, aparentando el caminar de un ser. Un ser que camina con las palmas de las manos y deja un rastro de brea. Es normal que un hecho tan sobrenatural te sobresalte, pero parece que has llamado la atención de esas pisadas, ya que se están dirigiendo lentamente hacia ti.', 0),

(6, 1, 'Te adentras frente a la masa de ojos y tentáculos. Sus movimientos son imprevisibles y la tierra tiembla bajo tus pies. Sombras similares comienzan a emerger del bosque, retorciéndose hacia ti mientras un chillido desgarrador resuena.', 0),

(7, 1, 'Corres mientras la masa se desliza por el suelo como un líquido oscuro. Cada giro del sendero parece multiplicar sus formas y el bosque se transforma en un laberinto que cambia a cada paso.', 0),

(8, 1, 'Te aproximas a los esqueletos llenos de oro y gemas. Al tocar el tesoro, notas que los huesos se mueven levemente, como si respiraran. Una sensación de éxtasis y miedo se mezcla mientras algo invisible parece observar tus manos.', 0),

(9, 1, 'Decides apartarte y seguir avanzando, dejando atrás el tesoro brillante. El bosque parece enfadarse: las sombras se alargan y un viento helado corta tu rostro, como si te estuvieran castigando por no tomar lo que deseabas.', 0),

(10, 1, 'Te aproximas a las huellas de brea. Cada paso que das hace que el aire se vuelva más pesado y pegajoso, y el bosque parece susurrarte secretos imposibles. Una figura deformada aparece entre los árboles, observándote con curiosidad inquietante.', 0),

(11, 1, 'Das un paso atrás y tratas de ocultarte entre los árboles. La criatura que dejó las huellas parece percibir tu presencia y empieza a deslizarse silenciosamente hacia ti, provocando un nudo en tu estómago.', 0),

(12, 1, 'Te adentras en el corazón de la masa de ojos y tentáculos. La criatura emite un rugido que resuena en tus huesos y parece observar tu alma. De repente, todo se vuelve blanco y sientes que flotas entre mundos. Cada decisión será irreversible.', 0),

(13, 1, 'Retrocedes usando la vegetación como cobertura. La criatura se detiene, pero una sensación de ser observado permanece. Un río de sombras corre a tu alrededor, forzándote a elegir un camino hacia la seguridad o el enfrentamiento final.', 0),

(14, 1, 'Te adentras en el sendero lateral que parece un refugio. Sombras líquidas se retuercen en las paredes de los árboles y cada paso te acerca a un portal que podría ser tu salvación o tu perdición.', 0),

(15, 1, 'Te detienes en la oscuridad, respirando con dificultad. La masa se disuelve y reaparece alrededor tuyo, obligándote a decidir entre atacar de frente o lanzarte a un escape arriesgado.', 0),

(16, 1, 'Tomas el oro y las gemas. Los huesos empiezan a girar, formando un círculo que te atrapa. Todo brilla y palpita al ritmo de tu corazón. Cada segundo cuenta y tu siguiente movimiento definirá si sobrevives al bosque maldito.', 0),

(17, 1, 'Decides retirarte con las manos vacías. La sensación de peligro aumenta y un viento helado te empuja hacia una senda que podría ser la salida o la trampa final del bosque.', 0),

(18, 1, 'Sigues avanzando, sintiendo que el bosque entero conspira en tu contra. Las ramas se alargan y voces apagadas murmuran tu nombre. Debes elegir un camino seguro o enfrentarte a la oscuridad que acecha al frente.', 0),

(19, 1, 'Te escondes entre los árboles, observando las sombras. La calma es temporal, y pronto un rugido profundo te obligará a decidir entre huir o lanzarte a un enfrentamiento que podría ser fatal.', 0),

(20, 1, 'Avanzas hacia la figura deformada. La forma se materializa y un chillido surrealista corta el aire. Sientes que el tiempo se distorsiona y tu próximo movimiento decidirá si quedas atrapado o logras escapar.', 0),

(21, 1, 'Te apartas lentamente, pero la figura parece perseguirte con cada mirada. El suelo se ondula y debes decidir entre correr por el sendero resbaladizo o esconderte entre la maleza que respira.', 0),

(22, 1, 'Corres hacia un claro iluminado tenuemente. Las sombras intentan arrastrarte, pero un árbol enorme parece ofrecer un refugio temporal. Debes decidir si te escondes o te enfrentas a lo que viene.', 0),

(23, 1, 'Te ocultas detrás de un tronco caído, esperando que la criatura pase de largo.', 0),

(24, 1, 'Decides fundirte con la criatura y aceptar su mundo desconocido.', 0),

(25, 1, 'Retrocedes con rapidez, escapando pero marcado por el terror.', 0),

(26, 1, 'Cruzas el portal sin dudar, adentrándote en lo desconocido.', 0),

(27, 1, 'Decides retroceder y regresar al sendero seguro.', 0),

(28, 1, 'Tomas el oro, arriesgándote a perderte en la ilusión.', 0),

(29, 1, 'Decides dejar el oro y continuar hacia la salida.', 0),

(30, 1, 'Enfrentas la oscuridad y atraviesas el claro.', 0),

(31, 1, 'Permaneces oculto hasta que la noche termina y logras escapar.', 0),

(32, 1, 'Confrontas a la figura y descubres su secreto.', 0),

(33, 1, 'Huyes del lugar, pero la visión persiste en tu mente.', 0),

(34, 1, 'Te escondes hasta que la amenaza desaparece.', 0),

(35, 1, 'Decides atacar con astucia y logras abrirte paso.', 0),

(36, 1, 'Confías en los ojos brillantes y sigues sus indicaciones.', 0),

(37, 1, 'Mantienes distancia y logras escapar.', 0),

(38, 1, 'Sigues tu instinto y avanzas entre los peligros.', 0),

(39, 1, 'Te refugias y esperas hasta que el peligro se disipa.', 0),

(40, 1, 'Sigues las luces y atraviesas el portal.', 0),

(41, 1, 'Ignoras las luces y continúas por un sendero seguro.', 0),

(42, 1, 'Tocas el objeto y eres transportado a otro mundo.', 0),

(43, 1, 'Decides seguir un camino seguro y evitas el peligro inmediato.', 0),

(44, 1, 'Sigues tu instinto y logras escapar del peligro inminente.', 0),

(45, 1, 'Esperas y finalmente logras salir ileso.', 0),

(46, 1, 'Te fusionas con la criatura y desapareces en un mundo desconocido lleno de maravillas y horrores.', 1),

(47, 1, 'Logras escapar de la masa, pero parte de tu mente queda marcada por el terror.', 1),

(48, 1, 'Cruzas el portal y despiertas en un mundo surrealista, lleno de maravillas y horrores incomprensibles.', 1),

(49, 1, 'Escapas del sendero y vuelves al bosque seguro, aunque con la sensación de que algo quedó atrás.', 1),

(50, 1, 'El oro te consume y el bosque te atrapa en una ilusión interminable.', 1),

(51, 1, 'Sueltas el oro y escapas, dejando atrás la codicia y el peligro.', 1),

(52, 1, 'Te enfrentas a la oscuridad y logras atravesar el claro, sobreviviendo con cicatrices.', 1),

(53, 1, 'Permaneces oculto hasta que la noche termina y logras escapar, marcado por el miedo.', 1),

(54, 1, 'Confrontas a la figura y descubres que es una prueba del bosque; sobrevives con conocimiento.', 1),

(55, 1, 'Escapas del lugar, pero la visión queda grabada en tus pesadillas.', 1),

(56, 1, 'Te escondes y las sombras desaparecen, permitiéndote escapar ileso.', 1),

(57, 1, 'Decides atacar con astucia y logras abrirte paso hacia la salida, aunque con miedo persistente.', 1),

(58, 1, 'Confías en los ojos brillantes y te guían a un lugar seguro y misterioso.', 1),

(59, 1, 'Mantienes distancia y logras escapar, aunque el misterio persiste.', 1),

(60, 1, 'Sigues avanzando con tu instinto y logras salir del bosque entre peligros insólitos.', 1),

(61, 1, 'Te refugias hasta que el bosque se calma y logras escapar.', 1),

(62, 1, 'Sigues las luces y descubres un portal hacia otro plano lleno de maravillas y horrores.', 1),

(63, 1, 'Decides ignorarlas y avanzar por un sendero seguro, abandonando el misterio.', 1),

(64, 1, 'Tocas el objeto y una visión surrealista te envuelve, llevándote a otro mundo.', 1),

(65, 1, 'Optas por un camino seguro, evitando el peligro inmediato pero dejando el misterio atrás.', 1),

(66, 1, 'Sigues tu instinto y logras escapar del peligro inminente.', 1),

(67, 1, 'Esperas y finalmente logras salir ileso.', 1);






-- tabla step_options
INSERT INTO Step_options (Id_step_option, Id_step_adventure, Leads_to, Description) VALUES

(1, 1, 2, 'Adentrarse en el Bosque Maldito'),

(2, 2, 3, 'Avanzar con decisión por el sendero principal, sin mirar atrás'),
(3, 2, 4, 'Explorar con cautela entre los árboles cercanos'),
(4, 2, 5, 'Detenerte un momento para analizar el entorno y orientarte'),

(5, 3, 6, 'Te giras para enfrentar a la masa horripilante y estudias sus movimientos'),
(6, 3, 7, 'Decides acelerar y huir por el sendero mientras el terror te persigue'),

(7, 4, 8, 'Te acercas cuidadosamente a los esqueletos llenos de tesoros y exploras su interior'),
(8, 4, 9, 'Decides apartarte y seguir avanzando por el bosque dejando los tesoros atrás'),

(9, 5, 10, 'Te aproximas a las huellas de brea para observar de qué criatura se trata'),
(10, 5, 11, 'Das un paso atrás y tratas de ocultarte entre los árboles'),

(11, 6, 12, 'Te lanzas hacia el corazón de la masa, decidido a descubrir su naturaleza'),
(12, 6, 13, 'Retrocedes lentamente, usando la vegetación para mantener la distancia'),

(13, 7, 14, 'Te desvías hacia un sendero lateral que parece un refugio temporal'),
(14, 7, 15, 'Te detienes, aprovechando la oscuridad para confundir a la masa y escapar'),

(15, 8, 16, 'Tomas un puñado de oro y gemas, ignorando la sensación de peligro'),
(16, 8, 17, 'Decides retirarte con las manos vacías, observando los movimientos de los esqueletos'),

(17, 9, 18, 'Sigues avanzando por el bosque, intentando mantener la calma mientras el aire se vuelve más pesado'),
(18, 9, 19, 'Decides esconderte entre los árboles hasta que la sensación de hostilidad disminuya'),

(19, 10, 20, 'Avanzas hacia la figura deformada, dejando que tu curiosidad venza al miedo'),
(20, 10, 21, 'Te apartas lentamente, intentando no llamar la atención y manteniendo la calma'),

(21, 11, 22, 'Corres en diagonal para escapar de la criatura, buscando un claro seguro'),
(22, 11, 23, 'Te ocultas detrás de un tronco caído, esperando que la criatura pase de largo'),

(23, 12, 24, 'Decides fundirte con la criatura y aceptar su mundo desconocido'),
(24, 12, 25, 'Retrocedes con rapidez, escapando pero marcado por el terror'),

(25, 13, 26, 'Cruzas el portal sin dudar, adentrándote en lo desconocido'),
(26, 13, 27, 'Decides retroceder y regresar al sendero seguro'),

(27, 14, 28, 'Tomas el oro, arriesgándote a perderte en la ilusión'),
(28, 14, 29, 'Decides dejar el oro y continuar hacia la salida'),

(29, 15, 30, 'Enfrentas la oscuridad y atraviesas el claro'),
(30, 15, 31, 'Permaneces oculto hasta que la noche termina y logras escapar'),

(31, 16, 32, 'Confrontas a la figura y descubres su secreto'),
(32, 16, 33, 'Huyes del lugar, pero la visión persiste en tu mente'),

(33, 17, 34, 'Te escondes hasta que la amenaza desaparece'),
(34, 17, 35, 'Decides atacar con astucia y logras abrirte paso'),

(35, 18, 36, 'Confías en los ojos brillantes y sigues sus indicaciones'),
(36, 18, 37, 'Mantienes distancia y logras escapar'),

(37, 19, 38, 'Sigues tu instinto y avanzas entre los peligros'),
(38, 19, 39, 'Te refugias y esperas hasta que el peligro se disipa'),

(39, 20, 40, 'Sigues las luces y atraviesas el portal'),
(40, 20, 41, 'Ignoras las luces y continúas por un sendero seguro'),

(41, 21, 42, 'Tocas el objeto y eres transportado a otro mundo'),
(42, 21, 43, 'Decides seguir un camino seguro y evitas el peligro inmediato'),

(43, 22, 44, 'Sigues tu instinto y logras escapar del peligro inminente'),
(44, 22, 45, 'Esperas y finalmente logras salir ileso'),

(45, 23, 44, 'Sigues observando hasta encontrar el momento adecuado para moverte'),
(46, 23, 45, 'Permaneces oculto esperando que todo pase'),

(47, 24, 46, 'Aceptas la fusión completamente'),
(48, 24, 47, 'Intentas resistir en el último momento'),

(49, 25, 46, 'Abrazas tu nuevo destino'),
(50, 25, 47, 'Luchas contra el terror que te marca'),

(51, 26, 48, 'Atraviesas el portal con determinación'),
(52, 26, 49, 'Dudas en el último segundo'),

(53, 27, 48, 'Insistes en cruzar el portal'),
(54, 27, 49, 'Regresas definitivamente al sendero'),

(55, 28, 50, 'Te aferras al oro'),
(56, 28, 51, 'Sueltas el oro en el último momento'),

(57, 29, 50, 'Regresas por el oro'),
(58, 29, 51, 'Sigues alejándote definitivamente'),

(59, 30, 52, 'Enfrentas la oscuridad con valor'),
(60, 30, 53, 'Te mantienes oculto'),

(61, 31, 52, 'Sales de tu escondite para enfrentar'),
(62, 31, 53, 'Permaneces oculto hasta el amanecer'),

(63, 32, 54, 'Confrontas directamente a la figura'),
(64, 32, 55, 'Retrocedes lentamente'),

(65, 33, 54, 'Regresas para confrontar'),
(66, 33, 55, 'Continúas huyendo'),

(67, 34, 56, 'Esperas pacientemente'),
(68, 34, 57, 'Preparas un ataque sorpresa'),

(69, 35, 56, 'Te ocultas mejor'),
(70, 35, 57, 'Atacas con determinación'),

(71, 36, 58, 'Confías plenamente en ellos'),
(72, 36, 59, 'Los sigues con cautela'),

(73, 37, 58, 'Te acercas más'),
(74, 37, 59, 'Mantienes la distancia segura'),

(75, 38, 60, 'Sigues tu instinto sin dudar'),
(76, 38, 61, 'Avanzas con precaución'),

(77, 39, 60, 'Sales del refugio'),
(78, 39, 61, 'Permaneces refugiado'),

(79, 40, 62, 'Atraviesas el portal de luz'),
(80, 40, 63, 'Retrocedes del portal'),

(81, 41, 62, 'Cambias de opinión y entras'),
(82, 41, 63, 'Continúas por el sendero seguro'),

(83, 42, 64, 'Tocas el objeto brillante'),
(84, 42, 65, 'Te alejas del objeto'),

(85, 43, 64, 'Regresas al objeto'),
(86, 43, 65, 'Sigues el camino seguro'),

(87, 44, 66, 'Sigues corriendo'),
(88, 44, 67, 'Te detienes a descansar'),

(89, 45, 66, 'Decides moverte'),
(90, 45, 67, 'Sigues esperando');

-- tabla users
use mydb;
INSERT INTO Users (id_user, username, password) Values 
(1,'Paco','1234'),
(2,'Maria','0987')




