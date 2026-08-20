1.	Бизнес-процесс: посещение тренировок. 
In: заявка на тренировку. 
Out: проведённая тренировка, получение оплаты за неё.

2.	Уровень детализации (grain): одна строка факта = одна конкретная тренировка в один конкретный день у конкретного тренера в конкретном городе.

3.	Таблица измерений (Dimensions):
dim_date
date_sk, source_date_id, год, месяц, день, время. 
dim_group_class
group_class_sk, source_group_class_id, название, цена. 
dim_customer
customer_sk, source_customer_id, город, имя, возраст, пол. 
dim_order
order_sk, source_order_id, статус, способ оплаты, тип оплаты. 
dim_coach
coach_sk, source_coach_id, имя, опыт, возраст. 
4.	Таблица фактов (Facts):
- price. Цена на момент продажи.
- discount_amount. Сумма скидки.
- line_total. Итог по позиции.
   5.  схема приложена на скриншоте
   6. Скрипты, которые записаны в порядке выполнения:

-- 1.

CREATE TABLE Dates (
    date_id SERIAL PRIMARY KEY,    
    year VARCHAR(50),    
    month VARCHAR(50),    
    day VARCHAR(50),    
    time TIME 
);

INSERT INTO Dates (year, month, day, time) VALUES 
('2026', 'may', 'Monday', '14:00:00'), 
('2026', 'may', 'Tuesday', '14:00:00'), 
('2026', 'may', 'Wednesday', '14:00:00'), 
('2026', 'may', 'Thursday', '14:00:00'), 
('2026', 'may', 'Friday', '14:00:00'), 
('2026', 'may', 'Saturday', '14:00:00'), 
('2026', 'may', 'Sunday', '14:00:00'); 

CREATE TABLE Coaches (
    coach_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),    
    last_name VARCHAR(50),    
    age INT,    
    experience INT
);

INSERT INTO Coaches (first_name, last_name, age, experience) VALUES 
('Ivan', 'Ivanov', 31, 5), 
('Petr', 'Petrov', 38, 9); 

CREATE TABLE Orderss (
    order_id SERIAL PRIMARY KEY,    
    status VARCHAR(50),    
    way_of_pay VARCHAR(50),    
    type_of_pay VARCHAR(50)   
    );

INSERT INTO Orderss (status, way_of_pay, type_of_pay) VALUES 
('Pending', 'post', 'Cash'), 
('Reject', 'prev', 'Cart'); 

CREATE TABLE Countries (
    country_id SERIAL PRIMARY KEY,    
    country_name VARCHAR(50)
    );

INSERT INTO Countries (country_name) VALUES 
('USA');

CREATE TABLE Categories (
    category_id SERIAL PRIMARY KEY,    
    stage VARCHAR(50)       
);

INSERT INTO Categories (stage) VALUES 
('Beginer'), 
('Hight'), 
('Middle'); 

-- 2.

CREATE TABLE Cities (
    city_id SERIAL PRIMARY KEY,
    country_id INT REFERENCES Countries (country_id),
    city_name VARCHAR(50)    
);

INSERT INTO Cities (country_id, city_name) VALUES 
(1, 'NY'), 
(1, 'LA'); 

CREATE TABLE Class_groups (
    class_group_id SERIAL PRIMARY KEY,    
    category_id INT REFERENCES Categories(category_id),    
    name VARCHAR(50),    
    price INT    
);

INSERT INTO Class_groups (category_id, name, price) VALUES 
(1, 'Yoga', 30), 
(2, 'Pilates', 30); 

-- 3.

CREATE TABLE Class_groups_coach (    
class_groups_coach_id SERIAL PRIMARY KEY,
       class_group_id INT REFERENCES class_groups(class_group_id),
       coach_id INT REFERENCES Coaches(coach_id)
);



INSERT INTO Class_groups_coach (class_group_id, coach_id) VALUES 
(1, 1), 
(1, 2), 
(2, 2); 



CREATE TABLE Customerss (
    customer_id SERIAL PRIMARY KEY,
    city_id INT REFERENCES Cities(city_id),
    full_name VARCHAR(50),    
    age INT,    
    sex VARCHAR(50) 
);

INSERT INTO Customerss (city_id, full_name, age, sex) VALUES 
(1, 'Alex Alexeev', 35, 'M'), 
(2, 'Sveta Svetikova', 32, 'F'), 
(2, 'Sid Sidorov', 22, 'M'); 


-- 4.

CREATE TABLE Trainings (
training_id SERIAL PRIMARY KEY,
date_id INT REFERENCES Dates(date_id),
order_id INT REFERENCES Orderss(order_id),
class_group_id INT REFERENCES Class_groups(class_group_id),
coach_id INT REFERENCES Coaches(coach_id),
customer_id INT REFERENCES Customerss(customer_id),    
country_id INT REFERENCES Countries(country_id),    
price DECIMAL(10, 2), 
discount_amount INT,   
line_total DECIMAL(10, 2) 
);

INSERT INTO Trainings (date_id, order_id, class_group_id, coach_id, customer_id, country_id, price, discount_amount, line_total) VALUES 
(1, 1, 2, 1, 1, 1, 30.00, 0, 30.00), 
(3, 2, 1, 1, 2, 1, 30.00, 10, 27.00), 
(5, 1, 2, 2, 3, 1, 30.00, 0, 30.00), 
(6, 2, 1, 1, 2, 1, 30.00, 20, 24.00), 
(7, 2, 2, 1, 3, 1, 30.00, 10, 27.00); 

7. Примеров аналитических запросов 

Дни с минимальным кол-ом тренировок. Возможно в эти дни стоит сделать какую-то скидку на посещение:
WITH DayStats AS (
    SELECT 
        d.day AS day_name,
        COUNT(t.training_id) AS total_trainings,
        RANK() OVER (ORDER BY COUNT(t.training_id) ASC) AS rank_num
    FROM Dates d
    LEFT JOIN Trainings t ON d.date_id = t.date_id
    GROUP BY d.day
)
SELECT 
    day_name,
    total_trainings
FROM DayStats
WHERE rank_num = 1;

Самый популярный тренер.  Возможно, тренерам нужно ввести градацию. И для тренеров с более высшей градацией цену тренировки делать выше и их оплата соответственно тоже выше:

WITH CoachStats AS (
    SELECT 
        c.coach_id,
        c.first_name,
        c.last_name,
        COUNT(t.training_id) AS total_trainings,
        DENSE_RANK() OVER (ORDER BY COUNT(t.training_id) DESC) AS rank_num
    FROM Coaches c
    LEFT JOIN Trainings t ON c.coach_id = t.coach_id
    GROUP BY c.coach_id, c.first_name, c.last_name
)
SELECT 
    coach_id,
    first_name,
    last_name,
    total_trainings
FROM CoachStats
WHERE rank_num = 1;

Популярность тренировок. Для более популярных тренировок сделать больше окошек:

SELECT 
    g.name AS class_name,
    COUNT(t.training_id) AS total_visits,
    DENSE_RANK() OVER (ORDER BY COUNT(t.training_id) DESC) AS popularity_rank
FROM Class_groups g
LEFT JOIN Trainings t ON g.class_group_id = t.class_group_id
GROUP BY g.class_group_id, g.name
ORDER BY total_visits DESC;


                                                                                                                                 


