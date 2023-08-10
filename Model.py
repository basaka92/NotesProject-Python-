import json
from datetime import datetime


class Model:
    def load(self):
        try:
            with open('notes.json', 'r', encoding='utf-8') as file:
                self.notes = dict(json.load(file))
                if len(self.notes) == 0:
                    self.last_id = 1
                else:
                    self.last_id = int(max(self.notes))+1
        except (json.decoder.JSONDecodeError):
            self.notes = {}
            self.last_id = 1
        except (FileNotFoundError):
            self.notes = {}
            self.last_id = 1

    def save(self):
        with open('notes.json', 'w', encoding='utf-8') as file:
            json.dump(self.notes, file)

    def add_notes(self, title, text):
        date = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        self.notes[self.last_id] = {'title': title, 'text': text, 'date': date}
        self.save()

    def edit_note(self, new_title, new_text, key):
        new_date = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        self.notes[key] = {'title': new_title,
                           'text': new_text, 'date': new_date}
        self.save()

    def delete_notes(self, id):
        for key in self.notes.keys():
            if key == id:
                self.notes.pop(key)
                self.update_keys()
                self.save()
                return True
        return False

    def update_keys(self):
        new_dict = {}
        new_id = 1
        for item in self.notes.values():
            new_dict[new_id] = item
            new_id += 1
        self.notes = new_dict

    def get_notes(self):
        return self.notes

    def search_notes(self, date_start, date_end):
        datetime_start = datetime.strptime(
            date_start, "%d/%m/%Y, %H:%M:%S")
        datetime_end = datetime.strptime(
            date_end, "%d/%m/%Y, %H:%M:%S")
        notes_by_date = {}
        for key, item in self.notes.items():
            if datetime_start <= datetime.strptime(dict(item).get('date'), "%d/%m/%Y, %H:%M:%S") and datetime_end >= datetime.strptime(dict(item).get('date'), "%d/%m/%Y, %H:%M:%S"):
                notes_by_date[key] = item
        return notes_by_date

    def check_len(self):
        if len(self.notes) == 0:
            return True
        else:
            return False
