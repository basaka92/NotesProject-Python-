from Presenter import Presenter


class View:
    def __init__(self):
        self.presenter = Presenter(self)
        self.working = True

    def run(self):
        while self.working:
            try:
                self.presenter.load_notes()
                command = input(
                    "\nВведите команду (введите info для отображения списка доступных команда): ")
                self.menu(command)
            except (PermissionError):
                print(
                    "\nНет доступа к файлу текущему файлу JSON! Сохранение изменений невозможно!")

    def info(self):
        print("\nСписок команд:",
              "add - добавить новую заметку",
              "delete - удаление заметки",
              "view - просмотр всех заметок",
              "search - поиск заметок по дате и времени создания/изменения",
              "edit - редактирование заметки",
              "exit - выход из программы", sep="\n")

    def view_notes(self, notes):
        if self.presenter.check_len():
            print("\nНе создано ни одной заметки!")
        else:
            print("\nCписок заметок.")
            for key, item in dict(notes).items():
                print("|\n|")
                print("ID: " + key, "Заголовок: " + dict(item).get("title"),
                      "Текст: " + dict(item).get("text"), "Дата и время создания/изменения: " + dict(item).get("date"), sep="\n")

    def add_notes(self):
        title = input("\nВведите заголовок заметки: ")
        text = input("\nВведите текст заметки: ")
        self.presenter.add_notes(title, text)

    def delete_notes(self):
        if self.presenter.check_len():
            print("\nЗаметки отсутствуют! Добавьте заметки перед тем, как удалять их!")
        else:
            id = input("\nВведите ID заметки, которую хотите удалить: ")
            if self.presenter.delete_notes(id) == True:
                print("\nЗапись успешно удалена!")
            else:
                print("\nЗаписи с таким ID не существует!")

    def search_notes(self):
        if self.presenter.check_len():
            print("\nЗаметки отсутствуют! Добавьте новые заметки перед тем, как искать!")
        else:
            print("\nПоиск заметок по временному промежутку.")
            date_start = input(
                "\nВведите начальную дату в формате 'dd/mm/yy, hh:mm:ss': ")
            date_end = input(
                "\nВведите конечную дату в формате 'dd/mm/yy, hh:mm:ss': ")
            try:
                if len(self.presenter.search_notes(date_start, date_end)) == 0:
                    print("\nПо данному запросу не найдено заметок.")
                else:
                    self.view_notes(
                        self.presenter.search_notes(date_start, date_end))
            except (ValueError):
                print("\nНеверный формат введённых данных!")

    def change_notes(self, notes):
        if self.presenter.check_len():
            print("\nЗаметки отсутствуют! Добавьте заметки прежде чем редактировать их!")
        else:
            id = input("\nВведите ID заметки, которую хотите редактировать: ")
            check = False
            for key in dict(notes).keys():
                if key == id:
                    new_title = input("\nВведите новый заголовок заметки: ")
                    new_text = input("\nВведите новый текст заметки: ")
                    self.presenter.edit_note(new_title, new_text, key)
                    check = True
            if check:
                print("\nЗаметка успешно изменена!")
            else:
                print("\nЗаметки с таким ID не существует!")

    def menu(self, command):
        match command:
            case "info":
                self.info()
            case "view":
                self.view_notes(self.presenter.get_notes())
            case "add":
                self.add_notes()
            case "delete":
                self.delete_notes()
            case "search":
                self.search_notes()
            case "edit":
                self.change_notes(self.presenter.get_notes())
            case "exit":
                self.working = False
            case _:
                print("\nТакой команды не существует!")
