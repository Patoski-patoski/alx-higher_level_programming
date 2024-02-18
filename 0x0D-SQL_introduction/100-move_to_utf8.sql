-- a script that converts hbtn_0c_0 database to UTF8
-- (utf8mb4, collate utf8mb4_unicode_ci)

-- Step 1: Convert the database to utf8mb4
ALTER DATABASE hbtn_0c_0
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

-- Step 2: Select the database
USE hbtn_0c_0;

-- Step 3: Convert the table 'first_table' to utf8mb4
ALTER TABLE hbtn_0c_0.first_table
CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Step 4: Convert the field 'name' in 'first_table' to utf8mb4
ALTER TABLE hbtn_0c_0.first_table
MODIFY name VARCHAR(255)
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
