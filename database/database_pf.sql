CREATE DATABASE people_finance;

USE people_finance;

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
    FOREIGN KEY (id_user) REFERENCES users(id_user)
);

CREATE TABLE category(
	id_category INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE transactions(
	id_transaction INT PRIMARY KEY AUTO_INCREMENT,
    type ENUM('Income', 'Spending')NOT NULL,
    amount DECIMAL(15,2) NOT NULL,
    tran_date DATETIME NOT NULL,
    description VARCHAR(255),
    id_account INT,
    id_category INT,
    FOREIGN KEY (id_account) REFERENCES accounts(id_account),
    FOREIGN KEY (id_category) REFERENCES category(id_category)
);



CREATE TABLE budget(
	id_budget INT PRIMARY KEY,
    limit_amount DECIMAL(15,2) NOT NULL,
    init_date DATE NOT NULL,
    end_date DATE NOT NULL,
    id_user INT,
    id_category INT,
    FOREIGN KEY (id_user) REFERENCES users(id_user),
    FOREIGN KEY (id_category) REFERENCES category(id_category)
);

CREATE TABLE saving_goal(
	id_saving INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    amount_goal DECIMAL(15,2) NOT NULL,
    amount_save DECIMAL(15,2) NOT NULL,
    init_date DATE NOT NULL,
    goal_date DATE NOT NULL,
    end_date DATE NOT NULL,
    id_user INT,
    FOREIGN KEY (id_user) REFERENCES users(id_user)
);