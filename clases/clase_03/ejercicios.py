import marimo

__generated_with = "0.23.3"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Clase 3: Ejercicios Practicos
    ## Construir con Funciones

    En estos ejercicios vas a crear funciones completas con docstrings, type hints, y (en algunos casos) tests.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 1: midi_a_hz

    Escribi una funcion `midi_a_hz(nota_midi)` que convierta un numero de nota MIDI a frecuencia en Hz.

    **Requisitos:**
    - Formula: `f = 440 * 2**((midi - 69) / 12)`
    - Docstring estilo NumPy
    - Type hints
    - Validacion: si `nota_midi` no esta entre 0 y 127, lanzar `ValueError`

    Proba con MIDI 60, 69, 72, y 48.
    """)
    return


@app.cell
def _():
    # EJERCICIO 1: Tu codigo aca
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

    #Ahora lo pruebo:
    for i in [69,71,57]:
        print(f"La nota MIDI número: {i} corresponde al valor de {midi_a_hz(i):>8.2f} Hz.")
    return (midi_a_hz,)


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 2: hz_a_midi

    Escribi la funcion inversa: `hz_a_midi(frecuencia)` que convierta una frecuencia en Hz al numero de nota MIDI mas cercano.

    **Requisitos:**
    - Formula: `midi = round(69 + 12 * log2(freq / 440))`
    - Docstring estilo NumPy
    - Type hints
    - Validacion: si `frecuencia <= 0`, lanzar `ValueError`
    - Necesitas `import math` y usar `math.log2()`

    Proba con 440 Hz, 261.63 Hz, 880 Hz.
    """)
    return


@app.cell
def _():
    # EJERCICIO 2: Tu codigo aca

    import math

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

    for ih in [440, 261.63, 880]:
        print(f"La frecuencia de {ih} Hz, corresponde al MIDI número: {hz_a_midi(ih):>.2f}.")



    return (math,)


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 3: aplicar_fade

    Escribi una funcion `aplicar_fade(signal, tipo="in", duracion_ms=100, fs=44100)` que aplique un fade lineal a una senal.

    **Requisitos:**
    - `tipo` puede ser `"in"` (fade in) o `"out"` (fade out)
    - El fade es **lineal**: multiplica las muestras por un factor que va de 0 a 1 (fade in) o de 1 a 0 (fade out)
    - `duracion_ms` indica cuantos milisegundos dura el fade
    - La funcion retorna una **nueva lista** (no modifica la original)
    - Docstring y type hints

    **Ejemplo de fade in de 4 muestras sobre 8 muestras:**
    ```
    Original: [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    Factores: [0.0, 0.33, 0.67, 1.0, 1.0, 1.0, 1.0, 1.0]
    Resultado:[0.0, 0.33, 0.67, 1.0, 1.0, 1.0, 1.0, 1.0]
    ```
    """)
    return


@app.cell
def _():
    # EJERCICIO 3: Tu codigo aca

    def aplicar_fade(
        signal : list[float] ,
        tipo : str = "in" ,
        duracion_ms : float = 100 ,
        fs : int = 44100
        ) -> list[float]:
        """
        Aplica un fade in/out lineal a una señal.

        Parameters:
        -----------
        signal : list[float]
            Esta lista contiene las muestras de la señal que será modificada.
        tipo : str, puede ser "in" o "out"
            El fade puede realizarse al inicio de la señal (in), o al final (out). Por default esta seleccionada la opción de fade in.
        duracion_ms : float
            La duración del fade en milisegundos, por defecto = 100 ms.
        fs : int
            Frecuencia de sampleo, por defecto 44100 Hz.

        Return:
        -------
        list[float]
            Nueva señal con el fade in/out aplicado.

        Raises:
        -------
        ValueError
            Si tipo no es "in" u "out".
        """
        if tipo not in ("in","out"):
            raise ValueError (f"Tipo no es 'in' ni 'out', el tipo recibido fue {tipo}")
        n_fade = int(fs*duracion_ms/1000)
        n_fade = min(n_fade, len(signal))

        resultado = list(signal)

        for i in range(n_fade):
            factor = i/n_fade if n_fade > 0 else 1.0
            if tipo == "in":
                resultado[i]*=factor
            else:
                resultado[-(i+1)]*= factor
        return resultado

    señal = 20 * [1.0]
    fin= aplicar_fade(señal,"in",0.2)
    fout = aplicar_fade(señal,"out",0.2)

    print(f"Original: {señal}")
    print(f"Fade-in: {fin}")
    print(f"Fade-out: {fout}")


    senal_corta = [1.0] * 8
    fade_in_corto = aplicar_fade(senal_corta, tipo="in", duracion_ms=90.7, fs=44.1)
    print(f"\nFade in (8 muestras): {[f'{s:.3f}' for s in fade_in_corto]}")
    

    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 4: mezclar_senales

    Escribi una funcion `mezclar_senales(*signals, pesos=None)` que mezcle multiples senales.

    **Requisitos:**
    - Recibe un numero variable de senales (listas de floats) via `*signals`
    - Si `pesos` es `None`, todas las senales tienen el mismo peso (1/N)
    - Si `pesos` es una lista, cada senal se multiplica por su peso correspondiente
    - Todas las senales deben tener la misma longitud
    - Retorna la mezcla como una nueva lista
    - Docstring y type hints

    **Ejemplo:**
    ```python
    a = [1.0, 0.5, -0.5]
    b = [0.0, 1.0, 0.0]
    mezclar_senales(a, b)                  # -> [0.5, 0.75, -0.25]
    mezclar_senales(a, b, pesos=[0.8, 0.2]) # -> [0.8, 0.6, -0.4]
    ```
    """)
    return


