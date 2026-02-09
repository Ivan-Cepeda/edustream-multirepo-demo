import os
from pathlib import Path

ROOT = Path.cwd()
print(f"🏗️  Construyendo Vecindario Multirepo en: {ROOT}")

# 1. Creamos las "Casas" (Repositorios independientes)
# Fíjate que también creamos el 'artifact-registry' (El Buzón Compartido)
repos = ["repo-ml", "repo-api", "artifact-registry"]

for repo in repos:
    (ROOT / repo).mkdir(parents=True, exist_ok=True)
    # Creamos un README en cada uno para simular que son proyectos distintos
    (ROOT / repo / "README.md").write_text(f"# Proyecto {repo.upper()}", encoding="utf-8")

# 2. Creamos los scripts vacíos para la clase
(ROOT / "repo-ml" / "train_publish.py").write_text("", encoding="utf-8")
(ROOT / "repo-api" / "serve_consume.py").write_text("", encoding="utf-8")

print("✅ Infraestructura Multirepo lista.")
print("   - repo-ml: Donde se cocina.")
print("   - repo-api: Donde se sirve.")
print("   - artifact-registry: El único punto de contacto.")