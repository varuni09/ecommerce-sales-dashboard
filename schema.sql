CREATE DATABASE ecommerce_db;

USE ecommerce_db;

CREATE TABLE sales (
    id INT PRIMARY KEY,
    title VARCHAR(255),
    price FLOAT,
    category VARCHAR(100),
    rating_rate FLOAT,
    rating_count INT,
    quantity_sold INT,
    revenue FLOAT
);