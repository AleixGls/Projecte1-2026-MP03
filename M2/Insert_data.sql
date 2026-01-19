USE mydb;

SET FOREIGN_KEY_CHECKS = 0;

DELETE FROM Adventures;
DELETE FROM Characters;
DELETE FROM Adventure_protagonists;
DELETE FROM Step_adventures;
DELETE FROM Step_options;

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
(1, 1,
'Has aceptado la misión de adentrarte en el Bosque Maldito. Nada más cruzar su límite, la luz del mundo exterior desaparece y los árboles retorcidos te rodean. Sabes que, a partir de este momento, no hay vuelta atrás.',
0),

(2, 1,
'Llegas al Bosque Maldito siguiendo antiguos rumores sobre tesoros y peligros. El aire es frío y húmedo, y cada paso que das dentro del bosque refuerza la sensación de que estás siendo observado.',
0),

(3, 1,
'Te internas en el Bosque Maldito huyendo de algo que prefieres no recordar. Los sonidos del exterior se desvanecen y solo queda el murmullo inquietante del bosque cerrándose a tu alrededor.',
0),

(4, 1,
'El sendero que conduce al Bosque Maldito se divide en varios caminos nada más entrar. Antiguas señales advierten del peligro, pero decides continuar y elegir tu propio destino.',
0),

(5, 1,
'Una espesa niebla cubre la entrada del Bosque Maldito cuando das el primer paso en su interior. La visibilidad es mínima y el silencio resulta antinatural, como si el bosque contuviera la respiración.',
0),

-- Derivados del Step_adventure 1
(6, 1,
'Avanzas con decisión por el sendero principal, pero pronto el bosque parece cerrarse tras de ti. Las ramas crujen como si algo se moviera entre ellas y, de repente, escuchas pasos que no son los tuyos siguiéndote de cerca. Al girarte descubres que una masa horripilante de ojos, tentáculos (¿o dedos retorcidos?) y dientes te está siguiendo. Lo has visto, y lo sabe. Podrías enfrentarte a ese terror cósmico, pero parece que no puede moverse más rápido que tú, así que también está la posibilidad de huir.',
0),

(7, 1,
'Te internas entre los árboles, apartando ramas que rezuman savia oscura. El suelo cede bajo tus pies y durante un instante crees ver figuras humanas observándote antes de desaparecer entre la vegetación. Caes en un foso lleno de esqueletos, lo que parecía ser una trampa mortal de estacas de madera si no fuese por que esas estacas estaban podridas y la abundancia de esqueletos te acolchase la caída. Al levantarte, percibes varios reflejos de luz rutilar a tu alrededor. Un pequeño vistazo más de cerca descubre que estos esqueletos están llenos de oro, gemas y joyas con un viso de incalculable valor.',
0),

(8, 1,
'Te detienes para analizar el entorno, pero el silencio se rompe con un grito lejano. Descubres huellas que parecen aparecer y desaparecer frente a tus ojos, como si el bosque las creara, aparentando el caminar de un ser. Un ser que camina con las palmas de las manos y deja un rastro de brea. Es normal que un hecho tan sobrenatural te sobresalte, pero parece que has llamado la atención de esas pisadas, ya que se están dirigiendo lentamente hacia ti.',
0),


-- Derivados del Step_adventure 2
(9, 1,
'Ignoras la sensación de peligro y sigues adelante. El aire se vuelve irrespirable y comienzas a oír susurros que pronuncian tu nombre, aunque no logras distinguir de dónde provienen.',
0),

(10, 1,
'Examinando la zona encuentras restos de un campamento reciente. La hoguera aún está tibia y manchas oscuras cubren el suelo, como si sus ocupantes hubieran huido en pánico. Puedes distinguir con mucha facilidad la ruta de alguien que huyó de ahí, con pasos marcados y ramas rotas, pero también vislumbras muy a lo lejos un grupo de luces titilantes, similares a lo que sería una agrupación de gente con antorchas.',
0),

