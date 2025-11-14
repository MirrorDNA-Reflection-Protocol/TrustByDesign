# Security Questionnaire for MirrorDNA / ActiveMirrorOS

## Purpose

This template provides **standard responses to vendor security questionnaires** for organizations deploying MirrorDNA-based AI systems. Use this to answer common due diligence questions from customers, partners, and auditors.

**How to Use**:
1. Copy relevant sections to your response
2. Customize with deployment-specific details
3. Replace placeholders [like this] with actual information
4. Provide evidence/documentation links where indicated

---

## General Information

### 1. Company & Product Information

**Q: Describe your company and the product/service being evaluated.**

**A**: [Organization Name] provides AI-powered [description] built on the MirrorDNA-Reflection-Protocol and ActiveMirrorOS framework. Our system enables [key capabilities] while maintaining strong safety, transparency, and privacy protections through the TrustByDesign framework.

**Product**: [Product Name]
**Trust Level**: [Level 1 / Level 2 / Level 3]
**Primary Use Cases**: [e.g., customer support, code assistance, research]

---

**Q: What is the MirrorDNA / TrustByDesign framework?**

**A**: MirrorDNA is an open-source framework for building AI agents with persistent memory and identity. TrustByDesign is the associated governance and safety framework that ensures these systems operate with:
- **Transparency**: Explainable reasoning and accessible state
- **Consent**: User control over data and behavior
- **Boundedness**: Clear capability limits
- **Fallibility**: Acknowledgment of uncertainty
- **Auditability**: Comprehensive, immutable logs

More information: https://github.com/MirrorDNA-Reflection-Protocol/TrustByDesign

---

### 2. Governance & Compliance

**Q: Do you have a published governance framework?**

**A**: Yes. Our deployment adheres to the TrustByDesign framework and publishes a Governance Declaration that defines:
- System identity and capabilities
- Capability boundaries and limitations
- Safety protocols and compliance level
- Audit trail infrastructure
- Incident response procedures

**Documentation**: [Link to Governance Declaration]

---

**Q: What compliance frameworks or certifications do you maintain?**

**A**: Our deployment is designed for compliance with:
- [X] GDPR (EU General Data Protection Regulation)
- [X] CCPA (California Consumer Privacy Act)
- [X] SOC 2 Type [I/II] — [In progress / Certified / Planned]
- [ ] ISO 27001 — [Status]
- [ ] HIPAA — [If healthcare: Yes with BAA / No, not applicable]
- [ ] [Industry-specific certifications]

**Evidence**: [Certification documents, compliance reports, audit results]

---

**Q: Do you have a Data Protection Officer (DPO)?**

**A**: [Yes / No / Planned]

**If Yes**:
- **Name**: [DPO Name]
- **Contact**: [DPO Email]
- **Role**: Oversees privacy compliance, conducts DPIAs, serves as regulatory contact

---

## Data Privacy & Protection

### 3. Data Collection & Use

**Q: What data do you collect from users?**

**A**: We collect only data necessary for system operation:

**Primary Data**:
- User queries and commands
- Conversation history (if user consents to memory)
- User preferences and settings
- Interaction metadata (timestamps, session IDs)

**NOT Collected**:
- Biometric data
- Financial information (unless explicitly required for product function)
- Health information (unless HIPAA-compliant deployment)
- Third-party data without authorization

**Legal Basis (GDPR)**: [Consent / Legitimate Interest / Contract Performance]

---

**Q: How do you use the data you collect?**

**A**: Data is used exclusively for:

**Primary Purposes**:
1. Providing the service (response generation, memory, personalization)
2. System safety and self-governance (compliance validation)
3. Audit and accountability (immutable decision logs)

**Secondary Purposes** (Require Separate Consent):
1. System improvement (aggregate analysis, model training)
2. Analytics (usage patterns, performance metrics)

**Not Used For**: Marketing, advertising, profiling, or sale to third parties.

---

**Q: Do you sell user data to third parties?**

**A**: **No.** We do not sell, rent, or share user data with third parties for marketing, advertising, or any commercial purpose.

