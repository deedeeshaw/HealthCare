Drop database if exists health_db;
create database health_db;

use health_db;

drop table per_person;

create table health as (
select g.Year, g.All_persons, g.Male, g.Female, e.Less_than_high_school, e.High_school,
e.Some_college, e.Less_than_18, h.Excellent as Excellent_health, h.Very_good as VG_health, 
h.Good as Good_health, h.Fair as Fair_health, h.Poor as Poor_health
from by_gender g
join by_education e 
on g.Year = e.Year
join by_health h
on g.Year = h.Year);

select * from num_health;

create table num_health as (
select ng.Year, ng.All_persons as Per_person, ng.Male as per_Male, ng.Female as per_Female,
ne.Less_than_high_school as per_Less_than_high_school, 
ne.High_school as per_High_school,
ne.Some_college as per_Some_college, 
ne.Inapplicable as "per Less than 18", nh.Excellent as per_Excellent_health,
nh.Very_good as per_VG_health, 
nh.Good as per_Good_health,
nh.Fair as per_Fair_health, 
nh.Poor as per_Poor_health
from no_by_gender ng, 
no_by_education ne, no_by_health nh
Where ng.Year = ne.Year 
and ng.Year = nh.Year
);

create table per_person as (
select
h.Year,
nu.Per_person, nu.per_Male, nu.per_Female,
nu.per_Less_than_high_school, 
nu.per_High_school,
nu.per_Some_college, 
nu.per_Less_than_18, nu.per_Excellent_health,
nu.per_VG_health, 
nu.per_Good_health,
nu.per_Fair_health, 
nu.per_Poor_health,
h.All_persons, h.Male, h.Female,
h.Less_than_high_school, 
h.High_school,
h.Some_college,
h.Less_than_18, 
h.Excellent_health,
h.VG_health, 
h.Good_health,
h.Fair_health, h.Poor_health
from
health h, num_health nu
where h.Year = nu.Year);

select * from num_health
;

Update per_person
SET 
Per_person = All_persons/Per_person,
per_Male = Male/per_Male,
per_Female = Female/per_Female,
per_Less_than_high_school = Less_than_high_school/per_Less_than_high_school,
per_High_school=High_school/per_High_school,
per_Some_college=Some_college/per_Some_college,
per_Less_than_18=Less_than_18/per_Less_than_18,
per_Excellent_health=Excellent_health/per_Excellent_health,
per_VG_health=VG_health/per_VG_health,
per_Good_health=Good_health/per_Good_health,
per_Fair_health=Fair_health/per_Fair_health,
per_Poor_health=Poor_health/per_Poor_health
;

ALTER TABLE per_person
DROP column All_persons, 
drop column Male, 
drop column Female, 
drop column Less_than_high_school, drop column High_school, 
drop column Some_college, drop column Less_than_18,
drop column Excellent_health, drop column VG_health, 
drop column Good_health, drop column Fair_health, drop column Poor_health
;

/*
Alter table per_person
add column exp_pp int,
add column exp_male int,
add column exp_female int,
add column exp_less_than_high_school int,
add column exp_high_school int,
add column exp_some_college int,
add column exp_less_than_18 int,
add column exp_ex_health int,
add column exp_vg_health int,
add column exp_good_health int,
add column exp_fair_health int,
add column exp_poor_health int;

Update per_person
SET 
exp_pp = All_persons/Per_person,
exp_male = Male/per_Male,
exp_female = Female/per_Female,
exp_less_than_high_school = Less_than_high_school/per_Less_than_high_school,
exp_high_school=High_school/per_High_school,
exp_some_college=Some_college/per_Some_college,
exp_less_than_18=Less_than_18/per_Less_than_18,
exp_ex_health=Excellent_health/per_Excellent_health,
exp_vg_health=VG_health/per_VG_health,
exp_good_health=Good_health/per_Good_health,
exp_fair_health=Fair_health/per_Fair_health,
exp_poor_health=Poor_health/per_Poor_health
;
*/


-- PROBLEM ID TABLE
create table problem (
ProblemID int not null,
primary key (ProblemID), 
Problem varchar (50)
);


insert into problem (
ProblemID, Problem)
Values 
(27, "Celiac Disease"),
(6, "Breast Cancer"),
(28, "Crohn's Disease"),
(18, "Depression"),
(3, "Gout"),
(2, "High Blood Pressure"),
(1, "High Cholestrol"),
(9, "Prostrate Cancer"),
(16, "Diabetes Type 2"),
(15, "Rhematoid Arthiritis"),
(12, "Stomach Cancer"),
(34, "Ulcers"),
(5, "Vitamin D Deficiency");

select * from problem;

