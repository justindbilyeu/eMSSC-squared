import importlib.util
from pathlib import Path


def load_module(name: str, relative_path: str):
    base = Path(__file__).resolve().parents[1]
    module_path = base / relative_path
    spec = importlib.util.spec_from_file_location(name, module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader, f"Cannot load module at {module_path}"
    spec.loader.exec_module(module)
    return module
