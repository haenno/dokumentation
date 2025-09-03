# Pausenfunktion

Die Pausenfunktion ermöglicht es Benutzern, vorübergehend Benachrichtigungen und Erinnerungen zu deaktivieren, um konzentriert und ungestört arbeiten zu können.

## Funktionsübersicht

Die Pausenfunktion bietet folgende Möglichkeiten:

- Temporäres Aussetzen von Benachrichtigungen für einen bestimmten Zeitraum
- Automatische Wiederaufnahme nach Ablauf der eingestellten Zeit
- Manuelle Kontrolle über den Pausenstatus
- Anpassbare Einstellungen für verschiedene Benachrichtigungstypen

## Verwendung der Pausenfunktion

### Pausenmodus aktivieren

1. Klicken Sie auf das Glockensymbol in der oberen Menüleiste
2. Wählen Sie "Pausenmodus aktivieren"
3. Stellen Sie die gewünschte Dauer ein (15 Minuten, 30 Minuten, 1 Stunde, 2 Stunden oder benutzerdefiniert)
4. Bestätigen Sie mit "Aktivieren"

```python
# Beispielcode zur Aktivierung der Pausenfunktion
def activate_pause_mode(duration_minutes):
    current_time = datetime.now()
    end_time = current_time + timedelta(minutes=duration_minutes)
    
    user_settings.update({
        'pause_mode': True,
        'pause_until': end_time,
        'notification_status': 'paused'
    })
    
    schedule_resume(end_time)
    return True
```

### Pausenmodus vorzeitig beenden

1. Klicken Sie auf das Glockensymbol mit dem Pauseindikator
2. Wählen Sie "Pausenmodus beenden"
3. Bestätigen Sie mit "Fortsetzen"

### Einstellungen anpassen

Im Bereich "Einstellungen" > "Benachrichtigungen" können Sie festlegen:

- Welche Benachrichtigungstypen von der Pausenfunktion betroffen sind
- Ob bestimmte wichtige Benachrichtigungen trotz aktivierter Pause angezeigt werden sollen
- Standard-Pausenzeiten für schnellen Zugriff

## Hinweise und Tipps

!!! tip "Tipp"
    Nutzen Sie die Pausenfunktion für konzentrierte Arbeitszeiten nach der Pomodoro-Technik: 25 Minuten Arbeit gefolgt von 5 Minuten Pause.

!!! warning "Achtung"
    Auch im Pausenmodus werden kritische Systembenachrichtigungen weiterhin angezeigt.

!!! note "Hinweis"
    Die Pausenfunktion synchronisiert sich automatisch über alle Ihre Geräte, auf denen Sie angemeldet sind.
