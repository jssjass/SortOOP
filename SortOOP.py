import random
import string

class TextProcessor:
    def __init__(self):
        self.words = []

    def input_data(self):
        choice = input("Выберите способ ввода данных: (1) Ввести вручную (2) Сгенерировать случайно: ")
        if choice == '1':
            text = input("Введите текст: ")
            self.words = self.extract_words(text)
        elif choice == '2':
            self.generate_random_text()
        else:
            print("Неверный выбор. Попробуйте снова.")

    def generate_random_text(self):
        pass

    def extract_words(self, text):
        return text.split()

    def sort_words_by_length(self):
        self.words.sort(key=len)

    def display_results(self):
        print("Отсортированные слова по возрастанию длины:")
        print(self.words)

class ConsoleApp:
    def __init__(self):
        self.processor = TextProcessor()

    def run(self):
        while True:
            print("\nМеню:")
            print("1. Ввод исходных данных")
            print("2. Выполнение алгоритма")
            print("3. Вывод результата")
            print("4. Завершение работы программы")

            choice = input("Выберите действие: ")

            if choice == '1':
                self.processor.input_data()
            elif choice == '2':
                self.processor.sort_words_by_length()
            elif choice == '3':
                self.processor.display_results()
            elif choice == '4':
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    app = ConsoleApp()
    app.run()
