SELECT * FROM user.blood;
use user
CREATE TABLE blood (id INTEGER(255),full_name VARCHAR(255), pass_word VARCHAR(255), gender VARCHAR(255), age VARCHAR(255),mobile_number INTEGER(255),email_id VARCHAR(255), city VARCHAR(255), pincode VARCHAR(255),  blood_type VARCHAR(255), months_donation INTEGER(250), number_donations integer(250),volume integer(250) )
LOAD DATA LOCAL INFILE "C:\\Users\\tanus\\Desktop\\BLOOD.csv" INTO TABLE user.blood
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
 show tables;
 select * from blood;
#drop table blood
select count(id) as "O+ donors" from blood where blood_type="O+"
select count(id) as "O- donors" from blood where blood_type="O-"
select count(id) as "A+ donors" from blood where blood_type="A+"
select count(id) as "A- donors" from blood where blood_type="A-"
select count(id) as "AB+ donors" from blood where blood_type="AB+"
select count(id) as "AB- donors" from blood where blood_type="AB-"
select count(id) as "B+ donors" from blood where blood_type="B+"
select count(id) as "B- donors" from blood where blood_type="B-"



