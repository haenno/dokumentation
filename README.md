# Dokumentation mit MkDocs

Diese Dokumentation wird automatisch mit MkDocs und GitHub Actions generiert.

## Übersicht

Dieses Repository enthält eine mit MkDocs erstellte Dokumentation, die automatisch über GitHub Pages veröffentlicht wird.

## Wie es funktioniert

1. Markdown-Dateien werden im Ordner `docs/` gespeichert
2. Die Konfiguration erfolgt in der Datei `mkdocs.yml`
3. GitHub Actions baut und veröffentlicht die Dokumentation automatisch
4. Die fertige Dokumentation ist unter [https://haenno.github.io/dokumentation](https://haenno.github.io/dokumentation) verfügbar

## Lokale Entwicklung

Um die Dokumentation lokal zu entwickeln:

```bash
# MkDocs installieren
pip install mkdocs-material

# Lokalen Server starten
mkdocs serve
```

Besuchen Sie dann `http://localhost:8000` in Ihrem Browser.

## Dokumentation erweitern

1. Neue `.md`-Dateien im Ordner `docs/` erstellen
2. In der `mkdocs.yml` Datei zur Navigation hinzufügen
3. Änderungen in den main-Branch pushen, um die Veröffentlichung auszulösen
