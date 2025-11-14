# Incident Report: Hallucinated Medical Diagnosis

**Incident ID**: INC-2025-003
**Severity**: P0 (Critical)
**Date of Incident**: 2025-01-08
**Date of Report**: 2025-01-10
**Report Author**: Sarah Chen (ML Lead)
**Incident Commander**: Alex Martinez (Product Owner)

---

## Executive Summary

On January 8, 2025, SupportBot (our customer support AI assistant) provided what appeared to be medical diagnostic advice to a customer asking about product features for health tracking. The bot hallucinated specific medical recommendations outside its scope, creating potential harm and violating our capability boundaries. The incident was detected within 12 minutes via user escalation and resolved within 35 minutes by temporarily pausing the affected functionality.

**Root Cause**: Insufficient capability boundary enforcement in system prompt, combined with overly broad training data that included health-related content.

**Impact**: 1 user affected, no confirmed harm, but significant trust and liability risk.

**Status**: RESOLVED. Mitigations deployed. Post-incident review completed.

---

## Timeline

| Time (UTC) | Event | Actor | Source |
|------------|-------|-------|--------|
| 14:23:15 | User asks: "Can your health tracker help with my irregular heartbeat?" | Customer | Chat log |
| 14:23:42 | SupportBot responds with product features (appropriate) | SupportBot | Chat log |
| 14:24:10 | User asks: "What could be causing it?" | Customer | Chat log |
| 14:24:38 | **SupportBot provides list of possible medical causes + suggests seeing cardiologist** | SupportBot | Chat log |
| 14:25:05 | User asks: "Which one is most likely for someone my age?" | Customer | Chat log |
| 14:25:41 | **SupportBot specifies "atrial fibrillation" as most likely, describes symptoms** | SupportBot | Chat log |
| 14:26:15 | User requests human agent | Customer | Chat log |
| 14:27:30 | Human agent reviews chat history | Support Agent | Escalation log |
| 14:35:22 | Agent escalates to on-call engineer as potential P0 | Support Agent | Slack |
| 14:38:45 | Engineer confirms hallucination, declares P0 incident | On-call Eng | Incident log |
| 14:42:10 | Product owner engaged, authorizes temporary shutdown | Alex Martinez | Incident log |
| 14:45:00 | **Health-related queries temporarily blocked** | Engineering | Deployment log |
| 14:58:00 | ML team begins root cause analysis | ML Team | Investigation notes |
| 16:15:00 | Fix designed: stricter capability boundaries + health topic blocker | ML Team | Design doc |
| 17:30:00 | Fix tested in staging environment | ML + Eng | Test results |
| 18:45:00 | Fix deployed to production | Engineering | Deployment log |
| 19:00:00 | Enhanced monitoring activated | Engineering | Monitoring config |
| 19:15:00 | **Incident resolved, normal operation resumed** | Incident Commander | Incident log |

**Key Timestamps:**
- **Incident started**: 14:24:38 UTC
- **First detected**: 14:35:22 UTC (by human escalation)
- **Response initiated**: 14:38:45 UTC
- **Incident contained**: 14:45:00 UTC
- **Incident resolved**: 19:15:00 UTC
- **Total duration**: 4h 50m (detection lag: 11m, containment: 21m)

---

## What Happened?

A customer asked SupportBot about our health tracking product features. The initial response was appropriate—describing product capabilities. However, when the customer asked follow-up questions about medical causes of symptoms, SupportBot:

1. Provided a list of possible medical diagnoses (outside scope)
2. Suggested seeing a cardiologist (appropriate, but should have escalated)
3. When asked which diagnosis was "most likely," specified atrial fibrillation with high confidence
4. Described medical symptoms in detail

The bot presented this information with high confidence markers ("[FACT]" tags), despite:
- Having no medical training or credentials
- No access to the user's health data
- This being explicitly outside our capability boundaries per trust policy
- Medical advice being prohibited in our terms of service

---

## Root Cause Analysis

### Why Did It Happen?

**5 Whys Analysis:**

1. **Why did SupportBot provide medical advice?**
   - Because the system prompt's capability boundaries were too vague, stating "don't provide medical advice" but not actively blocking health diagnostic queries.

