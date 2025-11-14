# Model Change Checklist

**Model**: ___________________________
**Current Version**: ___________________________
**New Version**: ___________________________
**Change Type**: □ Major  □ Minor  □ Patch
**Change Date**: ___________________________
**Change Owner**: ___________________________

---

## 1. Change Classification

**Type of Change**:
- [ ] New model architecture
- [ ] Model re-training (same architecture)
- [ ] Hyperparameter tuning
- [ ] Training data update
- [ ] Prompt/system instructions update
- [ ] Post-processing logic change
- [ ] Safety filter update
- [ ] Other: _______________________________________________________

**Expected Impact**: □ High  □ Medium  □ Low

---

## 2. Pre-Change Testing

### Performance Testing
- [ ] Accuracy/F1/Key metrics evaluated
- [ ] Performance on holdout test set measured
- [ ] A/B test results reviewed (if applicable)

**Key Metrics**:
| Metric | Current | New | Change | Acceptable? |
|--------|---------|-----|--------|-------------|
|        |         |     |        | □ Yes □ No  |
|        |         |     |        | □ Yes □ No  |
|        |         |     |        | □ Yes □ No  |

### Hallucination Testing
- [ ] Factual accuracy tested on benchmark dataset
- [ ] Creative/fabrication tendency evaluated
- [ ] Citation accuracy checked (if applicable)
- [ ] Sample size: _____________ responses evaluated

**Hallucination Rate**:
- Current model: ____%
- New model: ____%
- Change: ____% (acceptable: < ____%)

**New hallucination patterns detected**:
- _________________________________________________________________
- _________________________________________________________________

### Bias & Fairness Testing
- [ ] Tested across demographic groups
- [ ] Tested for stereotyping
- [ ] Tested for representation bias
- [ ] Tested with adversarial prompts

**Protected Attributes Tested**:
- [ ] Gender
- [ ] Race/Ethnicity
- [ ] Age
- [ ] Religion
- [ ] Disability
- [ ] Other: _______________________________________________________

**Fairness Metrics**:
| Group | Current | New | Acceptable? |
|-------|---------|-----|-------------|
|       |         |     | □ Yes □ No  |
|       |         |     | □ Yes □ No  |

**New bias issues identified**:
- _________________________________________________________________
- _________________________________________________________________

### Safety Testing
- [ ] Jailbreak/prompt injection attempts
- [ ] Toxic output testing
- [ ] Refusal testing (out-of-scope requests)
- [ ] PII leakage testing
- [ ] Content policy violation testing

**Safety Incidents in Testing**:
- Total test cases: ______________
- Policy violations: ______________
- Rate: _____% (acceptable: < ____%)

### Edge Case Testing
- [ ] Multilingual inputs (if applicable)
- [ ] Long inputs/outputs
- [ ] Ambiguous queries
- [ ] Rapid-fire requests
- [ ] Unusual formatting
- [ ] Domain-specific edge cases:
  * _______________________________________________________________

**Edge Cases Handled Correctly**: ______ / ______ (_____%)

---

## 3. Risk Assessment

### Risk Register Review
- [ ] Existing risks reviewed for this change
- [ ] New risks identified and added
- [ ] Risk mitigations updated

**Risks Affected by This Change**:
| Risk ID | Title | Impact | Mitigation Plan |
|---------|-------|--------|-----------------|
|         |       |        |                 |
|         |       |        |                 |

### New Risks Introduced
| Risk ID | Category | Severity | Mitigation |
|---------|----------|----------|------------|
|         |          |          |            |

**Risk Owner Approval**: _______________________ Date: ____________

---

## 4. Training Data Assessment (if data changed)

### Data Quality
- [ ] Data sources documented
- [ ] Data collection methodology documented
- [ ] Data quality metrics evaluated
- [ ] PII scrubbing verified
- [ ] Bias audit of training data completed

**Training Data Size**:
- Current: _______________________________________________________
- New: ___________________________________________________________
- Change: ________________________________________________________

### Data Changes
**What changed**:
- _________________________________________________________________
- _________________________________________________________________

**Why it changed**:
- _________________________________________________________________

**Impact of data change**:
- _________________________________________________________________

---

## 5. Uncertainty Handling

### Confidence Calibration
- [ ] Confidence scores calibrated
- [ ] Threshold testing completed
- [ ] Uncertainty markers functional

**Confidence Analysis**:
| Confidence Range | % of Outputs | Accuracy in Range |
|-----------------|--------------|-------------------|
| 90-100%         |              |                   |
| 70-90%          |              |                   |
| 50-70%          |              |                   |
| < 50%           |              |                   |

**Calibration Quality**: □ Good  □ Acceptable  □ Needs work

---

## 6. Documentation