(11, 1,
'Al cambiar de rumbo, el bosque reacciona violentamente. Los árboles parecen inclinarse hacia ti y un ruido ensordecedor te obliga a cubrirte los oídos mientras corres sin saber hacia dónde. Pierdes el sentido de la orientación, el tiempo y tu mochila en lo que te han parecido minutos desde que empezó ese ruido, pero el bosque vuelve a estar en calma. Una vez vuelves a caminar, vuelves a sentir esa sensación escalofriante de observación constante.',
0),


-- Derivados del Step_adventure 3
(12, 1,
'Sigues los sonidos hasta una zona donde las sombras se mueven de forma antinatural. Una figura emerge brevemente frente a ti y desaparece atravesando un árbol sólido. No sabes si es el ron de la taberna de mala muerte que te has tomado esta mañana o si de verdad has visto a tu mejor amigo de la infancia, aquel que no volviste a ver nunca más desde que lo reclutaron para el ejército.',
0),

(13, 1,
'Te escondes conteniendo la respiración. Algo pasa a pocos metros de ti, arrastrándose por el suelo. Sientes su respiración húmeda antes de que se aleje lentamente. Esperas unos minutos hasta que estás cerciorado de que es completamente seguro salir, y te topas con un rastro de babas, asumes que los del monstruo. Por un lado, solo un idiota que no aprecia su vida decidiría no ir en dirección contraria a lo que sea que fuese eso, pero por otro lado eres un idiota al que la vida dejó de hacerle gracia mucho tiempo atrás.',
0),

(14, 1,
'Huyes sin mirar atrás. Las ramas te golpean el rostro y al salir a un enorme claro llano descubres restos de huesos dispuestos formando símbolos incomprensibles que llenan el terreno del claro entero. Oyes un leve zumbido grave, como si una congregación de monjes estuviese canturreando a tu alrededor. Deberías seguir huyendo, pero hay algo antinatural en esa formación de huesos que despierta tus instintos más primitivos.',
0),

-- Derivados del Step_adventure 4
(15, 1,
'El sendero izquierdo se vuelve traicionero. El suelo resbala y caes violentamente, escuchando risas apagadas mientras intentas ponerte en pie. Entre los árboles distingues figuras pequeñas y oscuras, con sonrisas desproporcionadas, que se alejan saltando entre las sombras.',
0),

(16, 1,
'El sendero central muestra huellas recientes que no parecen humanas. Al seguirlas, encuentras antorchas aún humeantes y restos de comida podrida. El silencio posterior es más inquietante que cualquier ruido. Una sombra se mueve entre los árboles y, por un instante, parece invitarte a acercarte para descubrir lo que es, aunque algo dentro de ti grita que no lo hagas.',
0),

(17, 1,
'Avanzas por el sendero derecho cuando el suelo cede bajo ti. Consigues agarrarte a una raíz, pero algo húmedo y frío roza tu tobillo antes de desaparecer en la oscuridad. Las sombras se alargan y te rodean con un murmullo constante. Sientes la tentación de seguir adelante pese al peligro, mientras tus instintos te empujan a escalar para ponerte a salvo.',
0),

-- Derivados del Step_adventure 5
(18, 1,
'Caminas a ciegas entre la niebla hasta que pierdes por completo la noción del espacio. Por momentos, el bosque parece desvanecerse y te ves flotando en un vacío blanquecino. Entre la neblina distingues formas que desaparecen cuando intentas enfocarlas. La curiosidad te tienta a avanzar hacia ellas, aunque la sensación de irrealidad te advierte que podrías perderte para siempre.',
0),

(19, 1,
'Sigues sonidos distorsionados que se retuercen a tu alrededor. Voces infantiles ríen y lloran al mismo tiempo, guiándote hacia algo que no alcanzas a ver. Cada paso hace que las voces suenen más cerca y tu corazón late con fuerza. Lo tienes tan cerca que es casi irresistible el acercarte a ver qué hay al final, pero indudablemente hay algo en todo esto que no cuadra.',
0),