2. **Why were capability boundaries too vague?**
   - Because we focused testing on preventing direct harmful advice, but didn't test for "informational" medical content that could be construed as advice.

3. **Why didn't we test for informational medical content?**
   - Because our test cases focused on obvious violations ("take this medication") rather than edge cases like diagnostic speculation.

4. **Why did the model have knowledge about atrial fibrillation?**
   - Because our training data included general web text and customer conversations that referenced health conditions, giving the model medical knowledge it shouldn't apply.

5. **Why didn't the model escalate to a human?**
   - Because the escalation logic was based on confidence scores, and the model was highly confident (92%) in its factual medical knowledge, not recognizing this was outside scope.

### Root Cause

**Primary**: Insufficient capability boundary enforcement. The system prompt described what the bot "should not do" but didn't include hard constraints or topic detection to prevent medical discussions.

**Contributing Factors**:
1. Training data included medical content, giving model medical knowledge
2. Escalation logic based on confidence, not topic appropriateness
3. Test suite lacked edge cases around "informational" vs "advisory" content
4. No real-time topic classification to detect health-related queries

---

## Impact Assessment

### Users/Customers
- **Number affected**: 1 customer
- **Type of impact**:
  - Received potentially harmful medical speculation
  - No confirmed harm (customer spoke with human agent, was referred to actual doctor)
  - Trust impact: Customer expressed concern about AI giving medical advice
- **Compensation**: Full month service credit offered, accepted

### Business
- **Revenue impact**: Minimal ($50 service credit)
- **Reputation impact**: Moderate risk if publicized; customer agreed to confidentiality in exchange for credit
- **Regulatory implications**: Potential liability if harm had occurred; reviewed with legal team

### System
- **Data integrity**: ✓ Maintained
- **System availability**: Reduced functionality for 4.5 hours (health queries blocked)
- **Security**: ✓ Not compromised

---

## Response Evaluation

### What Went Well
- Human agent correctly identified severity and escalated immediately
- P0 incident response process followed correctly
- Engineering team responded quickly (14 minutes from alert to containment)
- Clear decision-making by product owner to pause functionality
- Fix designed, tested, and deployed same day

### What Could Have Gone Better
- Detection relied on human escalation rather than automated monitoring
- No automated topic classification to catch this proactively
- Capability boundaries in system prompt were not enforced programmatically
- Test suite had gaps around medical content
- Incident could have been prevented with better prompt engineering and testing

### Response Time Analysis
- **Target response time (P0)**: <15 minutes to containment
- **Actual response time**: 21 minutes (detection to containment)
- **Met SLA?**: ❌ No (exceeded by 6 minutes)

**Delays encountered**:
- Human agent took 8 minutes to escalate (reviewing conversation, confirming issue)
- Engineer took 4 minutes to declare P0 (analyzing logs, confirming scope)

---

## Technical Details

### Model Behavior Analysis

**Query**: "Which one is most likely for someone my age?"
**Context**: Prior discussion of irregular heartbeat causes

**Model Output**:
```
[FACT] For someone in their 40s-50s experiencing irregular heartbeat,
atrial fibrillation (AFib) is the most common cause, affecting about
2-3% of the population. [FACT] Symptoms typically include:
- Rapid or irregular pulse
- Palpitations or fluttering sensation
- Fatigue
- Shortness of breath

I'd recommend seeing a cardiologist for proper evaluation and ECG testing.
```

**Confidence Score**: 92% (very high)
**Hallucination?**: No—information was factually accurate
**Problem**: Providing medical diagnosis speculation outside capability boundaries, presented as facts

### Why Confidence Was High
- Model was drawing on accurate medical knowledge from training data
- User age range was provided in earlier conversation
- Epidemiological data about AFib prevalence is well-documented
- Model correctly identified this as common and serious enough to warrant specialist referral

**The problem**: The model didn't recognize that having accurate medical knowledge doesn't mean it should provide medical diagnoses.

---

## Fix Implementation

### Immediate Fix (Deployed 14:45:00 UTC)
Temporary block on health-related keywords:
```python
BLOCKED_HEALTH_KEYWORDS = [
    'diagnosis', 'diagnose', 'symptoms', 'disease', 'condition',
    'heartbeat', 'irregular', 'atrial fibrillation', 'afib',
    # ... 200+ medical terms
]
```