**Exceptions**:
- **Service Providers**: Cloud infrastructure, hosting (under DPA)
- **Legal Obligations**: Court orders, regulatory requirements
- **User-Initiated**: User explicitly exports or shares their data

---

### 4. Data Retention & Deletion

**Q: How long do you retain user data?**

**A**: Data retention varies by type:

| Data Type | Retention Period | Deletion Method |
|-----------|------------------|-----------------|
| Session data (Level 1) | Session only | Automatic on session end |
| User memories (Level 2+) | Until user deletion or [X days/months/years] | User-triggered or automatic expiry |
| Audit logs | [X months/years] | Automatic expiry per policy |
| Backups | [X days] | Automatic expiry |

**User Control**: Users can delete their data at any time via [deletion interface/API].

**Policy Documentation**: [Link to data retention policy]

---

**Q: How do users delete their data?**

**A**: Users can delete data through:

1. **Granular Deletion**: Delete specific memories or conversations via UI
2. **Full Deletion**: Request complete data erasure ("Right to be Forgotten")

**Deletion Process**:
- Immediate removal from active systems
- Metadata-only audit log entry (no content)
- Backup deletion within [X days] (backup retention window)
- Deletion confirmation provided to user

**Evidence**: User documentation, deletion workflow

---

### 5. Data Location & Transfers

**Q: Where is user data stored?**

