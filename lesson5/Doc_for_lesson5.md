1.	Бизнес-процесс: посещение тренировок. 
In: заявка на тренировку. 
Out: проведённая тренировка, получение оплаты за неё.

2.	Уровень детализации (grain): одна строка факта = одна оплаченная тренировка для одного клиента в один конкретный день в рамках определённого заказа.

3.	Таблица измерений (Dimensions):
dim_date
date_sk, source_date_id, год, месяц, день, время. 
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

CREATE TABLE dim_date (
    date_sk SERIAL PRIMARY KEY,    
    year VARCHAR(50),    
    month VARCHAR(50),    
    day VARCHAR(50),    
    time TIME 
);

INSERT INTO dim_date (year, month, day, time) VALUES 
('2026', 'may', 'Monday', '14:00:00'), 
('2026', 'may', 'Tuesday', '14:00:00'), 
('2026', 'may', 'Wednesday', '14:00:00'), 
('2026', 'may', 'Thursday', '14:00:00'), 
('2026', 'may', 'Friday', '14:00:00'), 
('2026', 'may', 'Saturday', '14:00:00'), 
('2026', 'may', 'Sunday', '14:00:00'); 

CREATE TABLE dim_coach (
    coach_sk SERIAL PRIMARY KEY,
    first_name VARCHAR(50),    
    last_name VARCHAR(50),    
    age INT,    
    experience INT
);



INSERT INTO dim_coach (first_name, last_name, age, experience) VALUES 
('Ivan', 'Ivanov', 31, 5), 
('Petr', 'Petrov', 38, 9); 


CREATE TABLE dim_order (
    order_sk SERIAL PRIMARY KEY,    
    status VARCHAR(50),    
    way_of_pay VARCHAR(50),    
    type_of_pay VARCHAR(50)   
    );

INSERT INTO dim_order (status, way_of_pay, type_of_pay) VALUES 
('Pending', 'post', 'Cash'), 
('Reject', 'prev', 'Cart'); 


CREATE TABLE dim_country (
    country_sk SERIAL PRIMARY KEY,    
    country_name VARCHAR(50)
    );

INSERT INTO dim_country (country_name) VALUES 
('USA');

CREATE TABLE dim_category (
    category_sk SERIAL PRIMARY KEY,    
    stage VARCHAR(50)       
);

INSERT INTO dim_category (stage) VALUES 
('Beginer'), 
('Hight'), 
('Middle'); 


-- 2.
CREATE TABLE dim_city (
    city_sk SERIAL PRIMARY KEY,
    country_sk INT REFERENCES dim_country (country_sk),
    city_name VARCHAR(50)    
);

INSERT INTO dim_city (country_sk, city_name) VALUES 
(1, 'NY'), 
(1, 'LA'); 


CREATE TABLE dim_class_group (
    class_group_sk SERIAL PRIMARY KEY,    
    category_sk INT REFERENCES dim_category(category_sk),    
    name VARCHAR(50),    
    price INT    
);

INSERT INTO dim_class_group (category_sk, name, price) VALUES 
(1, 'Yoga', 30), 
(2, 'Pilates', 30); 


-- 3.

CREATE TABLE dim_class_group_coach (    
class_group_coach_sk SERIAL PRIMARY KEY,
       class_group_sk INT REFERENCES dim_class_group(class_group_sk),
       coach_sk INT REFERENCES dim_coach(coach_sk)
);



INSERT INTO dim_class_group_coach (class_group_sk, coach_sk) VALUES 
(1, 1), 
(1, 2), 
(2, 2); 




CREATE TABLE dim_customer (
    customer_sk SERIAL PRIMARY KEY,
    city_sk INT REFERENCES dim_city(city_sk),
    full_name VARCHAR(50),    
    age INT,    
    sex VARCHAR(50) 
);

INSERT INTO dim_customer (city_sk, full_name, age, sex) VALUES 
(1, 'Alex Alexeev', 35, 'M'), 
(2, 'Sveta Svetikova', 32, 'F'), 
(2, 'Sid Sidorov', 22, 'M'); 


-- 4.

CREATE TABLE Trainings (
training_sk SERIAL PRIMARY KEY,
date_sk INT REFERENCES dim_date(date_sk),
order_sk INT REFERENCES dim_order(order_sk),
class_group_coach_sk INT REFERENCES dim_class_group_coach(class_group_coach_sk),
customer_sk INT REFERENCES dim_customer(customer_sk),    
country_sk INT REFERENCES dim_country(country_sk),    
price DECIMAL(10, 2), 
discount_amount INT,   
line_total DECIMAL(10, 2) 
);

INSERT INTO Trainings (date_sk, order_sk, class_group_coach_sk, customer_sk, country_sk, price, discount_amount, line_total) VALUES 
(1, 1, 2, 1, 1, 30.00, 0, 30.00), 
(3, 2, 1, 2, 1, 30.00, 10, 27.00), 
(5, 1, 2, 3, 1, 30.00, 0, 30.00), 
(6, 2, 1, 2, 1, 30.00, 20, 24.00), 
(7, 2, 2, 1, 1, 30.00, 10, 27.00); 

7. Примеров аналитических запросов 

Дни с минимальным кол-ом тренировок. Возможно в эти дни стоит сделать какую-то скидку на посещение:
WITH DayStats AS (
    SELECT 
        d.day AS day_name,
        COUNT(t.training_sk) AS total_trainings,
        RANK() OVER (ORDER BY COUNT(t.training_sk) ASC) AS rank_num
    FROM dim_date d
    LEFT JOIN Trainings t ON d.date_sk = t.date_sk
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
        c.coach_sk,
        c.first_name,
        c.last_name,
        COUNT(t.training_sk) AS total_trainings,
        DENSE_RANK() OVER (ORDER BY COUNT(t.training_sk) DESC) AS rank_num
    FROM dim_class_group_coach cgc
    LEFT JOIN Trainings t ON t.class_group_coach_sk = cgc.class_group_coach_sk
    LEFT JOIN dim_coach c ON c.coach_sk = cgc.coach_sk
    GROUP BY c.coach_sk, c.first_name, c.last_name
)
SELECT 
    coach_sk,
    first_name,
    last_name,
    total_trainings
FROM CoachStats
WHERE rank_num = 1;

Популярность тренировок. Для более популярных тренировок сделать больше окошек:

SELECT 
    g.name AS class_name,
    COUNT(t.training_sk) AS total_visits,
    DENSE_RANK() OVER (ORDER BY COUNT(t.training_sk) DESC) AS popularity_rank
FROM dim_class_group g
LEFT JOIN dim_class_group_coach cgc ON cgc.class_group_sk = g.class_group_sk
LEFT JOIN Trainings t ON cgc.class_group_coach_sk = t. class_group_coach_sk
GROUP BY g.class_group_sk, g.name
ORDER BY total_visits DESC;
