USE mydb;
-- Tabla adventures
INSERT INTO Adventures (Id_adventure, Name, Description) VALUES
(1, 'El Bosque Maldito', 'Explora un bosque lleno de misterios'),
(2, 'La Torre Oscura', 'Asciende una torre llena de peligros'),
(3, 'La Ciudad Perdida', 'Descubre una civilización olvidada'),
(4, 'El Reino Submarino', 'Aventura bajo el océano');

-- Tabla characters
INSERT INTO Characters (Id_character, Name, Description) VALUES
(1, 'Arin el Guerrero', 'Fuerte y valiente'),
(2, 'Lyra la Maga', 'Sabia y poderosa'),
(3, 'Korin el Explorador', 'Ágil y curioso');


-- Tabla adventure_protagonists
INSERT INTO Adventure_protagonists (Id_adventure, Id_character) VALUES
(1, 1), 
(2, 2), 
(3, 3),
(2, 4); 