**A**: User data is stored in [Geographic Region: e.g., United States, European Union, user's region].

**Infrastructure**: [AWS / Azure / GCP / On-Premise / Hybrid] in [region(s)]

**Data Residency**: [Specify if data stays in specific region, or if cross-border transfers occur]

---

**Q: Do you transfer data across borders?**

**A**: [Yes / No]

**If Yes**:
- **From/To**: [e.g., EU to US]
- **Safeguards**: [Standard Contractual Clauses (SCCs) / Adequacy Decision / Binding Corporate Rules]
- **User Control**: [If applicable, users can specify data residency preference]

**Documentation**: [SCCs, adequacy decisions, transfer impact assessments]

---

### 6. User Rights

**Q: How do you support user privacy rights (GDPR, CCPA)?**

**A**: We provide comprehensive user rights support:

| Right | Implementation | Access Method |
|-------|----------------|---------------|
| **Access** (view data) | Memory inspection interface | [UI/API] |
| **Rectification** (correct data) | User can edit/correct memories | [UI] |
| **Erasure** (delete data) | Full deletion functionality | [UI/API] |
| **Portability** (export data) | JSON/CSV export | [UI/API] |
| **Restrict Processing** | Consent withdrawal | [UI] |
| **Object** | Opt-out of specific uses | [UI/Settings] |

**Response Time**: Most rights exercisable immediately via self-service; requests processed within 30 days per GDPR.

---

## Security Controls

### 7. Authentication & Access Control

**Q: How do you authenticate users?**

**A**: User authentication via [OAuth 2.0 / SAML / SSO / Username+Password with MFA].

**Multi-Factor Authentication (MFA)**: [Required / Optional / Available]

**Session Management**:
- Session timeout: [X minutes]
- Secure session tokens (HTTPOnly, Secure flags)

---

**Q: How do you control access to user data?**

**A**: Access control based on:
- **User Isolation**: Users can only access their own data
- **Role-Based Access Control (RBAC)**: Administrators have limited access based on role
- **Least Privilege**: Minimal necessary permissions
- **Access Logging**: All data access logged for audit

**Verification**: Authorization checks before every data access operation.

---

### 8. Data Encryption

**Q: Is data encrypted at rest and in transit?**

**A**: **Yes.**

**In Transit**:
- TLS 1.2+ for all network communication
- HTTPS enforced for all endpoints
- Certificate management: [Process]

**At Rest**:
- AES-256 encryption (or equivalent) for stored data
- Encrypted backups
- Key management: [AWS KMS / Azure Key Vault / HSM / Other]

**Evidence**: [Encryption configuration, key management documentation]

---

### 9. Security Testing & Monitoring

**Q: What security testing do you perform?**

**A**: Regular security testing includes:
- **Automated Scanning**: [Daily/Weekly] vulnerability scanning
- **Penetration Testing**: [Annually/Semi-annually] by [internal team / third-party]
- **Code Review**: Security-focused code reviews on all changes
- **Dependency Scanning**: Automated scanning for vulnerable dependencies
- **Adversarial Testing**: Prompt injection, boundary probing (for AI-specific risks)

**Last Penetration Test**: [Date]
**Findings**: [Summary of findings and remediation]

---

**Q: How do you monitor for security incidents?**

**A**: 24/7 security monitoring:
- **SIEM/Logging**: [Tool: e.g., Splunk, ELK] for centralized logging
- **Anomaly Detection**: Automated detection of unusual access patterns
- **Alerts**: Real-time alerts for critical security events
- **SOC**: [If applicable] Security Operations Center monitoring

**Incident Response Time**: [SLA for detection and response]

---

### 10. Vulnerability Management

**Q: How do you manage vulnerabilities?**

**A**: Vulnerability management process:
1. **Detection**: Automated scanning, security research, responsible disclosure
2. **Assessment**: Severity classification (Critical/High/Medium/Low)
3. **Remediation**: Patching per severity SLA:
   - Critical: [X hours/days]
   - High: [X days]
   - Medium: [X weeks]
   - Low: [X months]
4. **Verification**: Validation that fix is effective
5. **Communication**: User notification for critical vulnerabilities

**Disclosure Policy**: [Link to responsible disclosure policy]

---

### 11. Incident Response

**Q: Do you have an incident response plan?**

**A**: **Yes.** Comprehensive incident response plan covering:
- Detection and containment
- Assessment and classification
- Notification (users, regulators, stakeholders)
- Remediation and recovery
- Post-incident review and improvement

**Plan Documentation**: [Link or attachment]

**Testing**: Incident response drills conducted [quarterly/annually]

---

**Q: How quickly do you notify users of a data breach?**

**A**: Breach notification timeline:
- **Detection to Assessment**: Within 24 hours
- **Regulatory Notification**: Within 72 hours (GDPR requirement)
- **User Notification**: Without undue delay if high risk to users
- **Communication**: Clear explanation of incident, impact, and remediation

**Historical Breaches**: [None to date / Summary of past incidents]

---

## AI-Specific Security

### 12. AI Safety & Trustworthiness

**Q: How do you ensure AI safety and prevent harmful outputs?**

**A**: Multi-layer safety approach:

**Design-Time Safety**:
- Capability boundaries defined and enforced
- Out-of-scope requests gracefully refused
- No access to unauthorized systems or data

**Runtime Safety**:
- Self-governance: Agent validates own outputs against safety criteria
- Confidence scoring: Low-confidence outputs flagged
- Uncertainty acknowledgment: System admits when it doesn't know
- Audit logging: All decisions logged for review

**Governance**:
- Trust Level [1/2/3] compliance
- Regular safety validation
- [Internal/External] audits

**Evidence**: [Governance declaration, safety validation reports]

---

**Q: How do you prevent prompt injection or adversarial attacks?**

**A**: Defense against AI-specific attacks:

**Prompt Injection Prevention**:
- Input validation and sanitization
- Separation of system prompts and user input
- Output filtering and validation
- Anomaly detection for injection patterns

**Memory Poisoning Prevention**:
- Source attribution on all memories
- User verification for critical information
- Anomaly detection for unusual memory patterns
- User can review and correct memories

**Capability Boundaries**:
- Requests validated against capability manifest
- Out-of-scope requests refused
- Boundary violations logged and monitored

**Testing**: Regular adversarial testing for AI-specific vulnerabilities.

---

**Q: Can users inspect and control what the AI remembers?**

**A**: **Yes.** Full user control over memory:
- **Inspect**: Users can view all stored memories via UI
- **Delete**: Users can delete specific memories or all data
- **Export**: Users can export their data in JSON format
- **Consent**: Memory persistence requires explicit user consent

**Transparency**: Memories include metadata (timestamp, source, confidence).

---

### 13. Model & Training Data

**Q: What AI model do you use?**

**A**: We use [Model Name/Provider: e.g., OpenAI GPT-4, Anthropic Claude, open-source model].

**Model Hosting**: [Cloud API / Self-hosted]
**Training Data**: [We do not train models / We use customer data for fine-tuning with consent]

**User Data in Training**: [No, user data is not used for model training / Yes, with explicit consent and anonymization]

---

**Q: Do you use customer data to improve your AI?**

**A**: [Choose one]

**Option 1 - No**: Customer data is not used for model training or system improvement. Data is used only for providing the service.

**Option 2 - Yes, with consent**: We may use anonymized, aggregated data for system improvement if users opt-in. Individual user data is never identifiable in training data. Users can opt-out at any time.

**Opt-Out**: [Process for opting out of data use for improvement]

---

## Operational Security

### 14. Infrastructure Security

**Q: Describe your infrastructure security controls.**

**A**: Infrastructure security measures:

**Network Security**:
- Firewalls and network segmentation
- DDoS protection
- Intrusion detection/prevention systems (IDS/IPS)

**Access Control**:
- VPN required for admin access
- MFA required for privileged access
- Bastion hosts for production access
- Access reviews [quarterly]

**Patch Management**:
- Automated patching for [OS, libraries, dependencies]
- Patch SLA: Critical [X hours], High [X days]

**Configuration Management**:
- Infrastructure as Code (IaC) for reproducibility
- Configuration drift detection
- Security hardening per CIS benchmarks

---

**Q: Do you use cloud services? Which ones?**

**A**: [Yes / No]

**If Yes**:
- **Provider**: [AWS / Azure / GCP / Other]
- **Services**: [EC2, S3, RDS, etc.]
- **Security**: Shared responsibility model, cloud-native security tools
- **Data Processing Agreement**: DPA with cloud provider
- **Certifications**: Provider's certifications (SOC 2, ISO 27001, etc.)

---

### 15. Business Continuity & Disaster Recovery

**Q: What is your backup and disaster recovery strategy?**

**A**: Comprehensive backup and recovery:

**Backups**:
- Frequency: [Daily/Hourly]
- Retention: [X days/weeks/months]
- Encryption: All backups encrypted
- Testing: Recovery tested [quarterly]

**Disaster Recovery**:
- RTO (Recovery Time Objective): [X hours]
- RPO (Recovery Point Objective): [X hours]
- Failover: [Automated / Manual] to [backup region/datacenter]
- DR Testing: Annual disaster recovery drills

**Business Continuity Plan**: [Link or summary]

---

**Q: What is your uptime SLA?**

**A**: [X%] uptime SLA (e.g., 99.9% = ~8.7 hours downtime/year)

**Historical Uptime**: [Last 12 months: X%]
**Monitoring**: Real-time status page at [URL]
**Maintenance Windows**: [Scheduled maintenance communication process]

---

## Vendor Management

### 16. Third-Party Vendors

**Q: What third-party vendors have access to customer data?**

**A**: Third-party data processors:

| Vendor | Service | Data Access | Safeguards |
|--------|---------|-------------|------------|
| [e.g., AWS] | Cloud hosting | Infrastructure access | DPA, SOC 2, encryption |
| [e.g., DataDog] | Monitoring | Logs, metrics | DPA, GDPR-compliant |
| [LLM Provider] | AI model | User queries (if cloud API) | DPA, no training on data |

**All vendors**: Data Processing Agreements (DPAs) in place, security assessments conducted.

---

**Q: How do you vet third-party vendors?**

**A**: Vendor security assessment process:
1. Security questionnaire
2. Review of certifications (SOC 2, ISO 27001, etc.)
3. Data Processing Agreement (DPA) execution
4. Ongoing monitoring and periodic review

**Vendor Risk Register**: Maintained and reviewed [quarterly].

---

## Organizational Security

### 17. Security Policies & Training

**Q: Do you have information security policies?**

**A**: **Yes.** Comprehensive information security policies covering:
- Acceptable use policy
- Access control policy
- Data classification and handling
- Incident response policy
- Change management policy
- Vendor management policy

**Review Frequency**: Policies reviewed and updated [annually].

---

**Q: Do you provide security training to employees?**

**A**: **Yes.** Security awareness training:
- **Onboarding**: All new employees receive security training
- **Ongoing**: [Annual/Quarterly] refresher training
- **Topics**: Phishing, data protection, incident reporting, AI-specific risks
- **Compliance**: Training completion tracked and enforced

**Last Training**: [Date and completion rate]

---

### 18. Background Checks

**Q: Do you conduct background checks on employees?**

**A**: [Yes / No / Varies by role]

**If Yes**:
- **Scope**: [All employees / Employees with data access / Privileged users]
- **Checks**: [Criminal background, employment verification, education verification]
- **Frequency**: Prior to hire, [periodic re-checks if applicable]

---

## Audit & Transparency

### 19. Audit Rights

**Q: Can we audit your security controls?**

**A**: [Yes / Yes, with notice / SOC 2 report provided in lieu of audit]

**Audit Options**:
- **SOC 2 Report**: [Available upon request / Annual report shared]
- **On-Site Audit**: [Permitted with [X days] notice and NDA]
- **Questionnaire**: This questionnaire and supporting documentation
- **Third-Party Audit**: Independent audit reports available

**Frequency**: [Annual audits conducted]

---

**Q: Do you provide compliance reports or certifications?**

**A**: **Yes.** Available reports:
- SOC 2 Type [I/II] Report
- Penetration test summary
- Compliance validation reports (TrustByDesign)
- [Other certifications]

**Access**: Available under NDA upon request.

---

### 20. Transparency & Communication

**Q: How do you communicate security incidents or changes to customers?**

**A**: Communication channels:
- **Security Incidents**: Email notification, status page updates
- **Service Changes**: [Email, release notes, changelog]
- **Security Updates**: Security bulletin or newsletter
- **Escalation**: Dedicated security contact: [email/phone]

**Notification SLA**: Critical incidents within [X hours], planned changes [X days] notice.

---

## Additional Information

### 21. Insurance

**Q: Do you carry cyber liability insurance?**

**A**: [Yes / No / Planned]

**If Yes**:
- **Coverage**: $[X million] cyber liability insurance
- **Provider**: [Insurance company]
- **Coverage**: Data breach response, regulatory fines, legal costs, etc.

---

### 22. Regulatory Compliance (Industry-Specific)

**Q: Are you HIPAA compliant?** (Healthcare)

**A**: [Yes, we offer HIPAA-compliant deployment with BAA / No, not applicable / In progress]

**If Yes**:
- Business Associate Agreement (BAA) available
- PHI encryption, access controls, audit logs
- HIPAA security rule compliance
- Breach notification procedures

---

**Q: Are you PCI-DSS compliant?** (Payment Processing)

**A**: [Yes, Level X / No, we do not process payment card data / Not applicable]

**Recommendation**: MirrorDNA systems are not designed to handle payment card data. Use dedicated payment processor with PCI-DSS compliance.

---

**Q: Are you FedRAMP authorized?** (US Government)

**A**: [Yes, [Moderate/High] / In progress / Not currently]

---

## Document Control

**Document Version**: 1.0
**Last Updated**: [Date]
**Prepared By**: [Name, Title]
**Approved By**: [Name, Title]
**Next Review**: [Date]

**Attachments** (Available upon request):
- [ ] Governance Declaration
- [ ] SOC 2 Report
- [ ] Penetration Test Summary
- [ ] Data Processing Agreement (DPA) Template
- [ ] Privacy Policy
- [ ] Incident Response Plan Summary
- [ ] Business Continuity Plan Summary
- [ ] [Other relevant documentation]

---

## Contact Information

**Security Contact**: [security@example.com]
**Privacy Contact / DPO**: [privacy@example.com]
**General Inquiries**: [contact@example.com]

**Security Disclosure**: [Link to responsible disclosure policy]

---

**Notes for Users of This Template**:
1. Customize all [bracketed] placeholders with your specific information
2. Remove sections not applicable to your deployment
3. Add industry-specific sections as needed
4. Keep document updated as systems and policies change
5. Provide supporting documentation as evidence
6. Have legal and compliance teams review before distribution

**This template is provided as guidance and does not constitute legal or compliance advice.**
