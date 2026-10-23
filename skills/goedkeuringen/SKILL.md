---
name: goedkeurings-assistent
description: Bewaak en beoordeel taken met mens-in-de-lus toezicht voordat externe acties worden uitgevoerd.
---

# Goedkeurings-assistent van aidministratie.be

Deze vaardigheid waarborgt te allen tijde menselijke controle (human-in-the-loop):
1. Vraag openstaande taken op via `haal_wachtende_taken_op`.
2. Controleer de details, gegenereerde concepten of voorgestelde wijzigingen.
3. Beoordeel de taak via `beoordeel_wachtende_taak` met 'approve', 'reject' of 'modify' en optionele feedback.
