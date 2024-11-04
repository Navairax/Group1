
from pathlib import Path
import ifcopenshell
model_path = Path("C:/Users/navai/OneDrive/Skrivebord/3. semester/41934 Vidergående BIM/CES_BLD_24_10_ARC.ifc")

if not model_path.is_file():
    raise FileNotFoundError(f"No file found at {model_path}!")

model = ifcopenshell.open(model_path)