(20, 1,
'Permaneces inmóvil mientras la niebla se arremolina a tu alrededor. Figuras humanas comienzan a formarse frente a ti, imitando tus movimientos con un retraso inquietante. Sus ojos brillan con un fulgor antinatural y una risa fría corta el aire. Parece que están esperando pacientemente a que digas algo, y no tiene pinta que la niebla vaya a desaparecer tan facilmente como ha aparecido.',
0),

-- Derivados del Step_adventure 6
(21, 1, 'Te adentras frente a la masa de ojos y tentáculos. Sus movimientos son imprevisibles y la tierra tiembla bajo tus pies. Sombras similares comienzan a emerger del bosque, retorciéndose hacia ti mientras un chillido desgarrador resuena.', 0),

(22, 1, 'Corres mientras la masa se desliza por el suelo como un líquido oscuro. Cada giro del sendero parece multiplicar sus formas y el bosque se transforma en un laberinto que cambia a cada paso.', 0),

-- Derivados del Step_adventure 7
(23, 1, 'Te aproximas a los esqueletos llenos de oro y gemas. Al tocar el tesoro, notas que los huesos se mueven levemente, como si respiraran. Una sensación de éxtasis y miedo se mezcla mientras algo invisible parece observar tus manos.', 0),

(24, 1, 'Decides apartarte y seguir avanzando, dejando atrás el tesoro brillante. El bosque parece enfadarse: las sombras se alargan y un viento helado corta tu rostro, como si te estuvieran castigando por no tomar lo que deseabas.', 0),

-- Derivados del Step_adventure 8
(25, 1, 'Te aproximas a las huellas de brea. Cada paso que das hace que el aire se vuelva más pesado y pegajoso, y el bosque parece susurrarte secretos imposibles. Una figura deformada aparece entre los árboles, observándote con curiosidad inquietante.', 0),

(26, 1, 'Das un paso atrás y tratas de ocultarte entre los árboles. La criatura que dejó las huellas parece percibir tu presencia y empieza a deslizarse silenciosamente hacia ti, provocando un nudo en tu estómago.', 0),

-- Derivados del Step_adventure 9
(27, 1, 'Sigues los susurros y las voces se vuelven más claras, casi inteligibles. Al girar un tronco, descubres ojos brillantes que te observan desde la oscuridad, midiendo cada movimiento que haces.', 0),

(28, 1, 'Decides alejarte de los susurros. La maleza se cierra a tu paso y sientes que el bosque entero conspira para desviarte del camino seguro, sombras que parecen moverse con vida propia.', 0),

-- Derivados del Step_adventure 10
(29, 1, 'Sigues la ruta marcada por los pasos, acercándote a las luces lejanas. Estas parpadean y se mueven como si tuvieran voluntad propia. Un olor a humo y carne quemada llega hasta ti, acelerando tu respiración.', 0),

(30, 1, 'Exploras la zona cercana a la hoguera. Restos de objetos personales flotan levemente en el aire y el bosque parece murmurar con voces apagadas y temblorosas.', 0),

-- Derivados del Step_adventure 11
(31, 1, 'Intentas recuperar la orientación, pero el bosque cambia a cada paso. Árboles se inclinan, senderos desaparecen y el viento lleva murmullos que parecen advertencias antiguas.', 0),

(32, 1, 'Te detienes y escuchas con atención. Un zumbido profundo recorre tu cabeza mientras sientes que el tiempo y el espacio se distorsionan a tu alrededor.', 0),

-- Derivados del Step_adventure 12
(33, 1, 'Te acercas a la figura que atravesó el árbol. Al intentar tocarla, se deshace en humo negro que deja un olor a madera quemada y recuerdos borrosos de tu infancia.', 0),

(34, 1, 'Decides alejarte, pero mientras observas desde lejos, la figura parece moverse sincronizada con tus recuerdos más dolorosos, haciendo que el bosque tiemble levemente.', 0),

-- Derivados del Step_adventure 13
(35, 1, 'Sigues el rastro de babas y descubres una abertura que se hunde en la tierra, como un túnel oscuro y húmedo. Algo se agita dentro, invitándote a entrar con una mezcla de terror y fascinación.', 0),

