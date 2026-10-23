# aidministratie.be // Digitale collega's en AI voor kmo's

[![Protocol](https://img.shields.io/badge/MCP%20Protocol-2024--11--05-blue.svg)](https://modelcontextprotocol.io)
[![Data Sovereignty](https://img.shields.io/badge/Data%20Sovereignty-100%25%20EU%20GDPR-emerald.svg)](https://aidministratie.be/privacy/mcp)
[![Terms of Service](https://img.shields.io/badge/Terms-MCP%20%26%20API-orange.svg)](https://aidministratie.be/terms/mcp)
[![Publisher](https://img.shields.io/badge/Publisher-aidministratie.be-black.svg)](https://aidministratie.be)
[![License](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)

Officiële Model Context Protocol (MCP) Gateway & open-source bridge voor **[aidministratie.be](https://aidministratie.be)**.

---

## 🇧🇪 Wat doet aidministratie.be voor jouw kmo?

**[aidministratie.be](https://aidministratie.be)** brengt **praktische AI en digitale collega's** naar Vlaamse en Europese kmo's. 

Wij verbinden jouw favoriete AI-apps (zoals Claude, Cursor, ChatGPT of Microsoft 365 Copilot) veilig met meewerkende digitale teamleden voor jouw dagelijkse administratie, **zónder dat jouw vertrouwelijke bedrijfsgegevens ooit gebruikt worden om publieke AI-modellen te trainen**.

### De drie garanties voor jouw onderneming:
1. **Verlicht jouw administratie:** Routineklussen zoals visitekaartjes inboeken, prospectiesignalen opvolgen en dossiers beheren worden zelfstandig voorbereid door je digitale collega's.
2. **Jij behoudt altijd de controle (Mens-in-de-lus):** Een digitale collega voert pas een definitieve actie uit (zoals een e-mail of CRM-mutatie) nadat jij een seintje van akkoord hebt gegeven via een eenvoudige goedkeuringswachtrij.
3. **100% Data-soevereiniteit & GDPR:** Al jouw bestanden en data worden verwerkt en versleuteld (AES-256 KMS) in gecertificeerde Europese datacenters (Duitsland & Finland). Geen ongewenste datadoorgiften naar Amerikaanse servers.

---

## 👥 Maak kennis met jouw Digitale Collega's

Via het Model Context Protocol (MCP) krijgen jouw AI-assistenten direct toegang tot gespecialiseerde teamleden:

| Digitale Collega | Wat doet deze collega voor jouw kmo? | Onderliggende MCP-tool |
| :--- | :--- | :--- |
| 📇 **De Visitekaartjes-collega** | Fotografeert visitekaartjes na een beurs of meeting, extraheert gegevens, valideert het KBO/BTW-nummer en synchroniseert direct naar jouw CRM of Google Sheets. | `trigger_visitekaartjes_scan` |
| 🎯 **De Prospectie-collega** | Monitort vacatures, aanbestedingen en marktsignalen en bereidt relevante opvolgacties voor jouw verkoopteam voor. | `trigger_prospectie_scan` |
| 📁 **De Dossier- & Archief-collega** | Beheert jouw versleutelde Virtuele Bestandssysteem (VFS). Zoekt razendsnel documenten op en legt nieuwe versies vast met verplichte audit-verantwoording. | `list_files`<br>`read_file_content`<br>`write_file_content` |
| 🤝 **De Goedkeurings-assistent** | Zet alle voorgestelde acties netjes voor je klaar in een review-wachtrij, zodat jij met één klik op 'akkoord' de controle behoudt. | `haal_wachtende_taken_op`<br>`beoordeel_wachtende_taak` |
| 🧠 **Het Lerend Geheugen** | Onthoudt specifieke bedrijfsvoorkeuren en werkinstructies ("stuur offertes voor klant X altijd naar finance@..."). | `voeg_agent_leermoment_toe` |
| 📊 **De Status-assistent** | Geeft direct inzicht in de live werking en achtergrondtaken van jouw actieve kmo-agents. | `check_agent_status` |

👉 **Meer informatie of een KMO-licentie aanvragen:** [https://aidministratie.be](https://aidministratie.be)  
👉 **Klantportaal & AI Loket:** [https://loket.aidministratie.be](https://loket.aidministratie.be)

---

## 🚀 Hoe praat jouw AI met je digitale collega's? (Quickstart)

### Optie A: Direct via de Remote Gateway (Aanbevolen)

#### 1. Claude Desktop (`claude_desktop_config.json`)
```json
{
  "mcpServers": {
    "aidministratie": {
      "url": "https://loket.aidministratie.be/?token=JOUW_TENANT_API_KEY"
    }
  }
}
```

#### 2. Cursor (`.cursor/mcp.json`)
```json
{
  "mcpServers": {
    "aidministratie": {
      "url": "https://loket.aidministratie.be",
      "headers": {
        "x-api-key": "JOUW_TENANT_API_KEY"
      }
    }
  }
}
```

#### 3. Google Antigravity (`~/.gemini/antigravity/mcp_config.json`)
```json
{
  "mcpServers": {
    "aidministratie": {
      "serverUrl": "https://loket.aidministratie.be",
      "headers": {
        "x-api-key": "JOUW_TENANT_API_KEY"
      }
    }
  }
}
```

---

### Optie B: Open-Source Python Stdio Bridge (Voor lokale CLI-omgevingen)

Voor ontwikkelaars die de voorkeur geven aan een lokaal subprocess via stdio:

```bash
git clone https://github.com/aidministratie/mcp.git
cd mcp

python bridge.py --token <JOUW_TENANT_API_KEY>
```

In `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "aidministratie": {
      "command": "python",
      "args": ["/pad/naar/mcp/bridge.py", "--token", "JOUW_TENANT_API_KEY"]
    }
  }
}
```

---

## 🔐 Veiligheid & Authenticatie

Jouw API-sleutel (`vlw_live_...`) wordt aangemaakt in het beveiligde [aidministratie.be Loket](https://loket.aidministratie.be).

* **HTTP Header:** `x-api-key: vlw_live_...` of `Authorization: Bearer vlw_live_...`
* **Query Parameter:** `https://loket.aidministratie.be/?token=vlw_live_...`

---

## 📄 Juridische Voorwaarden & Privacy (Belgisch Recht)

* **Privacy Policy (Zero Model Training):** [https://aidministratie.be/privacy/mcp](https://aidministratie.be/privacy/mcp)
* **Terms of Service (Mens-in-de-lus afspraken):** [https://aidministratie.be/terms/mcp](https://aidministratie.be/terms/mcp)
* **Website:** [https://aidministratie.be](https://aidministratie.be)
* **Contact:** Bram Vanzieleghem / ITeratief (BE 0671.637.106) // `bram@aidministratie.be`
