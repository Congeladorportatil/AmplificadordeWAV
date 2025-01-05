import soundfile as sf
import numpy as np
import argparse

def aumentar_volumen(input_file, output_file, factor):
    data, samplerate = sf.read(input_file)
    data_aumentada = data * factor
    sf.write(output_file, data_aumentada, samplerate)

def main():
    parser = argparse.ArgumentParser(description="Aumentar o reducir el volumen de un archivo WAV.")
    parser.add_argument("archivo", help="Ruta del .Wav (input)")
    parser.add_argument("factor", type=float, help="Factor de amplificación (>1 para amplificar, 1 para mantener, <1 para reducir)")
    args = parser.parse_args()
    
    archivo_entrada = args.archivo
    nombre_base = archivo_entrada.rsplit(".", 1)[0]
    archivo_salida = f"{nombre_base}_amp{args.factor}.wav"


    print(f"Archivo {archivo_entrada}, factor {args.factor}. Output: {archivo_salida}")
    aumentar_volumen(archivo_entrada, archivo_salida, args.factor)
    print("Done.")

if __name__ == "__main__":
    main()
