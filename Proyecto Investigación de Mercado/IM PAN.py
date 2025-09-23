import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime

# Configuración de estilo
plt.style.use('default')
sns.set_palette("husl")
plt.rcParams['figure.figsize'] = (12, 8)

# Cargar los datos
df = pd.read_csv('./IMPAN.csv')

# Mostrar información básica
print("=" * 60)
print("INFORMACIÓN BÁSICA DEL DATASET")
print("=" * 60)
print(f"Total de encuestas: {len(df)}")
print(f"Total de columnas: {len(df.columns)}")
print("\nColumnas disponibles:")
for i, col in enumerate(df.columns, 1):
    print(f"{i}. {col}")

print("\n" + "=" * 60)
print("PRIMERAS FILAS DEL DATASET")
print("=" * 60)
print(df.head())

print("\n" + "=" * 60)
print("INFORMACIÓN DE TIPOS DE DATOS Y VALORES NULOS")
print("=" * 60)
print(df.info())

print("\n" + "=" * 60)
print("ESTADÍSTICAS DESCRIPTIVAS")
print("=" * 60)
print(df.describe(include='all'))

# Limpieza y preprocesamiento
print("\n" + "=" * 60)
print("VALORES NULOS POR COLUMNA")
print("=" * 60)
print(df.isnull().sum())

# Limpiar datos: eliminar filas donde no consumen pan (ya que no completaron la encuesta)
df_clean = df[df['¿Consume pan?'] == 'Si'].copy()

print(f"\nEncuestas después de filtrar solo consumidores de pan: {len(df_clean)}")

# Análisis de variables categóricas clave
print("\n" + "=" * 60)
print("ANÁLISIS DE VARIABLES CLAVE")
print("=" * 60)

# 1. Consumo de pan
print("\n1. DISTRIBUCIÓN DE CONSUMO DE PAN:")
print(df_clean['¿Consume pan?'].value_counts())

# 2. Número de integrantes de la familia
print("\n2. DISTRIBUCIÓN DE INTEGRANTES FAMILIARES:")
print(df_clean['Número de integrantes de la familia'].value_counts())

# 3. Importancia del pan (escala 1-5)
print("\n3. IMPORTANCIA DE LA INGESTA DE PAN (1-5):")
print(df_clean['¿Qué tan importante es la ingesta de pan diariamente? 1 al 5, siendo 5 la más importante'].value_counts().sort_index())

# 4. Frecuencia de consumo
print("\n4. FRECUENCIA DE CONSUMO DE PAN:")
print(df_clean['Con que frecuencia consume pan'].value_counts())

# 5. Tipo de pan preferido
print("\n5. TIPO DE PAN PREFERIDO:")
print(df_clean['Cuando compra pan, ¿Qué prefiere usted?'].value_counts())

# 6. Lugar de compra
print("\n6. LUGAR DE COMPRA DE PAN:")
print(df_clean['Al momento de comprar pan, ¿Donde lo realiza?'].value_counts())

# VISUALIZACIONES
print("\n" + "=" * 60)
print("GENERANDO VISUALIZACIONES...")
print("=" * 60)

# Crear subplots para múltiples visualizaciones
fig, axes = plt.subplots(2, 3, figsize=(20, 15))
fig.suptitle('ANÁLISIS EXPLORATORIO - CONSUMO DE PAN', fontsize=16, fontweight='bold')

# 1. Importancia del pan (1-5)
importancia = df_clean['¿Qué tan importante es la ingesta de pan diariamente? 1 al 5, siendo 5 la más importante'].value_counts().sort_index()
axes[0,0].bar(importancia.index.astype(str), importancia.values, color='skyblue', alpha=0.7)
axes[0,0].set_title('Importancia del Pan (1-5)')
axes[0,0].set_xlabel('Nivel de Importancia')
axes[0,0].set_ylabel('Frecuencia')
for i, v in enumerate(importancia.values):
    axes[0,0].text(i, v + 0.5, str(v), ha='center', va='bottom')

# 2. Frecuencia de consumo
frecuencia = df_clean['Con que frecuencia consume pan'].value_counts()
axes[0,1].pie(frecuencia.values, labels=frecuencia.index, autopct='%1.1f%%', startangle=90)
axes[0,1].set_title('Frecuencia de Consumo de Pan')

# 3. Tipo de pan preferido
tipo_pan = df_clean['Cuando compra pan, ¿Qué prefiere usted?'].value_counts()
axes[0,2].bar(tipo_pan.index, tipo_pan.values, color='lightgreen', alpha=0.7)
axes[0,2].set_title('Tipo de Pan Preferido')
axes[0,2].tick_params(axis='x', rotation=45)
for i, v in enumerate(tipo_pan.values):
    axes[0,2].text(i, v + 0.5, str(v), ha='center', va='bottom')

