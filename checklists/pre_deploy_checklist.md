# Pre-Deployment Checklist

**System**: ___________________________
**Version**: ___________________________
**Deployment Date**: ___________________________
**Deployed By**: ___________________________

---

## 1. Testing & Validation

- [ ] All unit tests passing
- [ ] Integration tests passing
- [ ] End-to-end tests passing
- [ ] Performance benchmarks met
- [ ] Load testing completed
- [ ] Hallucination testing completed (sample size: _____)
- [ ] Bias testing completed for key demographics
- [ ] Red team / adversarial testing conducted
- [ ] Edge case testing completed

**Notes**:
___________________________________________________________________
___________________________________________________________________

---

## 2. Risk Assessment

- [ ] Risk register reviewed and up to date
- [ ] All Critical risks have mitigations in place
- [ ] All High risks assessed and plan documented
- [ ] New risks from this version identified and added
- [ ] Risk owner approval obtained

**Critical/High Risks for This Deployment**:
1. _________________________________________________________________
2. _________________________________________________________________
3. _________________________________________________________________

---

## 3. Documentation

- [ ] System documentation updated
- [ ] API documentation current
- [ ] User guides updated
- [ ] Trust policy reviewed and current
- [ ] Incident response procedures documented
- [ ] Rollback procedures documented
- [ ] Architecture diagrams updated
- [ ] Data flow diagrams updated

**Docs Location**: _________________________________________________

---

## 4. Monitoring & Alerts

- [ ] Production monitoring configured
- [ ] Key metrics dashboards created
- [ ] Alerting rules defined and tested
- [ ] Alert routing configured (who gets notified)
- [ ] Logging enabled and tested
- [ ] Log aggregation working
- [ ] Error tracking configured (e.g., Sentry)
- [ ] Performance monitoring configured (e.g., APM)

**Dashboard URL**: _________________________________________________
**Alert Recipients**: _______________________________________________

---

## 5. Safety & Governance

- [ ] Uncertainty tagging implemented where needed
- [ ] Output filtering/safety rails in place
- [ ] Rate limiting configured
- [ ] Input validation implemented
- [ ] PII detection/scrubbing active
- [ ] Content moderation active (if applicable)
- [ ] Audit logging enabled
- [ ] Privacy controls verified

**Safety Mechanisms**:
- _________________________________________________________________
- _________________________________________________________________

---

## 6. Data & Privacy

- [ ] Data retention policies configured
- [ ] User consent mechanisms working
- [ ] Right to deletion implemented and tested
- [ ] Data encryption verified (at rest and in transit)
- [ ] Access controls reviewed
- [ ] Backup procedures tested
- [ ] GDPR/CCPA compliance verified (if applicable)
- [ ] Data classification applied

**Data Steward Sign-off**: _________________________________________

---

## 7. Incident Response

- [ ] Incident response team identified
- [ ] On-call rotation configured
- [ ] Escalation path documented
- [ ] Emergency contacts list current
- [ ] Runbooks created for common issues
- [ ] Communication templates prepared
- [ ] Status page ready (if applicable)

**Primary On-Call**: _______________________________________________
**Backup On-Call**: ________________________________________________

---

## 8. Rollback Plan

- [ ] Rollback procedure documented and tested
- [ ] Previous version available for quick rollback
- [ ] Rollback can be performed within ____ minutes
- [ ] Database migration rollback tested (if applicable)
- [ ] Feature flags configured for gradual rollout
- [ ] Traffic splitting configured (if applicable)

**Rollback Time Estimate**: ________________________________________
**Rollback Owner**: ________________________________________________

---

## 9. Deployment Strategy

- [ ] Deployment method selected:
      □ Blue/Green  □ Canary  □ Rolling  □ All-at-once
- [ ] Staged rollout plan defined (if applicable)
- [ ] Initial rollout percentage: _____%
- [ ] Full rollout timeline: ________________________________________
- [ ] Success criteria defined for progression
- [ ] Deployment window scheduled
- [ ] Maintenance window communicated (if needed)

**Rollout Schedule**:
- Phase 1: _________________________________________________________
- Phase 2: _________________________________________________________
- Phase 3: _________________________________________________________

---

## 10. Communication

- [ ] Stakeholders notified of deployment
- [ ] Users notified (if user-facing changes)
- [ ] Customer support team briefed
- [ ] Marketing/PR aligned (if applicable)
- [ ] Change log prepared
- [ ] Release notes published

**Stakeholder Communication Date**: ___________________________________

---

## 11. Approvals

### Technical Approval
- [ ] Engineering Lead: _________________________ Date: __________
- [ ] QA Lead: __________________________________ Date: __________
- [ ] Security Review: ___________________________ Date: __________

### Business Approval
- [ ] Product Owner: ____________________________ Date: __________
- [ ] Risk Owner: _______________________________ Date: __________
- [ ] Executive Sponsor (if required): ____________ Date: __________

---

## 12. Post-Deployment Plan

- [ ] Monitoring duration defined (e.g., 48 hours intensive)
- [ ] Success metrics identified
- [ ] Post-deployment review scheduled
- [ ] Lessons learned session scheduled
- [ ] Documentation update plan

**Post-Deploy Review Date**: _______________________________________

---

## Final Go/No-Go Decision

### Pre-Deployment Score
Count the checkboxes:
- Total checks: _____
- Completed: _____
- Completion rate: _____%

**Minimum required for GO**: 95% (with no Critical items incomplete)

### Critical Blockers
Any unchecked items that are blockers:
1. _________________________________________________________________
2. _________________________________________________________________

### Decision
- [ ] **GO** - Ready to deploy
- [ ] **NO-GO** - Defer deployment

**Reason** (if NO-GO): ______________________________________________
___________________________________________________________________

**Decision Maker**: ________________________________________________
**Date/Time**: _____________________________________________________

---

## Deployment Execution

**Started**: _____________________ (Date/Time)
**Completed**: ___________________ (Date/Time)
**Deployed By**: _________________
**Deployment Notes**:
___________________________________________________________________
___________________________________________________________________
___________________________________________________________________

---

## Post-Deployment Verification (Within 1 Hour)

- [ ] System is live and accessible
- [ ] Core functionality verified
- [ ] Error rates within normal range
- [ ] Response times acceptable
- [ ] No critical alerts fired
- [ ] Smoke tests passing

**Verified By**: _________________________ Date/Time: _____________

---

*This checklist is based on the TrustByDesign framework for responsible AI deployment.*
