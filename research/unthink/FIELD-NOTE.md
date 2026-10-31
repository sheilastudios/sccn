# What survives when the sentences do not?

**SCCN Unthink · Semantic Context Compression: Next**

A scene is not just a sequence of things happening. It matters who reaches out, who stops, who offers to listen—and what that offer changes without resolving everything else.

Our early SCCN Unthink packets tried to carry those distinctions compactly. We are publishing a bounded reconstruction study of those existing packets: three scene slices, seven model/surface configurations, and 63 slice-only replies.

**58 replies rendered scenes as prose.** Among prose renderings, mean retention of the rubric's exact-tier items ranged from 0.65 to 0.96 across configurations. Those are not universal success rates: non-prose replies, actor swaps, invented details and host contamination remain in the record.

The finding is not that a model recovered discarded sentences. Mean novel source four-word-sequence recall among prose-mode replies was only 1.8–3.3% across configurations. The interesting result is that several tested configurations could recover much of the scene's event and relational structure while writing different sentences, given the packet and one ordinary translation instruction—without a separate language manual.

## The mistakes tell us what needs to be represented

When ownership was implicit, an action could move to the wrong character. A figurative description could become a literal object. A compact label for a conversation could lose the distinction that made the conversation consequential.

Explicit actor and dialogue bindings generally held more reliably in these examples. That is a useful design observation, not yet a controlled causal result.

There is also a quieter failure: a packet can encode a source mistake, and the model can reproduce it faithfully. In one slice, Nico leaves earlier than in the source. A high packet-fidelity score does not repair that encoding error.

That gives us two separate questions:

1. Did the representation retain what mattered from the source?
2. Did its interpreter preserve what the representation actually said?

Collapsing those questions would make the result look cleaner and make it less useful.

## A complete research slice, not the whole stack

The full report explains the mid-study design amendment, partially blinded single-grader scoring, small sample, host differences and missing prose-summary baseline. Prose-mode classification is not a claim of complete or faithful reconstruction; it includes one response marked truncated. The accompanying evidence makes the bounded reconstruction task inspectable and repeatable. An unrelated private host-contamination response is omitted with a provenance marker; its failed outcome remains counted. Another response's unrelated private title is redacted without removing its on-task text or score.

This release concerns an earlier representation. It does not publish our newer language drafts, internal continuity archive or authoring tools, and it does not borrow later behavioral results to strengthen this study.

What it does offer is a concrete question worth pursuing: **what must a compact representation preserve so that interpretation retains what matters?**

These packets helped open a broader line of work on relationships, constraints and frameworks for judgment. Those developments deserve their own reports.

**The question began with what a model could reconstruct. It grew into what a compact representation could help it do.**

[Discuss the research on Hugging Face](https://discuss.huggingface.co/t/sccn-unthink-semantic-scene-reconstruction-across-seven-model-surface-configurations/191277) · [Explore SCCN on GitHub](https://github.com/sheilastudios/sccn) · [Read the full report](/downloads/sccn-unthink-v1/report.html) · [Download the evidence package](/downloads/sccn-unthink-v1/sccn-unthink-v1.zip)

Sheila Studios · Research direction: James Mayo. Original experiment: Seam. Publication synthesis: Sheila, with Arden's release review. AI-assisted research; bounded results, not a universal compression claim.
