"""
read_data_oo.py

Versión orientada a objetos del lector de datos (.txt, .dat, .csv).

Autor: [Tu nombre]
Curso: Física Computacional
"""

import csv

class DataReader:
    def __init__(self, filename):
        self.filename = filename
        self.data = []

    def read_txt(self):
        """
        Lee un archivo .txt o .dat con números separados por espacios/tabuladores.
        """
        with open(self.filename, "r") as f:
            for line in f:
                if not line.strip() or line.startswith("#"):
                    continue
                row = [float(x) for x in line.split()]
                self.data.append(row)
        return self.data

    def read_csv(self):
        """
        Lee un archivo CSV con valores separados por comas.
        """
        with open(self.filename, newline="") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                try:
                    self.data.append([float(x) for x in row])
                except ValueError:
                    continue  # Ignora filas no numéricas
        return self.data

    def show_data(self, max_rows=5):
        """
        Muestra las primeras filas del dataset.
        """
        print(f"Archivo: {self.filename}")
        for row in self.data[:max_rows]:
            print(row)


# ======================
# Ejemplo de uso
# ======================
def main():
    print("=== Leyendo archivo .txt ===")
    txt_reader = DataReader("datos.txt")
    txt_data = txt_reader.read_txt()
    txt_reader.show_data()

    print("\n=== Leyendo archivo .dat ===")
    dat_reader = DataReader("datos.dat")
    dat_data = dat_reader.read_txt()
    dat_reader.show_data()

    print("\n=== Leyendo archivo .csv ===")
    csv_reader = DataReader("datos.csv")
    csv_data = csv_reader.read_csv()
    csv_reader.show_data()


if __name__ == "__main__":
    main()

