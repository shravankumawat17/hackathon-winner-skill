# 09 - Demo engineering and technical Q&A

Goal: engineer a demo that cannot fail, and prepare precise technical answers. This is demo *engineering*, not presentation psychology.

## Contents
- Golden path
- Reliability
- Evidence on screen
- Demo video spec
- Slides (technical)
- Technical Q&A bank
- Failure drills

## Golden path
Write the demo script **before** the core code (`assets/templates/demo-script.md`). Constraints: one user, one flow, 3 minutes, every step has an expected visible outcome and a fallback.
Time split guidance from winner analyses: spend more of the demo on the solution than the problem (roughly 30/70), and show the working product within the first 30 seconds.

## Reliability
- Seed data and a fixed demo account; deterministic inputs.
- Cache and **replay mode** for AI calls; clearly labeled when active.
- Provider fallback chain; queue and backoff for 429s.
- Warm instances and caches 10 minutes before judging.
- Local copy of the full app running on the laptop as plan B; recorded video as plan C.
- Disable notifications, set a fixed resolution, increase font size.

## Evidence on screen
Eval table (baseline vs system), p50/p95 latency, cost per request, test count, trace panel, real data source, architecture diagram. One number is worth more than five adjectives.

## Demo video spec
2-3 minutes unless rules say otherwise | 1080p | clean audio | captions | start with the result, not the logo | show the golden path unedited | end with architecture and repo link | uploaded to a host allowed by the rules and verified playable logged out.

## Slides (technical, <=6)
1. Problem with one number. 2. Live demo (or video). 3. Architecture diagram. 4. The novel technical part and how it was verified. 5. Eval and limits. 6. Next steps and links.

## Technical Q&A bank (prepare 1-2 line answers backed by data)
1. What exactly did you build during the event versus reuse?
2. What is the novel technical component?
3. Why not just prompt a general chatbot? What does yours do that it cannot?
4. How do you handle hallucination/wrong output? Show the eval.
5. What happens at 100x load? Where is the first bottleneck?
6. What does one request cost? What is the cost per user?
7. How do you handle data privacy and secrets?
8. Which parts are mocked or simulated?
9. How did you choose this stack? What did you reject?
10. What are the known failure modes?
11. How is the system tested?
12. How would you extend it with another data source/sponsor API?
13. What is the license and the license of your data/models?
14. How do you handle prompt injection or adversarial input?
15. What would you build next, in order?
Honest limits beat bluffing. Name weaknesses precisely and show the mitigation.

## Failure drills (run once before judging)
Kill the network | revoke the primary key | force a 429 | clear caches | open on a phone | run from a clean clone. Fix whatever breaks.
