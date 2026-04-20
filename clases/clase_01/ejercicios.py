import marimo

__generated_with = "0.23.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Clase 1: Ejercicios Practicos
    ## El Punto de Partida

    Resuelve cada ejercicio en la celda indicada. Cada ejercicio tiene una descripcion y un espacio para tu codigo.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 1: Total de muestras

    Calcula el **numero total de muestras** para un audio de **3 segundos** grabado a **48000 Hz**.
    Guarda el resultado en una variable llamada `total_muestras` e imprimi el resultado.
    """)
    return


@app.cell
def _():
    # EJERCICIO 1: Tu codigo aca
    # duracion = ...
    # sample_rate = ...
    # total_muestras = ...
    # print(...)

    duracion1 = 3 #segundos
    sample_rate1 = 48000 #Hz
    total_muestras1 = duracion1 * sample_rate1
    print(f"El número total de muestras para un audio de {duracion1} segundos, a una frecuencia de muestreo de {sample_rate1} Hz, es de un total de {total_muestras1:,} muestras.")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 2: Tamano de archivo WAV

    Calcula el **tamano en MB** de un archivo WAV con las siguientes caracteristicas:
    - Estereo (2 canales)
    - Bit depth: 16 bits
    - Sample rate: 44100 Hz
    - Duracion: 5 segundos

    Formula: `tamano_bytes = sample_rate * duracion * canales * (bit_depth / 8)`

    Guarda el resultado en `tamano_mb` e imprimi con 2 decimales.
    """)
    return


@app.cell
def _():
    # EJERCICIO 2: Tu codigo aca
    canales2 = 2 #estereo
    bit_depth2 = 16 #bits
    sample_rate2 = 44100 #Hz
    duracion2 = 5 #segundos

    tamano_bytes = sample_rate2 * duracion2 * canales2 * (bit_depth2/8)
    tamano_mb2 = tamano_bytes/(1024**2)
    print(f"El tamaño en MB de un archivo WAV es de {tamano_mb2:.2f} MB.")
    return (canales2,)


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 3: Convertir segundos a mm:ss

    Dada una duracion en segundos (`duracion_seg = 197`), convertila al formato **mm:ss** usando los operadores `//` y `%`.

    El resultado debe ser un string como `"3:17"`.
    """)
    return


@app.cell
def _():
    # EJERCICIO 3: Tu codigo aca
    # duracion_seg = 197

    duracion_seg3 = 197
    minutos3 = duracion_seg3//60
    segundos3 = duracion_seg3%60
    resultado3 = f"{minutos3}:{segundos3}"
    print(f"El resultado de {duracion_seg3} segundos es {resultado3}.")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 4: Extraer extension de archivo

    Dado el nombre de archivo `nombre = "mi_cancion_final_v2.wav"`, extraer:
    1. La **extension** (sin el punto): `"wav"`
    2. El **nombre sin extension**: `"mi_cancion_final_v2"`

    Usa metodos de strings (`.split()`, slicing, etc.).
    """)
    return


@app.cell
def _():
    # EJERCICIO 4: Tu codigo aca
    # nombre = "mi_cancion_final_v2.wav"
    nombre4 = "mi_cancion_final_v2.wav"

    extension4 = nombre4.split(".")[-1] # separa en lista y elige el ultimo elemento
    nombresinext4 = nombre4.split(".")[0] # separa en lista por . y elige el primer elemento.
    print(f"Nombre del archivo: {nombre4} \nLa extensión es: {extension4} \nEl nombre sin extensión es: {nombresinext4}")

    punto4= nombre4.rfind(".")
    ext4 = nombre4[punto4+1:]
    nomsinext4 = nombre4[:punto4]
    print(f"\nNombre del archivo: {nombre4} \nLa extensión es: {ext4} \nEl nombre sin extensión es: {nomsinext4}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 5: Frecuencia de una nota MIDI

    La formula para convertir un numero de nota MIDI a frecuencia en Hz es:

    $$f = 440 \times 2^{(midi - 69) / 12}$$

    Calcula la frecuencia de las siguientes notas MIDI:
    - **60** (Do central / Middle C)
    - **69** (La 440 / A4)
    - **72** (Do una octava arriba / C5)

    Imprimi cada resultado con 2 decimales.
    """)
    return


@app.cell
def _():
    # EJERCICIO 5: Tu codigo aca

    c = 60
    a4 = 69
    c5 = 72

    fc = 440*2**((c-69)/12)
    fa4 = 440*2**((a4-69)/12)
    fc5 = 440*2**((c5-69)/12)

    print(f"Midi de C = {c}, en frecuencia = {fc:.2f}Hz. \nMidi de A4 = {a4}, en frecuencia = {fa4:.2f}Hz. \nMidi de C5 = {c5}, en frecuencia = {fc5:.2f}Hz.")

    # otra opción sino es:

    #Hago 2 listas:
    midis = [60, 69, 72] # una con las frecuencias del midi
    nommidi = ["C (Do central)","A4 (La 440)","C5 (Do una octava arriba)"] # otra con el nombre de las notas

    #inicio un ciclo for:
    for i,n in zip(midis,nommidi):
        frecuencia5 = 440*2**((i-69)/12)
        print(f"Para la nota: {n} que corresponde al midi número: {i}, la frecuencia que sonará es de: {frecuencia5:.2f} Hz. ")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 6: f-string descriptivo

    Crea las siguientes variables:
    - `titulo = "Bohemian Rhapsody"`
    - `artista = "Queen"`
    - `duracion_seg = 354`
    - `sample_rate = 44100`
    - `bit_depth = 24`

    Usando f-strings, crea un string `info` que muestre:
    ```
    Pista: Bohemian Rhapsody - Queen
    Duracion: 5:54
    Formato: 44,100 Hz / 24 bits
    Total muestras: 15,609,400
    ```
    Imprimi el resultado.
    """)
    return


