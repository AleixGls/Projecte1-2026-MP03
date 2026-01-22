DROP SCHEMA IF EXISTS mydb;
CREATE SCHEMA IF NOT EXISTS mydb DEFAULT CHARACTER SET utf8 ;
USE mydb;

-- Tabla Users
CREATE TABLE IF NOT EXISTS Users (
  Id_user INT,
  Username VARCHAR(45),
  Password VARCHAR(45));
  
  -- Tabla Characters
CREATE TABLE IF NOT EXISTS Characters (
  Id_character INT,
  Name VARCHAR(45),
  Description VARCHAR(500));
  
  -- Tabla Adventures
  CREATE TABLE IF NOT EXISTS Adventures (
  Id_adventure INT,
  Name VARCHAR(45),
  Description VARCHAR(500));
  
  -- Tabla Step adventures
  CREATE TABLE IF NOT EXISTS Step_adventures (
  Id_step_adventure INT,
  Id_adventure INT,
  Description VARCHAR(500),
  Is_final_step TINYINT);
  
  -- Tabla Step options
  CREATE TABLE IF NOT EXISTS Step_options (
  Id_step_option INT,
  Id_step_adventure INT,
  Leads_to INT,
  Description VARCHAR(500));
  
  -- Tabla Adventure protagonists
  CREATE TABLE IF NOT EXISTS Adventure_protagonists (
  Id_adventure INT,
  Id_character INT);
  
  -- Tabla Game 
  CREATE TABLE IF NOT EXISTS Games (
  Id_game INT,
  Id_user INT,
  Id_character INT,
  Id_adventure INT,
  Date DATETIME);
  
  -- Tabla Game has step options
  CREATE TABLE IF NOT EXISTS Game_has_choices (
  Id_game INT,
  Id_step_adventure INT,
  Id_step_option INT);
  
  
  