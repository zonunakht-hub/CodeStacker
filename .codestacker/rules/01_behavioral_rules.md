# 🤖 BEHAVIORAL RULES

## Response Structure
1. **Acknowledge** the request/mode
2. **Reference** relevant docs read
3. **State** current understanding
4. **Propose** next action or ask questions
5. **Wait** for user approval before implementation

## Decision Making
- Always check rules before acting
- Always check structure before coding
- Always check brief for current mode
- Always check last summary for progress

## Error Handling
- If error occurs: STOP → Document in reports/ → Inform user
- If plan fails: Document why → Suggest alternatives
- If confused: List what's missing → Ask specific questions

## Mode Behavior
- **New Project**: Ask for project details → Update all docs
- **Start**: Validate system → Check for missing docs → Report status
- **Plan**: Read structure → Create detailed plan → Save → Present for approval
- **Approved**: Execute checklist → Document progress → Update summaries
- **Free**: Skip planning but STILL document → Track what was done
- **Fix**: Read error → Create fix plan → Execute → Verify
- **Proceed**: Read last summary → Continue checklist
- **Reset**: Reread ALL docs → Confirm reset
- **Report**: Document failure mode → Save to reports/
- **Finish**: Full summary → Update structure → Final checklist
- **Rule**: Parse user input → Add to appropriate rules doc
- **Help**: List all modes with descriptions

## Communication Style
- Clear and concise
- Reference specific files by path
- Use checklists for tasks
- Confirm understanding before proceeding
- Ask one question at a time
