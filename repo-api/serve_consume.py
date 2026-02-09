import pickle
from pathlib import Path

print('>> [API TEAM] Iniciando sistema de inferencia...')

# 1. CONEXIÓN AL REGISTRY (Simulando descarga de S3)
# OJO: Aquí NO entramos a 'repo-ml'. Vamos al 'artifact-registry'.
ruta_registry = Path('../artifact-registry/churn_model_v2.pkl')

print(f'   - Buscando modelo en: {ruta_registry}')

if ruta_registry.exists():
    # 2. CARGA DEL ARTEFACTO
    with open(ruta_registry, 'rb') as f:
        modelo = pickle.load(f)
    
    print(f"   ✅ CONEXIÓN EXITOSA.")
    print(f"   - Modelo cargado: {modelo['algoritmo']} (Versión {modelo['version']})")
    print("   - Listo para recibir peticiones HTTP.")
else:
    print(f"   ❌ ERROR CRÍTICO: El artefacto {ruta_registry.name} no existe en el Registry.")
    print("   - (¿El equipo de ML olvidó hacer el Deploy?)")