# Nitrosend for Cursor

AI-native email inside Cursor. Compose emails, build automation flows, manage contacts, and send campaigns — all from your editor.

Powered by 28 MCP tools and a 68K-word email marketing knowledge base (908 sources, 4,798 insights across 19 industry playbooks).

## Quick Start

### One-click install

[Install Nitrosend in Cursor](cursor://anysphere.cursor-deeplink/mcp/install?name=nitrosend&config=eyJ1cmwiOiJodHRwczovL2FwaS5uaXRyb3NlbmQuY29tL21jcCJ9)

On first use, your browser will open for Nitrosend sign-in. No API key needed.

### Manual install

Add to `~/.cursor/mcp.json` (global) or `.cursor/mcp.json` (project):

```json
{
  "mcpServers": {
    "nitrosend": {
      "url": "https://api.nitrosend.com/mcp"
    }
  }
}
```

Restart Cursor. On first tool call, your browser opens for Nitrosend sign-in (OAuth).

<details>
<summary>Older Cursor versions without remote MCP support</summary>

If your Cursor build cannot connect to a remote MCP server directly, use the stdio bridge instead:

```json
{
  "mcpServers": {
    "nitrosend": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://api.nitrosend.com/mcp"]
    }
  }
}
```

</details>

### Verify connection

Open Cursor Chat and ask:

```
Check my Nitrosend account status
```

## What You Can Do

### Email composition
Create section-based email templates with full brand styling, preview, and test sends.

```
Compose a welcome email for new SaaS signups — branded, with a single CTA to activate their account
```

### Automation flows
Build trigger-based sequences with waits, splits, webhooks, and SMS steps.

```
Build a 3-email cart abandonment flow: 1 hour, 24 hours, 72 hours. Include a 10% discount in the final email.
```

### Campaigns
Create, target, preview, approve, and send or schedule email and SMS campaigns.

```
Send our March newsletter to the "Active subscribers" segment, scheduled for Tuesday 10am
```

### Transactional email
Immediate single-recipient delivery for receipts, OTPs, confirmations.

```
Send a password reset email to user@example.com using the reset template
```

### Contact management
Import contacts, manage lists, define segments, bulk tag.

```
Import these 50 contacts and add them to the "Beta users" list
```

### Agent inboxes
Give your agent its own address, then read and reply to threads without leaving the editor.

```
Check my Nitrosend inbox and draft replies to anything that needs attention
```

### Analytics
Account-wide and per-campaign insights with trends and industry benchmarks.

```
How are my flows performing this month? Compare against benchmarks.
```

## MCP Tools (28)

### Account and brand

| Tool | Description |
|------|-------------|
| `nitro_get_status` | Account health, brand context, and onboarding state |
| `nitro_select_account` | Switch the OAuth MCP connection to another account |
| `nitro_select_brand` | Switch the current brand for OAuth MCP sessions |
| `nitro_set_brand_kit` | Brand Kit identity from a URL or manual fields |
| `nitro_manage_domains` | Add and verify sending domains |
| `nitro_configure_account` | Sender defaults and test recipients |
| `nitro_configure_providers` | BYO sending provider credentials and status (SES, Mailgun, Postmark, Resend, SendGrid) |
| `nitro_manage_billing` | Plan status and upgrades |

### Content and delivery

| Tool | Description |
|------|-------------|
| `nitro_manage_template` | Create, update, or clone email templates |
| `nitro_compose_campaign` | Create email or SMS campaigns |
| `nitro_compose_flow` | Build automation flows |
| `nitro_ingest` | Validate and store an image in the brand library, returning a durable email URL |
| `nitro_review_delivery` | Review content and delivery readiness |
| `nitro_control_delivery` | Approve, schedule, pause, or cancel delivery |
| `nitro_send_test_message` | Send test email or SMS messages |
| `nitro_send_message` | Immediate single-recipient transactional email or SMS |

### Contacts and segmentation

| Tool | Description |
|------|-------------|
| `nitro_manage_audience` | Create contacts, manage lists, tags, and events |
| `nitro_import_contacts` | Bulk import contact records |
| `nitro_define_segment` | Build segments with filters and preview counts |
| `nitro_search_contacts` | Find contacts by email, name, or phone |

### Inbox and outreach

| Tool | Description |
|------|-------------|
| `nitro_inbox` | Read the agent queue or mailbox |
| `nitro_inbox_action` | Reply to, handle, or escalate an inbox item |
| `nitro_manage_outreach` | Discover named people for outreach, gated by an explicit spend cap |

### Insight and support

| Tool | Description |
|------|-------------|
| `nitro_query` | Query campaigns, flows, templates, and segments |
| `nitro_get_insights` | Analytics with trends and industry benchmarks |
| `nitro_search_docs` | Search Nitrosend guides and API/MCP/CLI references |
| `nitro_set_memory` | Persistent AI memory across sessions |
| `nitro_request_support` | Submit a support request |

## Agents

Connecting from an agent surface — Cursor Chat, Cursor web, or a cloud agent like Grok Bot? Read the Nitrosend agent onboarding guide first: [nitrosend.com/SKILL.md](https://nitrosend.com/SKILL.md). The short version: call `nitro_get_status` before anything else, trust its snapshot over assumptions, and never approve or trigger a live send without explicit human confirmation.

## Requirements

- Cursor with MCP support — desktop, web, and cloud agents (including Grok Bot) are supported: the plugin connects to a remote MCP URL over OAuth, so no local process is required
- A Nitrosend account ([nitrosend.com](https://nitrosend.com))

This plugin is free. Nitrosend has a free tier; paid plans and usage are a separate, optional subscription to the Nitrosend service.

## Support

- Email: [contact@nitrosend.com](mailto:contact@nitrosend.com)
- [Documentation](https://docs.nitrosend.com)
- Security or vulnerability reports: [SECURITY.md](SECURITY.md)

## Links

- [Nitrosend](https://nitrosend.com)
- [Documentation](https://docs.nitrosend.com)
- [Agent onboarding guide (SKILL.md)](https://nitrosend.com/SKILL.md)
- [Privacy policy](https://nitrosend.com/privacy)
- [Terms](https://nitrosend.com/terms)
- [Security](https://nitrosend.com/security)
- [MCP package (@nitrosend/mcp)](https://www.npmjs.com/package/@nitrosend/mcp)
- [Email Marketing Bible](https://emailmarketingskill.com)

## License

[MIT](LICENSE)
