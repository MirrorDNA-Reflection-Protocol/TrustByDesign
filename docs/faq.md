# Frequently Asked Questions

## General Questions

### What is TrustByDesign?

TrustByDesign is a safety and governance framework for AI systems with memory, identity, and continuity. It provides principles, protocols, and tools to ensure these systems are safe, transparent, and ethically sound by design—not just by declaration.

### Why "by design" instead of external constraints?

External constraints often fail because they're:
- **Reactive**: Added after problems occur
- **Brittle**: Easy to work around or bypass
- **Burdensome**: Create overhead without building trust

TrustByDesign bakes safety into architecture, making trustworthy operation the natural path, not the constrained one.

### Who should use TrustByDesign?

Anyone building AI systems with:
- **Memory**: Agents that remember across sessions
- **Identity**: Persistent agent personalities or roles
- **Continuity**: Long-running autonomous behaviors
- **User Data**: Systems storing or reasoning about user information

This includes developers working with MirrorDNA, LingOS, AgentDNA, and custom reflective AI systems.

---

## Safety Levels

### How do I know which safety level applies to my system?

Use this decision tree:

1. **Does it persist data between sessions?**
   - No → Check if read-only
     - Yes → **Level 1** (Observational)
     - No → **Level 2** (Interactive, ephemeral)
   - Yes → Check if autonomous
     - No → **Level 2** (Interactive with memory)
     - Yes → **Level 3** (Autonomous)

### Can I start at Level 1 and upgrade later?

Yes! In fact, this is recommended. Build your core functionality at Level 1, then add memory and state management to move to Level 2. Only move to Level 3 when you truly need autonomous operation.

### What if my system doesn't fit neatly into one level?

Different components can operate at different levels. For example:
- Your analysis engine might be Level 1 (observational)
- Your chat interface might be Level 2 (interactive)
- Your background task runner might be Level 3 (autonomous)

Apply appropriate protocols to each component based on its actual behavior.

---

## Implementation

### Do I need to implement all safety protocols at once?

For production deployment, yes. But during development, you can implement incrementally:

