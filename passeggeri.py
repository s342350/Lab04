class Passeggeri:
    def __init__(self, codice, nome, cognome):
        self.codice=codice
        self.nome=nome
        self.cognome=cognome
        self.cabina=None

    def __str__(self):
        if self.cabina:
            cabina_info=f"Cabina: {self.cabina.codice}"
        else:
            cabina_info=f"Cabina non assegnata"
        return f"{self.codice}, {self.nome}, {self.cognome} -- {cabina_info}"