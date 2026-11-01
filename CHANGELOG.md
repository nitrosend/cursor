# Changelog

## 1.3.0

- Use the Nitrosend icon, as on nitrosend.com and in the app: the mark on its orange plate, as Cursor asks for logos, rendered at 1024x1024 from the vector master (`assets/icon.svg`). 1.2.0 had brought back the 1.1.0 mark.
- Describe the plugin as nitrosend.com/integrations/cursor does: one prompt scans your site into a Brand Kit, designs your newsletter on brand, drafts your flows and sends you the test.
- README: start with one prompt to paste into Cursor's agent, and link to the generated [MCP tools reference](https://docs.nitrosend.com/mcp) instead of a hand-kept tool table.
- Bump the Cursor and Grok Build manifests to 1.3.0.

## 1.2.0

- Ship eight agent skills (`skills/`): setup, compose-email, send-campaign, build-flow, send-transactional, import-contacts, analytics and an email marketing reference. Cursor, Grok Build and Grok Bot load them with the plugin.
- Use the 858x858 v2 Nitrosend logo.
- Bump the Cursor and Grok Build manifests to 1.2.0.
- Remove em dashes from the README and skills.
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
