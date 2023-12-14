-- Scriptto create a table 'unique_id' on MySQL server
CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1,
	name VARCHAR(256),
	UNIQUE KEY unique_id_unique_id (id));
