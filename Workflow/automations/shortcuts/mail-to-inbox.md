# Shortcut: Mail to Inbox

> **Status**: ✅ Active  
> **Hotkey**: `⌃⌥⌘M` (Control + Option + Command + M)  
> **Output**: `~/Documents/Notes/Inbox/Email/`

## Purpose

Captures the currently selected email thread from Apple Mail and exports it as a Markdown file to the Inbox for later processing by the AI extraction pipeline.

## Behavior

1. Reads the selected message in Mail
2. Expands selection to full thread (via `⌘⇧K` — "View → Select → All Messages in this Thread")
3. Sorts messages oldest → newest
4. Exports as Markdown with:
   - Thread subject as title
   - Export timestamp
   - Message count
   - Each message as a blockquoted section with sender, date, subject

## Output Format

**Filename**: `YYYY-MM-DD_HHMMSS_NNNN_{Subject-slug}.md`

Example: `2025-12-15_143022_4821_RE-VAST-Microsoft-Ignite.md`

**Content structure**:

```markdown
# RE: VAST Microsoft Ignite

- Exported: 2025-12-15 14:30:22
- Messages: 5

---

## 2025-12-10 09:15:22 — John Doe <john@example.com>

**Subject:** VAST Microsoft Ignite

> Original message content here...
> Multiple lines are blockquoted.

---

## 2025-12-11 14:22:33 — Jane Smith <jane@example.com>

**Subject:** RE: VAST Microsoft Ignite

> Reply content here...

---
```

---

## Setup Instructions

### Creating the Shortcut