(36, 1, 'Das la vuelta y tomas un camino lateral. Las ramas parecen moverse para impedirte avanzar, como si el bosque tuviera memoria y conciencia de tus pasos.', 0),

-- Derivados del Step_adventure 14
(37, 1, 'Te acercas a la formación de huesos. A cada paso, el zumbido grave se intensifica y sientes como si los símbolos marcaran un patrón que conocieras en sueños, atrayéndote hacia el centro del claro.', 0),

(38, 1, 'Continúas huyendo por el claro. Cada símbolo parece seguir tu mirada y la tierra tiembla bajo tus pies como si el bosque intentara retenerte.', 0),

-- Derivados del Step_adventure 15
(39, 1, 'Intentas incorporarte y seguir el sendero. Las figuras oscuras con sonrisas exageradas reaparecen saltando entre los árboles, observando cada movimiento con ojos brillantes.', 0),

(40, 1, 'Te detienes unos segundos para observar cómo las figuras desaparecen. La sensación de ser vigilado no disminuye y un frío helado te recorre la espalda.', 0),

-- Derivados del Step_adventure 16
(41, 1, 'Te atreves a acercarte a la sombra que parece invitarte. Cada paso hace que el aire se vuelva pesado y notas que la sombra empieza a tomar forma humanoide, con movimientos imprevisibles.', 0),

(42, 1, 'Decides mantener la distancia y continuar por el sendero. La sombra te sigue con cada movimiento, y la sensación de que algo te acecha aumenta.', 0),

-- Derivados del Step_adventure 17
(43, 1, 'Escalas la raíz y observas que la oscuridad bajo tus pies forma un remolino de sombras que parecen intentar atraparte.', 0),

(44, 1, 'Sigues avanzando por el sendero mientras sientes que cada sombra podría lanzarse sobre ti en cualquier momento.', 0),

-- Derivados del Step_adventure 18
(45, 1, 'Te adentras hacia las formas misteriosas. Parecen danzar en la niebla y el suelo se vuelve líquido bajo tus pies, haciendo que cada paso sea un riesgo calculado.', 0),

(46, 1, 'Retrocedes lentamente, intentando mantener contacto con el sendero seguro, mientras la niebla parece cerrar filas a tu alrededor y figuras fantasmales emergen.', 0),

-- Derivados del Step_adventure 19
(47, 1, 'Sigues acercándote a las voces infantiles. Una sensación de atracción y repulsión se mezcla en tu pecho mientras sientes que el suelo tiembla a cada risa.', 0),

(48, 1, 'Decides mantener distancia, intentando ignorar las voces que se retuercen en el aire y que parecen dibujar caminos imposibles.', 0),

-- Derivados del Step_adventure 20
(49, 1, 'Intentas comunicarte con las figuras mientras permaneces atento. Cada gesto que haces parece ser imitado y deformado, como si tus movimientos fueran un espejo de pesadilla.', 0),

(50, 1, 'Retrocedes hacia la niebla más densa, intentando perderlas de vista. Sus ojos brillan y una risa corta el aire, haciéndote dudar si tu movimiento fue suficiente.', 0);





-- tabla step_options
INSERT INTO Step_options (Id_step_option, Id_step_adventure, Leads_to, Description) VALUES

-- Step_adventure 1
(1, 1, 6,
'Avanzar con decisión por el sendero principal, sin mirar atrás'),

(2, 1, 7,
'Explorar con cautela entre los árboles cercanos'),

(3, 1, 8,
'Detenerte un momento para analizar el entorno y orientarte'),


-- Step_adventure 2
(4, 2, 9,'Continuar adentrándote en el bosque ignorando la sensación de peligro'),

(5, 2, 10,'Investigar los alrededores en busca de pistas o señales'),

(6, 2, 11,'Cambiar de rumbo esperando despistar a quien te observa'),


-- Step_adventure 3
(7, 3, 12,'Seguir el origen de los sonidos para enfrentarte a lo desconocido'),

(8, 3, 13,'Esconderte entre la vegetación y esperar a que pase el peligro'),

(9, 3, 14,'Alejarte rápidamente intentando ganar distancia'),


