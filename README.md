# API-Weather-Pyhton

 Script Python qui affiche en console les prévisions météo à 5 jours (min/max par jour) pour une liste de villes
 
Les données proviennent de l'API publique [OpenWeatherMap](https://openweathermap.org/forecast5)

## Sommaire
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Configuration](#configuration)
- [Utilisation](#utilisation)
- [Fonctionnement](#fonctionnement)
- [Notes](#notes)
- [Structure du projet](#structure-du-projet)

## Prérequis
 
- Python 3.14
- Un accès réseau
- Une clé API OpenWeatherMap (gratuite sur [openweathermap.org](https://openweathermap.org/api))


## Installation
 
```bash
# Créer et activer un environnement virtuel
python -m venv .venv
 
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
 
# Installer les dépendances
pip install -r requirements.txt
```
## Configuration
 
Le script lit la clé API depuis la variable d'environnement `API_KEY`
 
Dans PyCharm : `Run` -> `Edit Configurations...` -> `Environment variables` -> ajouter `API_KEY=la_clé_openweather`
 
## Utilisation
 
```bash
python weather.py
```
 
Exemple de sortie :
 
```
Saint-Geours-de-Maremne's weather
 
Date: 2026-09-22 | Min: 15.3°C | Max: 24.1°C
Date: 2026-09-23 | Min: 14.8°C | Max: 22.6°C
...
```
 
## Fonctionnement
 
| Fonction | Rôle |
|---|---|
| `get_weather_forecast()` | Récupère les prévisions brutes à 5 jours pour une ville (`forecast`) |
| `extract_daily_min_max()` | Regroupe les tranches de 3h par jour et calcule le min/max |
| `display_weather()` | Affiche le résumé quotidien pour chaque ville |
 
- Les villes affichées sont définies dans `display_weather()`
- Chaque appel HTTP a un timeout de 10 secondes
- En cas d'erreur, l'exception est loguée via `logger.exception`
## Notes
 
- Le pays est fixé sur `fr` dans la requête
- Le niveau de log par défaut est `ERROR` et il se règle dans `main()` via `logging.basicConfig`
- Si `API_KEY` n'est pas définie, le script s'arrête avec un message d'erreur
## Structure du projet
 
```
├── main.py
├── requirements.txt
└── README.md
```
## Licence
Projet effectué lors d'un exercice sur les fondamentaux des APIs
