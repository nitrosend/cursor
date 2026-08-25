# Changelog

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
