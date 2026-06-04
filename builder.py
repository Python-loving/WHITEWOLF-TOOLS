import os
import subprocess
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

icon_path = filedialog.askopenfilename(
    title="Choisir une icône",
    filetypes=[("ICO files", "*.ico")]
)

if not icon_path:
    print("Aucune icône choisie")
    exit()

output_dir = "covid-exe"
os.makedirs(output_dir, exist_ok=True)

subprocess.run([
    "pyarmor",
    "gen",
    "covid.py"
])

subprocess.run([
    "pyinstaller",
    "--onefile",
    "--noconsole",
    "--name", "Tools",
    "--distpath", output_dir,
    "--icon", icon_path,
    "dist/covid.py"  
])

print(f"Terminé -> {output_dir}/Tools.exe")
