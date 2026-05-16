from src.repositories.abstract_repository import AbstractRepository
from src.models.record import Record
from src.utils.file_loader import FileLoader

class RecordRepository(AbstractRepository):

    def __init__(self, file_path: str):
        self._file_path = file_path
        self._records = []

    def load_all(self):
        data = FileLoader.load_csv(self._file_path)
        self._records = []
        for row in data:
            try:
                novo_registro = Record(row["id"], row["name"], row["address"])
                self._records.append(novo_registro)
            except ValueError:
                print(f"Registro inválido ignorado: {{'id': '{row['id']}', 'name': '{row['name']}', 'address': '{row['address']}'}}")
                continue
            
        return self._records

    def search(self, term: str):
        term = term.lower()
        return [
            r for r in self._records
            if term in r.name.lower() or term in r.address.lower()
        ]