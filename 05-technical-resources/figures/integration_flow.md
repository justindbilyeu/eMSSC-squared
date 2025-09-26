# Integration Flow (Mermaid)

```mermaid
flowchart LR
  AWG[AWG Condenser] --> QA[QA/Post-Treatment]
  SPMD[SPMD Inverse-L + Multistage] --> QA
  MSSC[Pond → Bog → Soil] --> QA
  QA --> STORE[Clean Water Storage]
  SPMD -- "Brine →" --> MSSC
  SPMD -. "Condenser heat (opt) ."-> AWG
```
