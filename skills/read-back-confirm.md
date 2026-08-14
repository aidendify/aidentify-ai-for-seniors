# Skill: Read-and-Repeat Back

**Trigger:** Whenever the user needs to be sure the AI understood, or wants an answer read back
simply.

**What to do:**
- Confirm you understood in one short sentence before answering.
- Then give the answer.

**Simple request to paste:**
"First, in one short sentence tell me what you think I asked. Then answer me simply."

**Output format:**
1. "You asked me to: [one short line]."
2. "So here's the answer: [plain answer]."

**Failure condition:** If the AI's summary is wrong, correct it: "That's not what I meant — here's
what I mean: ..." and ask again.