# Tasks

This is a dashboard powered by the Obsidian Tasks plugin.

- [R] ## Proposed (?) – triage first

```tasks
not done
tags include #task
status.name includes Proposed
status.type is not CANCELLED
path does not include Inbox/_archive/
path does not include Workflow/
group by backlink
sort by priority
sort by created
```

## Not Started ([ ]) – priority → created

```tasks
not done
tags include #task
status.name includes Not Started
status.type is not CANCELLED
path does not include Inbox/_archive/
path does not include Workflow/
group by backlink
sort by priority
sort by created
```

## In Progress (/) – priority → created

```tasks
not done
tags include #task
status.name includes In Progress
status.type is not CANCELLED
path does not include Inbox/_archive/
path does not include Workflow/
group by backlink
sort by priority
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
