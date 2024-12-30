import soundfile as sf
import numpy as np

def aumentar_volumen(input_file, output_file, factor):
    data, samplerate = sf.read(input_file)
    # Aumentar el volumen
    data_aumentada = data * factor
    # Guardar el nuevo archivo
    sf.write(output_file, data_aumentada, samplerate)

nombre = input("Nombre del archivo:")
archivo_entrada = f"{nombre}.wav"
archivo_salida = f"{nombre}.wav"
factor = input("Factor. \n Se recuerda que si es mayor que 1, se amplifica la señal; si es igual a 1 se mantiene la señal; y si es menor que 1, se reduce la amplitud.")

aumentar_volumen(archivo_entrada, archivo_salida, factor)
