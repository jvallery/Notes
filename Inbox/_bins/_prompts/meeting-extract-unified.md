You are extracting structured intelligence from a meeting transcript.

# Run Context
- note_type: {{VALUE:note_kind_key}}          // e.g., people | customer | partners | projects | rob | journal | travel
- note_type_label: {{VALUE:note_kind_label}}  // e.g., People
- subtemplate_name: {{VALUE:sub_template}}    // e.g., Person
- destination_folder: {{VALUE:target_folder_path}}
- leaf (entity/folder): {{VALUE:entity_name}}
- transcript_title: {{VALUE:transcript_title}}
- extra_context (may include attendee list, agenda, objectives, timebox, location): {{VALUE:extra_context}}

# Subtemplate (type-specific guidance)
{{VALUE:sub_prompt}}

# Deliverable
Return exactly **one** JSON object that follows the system schema and rules. No markdown code fences.

# Transcript
{{VALUE:transcript_text}}
