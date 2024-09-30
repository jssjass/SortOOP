import random
import string

# Класс для работы с текстом
class TextProcessor:
    def __init__(self):
        self.words = []  # Список для хранения слов

    def input_data(self):
        """Метод для ввода данных пользователем или случайной генерации"""
        choice = input("Выберите способ ввода данных: (1) Ввести вручную (2) Сгенерировать случайно: ")

        if choice == '1':
            # Ввод данных вручную
            text = input("Введите текст: ")
            self.words = self.extract_words(text)
        elif choice == '2':
            # Генерация случайного текста
            self.generate_random_text()
        else:
            print("Неверный выбор. Попробуйте снова.")

    def generate_random_text(self):
        """Метод, который генерирует случайный текст"""
        length = random.randint(5, 15)
        random_text = ' '.join([''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 8)))
                                 for _ in range(length)])
        print(f"Сгенерированный текст: {random_text}")
        self.words = self.extract_words(random_text)

    def extract_words(self, text):
        """Метод для извлечения слов из текста, учитываем пробелы и знаки препинания"""
        # Удаляем знаки препинания и делим текст на слова
        words = text.translate(str.maketrans('', '', string.punctuation)).split()
        return words

    def sort_words_by_length(self):
        """Метод, который сортирует слова по их длине"""
        # Сортируем слова по длине, если они не пустые
        if self.words:
            self.words.sort(key=len)

    def display_results(self):
        """Метод для отображения результата обработки"""
        if self.words:
            print("Отсортированные слова по возрастанию длины:")
            print(self.words)
        else:
            print("Список слов пуст. Пожалуйста, введите данные.")

# Основной класс для управления приложением
class ConsoleApp:
    def __init__(self):
        self.processor = TextProcessor()  # Экземпляр класса TextProcessor

    def run(self):
        """Главный метод для запуска приложения"""
        while True:
            print("\nМеню:")
            print("1. Ввод исходных данных")
            print("2. Выполнение алгоритма")
            print("3. Вывод результата")
            print("4. Завершение работы программы")

            choice = input("Выберите действие: ")

            if choice == '1':
                # Ввод данных
                self.processor.input_data()
            elif choice == '2':
                # Выполнение алгоритма, если данные введены
                self.processor.sort_words_by_length()
                print("Алгоритм выполнен.")
            elif choice == '3':
                # Вывод результата, если алгоритм выполнен
                self.processor.display_results()
            elif choice == '4':
                # Завершение работы программы
                print("Завершение работы программы.")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    app = ConsoleApp()  # Создание экземпляра приложения
    app.run()  # Запуск приложения