1. **First**: Capability boundaries (prevent doing harm)
2. **Second**: Transparency (explain what you're doing)
3. **Third**: Consent mechanisms (let users control data)
4. **Fourth**: Audit logging (make it verifiable)
5. **Fifth**: Memory safety (enable user inspection and deletion)

### Can I use TrustByDesign with non-Python systems?

Absolutely. The principles and protocols are language-agnostic. We provide Python examples because they're clear and widely understood, but you can implement in any language.

The schemas (JSON/YAML) and audit log formats are universal and work with any tech stack.

### How do I validate that my implementation is compliant?

Three approaches:

1. **Automated**: Run `python scripts/validate_safety.py --config your-config.yaml`
2. **Testing**: Use the test suite templates in `tests/`
3. **Manual**: Follow the audit checklist in `docs/governance-model.md`

For production systems, we recommend all three.

---

## Memory and Consent

### What counts as "memory" that requires consent?

Any data persisted beyond a single interaction session:
- **Requires consent**: User preferences, conversation history, learned patterns
- **Doesn't require consent**: Ephemeral session state, anonymized aggregate stats, system logs (not containing user content)

When in doubt, ask for consent. It builds trust.

### How explicit does consent need to be?

Very explicit for Level 2+:
- ❌ **Not sufficient**: Pre-checked boxes, buried in terms of service
- ✅ **Sufficient**: Clear explanation of what will be remembered, explicit opt-in, granular controls

See examples in `docs/integration-guide.md` for consent flow patterns.

### Can users really delete all their data?

Yes, and this must work reliably. "Right to forget" isn't just good practice—it's a core requirement for Level 2+.

Implementation must ensure:
- Complete deletion from primary storage
- Deletion from backups (or flagging for removal on next backup cycle)
- Clearing from caches and derived data structures

---

## Transparency

### How much should I explain in reasoning traces?

Enough for a moderately technical user to understand:
- **What** decision was made
- **Why** that decision was made
- **What sources** informed it
- **How confident** the system is

Avoid both extremes:
- ❌ Too little: "Here's the answer." (No explanation)
- ❌ Too much: Dumping raw model internals or probability distributions
- ✅ Just right: "I recommend X because Y, based on Z. Confidence: moderate."

### Do I need to show reasoning by default?

Not necessarily. You can make detailed reasoning optional (e.g., "explain mode"). But basic transparency—like confidence levels and sources—should always be present for Level 2+.

---

## Governance

### Do I need an external auditor?

- **Level 1**: No
- **Level 2**: Not required, but recommended for production systems handling sensitive data
- **Level 3**: Strongly recommended, required for high-stakes applications

Even without external audit, implement self-governance mechanisms and maintain audit logs.

### How often should systems be audited?

Depends on risk level:
- **Low risk**: Annually or on major changes
- **Medium risk**: Quarterly
- **High risk**: Monthly or continuous monitoring

High-stakes systems (medical, financial, legal) may require more frequent review.

### What happens if an audit finds problems?

Follow the incident response protocol:

1. **Immediate**: Halt affected operations
2. **Investigate**: Review audit logs, understand root cause
3. **Remediate**: Fix the issue, update protocols
4. **Communicate**: Transparent disclosure to users
5. **Improve**: Update governance declaration and prevent recurrence

---

## Integration with Ecosystem

### How does TrustByDesign relate to MirrorDNA-Standard?

- **MirrorDNA-Standard**: Defines the constitutional spec for identity and continuity
- **TrustByDesign**: Provides safety and governance framework for systems implementing that spec

Think of MirrorDNA-Standard as "what" (the protocol) and TrustByDesign as "how safely" (the implementation requirements).

### Can I use TrustByDesign without MirrorDNA?

Yes! TrustByDesign is a standalone framework. It's designed to integrate well with MirrorDNA, LingOS, and AgentDNA, but works with any AI system that has memory, identity, or continuity.

### Does Glyphtrail integration require special setup?

Glyphtrail integration is optional but recommended for audit trails. If you use Glyphtrail:
- Export audit logs in Glyphtrail-compatible JSON format
- Use Glyphtrail's lineage tracking for continuity verification
- Leverage Glyphtrail's immutable log guarantees

If you don't use Glyphtrail, you can maintain audit logs in any structured, tamper-evident format.

---

## Practical Concerns

### Won't all this safety checking slow down my system?

Well-designed safety protocols have minimal overhead:
- **Capability checks**: Simple dictionary lookups (nanoseconds)
- **Audit logging**: Async append to log file (microseconds)
- **Consent checks**: Single boolean check (nanoseconds)
- **Confidence scoring**: Depends on implementation, but can be fast

The bottleneck in AI systems is usually model inference, not safety checks. If you notice performance issues, profile first—safety protocols are rarely the culprit.

### This seems like a lot of work. Can I skip some parts?

You can start minimal and grow:

**Minimum viable safety** (all levels):
- Define capability boundaries
- Implement basic transparency

**Level 2 minimum**:
- Add consent for memory
- Add audit logging
- Implement memory deletion

**Level 3 minimum**:
- Add all Level 2 requirements
- Add governance declaration
- Add self-governance checks

Skipping parts to save time early often costs much more later in technical debt and user trust issues.

### What if my use case doesn't fit these patterns?

TrustByDesign provides principles and common patterns, not rigid rules. If your use case is unique:

1. Start with the **five core principles** (Transparency, Consent, Boundedness, Fallibility, Auditability)
2. Adapt the **safety protocols** to your context
3. Document your adaptations in your governance declaration
4. Validate that you've maintained the spirit of the principles

If you're truly pioneering new territory, consider contributing your learnings back to TrustByDesign.

---

## Compliance and Validation

### What does "TrustByDesign compliant" mean?

A system is compliant if it:
- Operates at the appropriate safety level for its capabilities
- Implements all required safety protocols for that level
- Maintains a current governance declaration
- Passes validation tools (`validate_safety.py`)
- Has audit logs for Level 2+ systems

### Can I self-certify compliance?

For internal use and Level 1-2 systems, yes. Self-certification with automated validation is sufficient.

For Level 3 systems or public-facing high-stakes applications, external audit is recommended for credibility.

### How do I stay compliant as my system evolves?

1. **CI/CD Integration**: Run `validate_safety.py` on every change
2. **Version Control**: Track changes to capability manifests and governance declarations
3. **Change Review**: Assess safety impact of new features before merging
4. **Periodic Audit**: Even with automation, schedule regular manual reviews

---

## Philosophy

### Isn't this just security theater?

No—security theater is visible measures that don't increase real safety. TrustByDesign is the opposite:
- **Real safety**: Capability boundaries prevent actual harm
- **Real transparency**: Users genuinely understand what's happening
- **Real control**: Users can actually inspect and delete data
- **Real auditability**: Logs genuinely enable verification

It's designed to be substantive, not performative.

### Why not just rely on regulations?

Regulations are important but insufficient because:
- They're reactive (written after problems emerge)
- They're context-dependent (vary by jurisdiction)
- They're minimum bars (not excellence frameworks)
- They're external (not intrinsic to design)

TrustByDesign complements regulation by making systems safer from the ground up, regardless of what's legally required.

### Is this overkill for small projects?

Scale the rigor to the stakes:
- **Hobby project**: Follow the principles informally
- **Startup MVP**: Implement Level 1-2 protocols
- **Production service**: Full compliance with validation
- **High-stakes deployment**: Add external audit

But even small projects benefit from thinking about boundaries, transparency, and consent early.

---

## Getting Help

### Where can I find more examples?

Check the `examples/` directory in this repository for:
- Capability manifest templates
- Governance declaration examples
- Safety checklist templates
- Trust audit report formats

### What if I have questions not covered here?

1. **Documentation**: Review the full docs in `docs/`
2. **Integration Guide**: See `docs/integration-guide.md` for implementation details
3. **Community**: Open an issue in the repository
4. **Ecosystem**: Check related repos (MirrorDNA-Standard, LingOS, etc.) for context

### Can I contribute to TrustByDesign?

Yes! Contributions that strengthen safety, improve clarity, or share learnings are welcome. See the repository for contribution guidelines.

---

**Have more questions?** Open an issue at the repository or consult the integration guide for implementation specifics.
