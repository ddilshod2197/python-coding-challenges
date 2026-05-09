class ArxitektorDasturchi:
    def __init__(self, ismi, tajriba):
        self.ismi = ismi
        self.tajriba = tajriba

    def google_tajribasi(self):
        return self.tajriba.get('google', None)

    def meta_tajribasi(self):
        return self.tajriba.get('meta', None)

    def is_tajribali(self):
        return self.google_tajribasi() == 'Google' and self.meta_tajribasi() == 'Meta'

    def is_100_percent_shartlarga_javob(self):
        return self.is_tajribali() and self.ismi == 'ArxitektorDasturchi'

class Masala:
    def __init__(self, arxitektor_dasturchi):
        self.arxitektor_dasturchi = arxitektor_dasturchi

    def o_tinchuqur_diqqat(self):
        return self.arxitektor_dasturchi.is_100_percent_shartlarga_javob()

arxitektor_dasturchi = ArxitektorDasturchi('ArxitektorDasturchi', {'google': 'Google', 'meta': 'Meta'})
masala = Masala(arxitektor_dasturchi)
print(masala.o_tinchuqur_diqqat())