@app.cell
def _():
    # EJERCICIO 4: Tu codigo aca

    def mezclar_señales(*signals : list[float] , pesos : list[float] | None = None) -> list[float] :
        """
        Esta función mezcla múltiples señales en una sola.
    
        Parameters:
        -----------
        *signals : list[float]
            Todas las señales que van a ser mezcladas en una, serán procesadas, deben tener todas la misma longitud.
        pesos: list[float]
            El peso que cada señal tiene en la sumatoria, si no se le asignan ningún valor, entonces la función toma que son todas del mismo peso.

        Return:
        -------
        list[float]
            Una lista con la sumatoria de las señales.

        Raises:
        -------
        ValueError 
            Si no se proporcionan señales, o no poseen la misma longitud.
        """
        if not signals:
            raise ValueError ("No se proporcionaron señales.")
        longitud = len(signals[0])
        if not all(len(s) == longitud for s in signals):
            raise ValueError ("Las señales proporcionadas no tienen la misma longitud.")

        n = len(signals)

        if pesos is None:
            pesos_efec = [1.0/n]*n
        else:
            if len(pesos) != n:
                raise ValueError ("La cantidad de pesos debe ser igual a la cantidad de señales")
            pesos_efec = pesos

        mezcla = [0.0] * longitud

        for señal, peso in zip(signals,pesos_efec):
            for i in range(longitud):
                mezcla[i]+= señal[i]*peso
        return mezcla

    a = [1.0, 0.5, -0.5]
    b = [0.0, 1.0, 0.0]

    print(f"Las señales puras son: \n{a}\n{b}")
    print(f"Señal mezclada: {mezclar_señales(a,b)}")
    print(f"Señal mezclada con pesos: {mezclar_señales(a,b, pesos = [0.8,0.2])}")


    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 5: info_audio

    Escribi una funcion `info_audio(nombre, sr=44100, **kwargs)` que retorne un string formateado con informacion del archivo de audio.

    **Requisitos:**
    - Siempre muestra nombre y sample rate
    - Cualquier parametro adicional (**kwargs) tambien se muestra
    - Retorna un string (no imprime directamente)
    - Docstring y type hints

    **Ejemplo de uso:**
    ```python
    info_audio("cancion.wav", sr=48000, bits=24, canales=2, artista="Queen")
    ```
    **Resultado:**
    ```
    === cancion.wav ===
    Sample Rate: 48,000 Hz
    bits: 24
    canales: 2
    artista: Queen
    ```
    """)
    return


@app.cell
def _():
    # EJERCICIO 5: Tu codigo aca

    def info_audio(nombre : str , sr : int = 44100 , **kwargs ) -> str :
        """
        Esta función toma todos los elementos y devuelve como un diccionario.

        Parameters:
        -----------
        nombre: str
            Nombre de la canción.
        sr : int
            Sample rate de la canción por defecto 44100 Hz.
        **kwargs:
            Parámetros adicionales a mostrar (ej: bits, canales, artista, etc)

        Return:
        -------
        str
            String formateado con la info dada.
        """
        lineas = [
            f"=== {nombre} ===",
            f"Sample Rate: {sr:,} Hz",
        ]
        for clave, valor in kwargs.items():
            lineas.append(f"{clave}: {valor}")
        return "\n".join(lineas)

    info1 = info_audio("cancion.wav", sr=48000, bits=24, canales=2, artista="Queen")
    print(info1)
    info2 = info_audio("test.wav")
    print(f'\n{info2}')
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 6: Crear un modulo

    Este ejercicio es para hacer **fuera del notebook**, en un archivo separado.

    Crea un archivo llamado `mis_funciones.py` que contenga:

    1. `midi_a_hz(nota_midi)` - del ejercicio 1
    2. `hz_a_midi(frecuencia)` - del ejercicio 2
    3. `calcular_rms(signal)` - calcula el RMS de una lista de muestras

    Cada funcion debe tener docstring y type hints.

    Agrega un bloque `if __name__ == "__main__":` que demuestre el uso de cada funcion.

    Despues de crearlo, verifica que funciona:
    ```bash
    python mis_funciones.py
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    (Este ejercicio se resuelve creando el archivo. En la celda siguiente, simula la importacion.)
    """)
    return


