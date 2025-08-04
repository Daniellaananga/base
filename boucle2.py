import time
from rich import print
for i in range(10, 0, -1):
    print(f"[bold magenta]{i}[/bold magenta]")
    time.sleep(1) # pause d'une seconde entre chaque nombre

print("[bold green]Décolage ! [bolb green]")