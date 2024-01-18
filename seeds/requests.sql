
-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.
-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS requests;
DROP SEQUENCE IF EXISTS requests_id_seq;
-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS requests_id_seq;
CREATE TABLE requests (
    id SERIAL PRIMARY KEY,
    date_from DATE,
    date_to DATE,
    user_id int,
    listing_id int,
    status VARCHAR(20) CHECK(status IN ('approved', 'pending', 'denied'))
    -- constraint fk_user foreign key(user_id) references users(id) on delete cascade,
    -- constraint fk_listing foreign key(listing_id) references listings(id) on delete cascade,
);

-- Finally, we add any records that are needed for the tests to run
-- INSERT INTO requests (date_from, date_to, user_id, listing_id, confirmed) VALUES ('2024-04-03', '2024-04-10', '1', '3', 'true');
-- INSERT INTO requests (date_from, date_to, user_id, listing_id, confirmed) VALUES ('2024-03-20', '2024-03-27', '1', '3', 'true');

-- -- The job of this file is to reset all of our important database tables.
-- -- And add any data that is needed for the tests to run.
-- -- This is so that our tests, and application, are always operating from a fresh
-- -- database state, and that tests don't interfere with each other.
-- -- First, we must delete (drop) all our tables
-- DROP TABLE IF EXISTS requests;
-- DROP SEQUENCE IF EXISTS requests_id_seq;
-- -- Then, we recreate them
-- CREATE SEQUENCE IF NOT EXISTS requests_id_seq;
-- CREATE TABLE requests (
--     id SERIAL PRIMARY KEY,
--     date_from DATE,
--     date_to DATE,
--     user_id int,
--     listing_id int,
--     status VARCHAR(20) CHECK(status IN ('approved', 'pending', 'denied'))
--     -- constraint fk_user foreign key(user_id) references users(id) on delete cascade,
--     -- constraint fk_listing foreign key(listing_id) references listings(id) on delete cascade,
-- );
-- -- Finally, we add any records that are needed for the tests to run
-- INSERT INTO requests (date_from, date_to, user_id, listing_id, confirmed) VALUES ('2024-04-03', '2024-04-10', '1', '3', 'pending');
-- INSERT INTO requests (date_from, date_to, user_id, listing_id, confirmed) VALUES ('2024-03-20', '2024-03-27', '1', '3', 'pending');
-- INSERT INTO requests (date_from, date_to, user_id, listing_id, confirmed) VALUES ('2024-03-20', '2024-03-27', '2', '2', 'pending');
-- INSERT INTO requests (date_from, date_to, user_id, listing_id, confirmed) VALUES ('2024-03-20', '2024-03-27', '3', '1', 'pending');

INSERT INTO requests (date_from, date_to, user_id, listing_id, status) VALUES ('2024-04-03', '2024-04-10', '1', '3', 'pending');
INSERT INTO requests (date_from, date_to, user_id, listing_id, status) VALUES ('2024-03-20', '2024-03-27', '1', '3', 'pending');
INSERT INTO requests (date_from, date_to, user_id, listing_id, status) VALUES ('2024-03-20', '2024-03-27', '2', '2', 'pending');
INSERT INTO requests (date_from, date_to, user_id, listing_id, status) VALUES ('2024-03-20', '2024-03-27', '3', '1', 'pending');