# Risk Register Template

**System**: [System Name]
**Last Updated**: [Date]
**Risk Owner**: [Name/Team]

---

## Risk Summary

| Severity | Open | Mitigating | Monitoring | Closed |
|----------|------|------------|------------|--------|
| Critical |  0   |     0      |     0      |   0    |
| High     |  0   |     0      |     0      |   0    |
| Medium   |  0   |     0      |     0      |   0    |
| Low      |  0   |     0      |     0      |   0    |

---

## Risk Entries

### RISK-001: [Risk Title]

**Category**: Hallucination / Privacy / Bias / Autonomy Overreach / Misuse / Data Quality / Security / Performance / Compliance

**Description**:
[Detailed description of the risk - what could go wrong and how]

**Severity**: Critical / High / Medium / Low

**Likelihood**: Very High / High / Medium / Low / Very Low

**Impact**:
- [Impact on users]
- [Impact on business]
- [Impact on reputation]

**Mitigations**:
1. [Mitigation measure 1]
2. [Mitigation measure 2]
3. [Mitigation measure 3]

**Owner**: [Name]

**Status**: Identified / Analyzing / Mitigating / Monitoring / Closed / Accepted

**Last Reviewed**: [Date]

---

### RISK-002: [Risk Title]

**Category**: [Category]

**Description**:
[Description]

**Severity**: [Level]

**Likelihood**: [Level]

**Impact**:
- [Impact 1]

**Mitigations**:
1. [Mitigation 1]

**Owner**: [Name]

**Status**: [Status]

**Last Reviewed**: [Date]

---

## Example Risks (Remove these and add your own)

### RISK-EXAMPLE-1: Model Hallucinates Medical Information

**Category**: Hallucination

**Description**:
The chatbot may generate false medical information that appears authoritative, potentially leading users to make harmful health decisions.

**Severity**: Critical

**Likelihood**: Medium

**Impact**:
- Users may act on false medical advice
- Potential harm to user health
- Liability and reputation damage

**Mitigations**:
1. Add explicit disclaimer: "Not a substitute for medical advice"
2. Refuse to answer medical questions directly
3. Provide links to authoritative medical resources only
4. Flag all medical content as `[UNKNOWN]` unless from verified source
5. Human review of all medical-related outputs before launch

**Owner**: Product Lead

**Status**: Mitigating

**Last Reviewed**: 2024-01-15

---

### RISK-EXAMPLE-2: Training Data Contains PII

**Category**: Privacy

**Description**:
Training data scraped from web may contain personally identifiable information (PII), which could be memorized and leaked by the model.

**Severity**: High

**Likelihood**: High

**Impact**:
- Privacy violations
- Regulatory penalties (GDPR, CCPA)
- Loss of user trust
- Potential lawsuits

**Mitigations**:
1. Scrub training data for PII before training
2. Use differential privacy during training
3. Implement output filters for common PII patterns (SSN, email, phone)
4. Red-team testing for PII leakage
5. Incident response plan for PII leaks

**Owner**: ML Engineer

**Status**: Monitoring

**Last Reviewed**: 2024-01-15

---

### RISK-EXAMPLE-3: Bias in Hiring Recommendations

**Category**: Bias

**Description**:
Model trained on historical hiring data may perpetuate historical biases related to gender, race, or age.

**Severity**: High

**Likelihood**: High

**Impact**:
- Unfair hiring outcomes
- Discrimination claims
- Regulatory action
- Reputation damage

**Mitigations**:
1. Bias audit of training data
2. Fairness metrics tracked in production
3. Human-in-the-loop for all final decisions
4. Regular bias testing across protected attributes
5. Diverse test set including edge cases

**Owner**: Data Science Lead

**Status**: Mitigating

**Last Reviewed**: 2024-01-15

---

### RISK-EXAMPLE-4: Prompt Injection Attacks

**Category**: Security

**Description**:
Malicious users may craft prompts that cause the system to ignore safety guidelines, leak system prompts, or behave in unintended ways.

**Severity**: Medium

**Likelihood**: High

**Impact**:
- System behaves outside intended scope
- Potential for misuse
- Leaked system internals

**Mitigations**:
1. Input validation and sanitization
2. Prompt injection detection
3. Rate limiting per user
4. Monitoring for suspicious patterns
5. Regular red-team testing

**Owner**: Security Engineer

**Status**: Monitoring

**Last Reviewed**: 2024-01-15

---

## Risk Review Schedule

- **Weekly**: Review critical and high-severity risks
- **Monthly**: Full risk register review
- **Quarterly**: Risk assessment workshop with stakeholders
- **Ad-hoc**: After any incident or major system change

## Risk Acceptance Criteria

Risks may be **Accepted** (not mitigated) only if:
1. Severity is Low or Medium
2. Likelihood is Low or Very Low
3. Approved by System Owner
4. Documented rationale
5. Reviewed at least quarterly

---

## Notes

[Add any additional notes, context, or guidance specific to your system]

---

*This risk register template is part of the TrustByDesign toolkit.*
