import soundfile as sf
import numpy as np

def aumentar_volumen(input_file, output_file, factor):
    data, samplerate = sf.read(input_file)
    data_aumentada = data * factor
    sf.write(output_file, data_aumentada, samplerate)

nombre = input("Nombre del archivo:")
factor = input("Factor. \n Se recuerda que si es mayor que 1, se amplifica la señal; si es igual a 1 se mantiene la señal; y si es menor que 1, se reduce la amplitud.")
archivo_entrada = f"{nombre}.wav"
archivo_salida = f"{nombre}_amp" + f"{factor}.wav"

aumentar_volumen(archivo_entrada, archivo_salida, factor)
