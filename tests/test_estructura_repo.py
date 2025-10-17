import os

BASE = os.path.join(os.path.dirname(__file__), os.pardir)

REQUIRED_PATHS = [
    "README.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "LICENSE",
    ".gitignore",
    ".editorconfig",
    "pyproject.toml",
    "Makefile",
    os.path.join(".github", "workflows", "ci.yml"),
    os.path.join(".github", "PULL_REQUEST_TEMPLATE.md"),
    os.path.join("docs", "roadmap.md"),
    os.path.join("docs", "rubrica-evaluacion.md"),
    os.path.join("docs", "checklist-revision-pares.md"),
    os.path.join("01_intro", "README.md"),
    os.path.join("01_intro", "ejercicios.md"),
    os.path.join("01_intro", "ejemplos", "hola.py"),
]


def test_required_paths_exist():
    base = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    missing = []
    for path in REQUIRED_PATHS:
        if not os.path.exists(os.path.join(base, path)):
            missing.append(path)
    assert not missing, f"Faltan rutas requeridas: {missing}"
