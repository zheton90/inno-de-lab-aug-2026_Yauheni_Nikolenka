# copied the first exercise

class Trainee:
    def __init__(self, name: str, surname: str, score: int = 0, passing_grade: int = 10):
        self.name = name
        self.surname = surname
        self.__score = score
        self.passing_grade = passing_grade

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value: int):
        if type(value) != int:
            raise ValueError(f"Expected value of type int, got {type(value)}")
        elif value < 0:
            raise ValueError(f"The score shouldn't be less than 0!")
        else:
            self.__score = value

    def do_homework(self) -> None:
        """
        This function increases score by 1

        Returns:
            None
        """

        self.score += 1

    def miss_homework(self) -> None:
        """
        This function decreases score by 1

        Returns:
            None
        """

        self.score -= 1

    def visit_lecture(self) -> None:
        """
        This function increases score by 1

        Returns:
            None
        """

        self.score += 1

    def miss_lecture(self) -> None:
        """
        This function decreases score by 1

        Returns:
            None
        """

        self.score -= 1

    def is_passing(self) -> bool:
        """
        This function checks status finishing of course

        Returns:
            bool: true is passing else false
        """

        if self.score >= self.passing_grade:
            return True
        else:
            return False

class HardworkingTrainee(Trainee):

    def do_homework(self) -> None:
        """
        This function increases score by 2 for hardworking students

        Returns:
            None
        """

        self.score += 2

class AuditTrainee(Trainee):

    def is_passing(self) -> bool:
        return True

class Cohort:
    def __init__(self, title: str = "Python Core 2026", trainees: list[Trainee] = []):
        self.title = title
        self.trainees = trainees

    def add_trainee(self, trainee: Trainee) -> None:
        """
        This function adding student to student list
        
        Returns:
            None
        """

        self.trainees.append(trainee)

    def conduct_lecture(self) -> None:
        """
        This function call method visit_lecture for each student

        Returns:
            None
        """

        for trainee in self.trainees:
            trainee.visit_lecture()

    def get_passing_students(self) -> list[Trainee]:
        """
        This function return all students who are passing of course

        Returns:
            list[Trainee]: list of all students who are passing of course
        """

        return [trainee for trainee in self.trainees if trainee.is_passing()]

# 1. Создаем учащихся разных типов
std_trainee = Trainee("Алексей", "Смирнов", score=8, passing_grade=10)
hard_trainee = HardworkingTrainee("Елена", "Петрова", score=8, passing_grade=10)
audit_trainee = AuditTrainee("Дмитрий", "Сидоров", score=0, passing_grade=10)

# 2. Создаем группу и добавляем студентов
cohort = Cohort("Python Advanced")
cohort.add_trainee(std_trainee)
cohort.add_trainee(hard_trainee)
cohort.add_trainee(audit_trainee)

# 3. Проводим лекцию для всей группы (+1 балл всем)
cohort.conduct_lecture()

# 4. Проверяем работу переопределенного ДЗ для трудоголика (+2 балла)
hard_trainee.do_homework()

# 5. Выводим список тех, кто проходит курс
passing_students = cohort.get_passing_students()

print(f"=== УСПЕВАЕМОСТЬ ГРУППЫ '{cohort.title}' ===")
for student in cohort.trainees:
    print(f"{student.name} {student.surname} | Баллы: {student.score} | Проходит: {student.is_passing()}")
print("\nУспешно зачислены на следующий модуль:")
for student in passing_students:
    print(f"- {student.name} {student.surname}")