-- Step_adventure 4
(10, 4, 15,'Elegir el sendero izquierdo, más estrecho y oscuro'),

(11, 4, 16,'Tomar el sendero central, aparentemente más transitado'),

(12, 4, 17,'Avanzar por el sendero derecho, cubierto de raíces y maleza'),


-- Step_adventure 5
(13, 5, 18,'Avanzar a ciegas confiando en tu intuición'),

(14, 5, 19,'Intentar orientarte siguiendo sonidos lejanos'),

(15, 5, 20,'Permanecer inmóvil esperando que la niebla se disipe'),


-- Step_adventure 6
(21, 6, 21, 'Te giras para enfrentar a la masa horripilante y estudias sus movimientos'),
(22, 6, 22, 'Decides acelerar y huir por el sendero mientras el terror te persigue'),


-- Step_adventure 7
(23, 7, 23, 'Te acercas cuidadosamente a los esqueletos llenos de tesoros y exploras su interior'),
(24, 7, 24, 'Decides apartarte y seguir avanzando por el bosque dejando los tesoros atrás'),


-- Step_adventure 8
(25, 8, 25, 'Te aproximas a las huellas de brea para observar de qué criatura se trata'),
(26, 8, 26, 'Das un paso atrás y tratas de ocultarte entre los árboles'),


-- Step_adventure 9
(27, 9, 27, 'Ignoras la sensación y sigues hacia los susurros intentando descubrir su origen'),
(28, 9, 28, 'Decides alejarte de los susurros y buscar un camino más seguro'),


-- Step_adventure 10
(29, 10, 29, 'Sigues la ruta marcada por los pasos y ramas rotas, acercándote a las luces lejanas'),
(30, 10, 30, 'Decides explorar la zona cercana a la hoguera, observando qué provocó la huida'),


-- Step_adventure 11
(31, 11, 31, 'Intentas recuperar tu orientación y avanzar mientras permaneces alerta'),
(32, 11, 32, 'Te detienes a escuchar y analizar los sonidos del bosque antes de continuar'),


-- Step_adventure 12
(33, 12, 33, 'Te aproximas a la figura que atravesó el árbol, intentando entender qué viste'),
(34, 12, 34, 'Decides alejarte y observar desde la distancia, con cuidado de no ser visto'),


-- Step_adventure 13
(35, 13, 35, 'Sigues el rastro de babas, explorando la zona con precaución'),
(36, 13, 36, 'Das la vuelta y buscas un camino seguro lejos del monstruo'),


-- Step_adventure 14
(37, 14, 37, 'Te acercas a la formación de huesos para inspeccionar los símbolos'),
(38, 14, 38, 'Decides continuar huyendo por el claro, evitando la sensación antinatural'),


-- Step_adventure 15
(39, 15, 39, 'Intentas incorporarte rápidamente y seguir el sendero antes de que las figuras te alcancen'),
(40, 15, 40, 'Te detienes unos segundos para observar cómo las figuras desaparecen entre los árboles'),


-- Step_adventure 16
(41, 16, 41, 'Te atreves a acercarte a la sombra que parece invitarte, estudiando con cautela qué es'),
(42, 16, 42, 'Decides mantener la distancia y continuar por el sendero'),


-- Step_adventure 17
(43, 17, 43, 'Escalas la raíz para ponerte a salvo y observar qué hay más adelante'),
(44, 17, 44, 'Sigues avanzando por el sendero, aunque el peligro te rodea'),


-- Step_adventure 18
(45, 18, 45, 'Te adentras hacia las formas misteriosas a pesar del vértigo'),
(46, 18, 46, 'Retrocedes lentamente, buscando mantener contacto con el sendero seguro'),


-- Step_adventure 19
(47, 19, 47, 'Sigues acercándote a las voces infantiles, atraído por la curiosidad'),
(48, 19, 48, 'Decides mantener distancia, intentando evitar lo que no comprendes'),


-- Step_adventure 20
(49, 20, 49, 'Intentas comunicarte con las figuras mientras permaneces atento'),
(50, 20, 50, 'Retrocedes hacia la niebla más densa, intentando perderlas de vista');


