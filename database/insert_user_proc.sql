USE people_finance;

DELIMITER //
CREATE PROCEDURE userRegister (
	IN nombre VARCHAR(50),
    IN apellido VARCHAR(50),
    IN correo VARCHAR(100),
    IN contrasena VARCHAR(50)
)
BEGIN
	INSERT INTO users (name, surname, email, password, registry_date)
    VALUES (nombre, apellido, correo, contrasena, CURDATE());
END //
DELIMITER ;