@app.cell
def _():
    # EJERCICIO 6: Tu codigo aca

    tit6 = "Bohemian Rhapsody"
    art6 = "Queen"
    duraseg6 = 354
    sampler6 = 44100
    bitd6 = 24

    minu6 = duraseg6//60
    seg6 = duraseg6%60
    totmuestras6 = duraseg6*sampler6
    duracion6 = f"{minu6}:{seg6}"

    print(f"""Pista: {tit6} - {art6}
    Duración: {duraseg6} 
    Formato: {sampler6} Hz / {bitd6} 
    Total muestras: {totmuestras6:,}""")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 7: Logica booleana para calidad de audio

    Crea las variables:
    - `sr = 48000` (sample rate)
    - `bits = 24` (bit depth)
    - `canales = 2` (numero de canales)

    Determina (como booleanos):
    1. `es_profesional`: el sample rate es >= 44100 **Y** el bit depth es >= 16
    2. `es_hd`: el sample rate es >= 96000 **O** el bit depth es >= 24
    3. `es_surround`: el numero de canales es > 2
    4. `calidad_ok`: es profesional **Y NO** es surround (estereo profesional)

    Imprimi cada resultado.
    """)
    return


@app.cell
def _(canales2):
    # EJERCICIO 7: Tu codigo aca

    sr7 = 48000
    bit7 = 24
    canales7 = 2

    es_profesional = sr7>=44100 and bit7>=16
    es_hd= sr7>=96000 or bit7>=24
    es_surround = canales2 >2
    calidad_ok = es_profesional ==1 and   es_surround ==0
    print(f"SR: {sr7} BITS: {bit7} CANALES: {canales7}")
    print(f"\nEsprofesional?: {es_profesional} \nEs HD?: {es_hd} \nEs surround?: {es_surround} \nTiene buena calidad?: {calidad_ok}")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio 8: Frecuencia de Nyquist

    La **frecuencia de Nyquist** es la maxima frecuencia que se puede representar con un sample rate dado.
    Se calcula como: `f_nyquist = sample_rate / 2`

    Para los siguientes sample rates, calcula e imprimi la frecuencia de Nyquist:
    - 22050 Hz
    - 44100 Hz
    - 48000 Hz
    - 96000 Hz
    - 192000 Hz

    Imprimi en formato: `"SR: 44100 Hz -> Nyquist: 22050.0 Hz"`
    """)
    return


@app.cell
def _():
    # EJERCICIO 8: Tu codigo aca

    samples8 = [22050 , 44100 , 48000 , 96000 , 192000]
    for sample in samples8:
        f_nyquist = sample/2
        print ( f"Para el sample rate de : {sample} Hz, la frecuencia de Nyquist es de: {f_nyquist} Hz.")
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ### Ejercicio BONUS: Calculadora de latencia

    La **latencia** de un buffer de audio se calcula como:

    $$latencia_{ms} = \frac{buffer\_size}{sample\_rate} \times 1000$$

    Calcula la latencia para las siguientes combinaciones:
    - Buffer: 64, SR: 44100
    - Buffer: 128, SR: 44100
    - Buffer: 256, SR: 48000
    - Buffer: 512, SR: 96000

    Imprimi cada resultado con 2 decimales en formato:
    `"Buffer: 64 @ 44100 Hz -> Latencia: X.XX ms"`
    """)
    return


@app.cell
def _():
    # EJERCICIO BONUS: Tu codigo aca

    buffer = [64, 128, 256, 512]
    samplebonus = [44100, 44100, 48000, 96000]

    for b, s in zip(buffer,samplebonus):
        latencia = b*1000/s
        print(f"Buffer: {b} @ {s} Hz -> Latencia: {latencia:>4.2f} ms.")
    return


if __name__ == "__main__":
    app.run()
