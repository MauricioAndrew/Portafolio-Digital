import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from collections import Counter
import warnings
warnings.filterwarnings('ignore')

# Configuración de estilo
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

# Cargar los datos
df = pd.read_csv('./IMPAN.csv')

# Limpieza inicial de datos
df['Número de integrantes de la familia'] = df['Número de integrantes de la familia'].str.strip()
df['¿Qué tan importante es la ingesta de pan diariamente? 1 al 5, siendo 5 la más importante'] = pd.to_numeric(
    df['¿Qué tan importante es la ingesta de pan diariamente? 1 al 5, siendo 5 la más importante'], errors='coerce')

# Filtrar solo los que consumen pan
df_pan = df[df['¿Consume pan?'] == 'Si']

print("=== ANÁLISIS EXPLORATORIO DEL CONSUMO DE PAN ===\n")
print(f"Total de encuestados: {len(df)}")
print(f"Consumidores de pan: {len(df_pan)} ({len(df_pan)/len(df)*100:.1f}%)")

# 1. DISTRIBUCIÓN DE INTEGRANTES FAMILIARES
plt.figure(figsize=(10, 6))
fam_dist = df_pan['Número de integrantes de la familia'].value_counts()
plt.pie(fam_dist.values, labels=fam_dist.index, autopct='%1.1f%%', startangle=90)
plt.title('Distribución de Integrantes Familiares entre Consumidores de Pan')
plt.show()

print("\n1. DISTRIBUCIÓN FAMILIAR:")
print("La mayoría de consumidores de pan pertenecen a familias de más de 3 integrantes (56.5%),")
print("seguido por familias de 3 integrantes (29.5%). Esto sugiere que el pan es un alimento")
print("más consumido en hogares con mayor número de personas.\n")

# 2. IMPORTANCIA DEL PAN EN LA DIETA
plt.figure(figsize=(10, 6))
importance = df_pan['¿Qué tan importante es la ingesta de pan diariamente? 1 al 5, siendo 5 la más importante'].value_counts().sort_index()
plt.bar(importance.index, importance.values, color='lightblue')
plt.xlabel('Nivel de Importancia (1-5)')
plt.ylabel('Número de Personas')
plt.title('Importancia del Pan en la Dieta Diaria')
plt.xticks([1, 2, 3, 4, 5])
plt.grid(axis='y', alpha=0.3)
plt.show()

print("\n2. IMPORTANCIA DEL PAN:")
print("El pan tiene una alta valoración en la dieta, con un 38.2% dándole importancia 5 (máxima)")
print("y un 28.1% importancia 4. Solo un 5.7% lo considera poco importante (1-2).")
print("Esto indica que el pan es percibido como un alimento fundamental.\n")

# 3. FRECUENCIA DE CONSUMO
plt.figure(figsize=(10, 6))
freq_dist = df_pan['Con que frecuencia consume pan'].value_counts()
plt.bar(freq_dist.index, freq_dist.values, color='lightgreen')
plt.title('Frecuencia de Consumo de Pan')
plt.ylabel('Número de Personas')
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.show()

print("\n3. FRECUENCIA DE CONSUMO:")
print("El 67.8% consume pan diariamente, mientras que el 23.1% lo hace 3 o más veces por semana.")
print("Solo el 9.1% lo consume ocasionalmente. Esto confirma que el pan es un alimento de consumo habitual.\n")

# 4. PREFERENCIA DE TIPO DE PAN
plt.figure(figsize=(10, 6))
tipo_pan = df_pan['Cuando compra pan, ¿Qué prefiere usted?'].value_counts()
plt.bar(tipo_pan.index, tipo_pan.values, color='orange')
plt.title('Preferencia por Tipo de Pan')
plt.ylabel('Número de Personas')
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.show()

print("\n4. TIPO DE PAN PREFERIDO:")
print("El pan granel es el más preferido (56.9%), seguido del pan preparado (23.1%).")
print("El pan envasado tiene menor preferencia (12.3%), lo que sugiere que los consumidores")
print("prefieren pan fresco sobre el industrializado.\n")

# 5. LUGAR DE COMPRA
plt.figure(figsize=(10, 6))
lugar_compra = df_pan['Al momento de comprar pan, ¿Donde lo realiza?'].value_counts()
plt.bar(lugar_compra.index, lugar_compra.values, color='purple')
plt.title('Lugar Preferido para la Compra de Pan')
plt.ylabel('Número de Personas')
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.show()

print("\n5. LUGAR DE COMPRA:")
print("Las panaderías tradicionales son el lugar preferido (47.7%), seguidas de los")
print("almacenes de barrio (31.6%). Los supermercados tienen una participación menor (18.8%),")
print("lo que indica que los consumidores prefieren establecimientos especializados.\n")

# 6. VARIABLES DE DECISIÓN PARA PAN ENVASADO
plt.figure(figsize=(10, 6))
variables = df_pan['¿Qué variable considera al momento de comprar pan envasado?'].value_counts()
plt.bar(variables.index, variables.values, color='brown')
plt.title('Variables Consideradas al Comprar Pan Envasado')
plt.ylabel('Número de Personas')
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.show()

print("\n6. VARIABLES DE DECISIÓN (PAN ENVASADO):")
print("El precio es la variable más importante (35.8%), seguida de 'Todas las anteriores' (32.1%).")
print("La cantidad (13.2%) y la marca (10.4%) tienen menor peso. El valor nutricional es")
print("el factor menos considerado (8.5%), lo que sugiere que los aspectos económicos")
print("y prácticos priman sobre los saludables.\n")

