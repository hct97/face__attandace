drop database face_attandance;
create database face_attandance;
use face_attandance;
 
create table teachers (
	id int(10) auto_increment primary key,
    name varchar(30) character set utf8mb4 not  null,
    email varchar(30) not null,
    password varchar(30) not null
) ;

create table subjects (
	id int(10) auto_increment primary key,
    name varchar(30) character set utf8mb4 not null,
    detail nvarchar(100)
);

create table classes (
	id int(10) auto_increment primary key,
    name varchar(20) not null,
    teacherID int(10),
    subjectID int(10),
    foreign key (teacherID) references teachers(id),
    foreign key (subjectID) references subjects(id)
);

create table students (
	studentCode int(10) primary key,
    name varchar(30) character set utf8mb4 not null,
    birthday date,
    email varchar(30) not null
);

create table class_students (
	id int(10) auto_increment primary key,
    classID int(10) not null,
    studentCode int(10) not null,
    foreign key (classID) references classes(id),
    foreign key (studentCode) references students(studentCode)
);

create table classrooms (
	id int(10) auto_increment primary key,
    room varchar(10) not null
);

create table lessons (
	id int(10) auto_increment primary key,
    name varchar(30) character set utf8mb4  not null,
    timeStart datetime,
    timeEnd datetime,
	classroomID int(10) not null,
    classID int(10) not null,
    foreign key (classID) references classes(id),
    foreign key (classroomID) references classrooms(id)
);

insert into teachers(name, email, password) values ("admin", "admin@gmail.com", "123456")

