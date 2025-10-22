import datetime
import pandas as pd

from entities.slot import Slot


class Aeropuerto:
    def __init__(self, vuelos: pd.DataFrame, slots: int, t_embarque_nat: int, t_embarque_internat: int):
        self.df_vuelos = vuelos
        self.n_slots = slots
        self.slots = {}
        self.tiempo_embarque_nat = t_embarque_nat
        self.tiempo_embarque_internat = t_embarque_internat

        for i in range(1, self.n_slots + 1):
            self.slots[i] = Slot()

        self.df_vuelos['fecha_despegue'] = pd.NaT
        self.df_vuelos['slot'] = 0

    def calcula_fecha_despegue(self, row) -> pd.Series:
        # diferencia el tiempo de emarque nacional e internacional
        time_offset = self.tiempo_embarque_nat
        if row['tipo_vuelo'] == 'INTERNAT':
            time_offset = self.tiempo_embarque_internat

        if row['retraso'] != '-':
        # Si el retraso es '00:10', añade ':00' para segundos
            retraso_str = row['retraso']
            if len(retraso_str.split(':')) == 2:
                retraso_str += ':00'
            retraso = pd.to_timedelta(retraso_str)
        else:
            retraso = pd.Timedelta(0)
        
        
        row['fecha_despegue'] = row['fecha_llegada'] + retraso + pd.Timedelta(minutes=time_offset)
        return row

    def encuentra_slot(self, fecha_vuelo) -> int:
        slot = -1

        # Recorremos todos los slots del aeropuerto
        for id in self.slots:
            # Obtenemos el tiempo que queda para ese slot esté libre
            time = self.slots[id].slot_esta_libre_fecha_determinada(
                fecha_vuelo)
            # En caso que el slot ya esté libre paramos la busqueda
            if time == datetime.timedelta(0):
                return id
        return slot

    def asigna_slot(self, vuelo) -> pd.Series:
        slot = -1
        fecha_vuelo = vuelo['fecha_llegada']

        # Mientras no se asigne un slot al vuelo, sigue buscando slot disponibles
        while slot == -1:
            # Inicialmente la variable temporal tendrá el mismo valor la fecha de llegada
            vuelo['fecha_llegada'] = fecha_vuelo
            # Buscamos un slots disponible para el vuelo actual
            slot = self.encuentra_slot(vuelo['fecha_llegada'])
            # Actualizamos la variable temporal sumando 10 minutos por si acaso no se ha encontrado un slot
            if slot == -1: 
                fecha_vuelo = fecha_vuelo + datetime.timedelta(minutes=10)
        # Si se ha encontrado un slot, salimos del bucle

        # Calculamos la fecha de despegue
        vuelo = self.calcula_fecha_despegue(vuelo)

        # Asignamos ese vuelo al slot correspondiente dentro del aeropuerto
        self.slots[slot].asigna_vuelo(
            vuelo['id'], vuelo['fecha_llegada'], vuelo['fecha_despegue'])

        print('El vuelo {} con fecha de llegada y despegue {}, {} ha sido asignado al slot {}'.format(
            vuelo['id'], vuelo['fecha_llegada'], vuelo['fecha_despegue'], slot))

        vuelo['slot'] = slot
        return vuelo

    def asigna_slots(self):
        self.df_vuelos.sort_values(by=['fecha_llegada'], inplace=True)
        while len(self.df_vuelos) > 0:
            df_i = self.df_vuelos.iloc[0: self.n_slots, :]
            df_i = df_i.apply(lambda vuelo: self.asigna_slot(vuelo), axis=1)
            self.df_vuelos = self.df_vuelos.iloc[self.n_slots:, :]