# 7. RAZONES PARA COMPRAR PAN ENVASADO
plt.figure(figsize=(10, 6))
razones = df_pan['¿Porque razón compra pan envasado principalmente?'].value_counts()
plt.bar(razones.index, razones.values, color='pink')
plt.title('Razones Principales para Comprar Pan Envasado')
plt.ylabel('Número de Personas')
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.show()

print("\n7. RAZONES PARA COMPRAR PAN ENVASADO:")
print("Las 'Ocasiones especiales' son la razón principal (42.3%), seguida de la")
print("'Durabilidad' (21.5%) y 'Rápido de preparar' (18.5%). El sabor tiene menor")
print("importancia (17.7%), lo que refuerza que el pan envasado se ve como una")
print("solución práctica más que gourmet.\n")

# 8. PREFERENCIA DE MARCAS
plt.figure(figsize=(10, 6))
marcas = df_pan['¿Qué marca de pan envasado prefiere?'].value_counts()
plt.bar(marcas.index, marcas.values, color='teal')
plt.title('Marcas de Pan Envasado Preferidas')
plt.ylabel('Número de Personas')
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.show()

print("\n8. MARCAS PREFERIDAS:")
print("Ideal es la marca más preferida (30.4%), seguida de Castaño (22.6%) y Fuch (20.9%).")
print("Las marcas tradicionales de supermercados (15.2%) y Cena (10.9%) tienen menor preferencia.")
print("Esto muestra lealtad a marcas específicas del rubro panadero.\n")

# 9. ANÁLISIS CRUZADO: IMPORTANCIA vs FRECUENCIA
plt.figure(figsize=(12, 8))
cross_table = pd.crosstab(
    df_pan['¿Qué tan importante es la ingesta de pan diariamente? 1 al 5, siendo 5 la más importante'],
    df_pan['Con que frecuencia consume pan']
)
sns.heatmap(cross_table, annot=True, fmt='d', cmap='YlOrRd')
plt.title('Relación entre Importancia del Pan y Frecuencia de Consumo')
plt.show()

print("\n9. RELACIÓN IMPORTANCIA-FRECUENCIA:")
print("Existe una correlación positiva clara: quienes consideran el pan más importante")
print("(4-5) tienden a consumirlo diariamente. Quienes le dan menor importancia (1-2)")
print("lo consumen más ocasionalmente. Esto valida la consistencia en las respuestas.\n")

# 10. PREFERENCIA DE TAMAÑO DE ENVASE
plt.figure(figsize=(10, 6))
tamaño = df_pan['Respecto al tamaño del envase,¿Cuál prefiere?'].value_counts()
plt.bar(tamaño.index, tamaño.values, color='gold')
plt.title('Preferencia de Tamaño de Envase')
plt.ylabel('Número de Personas')
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.show()

print("\n10. TAMAÑO DE ENVASE PREFERIDO:")
print("El envase de 700 gramos es el más popular (47.7%), seguido de 580 gramos (19.2%)")
print("y 250 gramos (15.8%). El de 300 gramos es el menos preferido (17.3%).")
print("Esto sugiere que los consumidores prefieren formatos familiares/económicos.\n")

# 11. FRECUENCIA DE CONSUMO DE PAN ENVASADO
plt.figure(figsize=(10, 6))
freq_env = df_pan['¿Con qué frecuencia consume pan envasado?'].value_counts()
plt.bar(freq_env.index, freq_env.values, color='lightcoral')
plt.title('Frecuencia de Consumo de Pan Envasado')
plt.ylabel('Número de Personas')
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.show()

print("\n11. CONSUMO DE PAN ENVASADO:")
print("La mayoría consume pan envasado solo ocasionalmente (79.4%), mientras que")
print("solo el 12.7% lo consume todos los días. Esto confirma que el pan envasado")
print("es visto como un producto complementario, no como el principal.\n")

# RESUMEN FINAL DE INSIGHTS
print("="*60)
print("PRINCIPALES INSIGHTS Y RECOMENDACIONES")
print("="*60)
print("1. MERCADO MASIVO: El pan es consumido principalmente en familias numerosas")
print("   (>3 integrantes), lo que sugiere estrategias de marketing familiar.")
print("2. PRODUCTO ESENCIAL: Alto nivel de importancia en la dieta (66.3% = 4-5)")
print("   y consumo mayoritariamente diario (67.8%).")
print("3. PREFERENCIA POR FRESCO: Dominio del pan granel (56.9%) sobre envasado (12.3%)")
print("4. CANALES TRADICIONALES: Panaderías (47.7%) y almacenes de barrio (31.6%)")
print("   son los canales preferidos vs supermercados (18.8%).")
print("5. DECISIÓN ECONÓMICA: Precio es la variable principal al comprar pan envasado")
print("6. OCASIONES ESPECIALES: Principal razón para comprar pan envasado (42.3%)")
print("7. LEALTAD DE MARCA: Ideal, Castaño y Fuch dominan el mercado")
print("8. FORMATO FAMILIAR: Preferencia por envases grandes (700g = 47.7%)")
print("9. PAN ENVASADO COMPLEMENTARIO: 79.4% lo consume ocasionalmente")
print("10. CONSISTENCIA: Relación directa entre importancia percibida y frecuencia de consumo")