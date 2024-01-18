-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.
-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;
-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255)
);
-- Finally, we add any records that are needed for the tests to run
INSERT INTO users (name, email, password) VALUES ('name', 'hello@gmail.com', '7a3d5ed42db8e77d91a838e6ad6b45cf68caf8e5aa5afbe0f65a0eceb431cafa');
INSERT INTO users (name, email, password) VALUES ('name', 'hello2@gmail.com', '1e80e852ddd2372d676d70b3e21fcdb64b81296995e834e9bab70f29c78a5a53');
INSERT INTO users (name, email, password) VALUES ('name', 'hello3@gmail.com', '71d18101e1fbe08e981eecc390d2e6c065ad9c1a3475a3cbc97e020efee6c25a');
INSERT INTO users (name, email, password) VALUES ('name', 'hello4@gmail.com', 'c114744195fce958fa1dd33bbfd3c5da7a531da926d695bc316da25db834cf34');
-- testpassword1 (for hello@gmail.com)
-- testpassword2 (for hello2)
-- testpassword3 (for hello3)
-- testpassword4 (for hello4)

-- -- The job of this file is to reset all of our important database tables.
-- -- And add any data that is needed for the tests to run.
-- -- This is so that our tests, and application, are always operating from a fresh
-- -- database state, and that tests don't interfere with each other.
-- -- First, we must delete (drop) all our tables
-- DROP TABLE IF EXISTS users;
-- DROP SEQUENCE IF EXISTS users_id_seq;
-- -- Then, we recreate them
-- CREATE SEQUENCE IF NOT EXISTS users_id_seq;
-- CREATE TABLE users (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(255),
--     email VARCHAR(255),
--     password VARCHAR(255)
-- );
-- -- Finally, we add any records that are needed for the tests to run
-- INSERT INTO users (name, email, password) VALUES ('name', 'hello@gmail.com', '7a3d5ed42db8e77d91a838e6ad6b45cf68caf8e5aa5afbe0f65a0eceb431cafa')
-- INSERT INTO users (name, email, password) VALUES ('name', 'hello2@gmail.com', '1e80e852ddd2372d676d70b3e21fcdb64b81296995e834e9bab70f29c78a5a53')
-- INSERT INTO users (name, email, password) VALUES ('name', 'hello3@gmail.com', '71d18101e1fbe08e981eecc390d2e6c065ad9c1a3475a3cbc97e020efee6c25a')
-- INSERT INTO users (name, email, password) VALUES ('name', 'hello4@gmail.com', 'c114744195fce958fa1dd33bbfd3c5da7a531da926d695bc316da25db834cf34')
-- -- testpassword1 (for hello@gmail.com)
-- -- testpassword2 (for hello2)
-- -- testpassword3 (for hello3)
-- -- testpassword4 (for hello4)