# 4. Lugar de compra
lugar_compra = df_clean['Al momento de comprar pan, ¿Donde lo realiza?'].value_counts()
axes[1,0].barh(lugar_compra.index, lugar_compra.values, color='lightcoral', alpha=0.7)
axes[1,0].set_title('Lugar de Compra de Pan')
for i, v in enumerate(lugar_compra.values):
    axes[1,0].text(v + 0.5, i, str(v), va='center')

# 5. Variables consideradas al comprar pan envasado
variables = df_clean['¿Qué variable considera al momento de comprar pan envasado?'].value_counts()
axes[1,1].bar(variables.index, variables.values, color='gold', alpha=0.7)
axes[1,1].set_title('Variables al Comprar Pan Envasado')
axes[1,1].tick_params(axis='x', rotation=45)
for i, v in enumerate(variables.values):
    axes[1,1].text(i, v + 0.5, str(v), ha='center', va='bottom')

# 6. Marcas preferidas
marcas = df_clean['¿Qué marca de pan envasado prefiere?'].value_counts()
axes[1,2].bar(marcas.index, marcas.values, color='violet', alpha=0.7)
axes[1,2].set_title('Marcas de Pan Preferidas')
axes[1,2].tick_params(axis='x', rotation=45)
for i, v in enumerate(marcas.values):
    axes[1,2].text(i, v + 0.5, str(v), ha='center', va='bottom')

plt.tight_layout()
plt.show()

# Análisis de relaciones entre variables
print("\n" + "=" * 60)
print("ANÁLISIS DE RELACIONES ENTRE VARIABLES")
print("=" * 60)

# Relación entre importancia del pan y frecuencia de consumo
plt.figure(figsize=(12, 8))
cross_tab = pd.crosstab(
    df_clean['Con que frecuencia consume pan'], 
    df_clean['¿Qué tan importante es la ingesta de pan diariamente? 1 al 5, siendo 5 la más importante']
)
sns.heatmap(cross_tab, annot=True, fmt='d', cmap='YlOrRd', cbar_kws={'label': 'Número de Personas'})
plt.title('Relación: Frecuencia de Consumo vs Importancia del Pan')
plt.xlabel('Importancia del Pan (1-5)')
plt.ylabel('Frecuencia de Consumo')
plt.tight_layout()
plt.show()

# Análisis de tamaño de envase preferido
print("\n7. PREFERENCIA DE TAMAÑO DE ENVASE:")
tamaño_envase = df_clean['Respecto al tamaño del envase,¿Cuál prefiere?'].value_counts()
print(tamaño_envase)

plt.figure(figsize=(10, 6))
tamaño_envase.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
plt.title('Preferencia de Tamaño de Envase')
plt.ylabel('')
plt.show()

# Análisis de razones para comprar pan envasado
print("\n8. RAZONES PARA COMPRAR PAN ENVASADO:")
razones = df_clean['¿Porque razón compra pan envasado principalmente?'].value_counts()
print(razones)

plt.figure(figsize=(12, 6))
razones.plot(kind='bar', color='lightblue')
plt.title('Razones para Comprar Pan Envasado')
plt.xlabel('Razones')
plt.ylabel('Frecuencia')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Resumen ejecutivo
print("\n" + "=" * 60)
print("RESUMEN EJECUTIVO DEL ANÁLISIS")
print("=" * 60)
print(f"• Total de encuestas válidas (consumen pan): {len(df_clean)}")
print(f"• Importancia promedio del pan: {df_clean['¿Qué tan importante es la ingesta de pan diariamente? 1 al 5, siendo 5 la más importante'].mean():.2f}/5")
print(f"• Frecuencia principal de consumo: {df_clean['Con que frecuencia consume pan'].mode()[0]}")
print(f"• Tipo de pan más preferido: {df_clean['Cuando compra pan, ¿Qué prefiere usted?'].mode()[0]}")
print(f"• Lugar de compra principal: {df_clean['Al momento de comprar pan, ¿Donde lo realiza?'].mode()[0]}")
print(f"• Variable más importante al comprar pan envasado: {df_clean['¿Qué variable considera al momento de comprar pan envasado?'].mode()[0]}")
print(f"• Marca de pan más preferida: {df_clean['¿Qué marca de pan envasado prefiere?'].mode()[0]}")
print(f"• Tamaño de envase más popular: {df_clean['Respecto al tamaño del envase,¿Cuál prefiere?'].mode()[0]}")

# Análisis adicional: distribución temporal (si la marca temporal es útil)
try:
    df_clean['Marca temporal'] = pd.to_datetime(df_clean['Marca temporal'])
    print(f"\n• Período de recolección: {df_clean['Marca temporal'].min().strftime('%Y-%m-%d')} a {df_clean['Marca temporal'].max().strftime('%Y-%m-%d')}")
except:
    print("\n• No se pudo analizar la distribución temporal")

print("\n" + "=" * 60)
print("ANÁLISIS COMPLETADO EXITOSAMENTE")
print("=" * 60)