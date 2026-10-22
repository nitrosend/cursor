# Changelog

## 1.2.0

- Ship eight agent skills (`skills/`): setup, compose-email, send-campaign, build-flow, send-transactional, import-contacts, analytics and an email marketing reference. Cursor, Grok Build and Grok Bot load them with the plugin.
- Use the 858x858 v2 Nitrosend logo.
- Bump the Cursor and Grok Build manifests to 1.2.0.
- Remove em dashes from the README.

- Added a Grok Build manifest (`.grok-plugin/plugin.json`) and a standard
  `.mcp.json` so the same repo installs from the xAI plugin marketplace.
  No change to the Cursor plugin.
- Removed a fixed tool count and clarified the hosted OAuth connection in the Grok Build plugin manifest.

## 1.1.1

- Clarify the Cursor listing around the hosted MCP connection and current email workflows.
- Use the current Nitrosend mark in the marketplace card.

## 1.1.0

- Added an MIT `LICENSE` file (the manifest already declared MIT).
- Documented the full tool surface: 23 → 28 tools. Adds `nitro_inbox`,
  `nitro_inbox_action`, `nitro_manage_outreach`, `nitro_search_docs` and
  `nitro_select_account`.
- Renamed `nitro_ingest_image` → `nitro_ingest` to match the server.
- Switched the default install to a direct remote MCP URL instead of the
  `npx mcp-remote` stdio shim. The shim is kept as a documented fallback.
- Corrected the BYO sending provider list to SES, Mailgun, Postmark, Resend
  and SendGrid.
- Replaced the dead `api.nitrosend.com` documentation link with
  `docs.nitrosend.com`.
- Added support, privacy, terms and security links, and a note that the plugin
  itself is free.
- Grouped the tool table by area and added an agent inbox usage example.

## 1.0.0

- Initial release: Nitrosend MCP server as a Cursor plugin.