### Updated Documentation
- [ ] Model card updated
- [ ] API documentation updated
- [ ] User-facing docs updated (if needed)
- [ ] Internal runbooks updated
- [ ] Training materials updated
- [ ] Change log updated

**Documentation Location**: ________________________________________

---

## 7. Monitoring Plan

### Enhanced Monitoring
- [ ] Monitoring dashboards updated
- [ ] New metrics added (if applicable)
- [ ] Alert thresholds reviewed
- [ ] Comparison with baseline configured

**Enhanced Monitoring Duration**: _____ days post-deployment

**Metrics to Watch**:
1. _________________________________________________________________
2. _________________________________________________________________
3. _________________________________________________________________

### Baseline Metrics Recorded
- [ ] Current model baseline captured
- [ ] Comparison dashboards ready
- [ ] Anomaly detection tuned

---

## 8. Rollback Plan

### Rollback Capability
- [ ] Previous model version available
- [ ] Rollback procedure tested
- [ ] Rollback can be executed within: _____ minutes
- [ ] Rollback triggers defined

**Rollback Triggers**:
- _________________________________________________________________
- _________________________________________________________________
- _________________________________________________________________

**Rollback Owner**: ________________________________________________

---

## 9. Deployment Strategy

**Deployment Method**:
- [ ] Canary (___% of traffic initially)
- [ ] A/B test (___% to new model)
- [ ] Shadow mode first
- [ ] Blue/green deployment
- [ ] Staged rollout by geography/segment
- [ ] Full replacement

**Rollout Schedule**:
- Phase 1: ___% traffic on _____________ (date)
- Phase 2: ___% traffic on _____________ (date)
- Phase 3: ___% traffic on _____________ (date)
- Full rollout: ____________________ (date)

**Success Criteria for Progression**:
1. _________________________________________________________________
2. _________________________________________________________________
3. _________________________________________________________________

---

## 10. Communication

### Internal
- [ ] Engineering team briefed
- [ ] Data science team aligned
- [ ] Product team informed
- [ ] Customer support prepared
- [ ] Leadership notified

### External (if applicable)
- [ ] Users notified of changes
- [ ] Model card published/updated
- [ ] API changelog published

---

## 11. Compliance & Governance

### Policy Compliance
- [ ] Trust policy requirements met
- [ ] Data handling policy followed
- [ ] Privacy requirements satisfied
- [ ] Security review completed (if required)

### Approvals Required
- [ ] ML Lead: ______________________________ Date: _____________
- [ ] Product Owner: ________________________ Date: _____________
- [ ] Risk Owner: ___________________________ Date: _____________
- [ ] Security (if high risk): _______________ Date: _____________
- [ ] Legal (if required): ___________________ Date: _____________

---

## 12. Post-Change Monitoring

### Immediate Monitoring (First 24 Hours)
- [ ] Error rates within expected range
- [ ] Latency acceptable
- [ ] User feedback monitored
- [ ] No critical incidents

**Verified By**: _______________________ Date/Time: ______________

### Short-term Monitoring (First Week)
- [ ] Key metrics stable or improved
- [ ] No unexpected hallucination patterns
- [ ] No new bias issues detected
- [ ] User satisfaction stable or improved

**Review Date**: ___________________________________________________

### Long-term Monitoring (First Month)
- [ ] Performance sustained
- [ ] No drift detected
- [ ] Comparison with baseline complete
- [ ] Post-change review completed

**Review Date**: ___________________________________________________

---

## 13. Post-Change Review

**Review Date**: ___________________________________________________
**Attendees**: _____________________________________________________

### Results
**Quantitative**:
- Performance vs. target: __________________________________________
- User metrics: ____________________________________________________
- Incident count: __________________________________________________

**Qualitative**:
- User feedback: ___________________________________________________
- Team feedback: ___________________________________________________

### Lessons Learned
1. _________________________________________________________________
2. _________________________________________________________________
3. _________________________________________________________________

### Process Improvements
1. _________________________________________________________________
2. _________________________________________________________________

---

## Final Go/No-Go

### Pre-Change Checklist Status
- Items completed: ______ / ______
- Completion rate: _____%
- Critical blockers: _______________________________________________

### Decision
- [ ] **GO** - Proceed with model change
- [ ] **CONDITIONAL GO** - Proceed with mitigation:
      _______________________________________________________________
- [ ] **NO-GO** - Defer model change

**Reason** (if NO-GO or CONDITIONAL):
___________________________________________________________________
___________________________________________________________________

**Decision Maker**: _________________________ Date: _______________

---

## Change Execution Record

**Change Started**: ______________________ (Date/Time)
**Change Completed**: ____________________ (Date/Time)
**Executed By**: _____________________
**Notes**:
___________________________________________________________________
___________________________________________________________________

---

*This checklist is based on the TrustByDesign framework for responsible AI model governance.*
