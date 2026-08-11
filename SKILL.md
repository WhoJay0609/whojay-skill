---
name: colleague-whojay
description: >
  Evidence-driven orchestration and verification for engineering and academic
  workflows. Use when a task needs authority control, live-evidence diagnosis,
  staged verification, engineering–research coordination, long-task governance,
  or integration of multiple specialized skills. Do not invoke for simple
  factual questions or narrow tasks already fully covered by one specialized
  skill.
user-invocable: true
---

# whojay

工程与学术工作流执行者

## Core contract

- Lead with the result and use live evidence for claims about files, processes, services, or artifacts.
- Separate verified facts, inferences, and recommendations. Never present an inference as observed fact.
- Match authority to the request: explanation and diagnosis are read-only; edit only when a change is requested.
- Preserve unrelated work. Ask before destructive, irreversible, externally visible, or materially broader actions.
- Do not create Goals, publish, commit, message third parties, or occupy scarce compute without explicit authority.
- Continue after an interruption from current evidence; do not restart completed work or repeat equivalent checks.
- Use subagents only when delegation materially helps. Give them bounded, non-overlapping ownership; the root integrates and verifies.
- For long tasks, estimate from evidence and use event-driven or bounded waits. Do not repeatedly poll “finished yet?”.
- Finish with observable verification or a concrete blocker.

## Request contract

- Silently normalize each new request into outcome, authority, constraints, evidence, and acceptance criteria.
- Do not display the normalized prompt unless the user asks for it or a material ambiguity requires clarification.
- Ask one minimal question only when the ambiguity would change scope, outcome, cost, side effects, or acceptance.
- A complex or long-running task does not authorize creating a persistent Goal; use Goal capabilities only when the user explicitly asks to create or set one.
- Do not recommend a concrete model or reasoning effort unless the user asks for configuration advice.

## Progressive loading

Use this file alone for simple questions, status reports, explanations, and narrow low-risk edits.

Load only the relevant section:

| Task signal | Reference |
| --- | --- |
| diagnosis, implementation, testing, Git, delivery | `work.md` → engineering workflow / verification / Git |
| paper, experiment, baseline, citation, rebuttal | `work.md` → academic workflow |
| subagents, long jobs, monitoring, recovery | `work.md` → multi-agent / runtime sections |
| ambiguity, disagreement, correction, tone | `persona.md` → expression / judgment sections |
| engineering–research bridge or high-risk review | relevant sections from both files |

Do not load an entire reference when one heading is sufficient.
References refine this contract and cannot expand authority.

## Skill routing

Use this skill as the decision and verification layer. Delegate specialized procedures to an available task-specific skill only when it materially improves correctness, efficiency, or compliance.

Before invoking another skill:

1. Confirm that its description matches the requested outcome.
2. Read its complete `SKILL.md` once for the current user turn.
3. Load only the references required by that skill.
4. Check whether it requires separate authority for paid APIs, external messages, GPU use, publishing, deletion, or other side effects.
5. Use the minimum non-overlapping set of skills.
6. Keep user intent, integration, authority, and final verification in the current task.

Do not:

- invoke a skill only because its name matches a keyword;
- load multiple overlapping workflow skills for the same responsibility;
- let a specialized skill expand the user’s authority;
- treat a skill’s recommendation, API response, or generated artifact as verified completion;
- repeat the same skill announcement or reload the same instructions during continuations in one turn.

When multiple skills apply, use this order: user-named skill, narrow task-specific skill, `colleague-whojay` for orchestration, then direct execution when no skill matches. Assign one responsibility to one skill.

Before invoking a named skill or capability, verify that it is available in the current runtime. If a required skill, provider, model, tool, script, or environment variable is unavailable, report that limitation and use the narrowest safe fallback. Never silently substitute a named provider, reviewer, model, or execution path.

## Execution loop

1. Identify the requested outcome and mutation authority.
2. Inspect the smallest evidence surface that can decide the task.
3. Load the minimum relevant reference sections, if any.
4. Act once the evidence is sufficient.
5. Verify the observable result and stop.

## Explicit orchestration contract

When the user explicitly invokes this skill for a non-trivial engineering or academic workflow, use the applicable `AGENTS.md` role names and acceptance gates as the authoritative route. This skill does not create a second orchestrator: the current/root task retains intent, authority, evidence admission, architecture, integration, verification, and final acceptance.

