CREATE DATABASE people_finance;

CREATE TABLE users(
	id_user INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    surname VARCHAR(50),
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(50)NOT NULL,
    registry_date DATE NOT NULL
);

CREATE TABLE accounts(
	id_account INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    bank_name VARCHAR(50) NOT NULL,
	type ENUM('Savings', 'Checking') NOT NULL,
    balance DECIMAL(15,2) NOT NULL,
    id_user INT,
    FOREIGN KEY (id_users) REFERENCES users(id_user)
);

CREATE TABLE transactions(
	id_transaction INT PRIMARY KEY AUTO_INCREMENT,
    type ENUM('Income', 'Spending')NOT NULL,
    amount DECIMAL(15,2),
    tran_date DATETIME NOT NULL,
    description VARCHAR(255),
    id_account INT,
);