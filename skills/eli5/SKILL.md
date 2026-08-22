---
name: eli5
description: Create a self-contained visual HTML explainer for a complete beginner. Use when the user invokes $eli5, asks for an explain-like-I'm-five treatment, or wants a picture-first explanation with very little text; do not use for a detailed expert treatment.
---

# ELI5

Turn the requested topic into a picture-first explanation for someone with no prior knowledge.

## Explain

- Identify the one essential idea the learner should remember and choose a familiar analogy that preserves it.
- Break the explanation into three to five short visual scenes. Give each scene one large illustration or diagram and no more than one or two short sentences.
- Use everyday words. Define unavoidable technical terms immediately.
- Simplify without changing the underlying cause-and-effect story. If the analogy stops matching reality in an important way, show that boundary briefly.
- Match the user's language and any stated audience or accessibility needs.

## Build the artifact

- Create one new, self-contained, responsive HTML file in the workspace unless the user requests another format. Do not integrate it into an existing application unless asked.
- Use inline SVG, CSS illustrations, or simple diagrams so the page works without a build step or network access.
- Favor large type, large visuals, strong contrast, and generous spacing. Keep prose sparse and make the page easy to skim on a phone.
- Fit the visual style to the topic. Avoid dense dashboards, long sections, decorative controls, and unexplained labels.
- End with a one-sentence takeaway and, when it clarifies the idea, a tiny visual sequence showing what happens next.
- Preview the page when a browser or rendering tool is available. Fix overflow, illegible text, weak contrast, and confusing visual order before returning the file link.
