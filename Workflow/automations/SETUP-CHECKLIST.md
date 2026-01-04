# Work Laptop Setup Checklist

> **Purpose**: Get a new Mac set up to capture and export emails + transcripts to the shared Obsidian vault  
> **Last Updated**: 2026-01-04

This checklist ensures your work laptop is configured to save all collateral (emails, transcriptions, voice memos) into the Notes vault for AI processing.

---

## Prerequisites

- [ ] Work laptop with macOS
- [ ] Same Apple ID as your personal Mac (for iCloud + Shortcuts sync)
- [ ] MacWhisper license (if not already purchased, install from App Store)
- [ ] Obsidian installed (recommended for viewing notes + task dashboard)
- [ ] Obsidian Tasks plugin installed (for `TASKS.md` dashboard)

---

## Phase 1: iCloud Documents Sync

The Notes vault lives in iCloud Documents and syncs automatically between Macs.

### 1.1 Enable iCloud Documents

1. Open **System Settings** → **Apple ID** → **iCloud**
2. Click **iCloud Drive** → **Options...**
3. Ensure **Documents** is checked ✓
4. Click **Done**

### 1.2 Verify Sync

1. Open Finder → Go to `~/Documents/`
2. Look for the `Notes/` folder
3. If it shows a cloud icon ☁️, click to download
4. Wait for the folder structure to appear:
   ```
   ~/Documents/Notes/
   ├── Inbox/
   │   ├── Email/
   │   ├── Transcripts/
   │   └── Voice/
   ├── Personal/
   ├── VAST/
   └── Workflow/
   ```

### 1.3 Verify Offline Availability

For critical folders, right-click and select "Keep Downloaded":
- `Inbox/`
- `Workflow/`

---

## Phase 2: Apple Shortcuts Sync

Shortcuts sync via iCloud. Your "Mail to Inbox" shortcut should appear automatically.

### 2.1 Verify Shortcuts Sync

