USE people_finance;

CREATE PROCEDURE InsertUser(
	IN first_name VARCHAR(50),
    IN surname VARCHAR(50),
    IN email VARCHAR(100),
    IN password VARCHAR(18)
)
AS
	INSERT INTO users (name, surname, email, password, registry_date)
    VALUES(first_name, surname, email, password, CURDATE());
