-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Users` (
  `Id_user` INT NOT NULL,
  `Username` VARCHAR(45) NOT NULL,
  `Password` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Id_user`),
  UNIQUE INDEX `Username_UNIQUE` (`Username` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Characters`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Characters` (
  `Id_character` INT NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `Description` VARCHAR(200) NULL,
  PRIMARY KEY (`Id_character`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Adventure`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Adventure` (
  `Id_adventure` INT NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `Description` VARCHAR(200) NULL,
  PRIMARY KEY (`Id_adventure`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Step_adventure`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Step_adventure` (
  `Id_step_adventure` INT NOT NULL,
  `Id_adventure` INT NOT NULL,
  `Description` VARCHAR(45) NULL,
  `Is_final_step` TINYINT NULL,
  PRIMARY KEY (`Id_step_adventure`),
  INDEX `fk_Step_adventure_Adventure_idx` (`Id_adventure` ASC) VISIBLE,
  CONSTRAINT `fk_Step_adventure_Adventure`
    FOREIGN KEY (`Id_adventure`)
    REFERENCES `mydb`.`Adventure` (`Id_adventure`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Step_option`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Step_option` (
  `Id_step_option` INT NOT NULL,
  `Id_step_adventure` INT NOT NULL,
  `Leads_to` INT NOT NULL,
  `Description` VARCHAR(200) NULL,
  PRIMARY KEY (`Id_step_option`),
  INDEX `fk_Step_option_Step_adventure1_idx` (`Leads_to` ASC) VISIBLE,
  INDEX `fk_Step_option_Step_adventure2_idx` (`Id_step_adventure` ASC) VISIBLE,
  CONSTRAINT `fk_Step_option_Step_adventure1`
    FOREIGN KEY (`Leads_to`)
    REFERENCES `mydb`.`Step_adventure` (`Id_step_adventure`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Step_option_Step_adventure2`
    FOREIGN KEY (`Id_step_adventure`)
    REFERENCES `mydb`.`Step_adventure` (`Id_step_adventure`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Adventure_protagonists`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Adventure_protagonists` (
  `Id_adventure` INT NOT NULL,
  `Id_character` INT NOT NULL,
  PRIMARY KEY (`Id_adventure`, `Id_character`),
  INDEX `fk_Adventure_has_Characters_Characters1_idx` (`Id_character` ASC) VISIBLE,
  INDEX `fk_Adventure_has_Characters_Adventure1_idx` (`Id_adventure` ASC) VISIBLE,
  CONSTRAINT `fk_Adventure_has_Characters_Adventure1`
    FOREIGN KEY (`Id_adventure`)
    REFERENCES `mydb`.`Adventure` (`Id_adventure`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Adventure_has_Characters_Characters1`
    FOREIGN KEY (`Id_character`)
    REFERENCES `mydb`.`Characters` (`Id_character`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Game`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Game` (
  `Id_game` INT NOT NULL,
  `Id_user` INT NOT NULL,
  `Id_character` INT NOT NULL,
  `Id_adventure` INT NOT NULL,
  `Date` DATETIME NOT NULL,
  PRIMARY KEY (`Id_game`),
  INDEX `fk_Session_saves_Users1_idx` (`Id_user` ASC) VISIBLE,
  INDEX `fk_Game_Characters1_idx` (`Id_character` ASC) VISIBLE,
  INDEX `fk_Game_Adventure1_idx` (`Id_adventure` ASC) VISIBLE,
  CONSTRAINT `fk_Session_saves_Users1`
    FOREIGN KEY (`Id_user`)
    REFERENCES `mydb`.`Users` (`Id_user`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Game_Characters1`
    FOREIGN KEY (`Id_character`)
    REFERENCES `mydb`.`Characters` (`Id_character`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Game_Adventure1`
    FOREIGN KEY (`Id_adventure`)
    REFERENCES `mydb`.`Adventure` (`Id_adventure`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Game_has_step_options`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Game_has_step_options` (
  `Game_Id_game` INT NOT NULL,
  `Step_option_Id_step_option` INT NOT NULL,
  INDEX `fk_Step_option_has_Game_Game1_idx` (`Game_Id_game` ASC) VISIBLE,
  INDEX `fk_Step_option_has_Game_Step_option1_idx` (`Step_option_Id_step_option` ASC) VISIBLE,
  CONSTRAINT `fk_Step_option_has_Game_Step_option1`
    FOREIGN KEY (`Step_option_Id_step_option`)
    REFERENCES `mydb`.`Step_option` (`Id_step_option`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Step_option_has_Game_Game1`
    FOREIGN KEY (`Game_Id_game`)
    REFERENCES `mydb`.`Game` (`Id_game`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
