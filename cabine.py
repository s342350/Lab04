class Cabine:
    def __init__(self, codice, n_letti, ponte, prezzo):
        self.codice=codice
        self.n_letti=n_letti
        self.ponte=ponte
        self.prezzo=prezzo
        self.passeggeri=[]

    def __repr__(self):
        return f"{self.codice}, {self.n_letti} letti, ponte {self.ponte}, {self.prezzo} euro"

class Cabine_deluxe(Cabine):
    def __init__(self, codice, n_letti, ponte, prezzo, tipologia):
        super().__init__(codice, n_letti, ponte, prezzo)
        self.prezzo=prezzo*1.20
        self.tipologia=tipologia

    def __repr__(self):
        return (f"Deluxe - {super().__repr__()}, "
            f"tipologia: {self.tipologia}, sovraprezzo: €{self.prezzo:.2f}")


class Cabine_animali(Cabine):
    def __init__(self, codice, n_letti, ponte, prezzo, max_animali ):
        super().__init__(codice, n_letti, ponte, prezzo)
        self.prezzo=prezzo*(1+0.10*max_animali)
        self.max_animali=max_animali

    def __repr__(self):
        return (f"Animali - {super().__repr__()}, "
                f"max animali: {self.max_animali}, sovraprezzo: €{self.prezzo:.2f}")
