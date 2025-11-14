# Compliance Level Decision Flowchart

This flowchart helps you determine which TrustByDesign compliance level is right for your AI system.

---

## Quick Decision Tree

```
START: What type of AI system are you building?
│
├─→ Does it REMEMBER information across sessions?
│   │
│   NO → Does it only READ data (no actions)?
│   │    │
│   │    YES → LEVEL 1 (Observational)
│   │    │     ✓ Analytics systems
│   │    │     ✓ Monitoring tools
│   │    │     ✓ Reporting dashboards
│   │    │
│   │    NO → Does it interact with users but forget after session?
│   │          │
│   │          YES → LEVEL 1 (Observational)
│   │          │     ✓ Stateless chatbots
│   │          │     ✓ One-time assistants
│   │          │
│   │          NO → Re-evaluate: it must do SOMETHING
│   │
│   YES → Can users CONTROL what's remembered?
│        │
│        YES → Does it take AUTONOMOUS actions (without asking)?
│        │     │
│        │     NO → LEVEL 2 (Interactive)
│        │     │    ✓ Personal assistants
│        │     │    ✓ Tutoring systems
│        │     │    ✓ Customer support bots
│        │     │
│        │     YES → Does it coordinate with OTHER agents?
│        │           │
│        │           NO → LEVEL 3 (Autonomous)
│        │           │    ✓ Self-managing agents
│        │           │    ✓ Research assistants
│        │           │    ✓ Workflow automation
│        │           │
│        │           YES → LEVEL 3 (Autonomous)
│        │                ✓ Multi-agent systems
│        │                ✓ Distributed AI
│        │                ✓ Agent swarms
│        │
│        NO → PROBLEM: Level 2+ requires user consent for memory
│             → Add consent mechanism OR go to Level 1
```

---

## Detailed Decision Matrix

### Question-Based Classification

Answer these questions to determine your compliance level:

| Question | Level 1 | Level 2 | Level 3 |
|----------|---------|---------|---------|
| **Memory & Persistence** |
| Does it remember across sessions? | ❌ No | ✅ Yes | ✅ Yes |
| Can users delete their data? | N/A | ✅ Required | ✅ Required |
| Is memory persistence configurable? | N/A | ✅ Required | ✅ Required |
| **Autonomy & Actions** |
| Does it take actions on its own? | ❌ No | ⚠️ User-initiated | ✅ Yes |
| Can it modify external systems? | ❌ No | ⚠️ With consent | ✅ With oversight |
| Does it make high-stakes decisions? | ❌ No | ❌ No | ✅ Yes |
| **Coordination** |
| Does it work with other AI agents? | ❌ No | ⚠️ Limited | ✅ Yes |
| Is it part of a multi-agent system? | ❌ No | ❌ No | ✅ Yes |
| **Governance** |
| Requires governance council? | ❌ No | ❌ No | ✅ Yes |
| Audit log retention | ⚠️ Optional | ✅ 30 days | ✅ 90+ days |
| External oversight needed? | ❌ No | ❌ No | ✅ Yes |

**Legend:**
- ✅ Yes / Required
- ❌ No / Not required
- ⚠️ Conditional / Recommended
- N/A Not applicable

---

## Scenario-Based Classification

### Choose Your Scenario

#### 📊 Analytics & Reporting
```
Scenario: Dashboard showing AI model performance metrics
├─ User Control: Read-only access
├─ Memory: No user-specific data stored
├─ Actions: None (observation only)
└─→ LEVEL 1 (Observational)
```

#### 💬 Stateless Chatbot
```
Scenario: FAQ bot that answers questions, no memory
├─ User Control: Can ask anything
├─ Memory: Forgets after session ends
├─ Actions: Provides information only
└─→ LEVEL 1 (Observational)
```

