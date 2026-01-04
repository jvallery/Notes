# MacWhisper Configuration for Notes Vault

> **Status**: ⏳ Pending Setup  
> **Output**: `~/Documents/Notes/Inbox/Transcripts/`

## Purpose

Automatically export meeting transcripts from MacWhisper to the Inbox for processing by the AI extraction pipeline. Speaker diarization provides context for identifying participants and attributing tasks/statements.

---

## Required Settings

| Setting              | Value                                          |
| -------------------- | ---------------------------------------------- |
| Output Format        | **Markdown**                                   |
| Speaker Diarization  | **Enabled**                                    |
| Auto-Export          | **Enabled**                                    |
| Export Path          | `~/Documents/Notes/Inbox/Transcripts/`         |
| Filename Pattern     | `%Y-%m-%d %H %M - {title}.md`                  |

---

## Setup Instructions

### 1. Configure MacWhisper Preferences

1. Open **MacWhisper**
2. Go to **MacWhisper → Settings** (or `⌘,`)
3. Navigate to the **Export** tab

### 2. Set Output Format

1. Under "Default Export Format", select **Markdown**
2. Ensure "Include timestamps" is enabled (optional, but helpful)
3. Ensure "Include speaker labels" is enabled

### 3. Enable Speaker Diarization

1. Navigate to **Transcription** tab (or similar)
2. Enable **Speaker Diarization** / **Identify Speakers**
3. This is critical for the AI to attribute statements to participants

### 4. Configure Auto-Export

1. In Export settings, enable **"Auto-export after transcription"**
2. Set the export folder to:
   ```
   ~/Documents/Notes/Inbox/Transcripts/
   ```
   (Click "Choose..." and navigate to this folder)

### 5. Filename Pattern

MacWhisper uses the recording title for the filename. Before starting a recording:

1. Name your recording descriptively:
   - `Jeff Denworth 1-1`
   - `Google GDC RFP Call`
   - `Team Standup`
2. The output will be: `2026-01-04 14 30 - Jeff Denworth 1-1.md`

---

## Expected Output Format

MacWhisper produces markdown like:

```markdown
# Jeff Denworth 1-1

## Transcript

**Speaker 1** (00:00):
Hi Jeff, how's it going?

**Speaker 2** (00:03):
Good, good. Let's dive into the Q1 pipeline...

**Speaker 1** (00:15):
Sure. I've got updates on the Google deal...
```

The extraction pipeline parses speaker labels to:
- Identify participants
- Attribute tasks and commitments
- Track who said what for context

---

## Verification Checklist

Run through this checklist on your work Mac:

- [ ] MacWhisper installed and licensed
- [ ] Speaker diarization enabled
- [ ] Export format set to Markdown
- [ ] Auto-export enabled
- [ ] Export path set to `~/Documents/Notes/Inbox/Transcripts/`
- [ ] iCloud Documents syncing `~/Documents/Notes/`
- [ ] Test: Record a short clip, verify `.md` file appears in Inbox/Transcripts

---

## Troubleshooting

### No speaker labels in output?
- Check Settings → Transcription → Speaker Diarization is ON
- Some audio may not have enough speaker separation to diarize

### File not appearing in Inbox/Transcripts?
- Verify the export path in MacWhisper settings
- Check if iCloud is syncing (blue cloud icon in Finder)
- Check ~/Library/Mobile Documents/ for stuck files

### Wrong filename format?
- Ensure you name the recording BEFORE exporting
- "New Recording" is the default if no title is set

### Encoding issues?
- MacWhisper outputs UTF-8 by default
- If you see garbled characters, check the file encoding in VS Code

---

## Alternative: Manual Export

If auto-export isn't working or you prefer manual control:

1. After transcription, click **Export** (or `⌘E`)
2. Choose **Markdown** format
3. Navigate to `~/Documents/Notes/Inbox/Transcripts/`
4. Use naming convention: `YYYY-MM-DD HH MM - Title.md`

---

## Known Limitations

1. **Speaker names not preserved**: MacWhisper uses "Speaker 1", "Speaker 2", etc. The AI extraction pipeline infers real names from context and participant lists.

2. **Timestamp format varies**: Depending on settings, timestamps may be `(00:00)` or `[00:00:00]`. The pipeline handles both.

3. **Large files**: Very long meetings (2+ hours) may produce large markdown files. Consider splitting recordings.

---

## Related Automations

| Automation    | Purpose                              |
| ------------- | ------------------------------------ |
| Mail to Inbox | Email export (`⌃⌥⌘M`)                |
| Process Inbox | Run extraction pipeline (VS Code)   |

