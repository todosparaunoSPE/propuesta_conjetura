# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 11:22:16 2025

@author: jperezr
"""

import streamlit as st
import pandas as pd
import sympy as sp


# Estilo de fondo
page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background:
radial-gradient(black 15%, transparent 16%) 0 0,
radial-gradient(black 15%, transparent 16%) 8px 8px,
radial-gradient(rgba(255,255,255,.1) 15%, transparent 20%) 0 1px,
radial-gradient(rgba(255,255,255,.1) 15%, transparent 20%) 8px 9px;
background-color:#282828;
background-size:16px 16px;
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)


# Entrada de Streamlit para el número n
n = st.number_input("Introduce el número n", min_value=2, step=1)

# Función para encontrar números primos en un intervalo dado
def encontrar_primos_en_intervalo(inicio, fin):
    return list(sp.primerange(inicio, fin))

# Definir los cuatro casos según n
if n == 2:
    I1 = [n, 2 * n]
    I2 = I1  # Definir I2 para el caso n == 2
    combinaciones_p_q = [(2, 2)]
    
elif n > 2 and n % 2 == 0:  # Caso 2: n es par y no primo
    I1 = [n // 2, n]
    I2 = [n, 2 * n]
    primos_p = encontrar_primos_en_intervalo(I1[0], I1[1])
    primos_q = encontrar_primos_en_intervalo(I2[0], I2[1])
    combinaciones_p_q = [(p, q) for p in primos_p for q in primos_q if p + q == 2 * n]
    
elif n % 2 == 1 and sp.isprime(n):  # Caso 3: n es impar y primo
    I1 = [n, 2 * n]
    I2 = I1  # En este caso, I2 es igual a I1
    combinaciones_p_q = [(n, n)]
    
else:  # Caso 4: n es impar y no primo
    I1 = [(n - 1) // 2, n - 1]
    I2 = [n, 2 * n]
    primos_p = encontrar_primos_en_intervalo(I1[0], I1[1])
    primos_q = encontrar_primos_en_intervalo(I2[0], I2[1])
    combinaciones_p_q = [(p, q) for p in primos_p for q in primos_q if p + q == 2 * n]

# Preparar los datos para el DataFrame
datos = {
    "n": [n] * len(combinaciones_p_q),
    "Limite Inferior p": [I1[0]] * len(combinaciones_p_q),
    "Limite Superior p": [I1[1]] * len(combinaciones_p_q),
    "Limite Inferior q": [I2[0]] * len(combinaciones_p_q),
    "Limite Superior q": [I2[1]] * len(combinaciones_p_q),
    "# Primo p": [p[0] for p in combinaciones_p_q],
    "# Primo q": [p[1] for p in combinaciones_p_q],
    "Número par 2n": [2 * n] * len(combinaciones_p_q),
    "d(n, p)": [abs(n - p[0]) for p in combinaciones_p_q],  # Calculamos d(n, p)
    "d(q, n)": [abs(q - n) for q in [p[1] for p in combinaciones_p_q]]  # Calculamos d(q, n)
}

# Crear el DataFrame
df = pd.DataFrame(datos)

# Mostrar el DataFrame en Streamlit
st.write(df)
