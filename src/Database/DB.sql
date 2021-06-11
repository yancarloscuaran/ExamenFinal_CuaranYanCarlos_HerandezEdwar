-- --------------------------------------------------------
-- Host:                         localhost
-- Versión del servidor:         10.5.8-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Volcando estructura de base de datos para api_student
CREATE DATABASE IF NOT EXISTS `api_student` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `api_student`;

-- Volcando estructura para tabla api_student.academic_spaces
CREATE TABLE IF NOT EXISTS `academic_spaces` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `period_id` int(11) unsigned NOT NULL,
  `name` varchar(255) NOT NULL,
  `semester` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `academic_period_fk` (`period_id`),
  CONSTRAINT `academic_period_fk` FOREIGN KEY (`period_id`) REFERENCES `periods` (`id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla api_student.academic_spaces: ~6 rows (aproximadamente)
/*!40000 ALTER TABLE `academic_spaces` DISABLE KEYS */;
INSERT INTO `academic_spaces` (`id`, `period_id`, `name`, `semester`) VALUES
	(1, 1, 'Electiva', '5'),
	(2, 1, 'Base de Datos II', '5'),
	(3, 2, 'Electiva II', '6'),
	(4, 2, 'Integrales', '6'),
	(5, 2, 'Ingles III', '5'),
	(6, 1, 'Calculo', '5');
/*!40000 ALTER TABLE `academic_spaces` ENABLE KEYS */;

-- Volcando estructura para tabla api_student.assists
CREATE TABLE IF NOT EXISTS `assists` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `session_id` int(11) unsigned DEFAULT NULL,
  `student_id` int(11) unsigned DEFAULT NULL,
  `assistance` tinyint(3) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `assistance_session_fk` (`session_id`),
  KEY `assistance_student_fk` (`student_id`),
  CONSTRAINT `assistance_session_fk` FOREIGN KEY (`session_id`) REFERENCES `sessions` (`id`) ON UPDATE CASCADE,
  CONSTRAINT `assistance_student_fk` FOREIGN KEY (`student_id`) REFERENCES `students` (`id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla api_student.assists: ~3 rows (aproximadamente)
/*!40000 ALTER TABLE `assists` DISABLE KEYS */;
INSERT INTO `assists` (`id`, `session_id`, `student_id`, `assistance`) VALUES
	(1, 1, 1, 1),
	(2, 2, 28, 0),
	(3, 3, 29, 1);
/*!40000 ALTER TABLE `assists` ENABLE KEYS */;

-- Volcando estructura para tabla api_student.performed_activities
CREATE TABLE IF NOT EXISTS `performed_activities` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `academic_space_id` int(11) unsigned DEFAULT NULL,
  `cut` int(11) unsigned NOT NULL,
  `name` varchar(255) NOT NULL,
  `average_cut` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `performed_academic_fk` (`academic_space_id`),
  CONSTRAINT `performed_academic_fk` FOREIGN KEY (`academic_space_id`) REFERENCES `academic_spaces` (`id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla api_student.performed_activities: ~4 rows (aproximadamente)
/*!40000 ALTER TABLE `performed_activities` DISABLE KEYS */;
INSERT INTO `performed_activities` (`id`, `academic_space_id`, `cut`, `name`, `average_cut`) VALUES
	(1, 1, 2, 'exposicion', '3.78'),
	(2, 2, 1, 'consulta', '3.48'),
	(3, 3, 2, 'pronunciacion', '3.8'),
	(5, 5, 1, 'pronunciacion', '4.0');
/*!40000 ALTER TABLE `performed_activities` ENABLE KEYS */;

-- Volcando estructura para tabla api_student.periods
CREATE TABLE IF NOT EXISTS `periods` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `year` year(4) NOT NULL,
  `period` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla api_student.periods: ~4 rows (aproximadamente)
/*!40000 ALTER TABLE `periods` DISABLE KEYS */;
INSERT INTO `periods` (`id`, `year`, `period`) VALUES
	(1, '2021', 1),
	(2, '2021', 2),
	(3, '2022', 1),
	(4, '2022', 2);
/*!40000 ALTER TABLE `periods` ENABLE KEYS */;

-- Volcando estructura para tabla api_student.sessions
CREATE TABLE IF NOT EXISTS `sessions` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `academic_space_id` int(11) unsigned NOT NULL,
  `cut` int(11) NOT NULL,
  `date` varchar(50) NOT NULL,
  `start_time` varchar(50) NOT NULL,
  `end_time` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `session_academic_fk` (`academic_space_id`),
  CONSTRAINT `session_academic_fk` FOREIGN KEY (`academic_space_id`) REFERENCES `academic_spaces` (`id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla api_student.sessions: ~5 rows (aproximadamente)
/*!40000 ALTER TABLE `sessions` DISABLE KEYS */;
INSERT INTO `sessions` (`id`, `academic_space_id`, `cut`, `date`, `start_time`, `end_time`) VALUES
	(1, 1, 1, '10-03-2021', '08:00', '10:00'),
	(2, 2, 1, '11-03-2021', '16:00', '18:00'),
	(3, 3, 2, '12-03-2021', '10:00', '12:00'),
	(4, 4, 2, '13-03-2021', '14:00', '16:00'),
	(5, 2, 3, '06-06-2021', '18:00', '20:00');
/*!40000 ALTER TABLE `sessions` ENABLE KEYS */;

-- Volcando estructura para tabla api_student.students
CREATE TABLE IF NOT EXISTS `students` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `identification` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `surname` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `semester` varchar(50) NOT NULL,
  `period_id` int(11) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `student_period_fk` (`period_id`),
  CONSTRAINT `student_period_fk` FOREIGN KEY (`period_id`) REFERENCES `periods` (`id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla api_student.students: ~3 rows (aproximadamente)
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` (`id`, `identification`, `name`, `surname`, `phone`, `email`, `semester`, `period_id`) VALUES
	(1, '1006789060', 'yan', 'cuaran', '31343443333', 'yan@gmail.com', '5', 1),
	(28, '10232312122', 'carlos', 'imbacuan', '31243243434', 'carlos@gmail.com', '4', 2),
	(29, '10232312123', 'maximo', 'portilla', '31243243434', 'maximo@gmail.com', '3', 1),
	(37, '1007866567', 'alexander', 'mejia', '32156277272', 'alex@gmail.com', '5', 4);
/*!40000 ALTER TABLE `students` ENABLE KEYS */;

-- Volcando estructura para tabla api_student.students_notes
CREATE TABLE IF NOT EXISTS `students_notes` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `performed_activity_id` int(11) unsigned DEFAULT NULL,
  `student_id` int(11) unsigned DEFAULT NULL,
  `note` varchar(50) NOT NULL,
  `observation` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `note_performed_fk` (`performed_activity_id`),
  KEY `note_student_fk` (`student_id`),
  CONSTRAINT `note_performed_fk` FOREIGN KEY (`performed_activity_id`) REFERENCES `performed_activities` (`id`) ON UPDATE CASCADE,
  CONSTRAINT `note_student_fk` FOREIGN KEY (`student_id`) REFERENCES `students` (`id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla api_student.students_notes: ~5 rows (aproximadamente)
/*!40000 ALTER TABLE `students_notes` DISABLE KEYS */;
INSERT INTO `students_notes` (`id`, `performed_activity_id`, `student_id`, `note`, `observation`) VALUES
	(1, 1, 1, '3.5', 'mejorar presentacion'),
	(2, 2, 28, '4.0', 'mejorar ortografia'),
	(3, 3, 29, '4.4', 'muy bien'),
	(4, 1, 1, '3.9', 'falto informacion'),
	(5, 3, 28, '4.0', 'mejorar justificacion'),
	(9, 5, 29, '3.9', 'falto informacion');
/*!40000 ALTER TABLE `students_notes` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