1. Open **Shortcuts** app
2. Click **+** to create new shortcut
3. Name it: `Mail to Inbox`
4. Add action: **Run AppleScript**
5. Paste the script from [AppleScript Source](#applescript-source) below
6. Save the shortcut

### Setting the Hotkey

1. In Shortcuts, right-click `Mail to Inbox`
2. Select **Add Keyboard Shortcut**
3. Press `⌃⌥⌘M`
4. Verify it appears in the shortcut details

### Granting Permissions

The first time you run this shortcut, macOS will prompt for permissions:

| Permission                 | Location                           | Required For                             |
| -------------------------- | ---------------------------------- | ---------------------------------------- |
| Automation → Mail          | Privacy & Security → Automation    | Reading email content                    |
| Automation → System Events | Privacy & Security → Automation    | Selecting all messages in thread (`⌘⇧K`) |
| Accessibility              | Privacy & Security → Accessibility | UI scripting (keystroke simulation)      |

If permissions were denied, go to System Settings → Privacy & Security and enable manually.

---

## Verification Checklist

Run through this checklist on each Mac to confirm proper setup:

- [ ] Shortcut `Mail to Inbox` appears in Shortcuts app
- [ ] Keyboard shortcut `⌃⌥⌘M` is assigned
- [ ] Automation permission granted for Mail
- [ ] Automation permission granted for System Events
- [ ] `~/Documents/Notes/Inbox/Email/` folder exists
- [ ] Test: Select an email, press `⌃⌥⌘M`, verify `.md` file created

---

## AppleScript Source

Keep this as the canonical version. If the Shortcut needs to be rebuilt, copy from here.

```applescript
on run {input, parameters}
	-- === CONFIG ===
	-- Vault root (or whatever folder contains Inbox/Email)
	set destFolder to (POSIX path of (path to documents folder)) & "Notes"
	set subfolder to "Inbox/Email"

	-- ==============

	-- Ensure output folder exists
	set outDir to destFolder
	if subfolder is not "" then set outDir to (destFolder & "/" & subfolder)
	do shell script "mkdir -p " & quoted form of outDir

	-- Grab current selection (must exist)
	tell application "Mail"
		set preSel to selection
		if preSel is {} then error "No message selected in Mail."
	end tell

	-- If only one message is selected, expand selection to whole thread via Cmd-Shift-K
	-- (View → Select → All Messages in this Thread)
	if (count of preSel) = 1 then
		my selectAllMessagesInThread()
	end if

	-- Now re-read selection (should be the whole thread if available)
	tell application "Mail"
		set msgs to selection
		if msgs is {} then error "No message selected in Mail."
	end tell

	-- Sort oldest → newest
	set msgs to my sortMessagesByDate(msgs)

	-- Use newest message for filename timestamp
	tell application "Mail"
		set newestMsg to item (count of msgs) of msgs
		set threadSubject to subject of newestMsg
		set newestDate to date received of newestMsg
	end tell

	-- Timestamp + random suffix for uniqueness
	set newestParts to my dateParts(newestDate)
	set newestDateStamp to item 1 of newestParts
	set newestTimeNoColons to item 2 of newestParts

	set r to random number from 0 to 9999
	set rand4 to text -4 thru -1 of ("0000" & (r as string))

	-- Safe subject for filename
	set safeSubject to do shell script ¬
		"echo " & quoted form of threadSubject & " | tr -cd '[:alnum:] _-' | tr ' ' '-' | cut -c1-60"
	if safeSubject is "" then set safeSubject to "Email-Thread"

	set fileName to newestDateStamp & "_" & newestTimeNoColons & "_" & rand4 & "_" & safeSubject & ".md"
	set outPath to outDir & "/" & fileName

	-- Build markdown
	set exportStamp to my prettyDate(current date)
	set mdOutput to "# " & threadSubject & return & return & ¬
		"- Exported: " & exportStamp & return & ¬
		"- Messages: " & (count of msgs) & return & ¬
		"---" & return & return

	repeat with m in msgs
		tell application "Mail"
			set s to subject of m
			set who to sender of m
			set d to date received of m
			set bodyText to content of m
		end tell

		set mdOutput to mdOutput & "## " & (my prettyDate(d)) & " — " & who & return
		if s is not "" then set mdOutput to mdOutput & "**Subject:** " & s & return
		set mdOutput to mdOutput & return & (my blockquote(bodyText)) & return & return & "---" & return & return
	end repeat

	-- Write file as UTF-8
	my writeUTF8(mdOutput, outPath)

	return outPath
end run

-- Press Cmd-Shift-K in Mail to select all messages in the current thread
on selectAllMessagesInThread()
	tell application "Mail" to activate
	delay 0.15

	try
		tell application "System Events"
			tell process "Mail"
				set frontmost to true
				keystroke "k" using {command down, shift down}
			end tell
		end tell
	on error
		-- If UI scripting isn't permitted, we'll just continue with the single selected message.
	end try

	delay 0.25
end selectAllMessagesInThread

-- Sort a list of Mail message objects by date received (ascending)
on sortMessagesByDate(msgs)
	set sorted to msgs
	set n to count of sorted

	if n ≤ 1 then return sorted

	repeat with i from 1 to n - 1
		repeat with j from i + 1 to n
			set mi to item i of sorted
			set mj to item j of sorted

			tell application "Mail"
				set di to date received of mi
				set dj to date received of mj
			end tell

			if di > dj then
				set item i of sorted to mj
				set item j of sorted to mi
			end if
		end repeat
	end repeat

	return sorted
end sortMessagesByDate

-- Returns {YYYY-MM-DD, HHMMSS} for filenames
on dateParts(d)
	set y to year of d as string
	set mo to text -2 thru -1 of ("0" & (month of d as integer))
	set da to text -2 thru -1 of ("0" & (day of d as integer))
	set hh to text -2 thru -1 of ("0" & (hours of d as integer))
	set mi to text -2 thru -1 of ("0" & (minutes of d as integer))
	set ss to text -2 thru -1 of ("0" & (seconds of d as integer))

	set dateStamp to y & "-" & mo & "-" & da
	set timeNoColons to hh & mi & ss

	return {dateStamp, timeNoColons}
end dateParts

on prettyDate(d)
	set parts to my dateParts(d)
	set dateStamp to item 1 of parts

	set hh to text 1 thru 2 of (item 2 of parts)
	set mi to text 3 thru 4 of (item 2 of parts)
	set ss to text 5 thru 6 of (item 2 of parts)

	return dateStamp & " " & hh & ":" & mi & ":" & ss
end prettyDate

on blockquote(t)
	-- Normalize linefeeds to returns
	set t to my replaceText(linefeed, return, t)

	set AppleScript's text item delimiters to return
	set parts to text items of t
	set AppleScript's text item delimiters to return & "> "
	set q to parts as string
	set AppleScript's text item delimiters to ""

	return "> " & q
end blockquote

on replaceText(findText, replaceWith, theText)
	set AppleScript's text item delimiters to findText
	set parts to text items of theText
	set AppleScript's text item delimiters to replaceWith
	set theText to parts as string
	set AppleScript's text item delimiters to ""
	return theText
end replaceText

on writeUTF8(t, posixPath)
	set f to POSIX file posixPath
	set refNum to open for access f with write permission
	try
		set eof of refNum to 0
		write t to refNum as «class utf8»
		close access refNum
	on error errMsg number errNum
		try
			close access refNum
		end try
		error errMsg number errNum
	end try
end writeUTF8
```

---

## Known Limitations

1. **Attachments not captured**: Only email body text is exported. Attachments are ignored.
2. **HTML stripped**: Rich formatting is lost; only plain text content is preserved.
3. **Thread selection requires UI scripting**: The `⌘⇧K` keystroke needs Accessibility permission.
4. **Single mailbox only**: If thread spans multiple mailboxes, may not capture all messages.

---

## Resolved Design Decisions

| Topic   | Decision                       | Rationale                        |
| ------- | ------------------------------ | -------------------------------- |
| ING-1.2 | Full thread (option A)         | More context for AI extraction   |
| ING-1.3 | Ignore attachments (option A)  | Keep it simple for v1            |
| ING-1.4 | Strip to plain text (option A) | Markdown-native, simpler parsing |
