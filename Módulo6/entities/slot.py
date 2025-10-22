import datetime


class Slot:
    def __init__(self):
        self.id = None
        self.fecha_inicial = None
        self.fecha_final = None

    def asigna_vuelo(self, id, fecha_llegada, fecha_despegue):
        self.id = id
        self.fecha_inicial = fecha_llegada
        self.fecha_final = fecha_despegue

    def slot_esta_libre_fecha_determinada(self, fecha):
        # Si fecha_inicial está cargado
        if self.fecha_inicial is not None:
            # Si fecha_final es mayor a fecha devuelve el tiempo de espera
            if (self.fecha_final - fecha) >= datetime.timedelta(0):
                return self.fecha_final - fecha
            else:
                return datetime.timedelta(0)
        else:
            return datetime.timedelta(0)
