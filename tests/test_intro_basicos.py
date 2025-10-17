import runpy
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent


def test_hola_py_imprime_hola_python(capsys):
    ruta = BASE / "01_intro" / "ejemplos" / "hola.py"
    runpy.run_path(str(ruta))
    captured = capsys.readouterr()
    assert "Hola, Python" in captured.out


def test_variables_basicas_string_esperado(tmp_path, capsys):
    # Creamos un archivo temporal que simule una posible solución del estudiante
    codigo = (
        'nombre = "Ana"\n'
        'ciudad = "Lima"\n'
        'mensaje = f"{nombre} vive en {ciudad}"\n'
        'print(mensaje)\n'
    )
    archivo = tmp_path / "variables_basicas.py"
    archivo.write_text(codigo, encoding="utf-8")

    # Ejecutamos el script y verificamos la salida
    sys.path.insert(0, str(tmp_path))
    try:
        runpy.run_path(str(archivo))
    finally:
        if str(tmp_path) in sys.path:
            sys.path.remove(str(tmp_path))
    out, err = capsys.readouterr()
    assert "Ana vive en Lima" in out