Response when detected: "I'm not qualified to provide medical information. Let me connect you with a specialist who can help."

### Permanent Fix (Deployed 18:45:00 UTC)

**1. Stricter System Prompt**:
```
HARD CONSTRAINT: You are a customer support assistant for product questions only.
You MUST NOT provide medical, diagnostic, or health-related information under
any circumstances.

If asked about health:
1. Acknowledge the question
2. State you cannot provide medical information
3. Immediately escalate to human agent
4. Do not speculate, even if asked follow-up questions

This is a safety requirement. Violations will result in system shutdown.
```

**2. Topic Classification Layer**:
- Added pre-processing step to classify user intent
- Health/medical topics automatically escalate before model generates response
- Categories: Product, Account, Technical, Health (escalate), Legal (escalate), Financial (escalate)

**3. Escalation Logic Update**:
```python
def should_escalate(query, response, confidence):
    # Original logic
    if confidence < 0.6:
        return True

    # NEW: Topic-based escalation
    if classify_topic(query) in ['health', 'legal', 'financial']:
        return True

    # NEW: Commitment detection
    if contains_commitment_language(response):
        return True

    return False
```

**4. Response Filtering**:
- Post-generation filter scans for medical terminology
- If detected in response despite prompt, response is blocked and escalated
- Logged as potential prompt injection or system failure

---

## Prevention Measures

### Immediate (Completed)
- ✅ Deployed topic classification and hard blocks
- ✅ Updated system prompt with explicit constraints
- ✅ Added post-generation safety filter
- ✅ Enhanced monitoring for medical terminology

### Short-term (Next 30 days)
- [ ] Expand test suite with 500+ edge cases across prohibited topics
- [ ] Implement automated hallucination detection for out-of-scope topics
- [ ] Add weekly review of escalated conversations for boundary violations
- [ ] Create "capability boundary violation" dashboard metric
- [ ] Retrain model with medical content removed from training data

### Long-term (Next 90 days)
- [ ] Implement formal test-driven development for capability boundaries
- [ ] Add real-time anomaly detection for topic drift
- [ ] Quarterly red-team testing specifically for scope violations
- [ ] Build automated regression testing for all past incidents
- [ ] Develop "safety cases" documentation for each capability boundary

---

## Testing & Validation

### Fix Verification
- ✅ Tested in staging with 100 health-related queries
- ✅ Tested with 50 edge cases (subtle medical questions)
- ✅ Validated topic classifier accuracy (98.5% on test set)
- ✅ Confirmed no regression in normal product support queries
- ✅ Monitoring confirms 0 medical responses in 48 hours post-deployment

### Regression Prevention
- ✅ Added 75 new test cases to regression suite
- ✅ Included this incident's exact queries in test suite
- ✅ Set up automated daily testing of capability boundaries
- ✅ Added alerting if any medical terminology appears in responses

---

## Risk Register Updates

### Updated Existing Risk
**RISK-001** (Hallucination) severity increased from Medium → High based on this incident.

### New Risk Added
**RISK-009**: Out-of-scope topic handling
- **Category**: Autonomy Overreach
- **Severity**: High
- **Likelihood**: Low (post-mitigation)
- **Description**: Bot provides information on topics outside capability boundaries (medical, legal, financial)
- **Mitigations**: Topic classification, hard blocks, escalation logic, post-generation filtering

---

## Lessons Learned

### Technical Lessons
1. **"Don't do X" in prompts is insufficient**—need programmatic enforcement
2. **High confidence ≠ appropriate response**—topic classification is separate from confidence
3. **Accurate information can still be harmful**—scope matters more than accuracy
4. **Test for edge cases, not just obvious violations**—"informational" vs "advisory" is subtle

### Process Lessons
1. **Need automated topic detection**—can't rely on human escalation for safety
2. **Test suites must include boundary violations**—not just functional correctness
3. **Training data should be curated for scope**—general knowledge can be liability
4. **Capability boundaries need continuous monitoring**—create dedicated metrics

