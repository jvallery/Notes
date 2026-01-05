# Outbox

This folder contains AI-drafted email responses ready for review and sending.

## Workflow

1. When processing emails from `Inbox/Email/`, the pipeline identifies emails that need a response
2. AI drafts a response based on context from:
   - The email thread content
   - Related entity data (customer, person, project)
   - Open tasks and recent interactions
3. Drafts are saved here as `.md` files with the format: `YYYY-MM-DD_Reply-To_{Subject}.md`
4. Review, edit as needed, then copy to your email client
5. After sending, either:
   - Delete the draft, or
   - Move to `_sent/` folder to keep a record

## Draft Format

Each draft includes:
- **To:** Original sender
- **Subject:** Re: {original subject}
- **Context:** Summary of what prompted the response
- **Draft Body:** The suggested reply text

## Status Tags

Files may be tagged in frontmatter:
- `status: draft` — AI-generated, needs review
- `status: reviewed` — Human-edited, ready to send
- `status: sent` — Copied to email client and sent (if keeping records)
