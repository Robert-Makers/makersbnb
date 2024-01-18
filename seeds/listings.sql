DROP TABLE IF EXISTS listings;
DROP SEQUENCE IF EXISTS listings_id_seq;
CREATE SEQUENCE IF NOT EXISTS listings_id_seq;
CREATE TABLE listings(
    id SERIAL PRIMARY KEY, 
    title varchar(255), 
    description text, 
    price float, 
    user_id int
);

-- ONCE THIS IS READY REFERENECE THE USER ID
INSERT INTO listings (title, description, price, user_id) VALUES ('First Listing', 'This is a description for the first listing', 0.79, 1);
INSERT INTO listings (title, description, price, user_id) VALUES ('Second Listing', 'This is a description for the second listing', 2, 1);
INSERT INTO listings (title, description, price, user_id) VALUES ('Third Listing', 'This is a description for the third listing', 0, 3);
INSERT INTO listings (title, description, price, user_id) VALUES ('Fourth Listing', 'This is a description for the fourth listing', 0, 1);

-- DROP TABLE IF EXISTS listings;
-- DROP SEQUENCE IF EXISTS listings_id_seq;
-- CREATE SEQUENCE IF NOT EXISTS listings_id_seq;
-- CREATE TABLE listings(
--     id SERIAL PRIMARY KEY, title varchar(255), description text, price float, user_id int
-- );

-- -- ONCE THIS IS READY REFERENECE THE USER ID
-- INSERT INTO listings (title, description, price, user_id) VALUES ('First Listing', 'This is a description for the first listing', 0.79, 1);
-- INSERT INTO listings (title, description, price, user_id) VALUES ('Second Listing', 'This is a description for the second listing', 2, 1);
-- INSERT INTO listings (title, description, price, user_id) VALUES ('Third Listing', 'This is a description for the third listing', 0, 1);
-- INSERT INTO listings (title, description, price, user_id) VALUES ('Fourth Listing', 'This is a description for the fourth listing', 0, 1);

