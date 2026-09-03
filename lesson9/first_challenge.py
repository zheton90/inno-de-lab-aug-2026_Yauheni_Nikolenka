class Trainee:
    def __init__(self, name: str, surname: str, score: int = 0, passing_grade: int = 10):
        self.name = name
        self.surname = surname
        self.__score = score
        self.passing_grade = passing_grade

    @property
    def score(self) -> int:
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

# 1. Создание стажера с начальным баллом 9 и проходным баллом 10
trainee = Trainee(name="Иван", surname="Иванов", score=9, passing_grade=10)

title = "=== ПРОВЕРКА УСПЕВАЕМОСТИ СТАЖЕРА ==="

print(f'{title}')

# 2. Выполнение домашнего задания и проверка статуса
trainee.do_homework()
print(f"Баллы: {trainee.score}, Прошел курс: {trainee.is_passing()}")

# 3. Пропуск лекции и проверка статуса
trainee.miss_lecture()
print(f"Баллы: {trainee.score}, Прошел курс: {trainee.is_passing()}")

# 4. Проверка валидации (попытка задать неверный тип или отрицательное значение)
try:
    trainee.score = -5
except ValueError as e:
    print(f"Ошибка: {e}")
