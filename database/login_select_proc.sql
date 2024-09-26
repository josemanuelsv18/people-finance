USE people_finance;

DELIMITER $$
CREATE PROCEDURE userLogin (IN userEmail VARCHAR(100))
BEGIN
    SELECT id_user 
    FROM users 
    WHERE email = userEmail;
END$$
DELIMITER ;