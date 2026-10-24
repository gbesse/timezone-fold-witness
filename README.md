# timezone-fold-witness

## Français

Trouver les heures locales inexistantes ou présentes deux fois.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m timezone_fold_witness examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Interroge réellement zoneinfo et vérifie chaque fold par aller-retour UTC. Une heure répétée rend deux instants, une heure inexistante aucun ; les durées possibles ne sont pas réduites silencieusement à une valeur.

### Limites

Base de fuseaux de l’environnement non épinglée ; pas de promesse sur des règles futures modifiées. Dates locales explicites et choix de fold fourni si nécessaire ; aucun changement de fuseau système.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Find local times that do not exist or occur twice.

Synthetic data; no network access or secret required.

```sh
python -m timezone_fold_witness examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Actually queries zoneinfo and validates each fold by UTC roundtrip. Repeated local times yield two instants, nonexistent times none; possible durations are not silently collapsed.

### Limits

Runtime time-zone database is not pinned; no promise about future rule changes. Explicit local times and caller fold choice where needed; no system time-zone change.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Encontrar horas locales inexistentes o repetidas dos veces.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m timezone_fold_witness examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Consulta zoneinfo real y valida cada fold por ida y vuelta UTC. Horas repetidas producen dos instantes, inexistentes ninguno; no colapsa duraciones silenciosamente.

### Límites

Base de zonas del entorno sin fijar; sin promesa sobre futuras reglas. Fechas locales explícitas y elección fold suministrada; no cambia zona del sistema.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://docs.python.org/3/library/zoneinfo.html
- https://peps.python.org/pep-0495/
