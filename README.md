# Nitrosend for Cursor

AI-native email marketing inside Cursor. Compose emails, build automation flows, manage contacts, and send campaigns — all from your editor.

Powered by 20 MCP tools and a 65K-word email marketing knowledge base (908 sources, 4,798 insights across 19 industry playbooks).

## Quick Start

### 1. Get your API key

Get your API key at [nitrosend.com/settings/api-keys](https://nitrosend.com/settings/api-keys). It starts with `nskey_live_`.

### 2. Set your API key

Add to your shell profile (`~/.zshrc` or `~/.bashrc`):

```bash
export NITROSEND_API_KEY=nskey_live_your_key_here
```

### 3. Install the MCP server

**One-click install:**

[Install Nitrosend MCP in Cursor](cursor://anysphere.cursor-deeplink/mcp/install?name=nitrosend&config=eyJjb21tYW5kIjoibnB4IiwiYXJncyI6WyIteSIsIkBuaXRyb3NlbmQvbWNwQGxhdGVzdCJdLCJlbnYiOnsiTklUUk9TRU5EX0FQSV9LRVkiOiIke2VudjpOSVRST1NFTkRfQVBJX0tFWX0ifX0=)

**Or manually** — add to your `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "nitrosend": {
      "command": "npx",
      "args": ["-y", "@nitrosend/mcp@latest"],
      "env": {
        "NITROSEND_API_KEY": "${env:NITROSEND_API_KEY}"
      }
    }
  }
}
```

Restart Cursor after saving.

### 4. Verify connection

Open Cursor Chat and ask:

```
Check my Nitrosend account status
```

If connected, you'll see your account info and any onboarding steps.

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

### Analytics
Account-wide and per-campaign insights with trends and industry benchmarks.

```
How are my flows performing this month? Compare against benchmarks.
```

## MCP Tools (20)

| Tool | Description |
|------|-------------|
| `nitro_get_status` | Account health and onboarding state |
| `nitro_set_brand` | Brand identity from URL or manual fields |
| `nitro_manage_domains` | Add and verify sending domains |
| `nitro_configure_account` | Sender defaults and test recipients |
| `nitro_compose_email` | Create, update, or clone email templates |
| `nitro_compose_campaign` | Create email or SMS campaigns |
| `nitro_compose_flow` | Build automation flows |
| `nitro_control_delivery` | Approve, schedule, pause, or cancel delivery |
| `nitro_review_and_test` | Review email content and send test emails |
| `nitro_send_message` | Send transactional email or SMS immediately |
| `nitro_manage_audience` | Create contacts, manage lists, tags, events |
| `nitro_import_contacts` | Bulk import contact records |
| `nitro_define_segment` | Build segments with filters and preview |
| `nitro_search_contacts` | Find contacts by email, name, or phone |
| `nitro_query` | Query campaigns, flows, templates, segments |
| `nitro_get_insights` | Analytics with trends and benchmarks |
| `nitro_manage_billing` | Plan status and upgrades |
| `nitro_configure_providers` | BYO email provider (Mailgun, SES) |
| `nitro_set_memory` | Persistent AI memory across sessions |
| `nitro_request_support` | Submit a support request |

## Requirements

- Cursor with MCP support
- Node.js 18+
- Nitrosend API key (`NITROSEND_API_KEY` environment variable)

## Links

- [Nitrosend](https://nitrosend.com)
- [API docs](https://api.nitrosend.com)
- [MCP package (@nitrosend/mcp)](https://www.npmjs.com/package/@nitrosend/mcp)
- [Email Marketing Bible](https://emailmarketingskill.com)

## License

MIT
