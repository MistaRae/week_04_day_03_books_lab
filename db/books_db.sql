DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    author_id INT REFERENCES authors(id)
);

CREATE TABLE authors(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)

);
