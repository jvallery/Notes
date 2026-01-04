# Automations: Hotkeys, Shortcuts & Scripts

> **Last Updated**: 2026-01-03  
> **Related**: [DESIGN.md](../DESIGN.md) | [TOPICS.md](../TOPICS.md)

This folder contains all automation configurations for the knowledge management system. Because this vault syncs via iCloud between two Macs (Personal + Work), we document everything here so automations can be rebuilt on either machine.

---

## Multi-Mac Setup

| Environment | Machine          | Apple ID        | iCloud Status                |
| ----------- | ---------------- | --------------- | ---------------------------- |
| Personal    | Personal MacBook | (your Apple ID) | ✓ Syncs Documents, Shortcuts |
| Work        | Work MacBook     | (your Apple ID) | ✓ Syncs Documents, Shortcuts |

**Key sync behaviors:**

- **iCloud Documents**: `~/Documents/Notes/` syncs automatically
- **Apple Shortcuts**: Sync via iCloud (tied to Apple ID) — changes on one Mac appear on the other
- **AppleScript source**: Stored in this repo, but Shortcuts embed a _copy_ of the script
- **Keyboard shortcuts**: Do NOT sync — must be set manually per-machine

### First-Time Setup on a New Mac

1. **Verify iCloud Documents sync**

   - System Settings → Apple ID → iCloud → iCloud Drive → Options
   - Ensure "Documents" is checked
   - Wait for `~/Documents/Notes/` to sync

2. **Verify Shortcuts sync**

   - Open Shortcuts app
   - Confirm your shortcuts appear (may take a few minutes on first sync)

3. **Set keyboard shortcuts** (per-machine)

   - See [Hotkey Registry](#hotkey-registry) below
   - System Settings → Keyboard → Keyboard Shortcuts → Services

4. **Grant permissions**
   - Shortcuts needs Automation permission for Mail
   - System Settings → Privacy & Security → Automation → Shortcuts → Mail ✓

---

## Hotkey Registry

Central reference for all keyboard shortcuts. **Must be configured on each Mac.**

| Hotkey | Action                                | Implementation            | Status     |
| ------ | ------------------------------------- | ------------------------- | ---------- |
| `⌃⌥⌘M` | Export selected email thread to Inbox | Shortcut: "Mail to Inbox" | ✅ Active  |
| `⌃⌥⌘T` | (Future) Process pending transcripts  | TBD                       | ⏳ Planned |
| `⌃⌥⌘P` | (Future) Trigger agent processing     | TBD                       | ⏳ Planned |

### Setting Up Hotkeys

**For Shortcuts-based automations:**

1. Open **Shortcuts** app
2. Right-click the shortcut → "Add Keyboard Shortcut"
3. Press your key combination (e.g., `⌃⌥⌘M`)

**For Services/Quick Actions:**

1. System Settings → Keyboard → Keyboard Shortcuts → Services
2. Find your service under "General" or the relevant app
3. Double-click to set the shortcut

---

## Folder Structure

```
Workflow/automations/
├── README.md                    # This file (overview, hotkey registry)
├── shortcuts/                   # Apple Shortcuts documentation
│   ├── mail-to-inbox.md         # Email capture shortcut
│   └── (future shortcuts)
└── scripts/                     # Raw script files (for reference/rebuild)
    └── (AppleScript, shell scripts)
```

---

## Automation Inventory

### Active Automations

| Name          | Type                   | Trigger | Description                           | Docs                                           |
| ------------- | ---------------------- | ------- | ------------------------------------- | ---------------------------------------------- |
| Mail to Inbox | Shortcut + AppleScript | `⌃⌥⌘M`  | Export email thread to `Inbox/Email/` | [mail-to-inbox.md](shortcuts/mail-to-inbox.md) |

### Planned Automations

| Name                   | Type              | Trigger             | Description                       | Status       |
| ---------------------- | ----------------- | ------------------- | --------------------------------- | ------------ |
| MacWhisper auto-export | Folder Action     | On new file         | Move transcripts to archive       | Design phase |
| Process Inbox          | Python + Shortcut | `⌃⌥⌘P` or scheduled | Run extraction on all Inbox items | Design phase |
| Daily digest           | Python + launchd  | 6 PM daily          | Summarize day's updates           | Design phase |

---

## Troubleshooting

### Shortcut not working?

1. **Check Shortcuts app**: Is the shortcut present? (iCloud sync issue)
2. **Check permissions**: System Settings → Privacy & Security → Automation
3. **Check Mail is frontmost**: Shortcut requires Mail to be active
4. **Check hotkey conflict**: Another app may have claimed the shortcut

### AppleScript errors?

1. **"No message selected"**: Select an email in Mail before triggering
2. **"System Events got an error"**: Grant Accessibility permissions
   - System Settings → Privacy & Security → Accessibility → Shortcuts ✓
3. **File write errors**: Check `~/Documents/Notes/Inbox/Email/` exists

### Rebuilding a Shortcut

If a shortcut is lost or corrupted:

1. Open Shortcuts app
2. Create new shortcut
3. Add "Run AppleScript" action
4. Copy script from [mail-to-inbox.md](shortcuts/mail-to-inbox.md)
5. Save and set keyboard shortcut

---

## Version History

| Date       | Change                                        | Author |
| ---------- | --------------------------------------------- | ------ |
| 2026-01-03 | Initial documentation, Mail to Inbox shortcut | Jason  |
