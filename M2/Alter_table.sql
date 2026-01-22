USE mydb;


  -- Tabla Users
  ALTER TABLE Users
	ADD PRIMARY KEY (Id_user),
    MODIFY COLUMN username VARCHAR(45) NOT NULL,
    MODIFY COLUMN password VARCHAR(45) NOT NULL,
	ADD UNIQUE (username);
  
  -- Tabla Characters
  ALTER TABLE Characters
	ADD PRIMARY KEY (Id_character),
    MODIFY COLUMN Id_character int NOT NULL,
    MODIFY COLUMN name VARCHAR(45) NOT NULL;
  
  -- Tabla Adventures
  ALTER TABLE Adventures 
	ADD PRIMARY KEY (Id_adventure),
    MODIFY COLUMN Id_adventure int NOT NULL,
    MODIFY COLUMN name VARCHAR(45) NOT NULL;
  
  -- Tabla Step adventures
  ALTER TABLE Step_adventures 
	ADD PRIMARY KEY (Id_step_adventure),
    MODIFY COLUMN Id_step_adventure int NOT NULL,
    MODIFY COLUMN Id_adventure int NOT NULL,
	ADD FOREIGN KEY (Id_adventure) REFERENCES Adventures(Id_adventure); 
  
  -- Tabla Step options
  ALTER TABLE Step_options 
	ADD PRIMARY KEY (Id_step_option),
    MODIFY COLUMN Id_step_option int NOT NULL,
    MODIFY COLUMN Id_step_adventure int NOT NULL,
    MODIFY COLUMN Leads_to int NOT NULL,
    ADD CONSTRAINT Leads_to
	FOREIGN KEY (Leads_to) REFERENCES Step_adventures(Id_step_adventure), 
	ADD CONSTRAINT fk_step_adventure
	FOREIGN KEY (Id_step_adventure) REFERENCES Step_adventures(Id_step_adventure); 
    
  
  -- Tabla Adventure protagonists
  ALTER TABLE Adventure_protagonists 
	ADD PRIMARY KEY (Id_adventure, Id_character),
	MODIFY COLUMN Id_adventure int NOT NULL,
	MODIFY COLUMN Id_character int NOT NULL,
	ADD FOREIGN KEY (Id_adventure) REFERENCES Adventures(Id_adventure),
	ADD FOREIGN KEY (Id_character) REFERENCES Characters(Id_character); 
    
    
    
  -- Tabla Game 
  ALTER TABLE Games     
	ADD PRIMARY KEY (Id_game),
	MODIFY COLUMN Id_game int NOT NULL,
	MODIFY COLUMN Id_character int NOT NULL,
	MODIFY COLUMN Id_user int NOT NULL,
	MODIFY COLUMN Id_adventure int NOT NULL,
	MODIFY COLUMN date datetime NOT NULL,
	ADD FOREIGN KEY (Id_character) REFERENCES Characters(Id_character), 
	ADD FOREIGN KEY (Id_user) REFERENCES Users(Id_user),
	ADD FOREIGN KEY (Id_adventure) REFERENCES Adventures(Id_adventure); 
  
  -- Tabla Game has step options
  ALTER TABLE Game_has_choices 
	MODIFY COLUMN Id_game int NOT NULL,
	MODIFY COLUMN Id_step_adventure int NOT NULL,
    MODIFY COLUMN Id_step_option int NOT NULL,
    ADD FOREIGN KEY (Id_game) REFERENCES Games(Id_game),
    ADD FOREIGN KEY (Id_step_adventure) REFERENCES Step_options(Id_step_adventure),
    ADD FOREIGN KEY (Id_step_option) REFERENCES Step_options(Id_step_option);
  