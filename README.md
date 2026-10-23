# aidministratie MCP Gateway

[![Protocol](https://img.shields.io/badge/MCP%20Protocol-2024--11--05-blue.svg)](https://modelcontextprotocol.io)
[![GDPR Sovereign](https://img.shields.io/badge/Data%20Sovereignty-100%25%20EU%20GDPR-emerald.svg)](https://aidministratie.be/privacy/mcp)
[![Terms of Service](https://img.shields.io/badge/Terms-MCP%20%26%20API-orange.svg)](https://aidministratie.be/terms/mcp)
[![Publisher](https://img.shields.io/badge/Publisher-aidministratie.be-black.svg)](https://aidministratie.be)

Official Model Context Protocol (MCP) Streamable HTTP/SSE Gateway for **[aidministratie.be](https://aidministratie.be)** — Sovereign AI Agent-as-a-Service infrastructure for European SMEs.

Connect Claude, Cursor, Antigravity, or ChatGPT to your private company data room, autonomous workflow workers, and human-in-the-loop task queues with complete multi-tenant cryptographic isolation.

---

## 🛡️ Core Guarantees

* **Zero Foundation Model Training:** Your business data, contracts, invoices, and business cards are **never used to train or fine-tune public AI models**.
* **100% European Hosting:** Hosted entirely within ISO 27001-certified data centers in the EU (Germany & Finland).
* **AES-256 Envelope KMS Encryption:** Files committed to the Virtual File System (VFS) are encrypted at rest with tenant-isolated keys.
* **Human-in-the-Loop (HITL):** High-stakes mutations (ERP/CRM changes, outbound emails, filings) are staged in a review queue for explicit human authorization.

---

## 🛠️ Available MCP Tools

| Tool | Description |
| :--- | :--- |
| `check_agent_status` | Inspect the real-time health, worker heartbeats, and queue status of your tenant. |
| `haal_wachtende_taken_op` | Fetch staged administrative actions awaiting human review and approval. |
| `beoordeel_wachtende_taak` | Approve (`approved`) or reject (`rejected`) a staged mutation with feedback traces. |
| `trigger_visitekaartjes_scan` | Ingest and OCR business cards directly into your tenant database and CRM. |
| `trigger_prospectie_scan` | Process conference prospects with multi-image OCR and CRM enrichment. |
| `list_files` | List files and directories within your encrypted Virtual File System (VFS). |
| `read_file_content` | Securely retrieve document contents from tenant storage. |
| `write_file_content` | Commit or update files in your encrypted tenant storage. |
| `voeg_agent_leermoment_toe` | Record a domain heuristic or prompt adjustment for your autonomous agents. |

---

## 🚀 Quickstart & Configuration

### 1. Claude Desktop (`claude_desktop_config.json`)
Connect directly via SSE:

```json
{
  "mcpServers": {
    "aidministratie": {
      "url": "https://loket.aidministratie.be/?token=YOUR_TENANT_API_KEY"
    }
  }
}
```

### 2. Cursor (`.cursor/mcp.json`)

```json
{
  "mcpServers": {
    "aidministratie": {
      "url": "https://loket.aidministratie.be",
      "headers": {
        "Authorization": "Bearer YOUR_TENANT_API_KEY"
      }
    }
  }
}
```

### 3. Google Antigravity (`~/.gemini/antigravity/mcp_config.json`)

```json
{
  "mcpServers": {
    "aidministratie": {
      "serverUrl": "https://loket.aidministratie.be",
      "headers": {
        "Authorization": "Bearer YOUR_TENANT_API_KEY"
      }
    }
  }
}
```

---

## 🔐 Authentication

To interact with your tenant gateway, generate a live API Key (`vlw_live_...`) in the [aidministratie Loket](https://loket.aidministratie.be).

Credentials can be passed via:
* **HTTP Header:** `Authorization: Bearer vlw_live_...`
* **Query Parameter:** `https://loket.aidministratie.be/mcp?token=vlw_live_...`

---

## 📄 Compliance & Legal

* **Privacy Policy:** [https://aidministratie.be/privacy/mcp](https://aidministratie.be/privacy/mcp)
* **Terms of Service:** [https://aidministratie.be/terms/mcp](https://aidministratie.be/terms/mcp)
* **Security & Inquiries:** `privacy@aidministratie.be`
* **Operated by:** Bram Vanzieleghem / ITeratief (BE 0671.637.106)
