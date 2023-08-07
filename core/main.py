import os
from rich.console import Console
from rich.markdown import Markdown
from pathlib import Path 

console = Console()

MARKDOWN = """
# Automatisation windows, **by Naltos** !
"""

md = Markdown(MARKDOWN)
console.print(md)

def create_mkdir(path: str, directory_name: str) -> str:
    if not isinstance(path, str):
        print("Valeur incorrect !") 
    elif not isinstance(directory_name, str):
        print("Valeur incorrect !")
    else:
        os.mkdir(path + directory_name)
        console.print("Dossier créer avec succès ! => [cyan]{}{}[/]".format(path, directory_name), style='bold underline green')

def delete_mkdir(path: str, directory_name: str) -> str:
    if not isinstance(path, str):
        console.print("[bold red] Veuillez spécifier un chemin correct ![/]")
    elif not isinstance(directory_name, str):
        console.print("[bold red] Merci de spécifier un nom de dossier correct ![/]")
    else:
        os.chdir(path)
        os.rmdir(directory_name)
        console.print("[bold green]Dossier supprimé avec succès ![/]")
            
def create_file(path: str, directory: str, ext: str) -> str:
    pass

def rename_file(path: str, filename: str, new_name: str) -> str:
    if not isinstance(path, str):
        console.print("[bold red] Veuillez spécifier un chemin correct ![/]")
    elif not isinstance(filename, str):
        console.print("[bold red] Merci de spécifier un nom de fichier correct ![/]")
    elif not isinstance(new_name, str):
        console.print("[bold red] Merci de spécifier un nom de fichier correct ![/]")
    else:
        os.chdir(path)
        os.rename(new_name, filename)
        console.print("[bold green]Fichier renommé avec succès ![/]")

def see_files(path: str) -> str:
    p = Path(path)
    for files in os.scandir(p):
        print(files)

def delete_file(path: str, file_name: str) -> str:
    pass
    
def main():
    user_choice = int(console.input("Quelle action souhaitez vous effectuer ? [bold green][1]: Créer un dossier[/], [bold red][2]: Supprimer un dossier[/], [bold blue][3]: Voir le contenu d'un dossier/répertoire[/], [bold cyan][4]: Renommer un fichier existant[/]."))
    if user_choice == 1:
        path = console.input("[bold blue]Merci de spécifier le chemin d'accès dans lequel vous souhaitez créer votre dossier: [/]")
        directory_name = console.input("[bold blue]Merci de spécifier le nom du dossier que vous souhaitez créer [bold underline red](Merci de ne pas mettre d'espace, seulement des caractères spéciaux: '_, -')[/]: [bold magenta]")
        create_mkdir(path, directory_name)
    elif user_choice == 2:
        path = console.input("[bold blue]Merci de spécifier le chemin d'accès vers lequel se trouve le dossier à supprimer: [/]")
        directory_name = console.input("[bold blue]Merci de spécifier le nom du dossier que vous souhaitez supprimer: [/]")
        delete_mkdir(path, directory_name)
    elif user_choice == 3:
        path = console.input("[bold blue]Merci de spécifier le chemin d'accès dans lequel vous souhaitez analyser vos fichiers: [/]")
        see_files(path)
        console.print("[bold green]Dossier analysé avec succès ![/]")
    elif user_choice == 4:
        path = console.input("[bold blue]Merci de spécifier le chemin d'accès vers lequel se trouve le fichier à renommer: [/]")
        filename = console.input("[bold blue]Merci de spécifier le nom du fichier que vous souhaitez renommer [bold red](Veillez à bien spécifiez l'extension du fichier que vous souhaitez renommer)[/]: [/]")
        new_name = console.input("[bold blue]Merci de spécifier le nouveau nom à attribuer au fichier: [/]")
        rename_file(path, new_name, filename)

if __name__ == "__main__":
    main()