# Security Policy

## Reporting a vulnerability

Email **contact@nitrosend.com** with the details. Please do not open a public
GitHub issue for security reports.

Include where you can: what you found, how to reproduce it, and the impact you
believe it has. We will acknowledge your report and keep you updated on the fix.

## Scope

This repository contains plugin metadata only: manifests for Cursor
(`.cursor-plugin/plugin.json`) and Grok Build (`.grok-plugin/plugin.json`),
MCP server configs (`mcp.json`, `.mcp.json`) pointing at the hosted Nitrosend
MCP server, README and assets. It ships no executable code.

Vulnerabilities in the Nitrosend service or its MCP server itself should also go
to contact@nitrosend.com. See <https://nitrosend.com/security>.

## Data handling

The plugin connects Cursor or Grok Build to your own Nitrosend account over
OAuth. See the
[privacy policy](https://nitrosend.com/privacy) for how Nitrosend handles data.
