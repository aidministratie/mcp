#!/usr/bin/env python3
"""
aidministratie.be // MCP Stdio-to-HTTP Gateway Bridge
Open-Source Client Adapter for Model Context Protocol (MCP) clients.

Bridges local stdio-based MCP clients (such as Claude Desktop, Cursor, and Antigravity)
to the sovereign remote aidministratie.be gateway (https://loket.aidministratie.be).

Usage:
  python bridge.py --token <YOUR_TENANT_API_KEY>
  Or set environment variable: AIDMINISTRATIE_API_KEY=<token>
"""

import os
import sys
import json
import argparse
import urllib.request
import urllib.error

DEFAULT_GATEWAY_URL = os.environ.get("AIDMINISTRATIE_GATEWAY_URL", "https://loket.aidministratie.be")

def forward_request(gateway_url: str, token: str, payload: dict) -> dict:
    url = gateway_url.rstrip("/") + "/"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream",
        "x-api-key": token,
        "Authorization": f"Bearer {token}",
        "User-Agent": "aidministratie-mcp-bridge/1.0"
    }
    
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            content_type = resp.headers.get("Content-Type", "")
            raw = resp.read().decode("utf-8")
            
            # FastMCP streamable response format handling
            if "text/event-stream" in content_type or raw.startswith("event:") or raw.startswith("data:"):
                for line in raw.splitlines():
                    if line.startswith("data:"):
                        json_str = line[len("data:"):].strip()
                        if json_str:
                            return json.loads(json_str)
            return json.loads(raw)
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")
        return {
            "jsonrpc": "2.0",
            "id": payload.get("id"),
            "error": {
                "code": e.code,
                "message": f"HTTP {e.code}: {err_body}"
            }
        }
    except Exception as e:
        return {
            "jsonrpc": "2.0",
            "id": payload.get("id"),
            "error": {
                "code": -32603,
                "message": f"Bridge error: {str(e)}"
            }
        }

def main():
    parser = argparse.ArgumentParser(description="aidministratie.be MCP Stdio Bridge")
    parser.add_argument("--token", "-t", default=os.environ.get("AIDMINISTRATIE_API_KEY"),
                        help="Your aidministratie.be Tenant API Key (starts with vlw_live_...)")
    parser.add_argument("--url", "-u", default=DEFAULT_GATEWAY_URL,
                        help="Gateway URL (defaults to https://loket.aidministratie.be)")
    args = parser.parse_args()

    token = args.token
    if not token:
        sys.stderr.write("Error: Missing API token. Pass --token or set AIDMINISTRATIE_API_KEY environment variable.\\n")
        sys.exit(1)

    # Process JSON-RPC lines from stdin
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req_json = json.loads(line)
            resp_json = forward_request(args.url, token, req_json)
            sys.stdout.write(json.dumps(resp_json) + "\\n")
            sys.stdout.flush()
        except Exception as e:
            err_resp = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32700, "message": f"Parse error: {str(e)}"}
            }
            sys.stdout.write(json.dumps(err_resp) + "\\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
