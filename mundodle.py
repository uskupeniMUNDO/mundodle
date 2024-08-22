import random
from datetime import datetime
from clenove import clenove

class Clen:
    def __init__(self, jmeno: str, vek: datetime, oci: str, vzdelani: int, oblibena_hra: str, mesto: str, vztah: bool, nikotin: int, clenstvi: datetime):
        self.jmeno: str = jmeno
        self.vek: datetime = vek
        self.oci: str = oci
        self.vzdelani: int = vzdelani
        self.oblibena_hra: str = oblibena_hra
        self.mesto: str = mesto
        self.vztah: bool = vztah
        self.nikotin: int = nikotin
        self.clenstvi: datetime = clenstvi
    def Vzdelani(self):
        x = ("žádné", "základní", "střední", "vysoké")
        return x[self.vzdelani]
    def Vztah(self):
        if self.vztah:
            return "ano"
        else:
            return "ne"
    def Nikotin(self):
        x = ("ne", "ano", "on and off")
        return x[self.nikotin]

hadanka = random.choice(clenove)