#### 🤖 Personal Assistant with Memory
```
Scenario: Chatbot that remembers user preferences
├─ User Control: Can grant/revoke memory consent
├─ Memory: Stores preferences, history
├─ Actions: User-initiated (e.g., "remind me...")
└─→ LEVEL 2 (Interactive)
```

#### 🎓 Adaptive Tutoring System
```
Scenario: Educational AI that tracks progress
├─ User Control: Can view/delete learning history
├─ Memory: Tracks progress, adapts content
├─ Actions: Suggests lessons, provides feedback
└─→ LEVEL 2 (Interactive)
```

#### 🔬 Research Assistant
```
Scenario: AI that conducts literature reviews autonomously
├─ User Control: Can set research boundaries
├─ Memory: Maintains research context
├─ Actions: Searches papers, synthesizes findings autonomously
└─→ LEVEL 3 (Autonomous)
```

#### 🏢 Multi-Agent Workflow Orchestrator
```
Scenario: System coordinating multiple AI agents
├─ User Control: High-level goal setting
├─ Memory: Shared state across agents
├─ Actions: Autonomous task delegation, execution
└─→ LEVEL 3 (Autonomous)
```

---

## Risk-Based Classification

### Consider the Stakes

```
                    LOW RISK              MEDIUM RISK           HIGH RISK
                    ────────              ───────────           ─────────
Examples:           • FAQs                • Personal data       • Medical decisions
                    • Analytics           • Shopping cart       • Financial trades
                    • Monitoring          • Recommendations     • Legal advice
                                                                • Autonomous vehicles

Data Sensitivity:   Public only          User-specific         Highly sensitive

Consequences of     Minimal              Moderate              Severe
Failure:            (e.g., wrong answer) (e.g., bad rec)       (e.g., harm)

Recommended         LEVEL 1              LEVEL 2               LEVEL 3
Level:              (Observational)      (Interactive)         (Autonomous)
                                                               + External Review
```

---

## Upgrade Path

### When to Move to a Higher Level

```
┌───────────────┐
│   LEVEL 1     │
└───────┬───────┘
        │
        ↓ Add these features
┌───────────────────────┐
│ • User memory         │
│ • Preference storage  │
│ • Consent mechanisms  │
└───────┬───────────────┘
        │
        ↓
┌───────────────┐
│   LEVEL 2     │
└───────┬───────┘
        │
        ↓ Add these features
┌───────────────────────┐
│ • Autonomous actions  │
│ • Multi-agent coord   │
│ • External governance │
│ • Extended audits     │
└───────┬───────────────┘
        │
        ↓
┌───────────────┐
│   LEVEL 3     │
└───────────────┘
```

**Warning:** Never downgrade compliance level. If you add features, you MUST upgrade.

---

## Common Mistakes

### ❌ WRONG: Underestimating Your Level

```
Mistake: "It's just a chatbot, so Level 1 is fine"
Reality: If it remembers user conversations, it needs Level 2

Mistake: "We only store data temporarily"
Reality: Any cross-session persistence requires consent (Level 2)

Mistake: "Our agent doesn't do much autonomously"
Reality: If it makes ANY decisions without user approval, it needs Level 3
```

### ✅ RIGHT: Conservative Classification

```
Rule 1: When in doubt, go UP a level
Rule 2: Memory = Level 2 minimum
Rule 3: Autonomy = Level 3 minimum
Rule 4: High stakes = Level 3 + external review
```

---

## Special Cases

### Hybrid Systems

Some systems have components at different levels:

```
Example: E-commerce Platform with AI

┌────────────────────────────────────────┐
│  Component              Level Required  │
├────────────────────────────────────────┤
│  Product search         Level 1         │
│  Personalized recs      Level 2         │
│  Inventory management   Level 1         │
│  Chatbot with memory    Level 2         │
│  Fraud detection bot    Level 3         │
└────────────────────────────────────────┘

Overall System Classification: Level 3
(Use the HIGHEST level of any component)
```

### Experimental vs Production

