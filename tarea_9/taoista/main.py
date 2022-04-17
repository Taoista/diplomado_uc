CREATE TABLE IF NOT EXISTS movies(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    year INTEGER(4),
    ranking FLOAT(5)
);

CREATE TABLE IF NOT EXISTS actors(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(100),
    last_name VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS directors(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(100),
    last_name VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS movies_actors(
    actor_id INTEGER NOT NULL,
    movie_id INTEGER NOT NULL,
    role VARCHAR(100) NOT NULL,
);

CREATE TABLE IF NOT EXISTS movies_directors(
    director_id INTEGER NOT NULL,
    movie_id INTEGER NOT NULL
);