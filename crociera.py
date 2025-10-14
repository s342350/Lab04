from cabine import Cabine, Cabine_animali, Cabine_deluxe
from passeggeri import Passeggeri

class Crociera:
    def __init__(self, nome):
        self.nome=nome
        self.cabine=[]
        self.passeggeri=[]
        """Inizializza gli attributi e le strutture dati"""
        # TODO
    @property
    def nome(self):
        return self.nome
    @nome.setter
    def nome(self, nuovo_nome):
        self.nuovo_nome=nuovo_nome

    """Aggiungere setter e getter se necessari"""
    # TODO

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        try:
            with open(file_path, "r") as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue

                    parts = line.split(",")

                    # CABINA
                    if parts[0].upper().startswith("CAB"):
                        codice = parts[0]
                        n_letti = int(parts[1])
                        ponte = int(parts[2])
                        prezzo = float(parts[3])

                        if len(parts) == 5:
                            # Deluxe o Animali?
                            aggiunto = parts[4]
                            if aggiunto.isdigit():  # CabinaAnimali
                                max_animali = int(aggiunto)
                                cabina = Cabine_animali(codice, n_letti, ponte, prezzo, max_animali)
                            else:  # CabinaDeluxe
                                tipologia = aggiunto
                                cabina = Cabine_deluxe(codice, n_letti, ponte, prezzo, tipologia)
                        else:
                            # Cabina normale
                            cabina = Cabine(codice, n_letti, ponte, prezzo)

                        self.cabine.append(cabina)

                    # PASSEGGERO
                    elif parts[0].upper().startswith("P"):
                        codice = parts[0]
                        nome = parts[1]
                        cognome = parts[2]
                        passeggero = Passeggeri(codice, nome, cognome)
                        self.passeggeri.append(passeggero)


        except FileNotFoundError:
            print('file non trovato')
        # TODO

    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # TODO

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO

