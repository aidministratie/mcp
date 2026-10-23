---
name: visitekaartjes-collega
description: Automatiseer de intake van visitekaartjes, OCR, KBO/BTW-verificatie en menselijke controle voor kmo's.
---

# Visitekaartjes-collega van aidministratie.be

Deze vaardigheid activeert de Visitekaartjes-collega om afbeeldingen of scans van visitekaartjes uit te lezen:
1. Start een scan via de MCP-tool `trigger_visitekaartjes_scan`.
2. Extraheert contactgegevens, bedrijfsnaam, e-mailadres en telefoonnummer via OCR.
3. Valideert het Belgische ondernemingsnummer (KBO/BTW) indien aanwezig.
4. Biedt het resultaat altijd eerst aan in de goedkeuringswachtrij (`haal_wachtende_taken_op`) ter menselijke controle voor het in een CRM geplaatst wordt.