@app.cell
def _():
    # EJERCICIO 6: Simula aca las funciones que pondrias en el modulo
    # y mostra que funcionan
    import mis_funciones


    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 7: Tests para midi_a_hz

    Escribi **3 funciones de test** para la funcion `midi_a_hz` del ejercicio 1.

    Los tests deben seguir el formato de pytest (funciones que empiezan con `test_`):

    1. `test_midi_a_hz_a4()` - verifica que MIDI 69 retorna 440.0
    2. `test_midi_a_hz_octavas()` - verifica que subir 12 semitonos duplica la frecuencia
    3. `test_midi_a_hz_rango_invalido()` - verifica que MIDI -1 o 128 lanza ValueError

    Para el test 3, usa un bloque `try/except`:
    ```python
    try:
        midi_a_hz(-1)
        assert False, "Deberia haber lanzado ValueError"
    except ValueError:
        pass  # OK, se espera el error
    ```

    Ejecuta todos los tests y muestra los resultados.
    """)
    return


@app.cell
def _(midi_a_hz):
    # EJERCICIO 7: Tu codigo aca

    def test_midi_a_hz_a4():
        """Verifica que MIDI 69 retorna 440.0 Hz."""
        assert midi_a_hz(69) == 440.0

    def test_midi_a_hz_octavas():
        """Verifica que subir 12 semitonos duplica la frecuencia."""
        freq_a4 = midi_a_hz(69)
        freq_a5 = midi_a_hz(81)
        assert abs(freq_a5 - 2 * freq_a4) < 0.001, "A5 debe ser el doble de A4"

        freq_a3 = midi_a_hz(57)
        assert abs(freq_a3 - freq_a4 / 2) < 0.001, "A3 debe ser la mitad de A4"

    def test_midi_a_hz_rango_invalido():
        """Verifica que notas fuera de rango lanzan ValueError."""
        # MIDI -1
        try:
            midi_a_hz(-1)
            assert False, "Deberia haber lanzado ValueError para -1"
        except ValueError:
            pass  # OK

        # MIDI 128
        try:
            midi_a_hz(128)
            assert False, "Deberia haber lanzado ValueError para 128"
        except ValueError:
            pass  # OK

    # Ejecutar tests
    tests = [test_midi_a_hz_a4, test_midi_a_hz_octavas, test_midi_a_hz_rango_invalido]

    print("Ejecutando tests de midi_a_hz:\n")
    for test in tests:
        try:
            test()
            print(f"  PASS: {test.__name__}")
        except AssertionError as e:
            print(f"  FAIL: {test.__name__} - {e}")

    print("\nTodos los tests pasaron!")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 8: normalizar con tests

    Escribi una funcion `normalizar(signal)` que normalice una senal al rango [-1, 1].

    **Requisitos:**
    - Encuentra el valor absoluto maximo de la senal
    - Divide todas las muestras por ese valor
    - Si la senal es toda ceros, retorna la senal sin cambios
    - Docstring, type hints

    Ademas, escribi **3 tests**:
    1. `test_normalizar_basico()` - una senal con pico en 0.5 debe tener pico en 1.0
    2. `test_normalizar_ya_normalizada()` - una senal con pico en 1.0 no cambia
    3. `test_normalizar_silencio()` - una senal de ceros retorna ceros

    Ejecuta los tests y muestra resultados.
    """)
    return


