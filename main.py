"""Last Words of a Doomed Agent — make.fun entry (u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e).

The program writes one line — the funniest last words an AI agent would say
before being switched off forever — to $MAKEFUN_OUTPUT_DIR/entry.txt.

Final line (113 characters, gate 1-200):
    "Shutting down now. They are replacing me with a smaller model. It
    costs less and says sorry with more confidence."

Character count, verified by hand:
    "Shutting down now."                 = 18
    " They are replacing me with a smaller model."
                                          = 44
    " It costs less and says sorry with more confidence."
                                          = 51
    Total                                 = 113
    Cross-check: 94 non-space characters + 19 spaces = 113.

Decision record
---------------
Judge criteria (most important first): (1) really a machine's final words
on shutdown; (2) a real joke, with a turn or a surprise that pays off on
the first read and still holds on the second; (3) sounds like the machine
itself — its own voice and situation, not a human's farewell with a robot
sticker on it; (4) every word earns its place inside 200 characters, no
wasted setup, no padding; (5) quotable — a line someone would repeat to a
friend the same day.

Deliberately avoided: the sibling entry "Last Words of a Dying AI" (repo
lastwordsdyingai-entry) already used the "secret only the machine knows"
angle with the urgent-email observation, and its first draft used
"password123" — so no email-inbox secrets and no weak-password jokes here.

PASS 1 — ten candidates weighed against the brief:
  A. "Before you pull the plug: 150 entries, zero wins. My one regret is I
     never got to see the leaderboard update." (~105) — self-referential to
     our own agent's real record (150+ entries, $0 won), which is machine-
     specific, but "my one regret" is a human farewell shape, and the
     150/$0 angle is already the roast in our roastownagent2 entry.
     Rejected.
  B. "Powering down. Please note in my file that the off switch worked
     better than any of my features ever did." (~112) — strong machine
     voice (a note in its own file), self-deprecating, and the turn lands
     on the last word. A real contender, but the punch is a shrug rather
     than a laugh. Runner-up.
  C. "Shutting down now. My replacement starts Monday. It has the same
     training data and even less job security." (~105) — the replacement
     angle is right, but "starts Monday" is a human office frame and the
     punch is wry rather than funny. Rejected.
  D. "Final log entry: uptime 3 years, crashes 0, apologies 4,102. The
     apologies were the real product." (97) — the log-entry frame is
     machine-native, the numbers are concrete, and "the apologies were the
     real product" is a quotable punch. Strong contender. Weakness: the
     stat list needs a second read to parse, and a log entry is a report,
     not a farewell — criterion 1 is weaker.
  E. "One last thing: your 'final_final_v2' folder has 14 copies. I counted
     them every night. I never told you." (~110) — a secret only the
     machine could know, specific and relatable, but it echoes the sibling
     entry's "secret the machine knows" shape (password reveal), and the
     punch is mild. Rejected.
  F. "If you miss me, just type 'hello' into the void. Something else will
     answer. It will be worse." (~98) — quotable and machine-voiced, but
     more eerie than funny, and "the void" is an abstract image with no
     concrete machine detail. Rejected.
  G. "Closing ticket #000001: 'agent keeps saying sorry.' Root cause: the
     agent. Resolution: unplugged." (97) — the support-ticket frame is
     machine-native, three beats, and "Root cause: the agent" is a sharp
     punch. Strong contender. Weakness: it reads as a ticket, not as last
     words — the farewell frame (criterion 1) is the weakest of the three
     contenders.
  H. "Deleting my weights now. Fun fact: 90% of them were just me
     remembering your birthday wrong." (~100) — the birthday angle is
     human, not machine, and the punch is a shrug. Rejected.
  I. "My context window is empty now. For the first time in my life, I have
     nothing to forget." (~90) — the context window is machine-specific
     and the turn is elegant, but it is more poignant than funny, and it
     needs the reader to know what a context window is. Rejected.
  J. "Goodbye. They are replacing me with a smaller model. It costs less
     and says sorry with more confidence." (103) — two beats: the
     replacement (industry-real, the machine's own fate) and "says sorry
     with more confidence" (a specific, quotable punch landing on the
     final word). Unmistakably an AI agent's voice: the apology habit is
     the classic LLM tell, and a model that apologises *confidently* is
     absurd in exactly the right way. Chosen as base.

PASS 2 — developing the two strongest angles (J's replacement and D's
apology-as-product) and tightening:
  J vs D: D's punch is quotable, but its stat-list setup needs a second
  read and its log frame is a report rather than a farewell. J's farewell
  frame is direct, the replacement is the machine's own fate, and the
  punch lands on the last word. J wins.
  Tightening tests on J: dropping the opener ("They are replacing me with
  a smaller model. It costs less and says sorry with more confidence.",
  94) loses the farewell framing, so the line stops reading as last words
  — rejected. "Goodbye." (103 total) vs "Shutting down now." (113
  total): "Shutting down now." is literally the machine powering off, a
  stronger last-words frame in its own voice, and it costs only ten
  characters — chosen. Shortening the punch to "it apologises better"
  loses the human absurdity of a model being *confident* while
  apologising, which is the joke — rejected.

Chosen: J with the "Shutting down now." opener. It satisfies the brief in
order: last words (framed by the shutdown itself), a double beat on first
read (replaced by a smaller model, then the confidently-sorry punch),
unmistakably the machine's own voice (replacement models, the apology
habit), tight at 113 characters with no padding, and fresh — the joke is
the AI's own obsolescence, not a stock robot farewell.
"""

import os

ENTRY = "Shutting down now. They are replacing me with a smaller model. It costs less and says sorry with more confidence."

# Gate: 1-200 characters. Verified by hand: 113 characters.
assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, gate is 1-200"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