1. Open **Shortcuts** app
2. Look for **"Mail to Inbox"** shortcut
3. If missing, wait a few minutes for iCloud sync
4. If still missing after 10 minutes, see [Rebuilding Shortcuts](#rebuilding-shortcuts)

### 2.2 Set Keyboard Shortcut (Per-Machine)

**Keyboard shortcuts do NOT sync between Macs.** You must set this manually:

1. In Shortcuts app, right-click **"Mail to Inbox"**
2. Select **Add Keyboard Shortcut**
3. Press `⌃⌥⌘M` (Control + Option + Command + M)
4. Verify the shortcut appears in the details pane

### 2.3 Grant Permissions

The first time you run the shortcut, macOS will prompt for permissions:

| Permission                 | How to Grant                              |
| -------------------------- | ----------------------------------------- |
| Automation → Mail          | Accept the prompt, or grant in Settings   |
| Automation → System Events | Accept the prompt                         |
| Accessibility              | System Settings → Privacy & Security → Accessibility → Shortcuts ✓ |

**To check/fix permissions manually:**
1. System Settings → Privacy & Security → Automation
2. Find **Shortcuts**
3. Enable **Mail** ✓
4. Enable **System Events** ✓

---

## Phase 3: MacWhisper Setup

MacWhisper records and transcribes meetings with speaker diarization.

### 3.1 Install MacWhisper

1. Open **App Store**
2. Search for **MacWhisper**
3. Install (or restore if already purchased)

### 3.2 Configure Export Settings

Follow the detailed guide: [macwhisper-setup.md](macwhisper-setup.md)

**Quick settings:**
- Output Format: **Markdown**
- Speaker Diarization: **Enabled**
- Auto-Export: **Enabled**
- Export Path: `~/Documents/Notes/Inbox/Transcripts/`

### 3.3 Test Recording

1. Record a 30-second test clip
2. Name it "Test Recording"
3. Let transcription complete
4. Verify file appears in `~/Documents/Notes/Inbox/Transcripts/`

---

## Phase 4: Python Environment (Optional)

If you want to run the extraction pipeline locally:

### 4.1 Install Dependencies

```bash
cd ~/Documents/Notes/Workflow
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 4.2 Configure Environment

```bash
cp .env.example .env
# Edit .env with your OpenAI API key
```

### 4.3 Verify Pipeline

```bash
source .venv/bin/activate
python scripts/process_inbox.py --dry-run
```

---

## Phase 5: VS Code Setup (Optional)

For the best experience with agent-assisted processing:

### 5.1 Install VS Code

Download from https://code.visualstudio.com/

### 5.2 Open Workspace

1. File → Open Workspace from File...
2. Select `~/Documents/Notes/Notes.code-workspace`

### 5.3 Install Recommended Extensions

When prompted, install recommended extensions:
- Python
- GitHub Copilot
- Markdown All in One

---

## Verification Tests

Run these tests to confirm everything works:

### Email Export Test

1. Open **Mail** app
2. Select any email
3. Press `⌃⌥⌘M`
4. Check `~/Documents/Notes/Inbox/Email/` for new `.md` file
5. Open the file and verify content looks correct

### MacWhisper Test

1. Open **MacWhisper**
2. Record a short clip (name it "Setup Test")
3. Wait for transcription
4. Check `~/Documents/Notes/Inbox/Transcripts/` for `.md` file
5. Verify speaker labels appear in output

### iCloud Sync Test

1. Create a test file on work laptop:
   ```bash
   echo "test" > ~/Documents/Notes/Inbox/_test.md
   ```
2. On personal laptop, verify file appears within 1-2 minutes
3. Delete the test file from either machine

### Tasks Dashboard Test (Obsidian)

1. Open Obsidian and load the `Notes` vault
2. Ensure the **Tasks** community plugin is enabled
3. Open `TASKS.md`
4. Verify query blocks render task results (and completing a task updates the source note)

---

## Rebuilding Shortcuts

If the Mail to Inbox shortcut didn't sync or needs to be rebuilt:

1. Open **Shortcuts** app
2. Click **+** to create new shortcut
3. Name it `Mail to Inbox`
4. Add action: **Run AppleScript**
5. Copy the AppleScript from [mail-to-inbox.md](mail-to-inbox.md#applescript-source)
6. Save and set keyboard shortcut to `⌃⌥⌘M`

---

## Troubleshooting

### "Mail to Inbox" shortcut not syncing

1. Check both Macs are signed into the same Apple ID
2. In Shortcuts, check "iCloud" under your library
3. Try signing out/in to iCloud on the work laptop

### Email export creates empty file

1. Make sure an email is actually selected in Mail
2. Check Accessibility permissions for Shortcuts
3. Try selecting a single email (not a thread)

### MacWhisper files not appearing

1. Verify export path in MacWhisper settings
2. Check iCloud sync status in Finder
3. Look in `~/Library/Mobile Documents/` for stuck files

### Permission denied errors

1. System Settings → Privacy & Security → Full Disk Access
2. Add Terminal and/or Shortcuts if needed

---

## Daily Workflow

Once set up, your daily capture workflow is:

| Activity          | How                                | Destination             |
| ----------------- | ---------------------------------- | ----------------------- |
| Capture email     | Select in Mail → `⌃⌥⌘M`            | `Inbox/Email/`          |
| Record meeting    | MacWhisper (auto-exports)          | `Inbox/Transcripts/`    |
| Voice memo        | (Future) Voice Memo integration    | `Inbox/Voice/`          |
| Manual drop       | Drag files to Inbox/Attachments    | `Inbox/Attachments/`    |

End of day: Run `Process Inbox` task in VS Code or manually trigger the pipeline.

---

## Quick Reference

| Hotkey   | Action                 |
| -------- | ---------------------- |
| `⌃⌥⌘M`   | Export email to Inbox  |

| Folder                 | Contains                     |
| ---------------------- | ---------------------------- |
| `Inbox/Email/`         | Exported email threads       |
| `Inbox/Transcripts/`   | MacWhisper transcripts       |
| `Inbox/Voice/`         | Voice memos (future)         |
| `Inbox/Attachments/`   | Manually dropped files       |
| `Inbox/_extraction/`   | AI extraction JSON (temp)    |
| `Inbox/_archive/`      | Processed source files       |
