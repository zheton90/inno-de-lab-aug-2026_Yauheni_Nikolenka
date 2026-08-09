Part1: Для данной работы выбран сценарий:  Управление фитнес-клубом. Эта система будет управлять записью клиентов на групповые занятия к тренерам.

Part2:
Идентификация Сущностей и Атрибутов:
1.	Клиенты (Clients)
2.	Тренера (Coachs)
3.	Групповые Занятия (Group Classes)
4.	Слоты Тренировок (Traning Slots)
5.	Запись на Групповое Занятие (Sing up for traning)
Проектирование Таблиц:
1.	Table Name: Clients
○ Description: Хранит информацию о клиентах

○ Attributes: 
■ ClientID: INTEGER, PK, NOT NULL, UNIQUE 
■ FirstName: VARCHAR(30), NOT NULL 
■ LastName: VARCHAR(30), NOT NULL 

○ Constraints: 
■ PK_ Clients: PRIMARY KEY (ClientID) 
■ UQ_AuthorFullName: UNIQUE (FirstName, LastName) 

2.	Table Name: Coachs
○ Description: Хранит информацию о тренерах

○ Attributes: 
■ CoachID: INTEGER, PK, NOT NULL, UNIQUE 
■ FirstName: VARCHAR(30), NOT NULL 
■ LastName: VARCHAR(30), NOT NULL 
■ Traning Experience: INTEGER
■ Group Classes Offered: ARRAY, NOT NULL 


○ Constraints: 
■ PK_ Coachs: PRIMARY KEY (CoachID) 
■ UQ_CoachFullName: UNIQUE (FirstName, LastName) 

3.	Table Name: GroupClasses
○ Description: Хранит информацию о групповых занятиях

○ Attributes: 
■ GroupClassID: INTEGER, PK, NOT NULL, UNIQUE 
■ ClassName: VARCHAR(30), NOT NULL 
■ Class Coach: ARRAY, NOT NULL 


○ Constraints: 
■ PK_ Class: PRIMARY KEY (ClassID) 
■ UQ_ClassName: UNIQUE (ClassName) 

4.	Table Name: TraningSlots
○ Description: Таблица для реализации связи многие-ко-многим. Записывает информацию о какой тренер и когда ведёт групповое занятие.

○ Attributes: 
■ SlotID: INTEGER, PK, NOT NULL, UNIQUE 
■ GroupID:  INTEGER, FK (REFERENCES GroupClasses), NOT NULL 
■ CoachID: INTEGER, FK (REFERENCES Coachs), NOT NULL 
■ Date :  TIMESTAMP, NOT NULL

○ Constraints: 
■ PK_ TraningSlots: PRIMARY KEY (SlotID) 
■ FK_ TraningSlots _ GroupClasses: FOREIGN KEY (GroupClassID) REFERENCES GroupClasses(GroupClassID) 
■ FK_ TraningSlots _ Coachs: FOREIGN KEY (CoachsID) REFERENCES Coachs(CoachsID) 
■ CHK_Dates: CHECK (Date IS NULL OR Date >= CurrentDate) 

5.	Table Name: SingUpForTraning
○ Description: Таблица для реализации связи многие-ко-многим. Записывает информацию о бронировании слотов для тренировок клиентами.

○ Attributes: 
■ TreningID: INTEGER, PK, NOT NULL, UNIQUE 
■ SlotID:  INTEGER, FK (REFERENCES GroupClasses), NOT NULL 
■ ClientD: INTEGER, FK (REFERENCES Coachs), NOT NULL 
■ NumberOfParticipants :  INTEGER, NOT NULL

○ Constraints: 
■ PK_ SingUpForTraning: PRIMARY KEY (TreningID) 
■ FK_ SingUpForTraning _ Clients: FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) 
■ FK_ SingUpForTraning _ TraningSlots: FOREIGN KEY (SlotID) REFERENCES TraningSlots(SlotID) 
■ CHK_Participant: CHECK (Participant IS NOT NULL AND Participant >= 4 AND Participant <= 15  ) 

Взаимосвязи:
● TraningSlot и GroupClass (Один-ко-Многим): Одна групповая тренировка может проводиться несколько раз, но в определённое время может пройти только одна групповая тренировка.
○ TraningSlot.GroupID является внешним ключом, ссылающимся на GroupClass.ClassID. 

	

● TraningSlot и Coach (Один-ко-Многим): Один тренер может проводить несколько групповых занятий, но в определённое время может пройти только одна групповая тренировка.
○ TraningSlot.СoachID является внешним ключом, ссылающимся на Coach.CoachID. 

● SingUpRorTraning и Client (Один-ко-Многим): Один клиент может записаться на  несколько групповых занятий, но в определённое время может записаться только одну групповую тренировку.
○ SingUpRorTraning.СlientID является внешним ключом, ссылающимся на Client.ClientID. 

● SingUpRorTraning и TraningSlot (Один-ко-Многим): Имеется много тренинг слотов, но в определённое время проходит только одна групповая тренировка.
○ SingUpRorTraning.SlotID является внешним ключом, ссылающимся на TraningSlot.SlotID. 
