class Record:
    def __init__(self, record_id: int, name: str, address: str):
        try:
            id_convertido = int(record_id)
        except (ValueError, TypeError):
            raise ValueError("ID deve ser um número inteiro válido.")
        
        if id_convertido < 0:
            raise ValueError(f'ID deve ser inteiro E positivo.')
        
        if not name or name.strip() == '':
            raise ValueError(f'Nome não pode ser vazio.')
        
        if not address or address.strip() == '':
            raise ValueError(f'Endereço não pode ser vazio.')
        
        self._id = id_convertido
        self._name = name.strip()
        self._address = address.strip()

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def address(self):
        return self._address
    
             
    def __repr__(self):
        return f"Record(id={self._id}, name='{self._name}', address='{self._address}')"