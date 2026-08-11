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
■ PK_Clients: PRIMARY KEY (ClientID) 
■ UQ_ClientFullName: UNIQUE (FirstName, LastName) 

2.	Table Name: Coaches
○ Description: Хранит информацию о тренерах

○ Attributes: 
■ CoachID: INTEGER, PK, NOT NULL, UNIQUE 
■ FirstName: VARCHAR(30), NOT NULL 
■ LastName: VARCHAR(30), NOT NULL 
■ TrainingExperience: INTEGER

○ Constraints: 
■ PK_Coaches: PRIMARY KEY (CoachID) 
■ UQ_CoachFullName: UNIQUE (FirstName, LastName) 

3.	Table Name: GroupClasses
○ Description: Хранит информацию о групповых занятиях

○ Attributes: 
■ GroupClassID: INTEGER, PK, NOT NULL, UNIQUE 
■ ClassName: VARCHAR(30), NOT NULL 

○ Constraints: 
■ PK_Class: PRIMARY KEY (GroupClassID) 
■ UQ_ClassName: UNIQUE (ClassName) 



4.	Table Name: TrainingSlots
○ Description: Таблица для реализации связи многие-ко-многим. Записывает информацию о какой тренер и когда ведёт групповое занятие.

○ Attributes: 
■ SlotID: INTEGER, PK, NOT NULL, UNIQUE 
■ GroupClassID:  INTEGER, FK (REFERENCES GroupClasses), NOT NULL 
■ CoachID: INTEGER, FK (REFERENCES Coaches), NOT NULL 
■ Date:  TIMESTAMP, NOT NULL

○ Constraints: 
■ PK_TrainingSlots: PRIMARY KEY (SlotID) 
■ FK_TrainingSlots_GroupClasses: FOREIGN KEY (GroupClassID) REFERENCES GroupClasses(GroupClassID) 
■ FK_TrainingSlots_Coaches: FOREIGN KEY (CoachID) REFERENCES Coaches(CoachID) 
■ CHK_Dates: CHECK (Date IS NOT NULL OR Date >= CURRENT_DATE) 

5.	Table Name: SignUpForTraining
○ Description: Таблица для реализации связи многие-ко-многим. Записывает информацию о бронировании слотов для тренировок клиентами.

○ Attributes: 
■ TrainingID: INTEGER, PK, NOT NULL, UNIQUE 
■ SlotID:  INTEGER, FK (REFERENCES TrainingSlots), NOT NULL 
■ ClientID: INTEGER, FK (REFERENCES Clients), NOT NULL 
■ NumberOfParticipants:  INTEGER, NOT NULL

○ Constraints: 
■ PK_SignUpForTraining: PRIMARY KEY (TrainingID) 
■ FK_SignUpForTraining_Clients: FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) 
■ FK_SignUpForTraining_TrainingSlots: FOREIGN KEY (SlotID) REFERENCES TrainingSlots(SlotID) 
■ CHK_Participant: CHECK (NumberOfParticipants IS NOT NULL AND NumberOfParticipants >= 4 AND NumberOfParticipants <= 15  ) 

6.	Table Name: CoachesClasses
○ Description: Таблица для реализации связей многие-ко-многим. Хранит информацию о том какой тренер какие занятия может вести.

○ Attributes: 
■ CoachID: INTEGER, FK, NOT NULL 
■ GroupClassID: INTEGER, FK, NOT NULL

○ Constraints: 
■ PK_CoachesClasses: PRIMARY KEY (CoachID, GroupClassID) 
■ FK_CoachesClasses_Coach: FOREIGN KEY (CoachID) REFERENCES Coaches(CoachID)
■ FK_CoachesClasses_GroupClasses: FOREIGN KEY (GroupClassID) REFERENCES GroupClasses(GroupClassID)




Взаимосвязи:
● TrainingSlots и GroupClasses (Один-ко-Многим): Одна групповая тренировка может проводиться несколько раз, но в определённое время может пройти только одна групповая тренировка.
○ TrainingSlots.GroupClassID является внешним ключом, ссылающимся на GroupClasses.GroupClassID. 

● TrainingSlots и Coaches (Один-ко-Многим): Один тренер может проводить несколько групповых занятий, но в определённое время может пройти только одна групповая тренировка.
○ TrainingSlots.CoachID является внешним ключом, ссылающимся на Coaches.CoachID. 

● SignUpForTraining и Clients (Один-ко-Многим): Один клиент может записаться на несколько групповых занятий, но в определённое время может записаться только одну групповую тренировку.
○ SignUpForTraining.ClientID является внешним ключом, ссылающимся на Clients.ClientID. 

● SignUpForTraining и TrainingSlots (Один-ко-Многим): Имеется много тренинг слотов, но в определённое время проходит только одна групповая тренировка.
○ SignUpForTraining.SlotID является внешним ключом, ссылающимся на TrainingSlots.SlotID. 

● Coaches и CoachesClasses (Один-ко-Многим): В таблице CoachClasses может быть несколько одинаковых CoachID но все она ссылаются на одного тренера из таблицы Coaches.
○ CoachesClasses.CoachID является внешним ключом, ссылающимся на Coaches.CoachID

● GroupClasses и CoachesClasses (Один-ко-Многим): В таблице CoachClasses может быть несколько одинаковых GroupClassID но все она ссылаются на одно занятие в таблице GroupClasses.
○ CoachesClasses.GroupClassID является внешним ключом, ссылающимся на GroupClasses.GroupClassID

