USE people_finance;

DELIMITER $$
CREATE PROCEDURE userVerification (IN userEmail VARCHAR(100))
BEGIN
    SELECT email, password 
    FROM users 
    WHERE email = userEmail;
END$$
DELIMITER ;