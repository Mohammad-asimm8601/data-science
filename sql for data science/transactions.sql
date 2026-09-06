-- SELECT @@AUTOCOMMIT;
-- SET AUTOCOMMIT = 0;

-- START TRANSACTION;
-- UPDATE student SET age = age + 1 WHERE id = 5;
-- UPDATE student SET age = age - 1 WHERE id = 8;
-- COMMIT
-- ROLLBACK;
SELECT * FROM student;
SET AUTOCOMMIT = 1;