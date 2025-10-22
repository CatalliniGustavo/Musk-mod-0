
import json
import os

import pandas as pd


class Lector:
    def __init__(self, path: str):
        self.path = path

    def _comprueba_extension(self, extension):
        file_extension = os.path.splitext(self.path)[1]
        if extension != file_extension:
            raise ValueError("El archivo no tiene la extensión correcta.")
        return True

    def lee_archivo(self):
        pass

    # Devuelve un DataFrame
    @staticmethod
    def convierte_dict_a_csv(data: list[dict]) -> pd.DataFrame:
        df = pd.DataFrame.from_dict(data)
        return df


class LectorCSV(Lector):
    def __init__(self, path: str):
        super().__init__(path)

    def lee_archivo(self, datetime_columns=None) -> pd.DataFrame:
        df_vuelos = None
        if super()._comprueba_extension(".csv"):
            df_vuelos = pd.read_csv(self.path)
            if datetime_columns:
                for col in datetime_columns:
                    df_vuelos[col] = pd.to_datetime(df_vuelos[col])
        return df_vuelos


class LectorJSON(Lector):
    def __init__(self, path: str):
        super().__init__(path)

    def lee_archivo(self):
        if super()._comprueba_extension(".json"):
            with open(self.path, "r", encoding="utf-8") as f:
                list_vuelos = json.load(f)
        return list_vuelos


class LectorTXT(Lector):
    def __init__(self, path: str):
        super().__init__(path)

    def lee_archivo(self):
        if super()._comprueba_extension(".txt"):
            with open(self.path, 'r', encoding='utf-8') as f:
                cabecera = f.readline().strip().split(", ")
                data = []
                for linea in f:
                    valores = linea.replace(' ', '').replace('\n', '').split(',')
                    registro = {cabecera[i]: valores[i] for i in range(len(cabecera)) }
                    data.append(registro)
        return data
