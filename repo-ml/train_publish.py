import pickle
import os
import shutil
from pathlib import Path

# Calculamos la ruta base basándonos en la ubicación de ESTE archivo script
BASE_DIR = Path(__file__).resolve().parent 

print('>> [ML TEAM] Iniciando entrenamiento v2.0...')

modelo = {
    'version': 'v2.0', 
    'algoritmo': 'RandomForest', 
    'status': 'production'
}

# Guardado Local (Usando BASE_DIR)
local_folder = BASE_DIR / 'models'
os.makedirs(local_folder, exist_ok=True)
local_path = local_folder / 'churn_model_v2.pkl'

with open(local_path, 'wb') as f:
    pickle.dump(modelo, f)
print(f'   - Modelo guardado localmente en: {local_path.name}')

# PUBLICACIÓN
# Navegamos desde BASE_DIR hacia el registro
# "Sube uno (parent) y busca 'artifact-registry'"
registry_path = BASE_DIR.parent / 'artifact-registry' / 'churn_model_v2.pkl'

print(f'   - ☁️  Subiendo artefacto al Registry...')

# Verificación de seguridad para la demo
if not registry_path.parent.exists():
    print(f"   ❌ ERROR: No encuentro la carpeta {registry_path.parent}")
else:
    shutil.copy(local_path, registry_path)
    print(f'   ✅ DEPLOY EXITOSO. El modelo está disponible en el Registry.')