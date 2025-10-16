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
        cabina = None
        for c in self.cabine:
            if c.codice == codice_cabina:
                cabina = c
                break

        # Cerca il passeggero con il codice indicato
        passeggero = None
        for p in self.passeggeri:
            if p.codice == codice_passeggero:
                passeggero = p
                break

        # Verifica che entrambi siano stati trovati
        if cabina is None:
            print(f"Errore: la cabina con codice {codice_cabina} non è stata trovata.")
            return

        if passeggero is None:
            print(f"Errore: il passeggero con codice {codice_passeggero} non è stato trovato.")
            return

        # Verifica se ci sono letti disponibili nella cabina
        numero_occupanti = len(cabina.passeggeri)
        capacita_massima = cabina.n_letti

        if numero_occupanti < capacita_massima:
            # Assegna il passeggero alla cabina
            cabina.passeggeri.append(passeggero)
            passeggero.cabina = cabina
            print(
                f"Il passeggero {passeggero.nome} {passeggero.cognome} è stato assegnato alla cabina {cabina.codice}.")
        else:
            print(f"La cabina {cabina.codice} è piena. Capacità massima: {capacita_massima} letti.")
        # TODO

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        return sorted(self.cabine, key=lambda c: c.prezzo)
        # TODO


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        for p in self.passeggeri:
            if p.cabina is not None:
                cabina_info = f"Cabina: {p.cabina.codice}"
            else:
                cabina_info = "Nessuna cabina assegnata"
            print(f"{p.codice} - {p.nome} {p.cognome} - {cabina_info}")
        # TODO

