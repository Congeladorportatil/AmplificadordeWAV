# Amplificador de volumen de archivos .wav

Hace unas semanas me enfrenté a un problema que estaba teniendo: la mesa de mezclas con la que estaba trabajando grababa bajo el audio. Por ello, hize este programa. 
Es posible que te hayas visto con el mismo problema que yo. Si es así, aquí tienes mi solución.

## La base de lo que quería hacer

Estoy aprendiendo por mi cuenta a tocar guitarra española. Llevaba teniendo mucho tiempo la pregunta de como variar el volumen de una onda, ya que variar la frecuencia cambia la nota musical que se está tocando. Fue jugando con la guitarra que me dí cuenta que lo que había que cambiar era la amplitud.

## Mis pasos para utilizarlo


1. Inicia el main.py 
2. Escriba el nombre del archivo. El archivo, debe estar en el mismo directorio, y al escribirlo debe poner el nombre pero sin el ".wav". Por ejemplo, para el archivo "archivo.wav", solo se deberá escribir archivo.
3. Por último, escriba el factor: si es mayor que 1, se amplifica la señal; si es igual a 1 se mantiene la señal; y si es menor que 1, se reduce la amplitud.
4. El archivo resultante será el amplificado. Se llamará igual que el anterior, pero con un añadido del tipo: _amp{factor}. Por ejemplo, si amplifica el archivo del ejemplo anterior, con un factor de 2, el archivo resultante se llamará: archivo_amp2.wav


