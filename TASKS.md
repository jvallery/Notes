# Tasks

This is a dashboard powered by the Obsidian Tasks plugin.

## Accepted (All) – priority → due → created

```tasks
not done
tags include #task
tags do not include #proposed
path does not include Inbox/_archive/
path does not include Workflow/
sort by priority
sort by due
sort by created
```

## Work (VAST)

### Overdue

```tasks
not done
tags include #task
tags do not include #proposed
root includes VAST
path does not include Inbox/_archive/
due before today
group by backlink
sort by due
```

### Due Soon (next 2 weeks)

```tasks
not done
tags include #task
tags do not include #proposed
root includes VAST
path does not include Inbox/_archive/
due on or after today
due on or before in two weeks
group by backlink
sort by due
```

### No Due Date

```tasks
not done
tags include #task
tags do not include #proposed
root includes VAST
path does not include Inbox/_archive/
no due date
group by backlink
sort by priority
```

### All Open (by priority)

```tasks
not done
tags include #task
tags do not include #proposed
root includes VAST
path does not include Inbox/_archive/
short mode
group by priority
group by backlink
sort by priority
sort by due
sort by created
```

## Personal

### Overdue

```tasks
not done
tags include #task
tags do not include #proposed
root includes Personal
path does not include Inbox/_archive/
due before today
group by backlink
sort by due
```

### Due Soon (next 2 weeks)

```tasks
not done
tags include #task
tags do not include #proposed
root includes Personal
path does not include Inbox/_archive/
due on or after today
due on or before in two weeks
group by backlink
sort by due
```

### No Due Date

```tasks
not done
tags include #task
tags do not include #proposed
root includes Personal
path does not include Inbox/_archive/
no due date
group by backlink
sort by priority
```

### All Open (by priority)

```tasks
not done
tags include #task
tags do not include #proposed
root includes Personal
path does not include Inbox/_archive/
short mode
group by priority
group by backlink
sort by priority
sort by due
sort by created
```

## Proposed (needs acceptance)

```tasks
not done
tags include #task
tags include #proposed
path does not include Inbox/_archive/
path does not include Workflow/
group by backlink
sort by priority
sort by due
sort by created
```

## Inbox (capture list)

```tasks
not done
tags include #task
path includes TASKS_INBOX.md
sort by priority
sort by due
sort by created
```

## Backlog (legacy task list)

```tasks
not done
tags include #task
path includes TASKS_BACKLOG.md
group by heading
sort by priority
sort by due
```

## Untriaged (missing `#task`)

```tasks
not done
tags do not include #task
path does not include Inbox/_archive/
path does not include Workflow/
group by backlink
sort by created reverse
```
