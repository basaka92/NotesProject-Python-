from Model import Model


class Presenter():
    def __init__(self, view):
        self.model = Model()
        self.view = view

    def load_notes(self):
        self.model.load()

    def get_notes(self):
        return self.model.get_notes()

    def add_notes(self, title, text):
        self.model.add_notes(title, text)

    def delete_notes(self, id):
        return self.model.delete_notes(id)

    def search_notes(self, date_start, date_end):
        return self.model.search_notes(date_start, date_end)

    def edit_note(self, new_title, new_text, key):
        self.model.edit_note(new_title, new_text, key)

    def check_len(self):
        return self.model.check_len()
