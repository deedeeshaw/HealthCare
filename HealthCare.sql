Drop database if exists health_db;
create database health_db;

use health_db;

drop table health;

create table health as (
select g.Year, g.All_persons, g.Male, g.Female, e.Less_than_high_school, e.High_school,
e.Some_college, e.Inapplicable as "Less than 18", h.Excellent as Excellent_health, h.Very_good as VG_health, 
h.Good as Good_health, h.Fair as Fair_health, h.Poor as Poor_health
from by_gender g
join by_education e 
on g.Year = e.Year
join by_health h
on g.Year = h.Year);

select * from health;

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

select * from by_difficulty;