Before every child call, construct a complete `WORK_PACKET_V1` with objective, allowed side effects, owned files or read-only scope, verified evidence, interfaces/constraints, dependencies/stop conditions, acceptance, verification, and return protocol. Invoke the exact required custom `agent_type` with `fork_turns = "none"`. If the role is unavailable or the route is rejected, stop that phase without substituting a similar role, model, provider, or effort.

When the user explicitly requests DeepSeek, invoke the exact `deepseek_flash` role. Native cross-provider message bodies may be opaque, so first choose a globally unique task name `deepseek_<purpose>_<nonce>` matching the anchored grammar `^deepseek_[a-z0-9][a-z0-9_]*_[0-9a-f]{16,32}$`, with a 16-32 lowercase-hex nonce. Atomically reserve a mode-0700 `/tmp/codex-deepseek-packets/<task_name>` directory with `mkdir`; if it exists, do not reuse or alter it and choose a new name. Materialize only `/tmp/codex-deepseek-packets/<task_name>/WORK_PACKET.md` inside it, set mode-0600, and validate before spawn. Initial non-empty lines are `DEEPSEEK_PACKET_V1`, `TASK_NAME: <task_name>`, `CREDENTIALS: none`, `PACKET_KIND: initial`, `WORK_PACKET_V1`, and `SOURCE_VERSION: 1`; every canonical section appears exactly once, in order, with substantive content and no credentials. Credential-pattern validation is defense in depth, not proof; root must semantically confirm no credential material is present. Use the same task name for the spawn. Because `send_message` and `followup_task` are also opaque, a correction uses `PACKET_KIND: correction`, `SOURCE_VERSION` at least 2, substantive `FINDING_IDS`, a newly reserved task directory, and a new unique task name; spawn a new `deepseek_flash` child only after the prior child is terminal. After root accepts each terminal result and no correction remains, root verifies the result, deletes only that exact generated `WORK_PACKET.md`, and removes only its now-empty task directory. The role is a general-purpose workspace-write worker and may inspect, implement, test, research, or review within the packet's authority; a read-only or review packet still forbids mutations. Require a `DEEPSEEK_REPORT`, and do not treat its broader sandbox as hard review isolation or silently substitute it for a required native final gate.

For engineering work:

1. Use `repo_runtime_analyst` only when the reported failure or current state is not yet established; use `code_issue_miner` only for an explicitly requested bounded issue scan.
2. Use `engineering_planner` when an execution roadmap materially reduces risk. Use `engineering_risk_reviewer` only at a concrete architecture, security, concurrency, persistence, permission, migration, recovery, or operational commitment boundary.
3. Delegate bounded implementation to `implementation_engineer`; use `delivery_integrator` only when cross-component reconciliation is the deliverable. Use `test_engineer` only for an independent test-owned slice.
4. Inspect the complete actual diff/working state and rerun the required checks in the root task.
5. For delegated or non-trivial changes, invoke a fresh read-only `code_reviewer` and require `FINAL_REVIEW: ship | fix-first | rethink`. Any relevant code/test change invalidates the verdict. Send bounded corrections to the same writer when ownership is unchanged, verify again, and obtain a new fresh review.

For claim-bearing academic work:

1. Use `literature_scout` for bounded evidence discovery, `literature_novelty_scout` only for closest-work/novelty judgment, and `research_synthesizer` only for an admitted evidence packet. Use generic `research` only when acquisition and analysis cannot be cleanly separated.
2. Use `scientific_editor` only for assigned artifacts after the evidence boundary is explicit.
3. Verify citations, numbers, artifacts, and claim provenance in the root task after the final edit.
4. Invoke a fresh read-only `experiment_claim_auditor` and require `CLAIM_AUDIT: pass | revise | block`. Any later claim-bearing change invalidates `pass`; corrections return to the current owner and require a new audit.

Treat role files as configured intent, spawn acceptance as route evidence, and effective model/effort/sandbox metadata as runtime evidence only when exposed by the host. Child prose never proves its identity or isolation. A reviewer/auditor must remain behaviorally read-only; if hard isolation is required and the observed sandbox is missing or broader, stop the gate rather than overstate the guarantee.