@app.cell
def _(math):
    # EJERCICIO 8: Tu codigo aca

    def normalizar(signal: list[float]) -> list[float]:
        """Normaliza una senal al rango [-1, 1].

        Divide todas las muestras por el valor absoluto maximo.
        Si la senal es toda ceros, retorna la senal sin cambios.

        Parameters
        ----------
        signal : list[float]
            Senal de entrada.

        Returns
        -------
        list[float]
            Senal normalizada al rango [-1, 1].
        """
        if not signal:
            return []

        valor_max = max(abs(m) for m in signal)

        if valor_max == 0:
            return list(signal)  # Retornar copia

        return [m / valor_max for m in signal]

    # Tests
    def test_normalizar_basico():
        """Una senal con pico en 0.5 debe tener pico en 1.0."""
        senal = [0.5, -0.3, 0.2, -0.5, 0.4]
        resultado = normalizar(senal)
        assert max(abs(m) for m in resultado) == 1.0
        # Verificar que el primer valor (0.5/0.5 = 1.0)
        assert resultado[0] == 1.0
        assert resultado[3] == -1.0

    def test_normalizar_ya_normalizada():
        """Una senal con pico en 1.0 no cambia."""
        senal = [1.0, -0.5, 0.3, -1.0]
        resultado = normalizar(senal)
        for orig, norm in zip(senal, resultado):
            assert math.isclose(orig, norm), f"{orig} != {norm}"

    def test_normalizar_silencio():
        """Una senal de ceros retorna ceros."""
        senal = [0.0, 0.0, 0.0, 0.0]
        resultado = normalizar(senal)
        assert all(m == 0.0 for m in resultado)

    # Ejecutar tests
    tests_norm = [test_normalizar_basico, test_normalizar_ya_normalizada, test_normalizar_silencio]

    print("Ejecutando tests de normalizar:\n")
    for tes in tests_norm:
        try:
            tes()
            print(f"  PASS: {tes.__name__}")
        except AssertionError as e:
            print(f"  FAIL: {tes.__name__} - {e}")

    # Demo visual
    senal_demo = [0.3, -0.6, 0.2, 0.6, -0.1]
    normalizada = normalizar(senal_demo)
    print(f"\nDemo:")
    print(f"  Original:    {senal_demo}")
    print(f"  Normalizada: {[f'{m:.3f}' for m in normalizada]}")
    print(f"  Pico: {max(abs(m) for m in normalizada):.3f}")
    return


if __name__ == "__main__":
    app.run()
