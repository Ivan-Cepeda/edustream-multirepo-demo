# 🏘️ EduStream: Multirepo Architecture Demo

Este repositorio demuestra una implementación práctica de una arquitectura **Multirepo** (Desacoplada) para un sistema de Machine Learning end-to-end.

⚠️ **NOTA IMPORTANTE:**
Para fines educativos, este repositorio contiene **tres carpetas que simulan ser repositorios totalmente independientes**.
En un escenario real, cada carpeta (`repo-ml`, `repo-api`) viviría en su propio repositorio de GitHub y el `artifact-registry` sería un servicio de almacenamiento en la nube (como AWS S3, Azure Blob Storage o Google Cloud Storage).

---

## 🗺️ Mapa del "Vecindario" (Estructura)

En esta arquitectura, los equipos viven en "casas" separadas y no tienen llaves para entrar a la casa del otro.

### 1. `repo-ml/` (El Productor) 🍳
* **Rol:** Equipo de Data Science.
* **Misión:** Entrenar modelos y **publicarlos**.
* **Regla de Oro:** No sabe que existe una API. Su trabajo termina cuando sube el archivo `.pkl` al Registro.
* **Simulación:** Al ejecutar su código, "sube" un archivo a la carpeta compartida.

### 2. `repo-api/` (El Consumidor) 🍽️
* **Rol:** Equipo de Backend.
* **Misión:** Leer el modelo publicado y usarlo para predecir.
* **Regla de Oro:** No tiene acceso al código de entrenamiento ni a los datos originales. Solo confía en los archivos que aparecen en el Registro.

### 3. `artifact-registry/` (El Intermediario) ☁️
* **Rol:** Almacenamiento Central (Simulación de la Nube).
* **Misión:** Es el único punto de contacto entre los dos equipos. Funciona como un "buzón de entrega".

---

## 🚀 Guía de Ejecución (Roleplay)

Para entender esta arquitectura, debes actuar como si fueras dos personas distintas en momentos distintos. Sigue estos pasos en tu terminal:

### Paso 0: Clonar el Proyecto
```bash
git clone [https://github.com/TU_USUARIO/edustream-multirepo-demo.git](https://github.com/TU_USUARIO/edustream-multirepo-demo.git)
cd edustream-multirepo-demo
```
### Paso 1: Rol de Científico de Datos (Train & Deploy)
Primero, ponte el sombrero de Data Scientist. Debes entrar a tu repositorio para trabajar.

```Bash
# 1. Entramos a la "oficina" de ML
cd repo-ml

# 2. Ejecutamos el pipeline
# Este script entrena el modelo y lo COPIA (Deploy) al registry
python train_publish.py
```

## ✅ Resultado Esperado: 
Verás un mensaje de DEPLOY EXITOSO. Si revisas la carpeta artifact-registry, verás que ha aparecido un archivo churn_model_v2.pkl.

### Paso 2: Rol de Desarrollador Backend (Consume)
Ahora cámbiate de sombrero. Sal de la oficina de ML y entra a la de la API. La API no sabe cómo se cocinó el modelo, solo lo consume.

```Bash
# 1. Salimos de ML y entramos a API
cd ..
cd repo-api

# 2. Ejecutamos el servidor de inferencia
python serve_consume.py
```

##✅ Resultado Esperado: 
La API leerá el archivo desde el artifact-registry y confirmará que el modelo v2.0 está cargado y listo.

## 🧪 Experimento de Desacoplamiento
Para demostrar la independencia de los sistemas, intenta lo siguiente:

Borra el archivo .pkl de la carpeta artifact-registry.

Intenta ejecutar la API (python serve_consume.py).

Resultado: Fallará con un error controlado.

## Lección: 
A diferencia del Monorepo, si no hay un "Release" explícito en el medio (el archivo en el registry), la API no puede funcionar, incluso si el código de ML está perfecto en su propia carpeta.

| Característica | Monorepo (La Casa Familiar) | Multirepo (Este Ejemplo) |
| :--- | :--- | :--- |
| **Acceso a Código** | La API puede importar funciones de ML directamente. | **Prohibido.** Aislamiento total. |
| **Compartir Modelos** | Leyendo la carpeta de al lado (Ruta relativa). | **Publicando** en un Registry externo (S3/Artifactory). |
| **Coordinación** | Implícita (cambios inmediatos). | **Explícita** (versiones y contratos). |
| **Independencia** | Baja (Si rompes Core, rompes todo). | Alta (Cada equipo tiene su ciclo de vida). |

📝 Licencia
Este proyecto es parte del material educativo de Soy Henry - Carrera de Data Science - Módulo 5.
