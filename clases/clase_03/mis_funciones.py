import math

def midi_a_hz(nota_midi : int) -> float:
    """Convierte un número de nota de MIDI a frecuencia en Hz.
    
    Parameters:
    ------------
    nota_midi : int
        Número de nota MIDI (0-127)

    Returns:
    ------------
    float
        El valor en Hz al que le corresponde nota_midi

    Raises:
    ------------
    ValueError 
        Si nota_midi no está entre o y 127.
    """
    if not (0 <= nota_midi <=127):
        raise ValueError(f"El valor de nota_midi debe estar entre 0 y 127, y se recibió {nota_midi}")
    return 440 * 2** ((nota_midi-69)/12)

def hz_a_midi(frecuencia : float) -> int:
    """Convierte una frecuencia en Hz al número de nota MIDI más cercano
    
    Parameters:
    -----------
    frecuencia : float
        frecuencia en Hz (Debe ser positiva).
    
    Return:
    -----------
    int
        El valor de la nota midi para la frecuencia dada (Entre 0 y 127).

    Raises:
    -----------
    ValueError
        Si la frecuencia no es positiva
    """
    if frecuencia<=0:
        raise ValueError (f"La frecuencia en Hz debe ser positiva, y la recibida fue {frecuencia}.")
    return round(69+12*math.log2(frecuencia/440))

def calcular_rms(signal):
    """Calcula el valor RMS (Root Mean Square) de una senal.

    El valor RMS es una medida de la "potencia" promedio de una senal.
    Se calcula como la raiz cuadrada del promedio de los cuadrados
    de las muestras.

    Parameters
    ----------
    signal : list[float]
        Senal de entrada como lista de muestras.

    Returns
    -------
    float
        Valor RMS de la senal.

    Examples
    --------
    >>> calcular_rms([1.0, -1.0, 1.0, -1.0])
    1.0
    >>> calcular_rms([0.0, 0.0, 0.0])
    0.0
    """
    if not signal:
        return 0.0
    suma_cuadrados = sum(m ** 2 for m in signal)
    return math.sqrt(suma_cuadrados / len(signal))\
    
if __name__ == "___main____":
    print("La función 'midi_a_hz' devuelve a cual frecuencia en Hz corresponde cada nota de un Midi.")
    print("La función 'hz_a_midi' devuelve a cual nota de un Midi corresponde una frecuencia en Hz.")
    print("La función 'calcular_rms' Calcula el valor rms de una señal.")
    print("=== Demo de mis_funciones.py ===")
    print(f"MIDI 69 -> {midi_a_hz(69)} Hz")
    print(f"MIDI 60 -> {midi_a_hz(60):.2f} Hz")
    print(f"440 Hz -> MIDI {hz_a_midi(440)}")
    print(f"RMS de [0.5, -0.5, 0.5, -0.5] = {calcular_rms([0.5, -0.5, 0.5, -0.5]):.4f}")
