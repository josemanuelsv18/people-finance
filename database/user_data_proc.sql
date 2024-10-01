USE people_finance;

DELIMITER $$
CREATE PROCEDURE userData (IN userId INT)
BEGIN
    SELECT id_user, name, email, registry_date
    FROM users 
    WHERE id_user = userId;
END$$
DELIMITER ;