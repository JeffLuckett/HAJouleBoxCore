# HAJouleBoxCore

Modular Energy Framework for Home Assistant.

Adapters ingest raw energy data (MQTT, REST, APIs), normalize it into a **Core Entity Schema**, and expose it to dashboards and automations.
This keeps your setup resilient against device swaps or broken integrations.

## Getting Started

Clone the repo and install dependencies:

```bash
git clone https://github.com/JeffLuckett/HAJouleBoxCore.git
cd HAJouleBoxCore
pip install -r requirements.txt
pytest
```

## Project Layout

 * hajouleboxcore/schema/ — schema validator
 * adapters/ — pluggable adapters (example included)
 * dashboards/ — reference configs
 * tests/ — unit/integration/schema tests
 * docs/spec.md — Core Entity Schema contract

Status
MVP skeleton — passes tests in CI, ready for adapter development.