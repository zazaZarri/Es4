class RegistroVoti:
    def __init__(self):
        self.voti = []

    def aggiungi_voto(self, voto):
        if 0 <= voto <= 10:
            self.voti.append(voto)
            print("Voto aggiunto.")
        else:
            print("Voto non valido")

    def calcola_media(self):
        if not self.voti:
            return 0.0
        return sum(self.voti) / len(self.voti)

if __name__ == "__main__":
    registro = RegistroVoti()
    
    registro.aggiungi_voto(8)
    registro.aggiungi_voto(7)
    registro.aggiungi_voto(9)

    print(f"Media voti: {registro.calcola_media():.2f}")