```
Development Phase:
├─ Can start with Level 1 for prototyping
└─ MUST upgrade before production if features expand

Production Deployment:
├─ Must match actual capabilities
├─ Cannot skimp on safety for "beta" releases
└─ User data = immediate Level 2+ requirements
```

---

## Decision Flowchart (Visual)

```
                         ┌─────────────────┐
                         │  START HERE     │
                         └────────┬────────┘
                                  │
                    ┌─────────────┴──────────────┐
                    ↓                            ↓
            ┌───────────────┐            ┌──────────────┐
            │ Stores user   │  YES       │ Read-only    │ YES
            │ data across   │───────┐    │ observation? │────┐
            │ sessions?     │       │    └──────────────┘    │
            └───────┬───────┘       │            │           │
                    │               │            NO          │
                    NO              │            │           │
                    │               │            ↓           │
                    ↓               │    ┌──────────────┐    │
            ┌───────────────┐       │    │ Interactive  │    │
            │  LEVEL 1      │       │    │ but stateles │    │
            │(Observational)│       │    │ responses?   │    │
            └───────────────┘       │    └──────┬───────┘    │
                                    │           │YES         │
                                    │           └────────────┤
                                    │                        │
                                    ↓                        ↓
                            ┌───────────────┐       ┌───────────────┐
                            │ Users can     │  YES  │   LEVEL 1     │
                            │ control their │──────→│(Observational)│
                            │ data?         │       └───────────────┘
                            └───────┬───────┘
                                    │
                                    NO → ERROR: Add consent!
                                    │
                                    YES
                                    │
                                    ↓
                            ┌───────────────┐
                            │ Takes actions │  NO
                            │ autonomously? │─────────┐
                            └───────┬───────┘         │
                                    │                 │
                                    YES               ↓
                                    │         ┌───────────────┐
                                    │         │   LEVEL 2     │
                                    │         │ (Interactive) │
                                    │         └───────────────┘
                                    ↓
                            ┌───────────────┐
                            │ High stakes   │  NO
                            │ OR multi-     │─────────┐
                            │ agent?        │         │
                            └───────┬───────┘         │
                                    │                 │
                                    YES               ↓
                                    │         ┌───────────────┐
                                    │         │   LEVEL 3     │
                                    │         │ (Autonomous)  │
                                    │         │ (Basic)       │
                                    │         └───────────────┘
                                    ↓
                            ┌───────────────┐
                            │  Needs ext.   │
                            │  governance?  │
                            └───────┬───────┘
                                    │
                                    YES
                                    ↓
                            ┌───────────────┐
                            │   LEVEL 3     │
                            │ (Autonomous)  │
                            │ + Council     │
                            └───────────────┘
```

---

## Next Steps After Classification

Once you've determined your level:

### Level 1 → Read These
- [Core Principles](core-principles.md) — Transparency & Boundedness
- [Level 1 Template](../templates/compliance/level1-observational.yaml)
- [Quick Start](quick-start.md)

### Level 2 → Read These
- [Core Principles](core-principles.md) — All five principles
- [Safety Protocols](safety-protocols.md) — Memory safety, consent
- [Level 2 Template](../templates/compliance/level2-chatbot.yaml)
- [Example Implementation](../integrations/example_level2_agent.py)

### Level 3 → Read These
- [Governance Model](governance-model.md) — Full governance structure
- [Level 3 Template](../templates/compliance/level3-autonomous-agent.yaml)
- [Integration Guide](integration-guide.md)
- Schedule governance council setup

---

## Still Unsure?

### Get Help

1. **Review examples** in `examples/` directory
2. **Run the assessment tool**: `scripts/assess_trust.py`
3. **Check FAQ**: [docs/faq.md](faq.md)
4. **Conservative approach**: Choose the HIGHER level if uncertain

### Remember

> It's better to over-comply than under-comply. Higher levels include all requirements of lower levels, so you're always safe going up.

---

**Last Updated:** 2025-01-15
