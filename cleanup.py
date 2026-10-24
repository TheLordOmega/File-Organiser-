from pathlib import Path

md_path = Path(__file__).parent / "test Orient.md"
output_path= md_path.with_name(f"{md_path.stem}_clean.md")

text= md_path.read_text(encoding="utf-8")

text= text.replace("\x0c","\n")

lines = [line.strip() for line in text.splitlines()]

cleaned_lines= []

for line in lines:
    if line:
        cleaned_lines.append(line)
    elif cleaned_lines and cleaned_lines[-1] !="":
        cleaned_lines.append("")

while cleaned_lines and cleaned_lines [-1] == "":
    cleaned_lines.pop()

output_path.write_text(
    "\n".join(cleaned_lines)+ "\n",
    encoding="utf-8"
)
print(f"Cleaned Makrdown saved to :{output_path}")
