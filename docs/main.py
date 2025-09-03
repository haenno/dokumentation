"""
Dieses Skript stellt Makros für MkDocs bereit.
Es wird vom mkdocs-macros-plugin geladen, um dynamischen Inhalt zu erzeugen.
"""

import subprocess
import os

def define_env(env):
    """
    Diese Funktion definiert Makros und Variablen für MkDocs.
    Sie wird vom mkdocs-macros-plugin aufgerufen.
    """
    
    @env.macro
    def get_git_changelog():
        """
        Erzeugt ein Changelog basierend auf Git-Commits.
        Dies ist ein Fallback für das changelog-Plugin.
        """
        try:
            # Prüfen, ob wir in einem Git-Repository sind
            if not os.path.exists('.git'):
                return "**Hinweis:** Kein Git-Repository gefunden."
                
            # Git-Log abrufen und formatieren
            result = subprocess.run(
                ['git', 'log', '--pretty=format:### %ad - %an%n%s%n%n', '--date=short'], 
                stdout=subprocess.PIPE, 
                universal_newlines=True
            )
            
            if result.returncode != 0:
                return "**Fehler:** Git-Changelog konnte nicht generiert werden."
                
            return result.stdout
            
        except Exception as e:
            return f"**Fehler bei der Changelog-Generierung:** {str(e)}"
