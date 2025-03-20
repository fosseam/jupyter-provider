# jupyter-provider
Alles über Jupyter Labs & NoteBooks im SaaS Format.

Dieses Repository bietet ein strukturiertes JSON-Dataset mit umfassenden Informationen zu öffentlichen und kommerziellen Jupyter-Notebook-Anbietern. Es dient als Referenz, Entscheidungshilfe sowie zur systematischen Bewertung und Auswahl geeigneter Anbieter.  
  
🇺🇳 🇺🇸 🇬🇧 (eng) -> readme.md  

## 1. Einleitung & Zweck

Dieses Dataset hilft Nutzer\:innen, Forschende und Teams, die passende Jupyter-Notebook-Umgebung zu finden, zu vergleichen und fundierte Entscheidungen zu treffen. Der Schwerpunkt liegt auf Transparenz, Qualitätssicherung und gemeinschaftlicher Pflege (Open-Research-Ansatz).

## 2. Anbietergruppen

Anbieter werden in drei Hauptgruppen unterteilt:

- **Free**: Vollständig kostenlose Jupyter-Umgebungen ohne langfristige Kosten.
- **Cloud**: Notebooks von Cloud-Plattformen (AWS, Azure, GCP etc.), meist an bestehende Cloud-Accounts gebunden.
- **Subscription**: Kommerzielle Anbieter, hauptsächlich im Abo-Modell mit wenigen oder keinen dauerhaft kostenlosen Optionen.

## 3. Attribute und Attributgruppen

Jeder Anbieter wird anhand der folgenden Gruppen charakterisiert:

- **Basics**: Allgemeine Informationen wie Beschreibung, URL, Anbietername.
- **Access**: Zugangsmöglichkeiten, Registrierung, OAuth-Login, Session-Dauer, Import-/Export-Funktionen.
- **Functionality**: Funktionale Möglichkeiten (GPU/TPU, JupyterLab-Unterstützung).
- **Scalability**: Ressourcen-Limits (RAM, CPU, Speicher).
- **Integrations**: Integration externer Dienste wie Git oder Cloud-Speicher.
- **Security**: Datenschutz, Verschlüsselung, Authentifizierung.
- **Community**: Verfügbare Dokumentation, Support-Kanäle, Community-Größe.
- **SWOT**: Stärken und Schwächen der jeweiligen Plattform.

## 4. JSON-Schema & Qualitätskontrolle

Um Datenqualität und Transparenz sicherzustellen, enthält jedes Attribut:

- `lastCheck`: Datum der letzten Prüfung (Gruppen-Ebene).
- `confidence`: Qualitätsindikator:
  - `["high"]`: Gesicherte Information mit Quellenangabe (URL optional).
  - `["medium"]`: Plausibel, aber ohne explizite Quelle.
  - `["low"]`: Unsicher, geschätzt oder geraten.

Jede Attributgruppe und die Gesamtbewertung des Anbieters werden automatisch aggregiert:

- **Alle Attribute high** → Gruppen-Confidence = `high`.
- **Mindestens ein medium, kein low** → `medium`.
- **Mindestens ein Attribut low** → Gruppe = `low`.

### Vorsicht-vor-Optimismus-Regel

Die Bewertung erfolgt bewusst konservativ, um Fehleinschätzungen zu vermeiden:

| Situation | Confidence-Wert |
|-----------|----------------|
| **Keine Informationen oder vage Andeutungen** | `low` |
| **Widersprüchliche Infos (z. B. manche Quellen sagen ja, andere nein)** | `low` |
| **Nur inoffizielle Community-Berichte, keine offizielle Quelle** | `medium` |
| **Community-Berichte + indirekte Hinweise aus offiziellen Quellen** | `medium` |
| **Offizielle Quelle nennt es klar (aber nicht prominent)** | `high` |
| **Offizielle Quelle bestätigt es eindeutig** | `high` |

Falls neue Informationen auftauchen, können Werte nach oben korrigiert werden – aber **nie umgekehrt geschätzt**.

Bei Attributen mit unsicherem Status (`"available": "unsure"`) wird zusätzlich ergänzt:

- `reasoning`: Erklärung der Unsicherheit.
- `lastCheck`: Datum der letzten Prüfung.

#### **Praxis-Beispiele**

- **GPU-Unterstützung bei Copernicus** → `low`, da keine offizielle Bestätigung existiert.
- **MFA bei Copernicus** → `low`, weil es nirgends erwähnt wird.
- **Max. CPU/RAM bei Copernicus** → `low`, da die Spezifikationen unklar sind.
- **nbgitpuller in Copernicus** → `high`, da offiziell dokumentiert.
- **Echtzeit-Kollaboration bei Copernicus** → `high`, da in offiziellen Quellen explizit erwähnt.
- **Scheduling in PAWS (über Toolforge)** → `medium`, da die Community eine Lösung bestätigt, aber keine offizielle Wikimedia-Aussage existiert.

Diese Praxisfälle sorgen für Konsistenz und Nachvollziehbarkeit in der Bewertung.

## 5. Pflege, Community & Open-Research

Dieses Dataset lebt von gemeinsamem Wissen. Bitte hilf mit:

- Vorhandene Daten überprüfen und korrigieren.
- Fehlende Details und Quellen ergänzen.
- Informationen regelmäßig aktualisieren.

Pull Requests, Issues und Diskussionen sind herzlich willkommen!

## 6. Technische Integration (CI/CD)

Die JSON-Daten werden für jeden Anbieter in separaten Dateien gepflegt und automatisiert zusammengeführt:

```bash
providers/
├── free/
│   ├── kaggle-kernels.json
│   └── google-colab.json
├── cloud/
└── subscription/
```

Zum Zusammenführen der Daten wird folgendes Python-Skript genutzt:

```python
import os, json

def generate_main_json(input_dir, output_file):
    main_json = {"Free":{}, "Cloud":{}, "Subscription":{}}
    for category in ["free", "cloud", "subscription"]:
        category_path = os.path.join(input_dir, category)
        for provider_json in os.listdir(category_path):
            with open(os.path.join(category_path, provider_json), "r") as f:
                data = json.load(f)
                main_key, main_value = next(iter(data.items()))
                main_json[category.capitalize()][main_key] = main_value

    with open(output_file, "w") as out:
        json.dump(main_json, out, indent=4, ensure_ascii=False)

# Beispiel-Aufruf:
generate_main_json("providers", "main.json")
```

Issues und Pull Requests zur kontinuierlichen Verbesserung sind willkommen!

## 🚀 Call to Action

- Nutze das Dataset aktiv und teile dein Feedback!
- Unterstütze uns mit Ergänzungen und Verbesserungen.
- Hilf mit, Wissen offen und gemeinsam zugänglich zu machen!

