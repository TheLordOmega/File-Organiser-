from pathlib import Path

##Inisialisation:
text_folder = Path("text_files")
text_folder.mkdir(exist_ok=True)


topics = {
    "physics": ["physics", "thermodynamics", "fluids"],
    "maths": ["calculus", "algebra", "maths"],
}