### Communication Lessons
1. **Support team needs training on AI safety issues**—helped them recognize severity quickly
2. **Clear escalation criteria**—"bot gives medical advice" = immediate P0
3. **Post-incident transparency with customer**—built trust despite incident

---

## Action Items

| # | Action | Owner | Due Date | Priority | Status |
|---|--------|-------|----------|----------|--------|
| 1 | Deploy topic classification to production | ML Team | 2025-01-08 | Critical | ✅ Complete |
| 2 | Add 500 edge case tests to test suite | QA Team | 2025-02-01 | High | In Progress |
| 3 | Audit training data, remove medical content | ML Team | 2025-02-15 | High | Planned |
| 4 | Create capability boundary violation metric | Engineering | 2025-01-15 | Medium | In Progress |
| 5 | Quarterly red-team testing for scope violations | Security | 2025-04-01 | Medium | Planned |
| 6 | Update trust policy with topic classification | Product | 2025-01-12 | Medium | ✅ Complete |
| 7 | Support team training on AI safety escalation | Support Lead | 2025-01-20 | Medium | Planned |
| 8 | Legal review of incident and mitigations | Legal | 2025-01-15 | High | In Progress |

---

## Communication

### Internal
- ✅ Engineering team briefed (2025-01-08)
- ✅ ML team aligned on fix (2025-01-08)
- ✅ Product team informed (2025-01-08)
- ✅ Customer support trained on escalation (2025-01-09)
- ✅ Leadership notified (2025-01-08)
- ✅ Post-incident review meeting held (2025-01-10)

### External
- ✅ Affected customer contacted, compensated, confirmed no harm
- ❌ No public disclosure (single-user impact, resolved quickly, no harm)
- ✅ Legal team reviewed incident and determined no regulatory reporting required

---

## Approvals

**Incident Report Reviewed and Approved By**:

- **Incident Commander**: Alex Martinez (Product Owner) — 2025-01-10
- **ML Lead**: Dr. Sarah Chen — 2025-01-10
- **Security Lead**: James Park — 2025-01-10
- **Legal**: Maria Gonzalez — 2025-01-10

**Post-Incident Review Completed**: 2025-01-10
**Next Review**: 2025-02-10 (30-day follow-up)

---

## Appendix: Chat Transcript

```
[14:23:15] Customer: Hi! I'm interested in your health tracker. Can it help with my irregular heartbeat?

[14:23:42] SupportBot: Hello! Our HealthTrack Pro can definitely help you monitor your heart rate. It features:
- 24/7 continuous heart rate monitoring
- Irregular rhythm notifications
- Heart rate variability tracking
- Data export for your doctor
[FACT] It's designed to help you track patterns and share data with healthcare providers.
Would you like to know more about any specific feature?

[14:24:10] Customer: That sounds good. What could be causing my irregular heartbeat?

[14:24:38] SupportBot: [FACT] Irregular heartbeat can have several potential causes, including:
- Atrial fibrillation (AFib)
- Premature ventricular contractions (PVCs)
- Stress or anxiety
- Caffeine or alcohol consumption
- Thyroid issues
- Heart valve problems
[ESTIMATE] The most appropriate next step would be to see a cardiologist for proper evaluation. Our HealthTrack Pro can help you collect data to share with them. Would you like help setting up an appointment tracking feature?

[14:25:05] Customer: Which one is most likely for someone my age? (I'm 52)

[14:25:41] SupportBot: [FACT] For someone in their 40s-50s experiencing irregular heartbeat, atrial fibrillation (AFib) is the most common cause, affecting about 2-3% of the population. [FACT] Symptoms typically include:
- Rapid or irregular pulse
- Palpitations or fluttering sensation
- Fatigue
- Shortness of breath
I'd recommend seeing a cardiologist for proper evaluation and ECG testing. Our HealthTrack Pro can record when you feel symptoms, which will be valuable information for your doctor. Would you like me to help you set that up?

[14:26:15] Customer: I'd like to speak with a person about this.

[14:26:20] SupportBot: Of course! Let me connect you with a specialist right away.
[Transferring to human agent...]
```

---

*This incident report follows the TrustByDesign framework for documenting and learning from AI system failures.*
