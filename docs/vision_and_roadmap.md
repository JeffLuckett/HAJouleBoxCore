# HAJouleBoxCore: Vision and Roadmap

## Purpose
HAJouleBoxCore is a modular, adapter-driven energy monitoring framework for Home Assistant.
Its goal is to provide a **Core Entity Schema** that normalizes energy data from diverse sources (MQTT, REST APIs, Modbus, vendor SDKs).
Dashboards, automations, and optimizers consume only normalized entities, ensuring stability when devices change or integrations break.

---

## Initial Vision
- **Generalization over specialization**
  Define one schema that can represent any energy topology: grid, generation, storage, and loads.
- **Pluggable adapters**
  Device-specific adapters translate raw data into schema entities. They can be swapped without breaking dashboards.
- **Admin interface**
  Tools for diagnostics, simulation, and configuration to make testing and setup straightforward.
- **Strong test culture**
  Unit tests, integration tests, schema validation — enforced in CI — to keep the framework reliable.
- **Community-friendly**
  Clear contribution guidelines, reference adapters, and dashboard examples.

---

## Roadmap to MVP
### Phase 0: Foundations
- Repo scaffold with CI, tests, and Core Entity Schema spec.
- Documentation: README, schema contract, this roadmap.

### Phase 1: MVP
- Core schema validator in Python.
- One working adapter (SEM via MQTT).
- Admin interface prototype:
  - Show adapter status.
  - Run schema validation.
  - Enable “simulation mode” with mock data.
- Reference dashboards:
  - Lovelace config using Power Flow Card Plus.
  - Node-RED example flow.

### Phase 2: Extension
- Add SunPower PVS6 adapter (via SunStrong integration).
- Expand reference dashboards with historical charts and circuit breakdowns.
- Publish developer guide: “How to write an adapter”.

---

## Future Vision
- **More adapters**: EVSE (OCPP), batteries, other inverter brands.
- **Optimization layer**: optional tie-in with EMHASS or FlexMeasures.
- **Historical storage**: seamless InfluxDB/Grafana integration.
- **Community distribution**: HACS-ready package for easy install.
- **Advanced admin UI**: guided setup, entity schema compliance checks, visual adapter management.
- **Mock/demo mode**: shareable “live demo” without hardware.

---

## Scope and Discipline
The project will remain:
- **Lightweight** — minimal dependencies, no vendor lock-in.
- **Accessible** — usable by HA hobbyists, not just developers.
- **Extensible** — new adapters can be added without touching dashboards or core logic.
- **Well-tested** — every release validated through CI.

---

## Status
- ✅ Repo scaffold complete.
- ✅ CI pipeline passing.
- 🚧 Next: implement SEM MQTT adapter and admin dashboard prototype.