# Data Processing Addendum (DPA) - Template Stub

## Purpose

This template provides a **starting point for Data Processing Agreements** (DPAs) required under GDPR and other privacy regulations for organizations deploying MirrorDNA-based systems as data processors.

**IMPORTANT**: This is a template stub for reference only and **does not constitute legal advice**. Have your legal counsel review and customize this agreement before use.

---

## When to Use This Template

**Use a DPA when**:
- You process personal data on behalf of another organization (you are the "Processor")
- You engage third-party vendors to process data (they are "Sub-Processors")
- GDPR, CCPA, or other regulations require a data processing agreement

**Parties**:
- **Data Controller**: Organization that determines purposes and means of data processing
- **Data Processor**: Organization that processes data on behalf of the Controller (e.g., your MirrorDNA deployment)

---

## Data Processing Addendum

**THIS ADDENDUM** is entered into as of [Date] between:

**DATA CONTROLLER**:
- Legal Name: [Controller Company Name]
- Address: [Controller Address]
- Contact: [Controller Contact]
- ("Controller")

**DATA PROCESSOR**:
- Legal Name: [Processor Company Name]
- Address: [Processor Address]
- Contact: [Processor Contact]
- ("Processor")

**WHEREAS**, the Processor provides [Service Description: e.g., AI-powered customer support system] to the Controller under a [Master Services Agreement / Terms of Service] dated [Date] ("Main Agreement");

**WHEREAS**, in providing the Services, Processor will process personal data on behalf of Controller;

**WHEREAS**, the parties wish to comply with applicable data protection laws, including the EU General Data Protection Regulation (GDPR) and other applicable privacy regulations;

**NOW THEREFORE**, the parties agree as follows:

---

## 1. Definitions

1.1 **"Personal Data"** means any information relating to an identified or identifiable natural person as defined by applicable data protection laws.

1.2 **"Processing"** means any operation performed on Personal Data, including collection, storage, use, disclosure, or deletion.

1.3 **"Data Subject"** means the individual to whom Personal Data relates.

1.4 **"Sub-Processor"** means any third party engaged by Processor to process Personal Data on behalf of Controller.

1.5 **"Applicable Data Protection Law"** means GDPR, CCPA, and any other applicable privacy or data protection law.

1.6 **"Security Incident"** means any breach of security leading to accidental or unlawful destruction, loss, alteration, unauthorized disclosure of, or access to Personal Data.

---

## 2. Scope and Details of Processing

2.1 **Subject Matter**: Provision of [Service Description, e.g., "AI-powered conversational agent with memory capabilities"]

2.2 **Duration**: The term of the Main Agreement

2.3 **Nature and Purpose of Processing**: [Describe, e.g., "Storing and retrieving user conversation history to provide personalized responses; analyzing user queries to generate relevant outputs"]

2.4 **Types of Personal Data**:
- [e.g., User queries and commands]
- [e.g., Conversation history]
- [e.g., User preferences and settings]
- [e.g., Interaction metadata (timestamps, session IDs)]
- [Other types]

2.5 **Categories of Data Subjects**:
- [e.g., Controller's employees]
- [e.g., Controller's customers]
- [e.g., Controller's partners]
- [Other categories]

2.6 **Special Categories of Personal Data**: [None / Specify if processing sensitive data under GDPR Art. 9]

---

## 3. Processor Obligations

3.1 **Processing Instructions**: Processor shall process Personal Data only on documented instructions from Controller, including with regard to transfers of Personal Data to third countries or international organizations, unless required by applicable law.

3.2 **Confidentiality**: Processor shall ensure that persons authorized to process Personal Data are under appropriate confidentiality obligations.

3.3 **Security Measures**: Processor shall implement appropriate technical and organizational measures to ensure a level of security appropriate to the risk, including:
- Encryption of Personal Data in transit and at rest
- Measures to ensure ongoing confidentiality, integrity, availability, and resilience
- Regular testing and evaluation of security measures
- Specific measures outlined in Annex A (Technical and Organizational Measures)

3.4 **Sub-Processors**:
- Processor may engage Sub-Processors with Controller's prior written consent.
- Current Sub-Processors are listed in Annex B.
- Processor shall notify Controller of any intended changes (additions or replacements) to Sub-Processors, giving Controller the opportunity to object.
- Processor remains fully liable for Sub-Processor performance.

3.5 **Data Subject Rights**: Processor shall assist Controller in responding to Data Subject requests to exercise their rights under Applicable Data Protection Law (access, rectification, erasure, portability, etc.) by:
- Providing mechanisms for Data Subjects to exercise rights (e.g., deletion interface)
- Responding to Controller requests within [X business days]
- Implementing appropriate technical measures to facilitate rights

3.6 **Assistance to Controller**: Processor shall assist Controller in:
- Ensuring compliance with security obligations (GDPR Art. 32)
- Data protection impact assessments (GDPR Art. 35)
- Prior consultation with supervisory authorities (GDPR Art. 36)
- Responding to Data Subject requests (GDPR Art. 12-22)

3.7 **Security Incident Notification**: Processor shall notify Controller without undue delay (and in any event within [24/48/72 hours]) after becoming aware of a Security Incident, providing:
- Description of the incident
- Affected Personal Data categories and approximate number of Data Subjects
- Likely consequences
- Measures taken or proposed to mitigate

3.8 **Deletion or Return of Data**: Upon termination of Services, Processor shall (at Controller's choice):
- Delete all Personal Data, OR
- Return all Personal Data to Controller in machine-readable format
- Provide certification of deletion
- Exception: Data retained as required by applicable law

3.9 **Audit Rights**: Processor shall make available to Controller all information necessary to demonstrate compliance with this DPA and allow for and contribute to audits, including inspections, by:
- Providing SOC 2 or equivalent compliance reports
- Allowing on-site audits with [X days] prior notice (up to [X] times per year)
- Responding to compliance questionnaires

---

## 4. Controller Obligations

4.1 **Lawful Processing**: Controller warrants that its instructions for Processing comply with Applicable Data Protection Law.

4.2 **Processing Instructions**: Controller shall provide clear, documented instructions for Processing.

4.3 **Consent and Legal Basis**: Controller is responsible for obtaining necessary consents and establishing legal basis for Processing.

---

## 5. International Data Transfers

5.1 **Transfer Mechanism**: If Processor transfers Personal Data outside the EEA, UK, or Switzerland, such transfers shall be subject to appropriate safeguards as required by Applicable Data Protection Law:
- [ ] Standard Contractual Clauses (SCCs) — Annex C
- [ ] Adequacy Decision
- [ ] Binding Corporate Rules
- [ ] Other: [Specify]

5.2 **Transfer Impact Assessment**: Processor shall conduct and provide Transfer Impact Assessments as required by GDPR and Schrems II.

5.3 **Data Localization**: [If applicable] Personal Data shall be stored and processed only in [specific countries/regions].

---

## 6. Liability and Indemnification

6.1 **Liability**: Each party's liability under this DPA shall be subject to the limitations and exclusions set forth in the Main Agreement.

6.2 **Processor Liability**: Processor shall be liable for damages caused by Processing only where it has not complied with obligations specifically directed to processors under Applicable Data Protection Law or has acted outside or contrary to lawful instructions of Controller.

6.3 **Indemnification**: Processor shall indemnify and hold harmless Controller from any fines, penalties, or damages arising from Processor's breach of this DPA or Applicable Data Protection Law.

---

## 7. Term and Termination

7.1 **Term**: This DPA shall commence on the date first written above and continue for the duration of the Main Agreement.

7.2 **Termination**: This DPA may be terminated:
- Upon termination of the Main Agreement
- By either party for material breach with [X days] written notice
- Immediately by Controller if Processor suffers a Security Incident

7.3 **Survival**: Obligations regarding data deletion, confidentiality, and liability shall survive termination.

---

## 8. General Provisions

8.1 **Governing Law**: This DPA shall be governed by [Jurisdiction, e.g., "the laws of the State of Delaware, USA" or "the laws of England and Wales"].

8.2 **Amendments**: This DPA may only be amended by written agreement of both parties.

8.3 **Severability**: If any provision is found invalid, the remainder shall remain in effect.

8.4 **Order of Precedence**: In case of conflict between this DPA and the Main Agreement, this DPA shall prevail with respect to data protection matters.

8.5 **Entire Agreement**: This DPA, together with the Main Agreement and Annexes, constitutes the entire agreement regarding data processing.

---

## 9. Signatures

**DATA CONTROLLER**:

Signature: _______________________
Name: [Name]
Title: [Title]
Date: [Date]

**DATA PROCESSOR**:

Signature: _______________________
Name: [Name]
Title: [Title]
Date: [Date]

---

## ANNEX A: Technical and Organizational Measures

### Security Measures Implemented by Processor

**Access Control**:
- User authentication via [OAuth 2.0 / SAML / SSO]
- Multi-factor authentication [required / optional]
- Role-based access control (RBAC)
- Principle of least privilege
- Access logging and monitoring

**Encryption**:
- Data in transit: TLS 1.2+ encryption
- Data at rest: AES-256 encryption (or equivalent)
- Encrypted backups
- Key management: [AWS KMS / Azure Key Vault / HSM]

**Data Segregation**:
- User data isolated per account
- Multi-tenant architecture with logical separation
- [Physical separation if applicable]

**Logging and Monitoring**:
- Comprehensive audit logging of all critical operations
- Immutable logs (Glyphtrail or equivalent)
- Security monitoring and anomaly detection
- 24/7 security monitoring

**Incident Response**:
- Documented incident response plan
- Security incident notification within [24/48/72] hours
- Regular incident response drills

**Backup and Recovery**:
- Daily automated backups
- Encrypted backup storage
- Backup retention: [X days]
- Disaster recovery plan with RTO [X hours], RPO [X hours]
- Quarterly backup restoration testing

**Vulnerability Management**:
- Regular vulnerability scanning
- Patch management with defined SLAs
- [Annual / Semi-annual] penetration testing
- Responsible disclosure program

**Physical Security** (if applicable):
- Datacenter security per [SOC 2 / ISO 27001]
- Access controls and video surveillance
- [Or: Cloud provider security - AWS / Azure / GCP]

**Personnel Security**:
- Background checks for employees with data access
- Confidentiality agreements
- Security awareness training
- Access revocation on termination

**Development Security**:
- Secure software development lifecycle (SDLC)
- Code review and security testing
- Dependency scanning
- Version control and change management

---

## ANNEX B: Sub-Processors

### List of Authorized Sub-Processors

| Sub-Processor | Service | Data Access | Location | Safeguards |
|---------------|---------|-------------|----------|------------|
| [e.g., Amazon Web Services] | Cloud hosting | Infrastructure access to all data | [US, EU] | DPA, SOC 2, ISO 27001 |
| [e.g., Anthropic] | LLM API | User queries | [US] | DPA, no training on data |
| [e.g., DataDog] | Monitoring | Logs and metrics | [US, EU] | DPA, GDPR-compliant |
| [Add others] | | | | |

**Notification of Changes**: Processor shall notify Controller at least [30 days] in advance of adding or replacing Sub-Processors. Controller may object within [14 days] of notification.

---

## ANNEX C: Standard Contractual Clauses (SCCs)

### EU Standard Contractual Clauses for International Transfers

[If transfers occur from EEA/UK/Switzerland to non-adequate countries, attach the appropriate EU Standard Contractual Clauses:]

- **Module 2**: Controller to Processor transfers
- **Module 3**: Processor to Processor (for sub-processors)

**Current SCCs**: EU Commission Decision 2021/914 (June 2021)

[Attach full SCC text or incorporate by reference]

**Transfer Impact Assessment**: Available upon request, demonstrating that applicable law in destination country does not impinge on SCC protections.

---

## ANNEX D: Data Subject Rights Support

### Processor Support for Data Subject Requests

Processor provides the following mechanisms to support Data Subject rights:

| Right (GDPR Article) | Implementation | Controller Access | Timeline |
|----------------------|----------------|-------------------|----------|
| **Access** (Art. 15) | Memory inspection interface, data export API | Self-service or API | Immediate |
| **Rectification** (Art. 16) | User can edit/correct memories | Self-service | Immediate |
| **Erasure** (Art. 17) | Deletion interface and API | Self-service or API | Immediate (active data); [X days] (backups) |
| **Restriction** (Art. 18) | Consent withdrawal, processing pause | Settings interface | Immediate |
| **Portability** (Art. 20) | JSON/CSV export | Self-service or API | Immediate |
| **Object** (Art. 21) | Opt-out mechanisms | Settings interface | Immediate |
| **Automated Decision-Making** (Art. 22) | Explanation of reasoning, human review option | Built-in | N/A (ongoing) |

**Process for Controller Requests**:
1. Controller submits request via [email / support portal / API]
2. Processor verifies authorization
3. Processor executes request within [X business days]
4. Processor provides confirmation and evidence to Controller

---

## Notes for Using This Template

**Customization Required**:
1. Fill in all [bracketed] placeholders with specific information
2. Select applicable options (delete inapplicable ones)
3. Customize security measures in Annex A to match your implementation
4. Update Sub-Processor list in Annex B
5. Attach SCCs in Annex C if international transfers occur

**Legal Review Essential**:
- Have legal counsel review before execution
- Ensure consistency with Main Services Agreement
- Verify compliance with all applicable jurisdictions
- Update as regulations and services change

**Regulatory References**:
- GDPR Article 28: Processor obligations
- GDPR Article 32: Security of processing
- GDPR Chapter V: International transfers
- CCPA Section 1798.100: Consumer rights

**Related Documents**:
- [Privacy and Data Handling](../docs/privacy_and_data_handling.md)
- [Security Questionnaire](security_questionnaire.md)
- [Trust Framework](../docs/trust_framework.md)

---

**Template Version**: 1.0
**Last Updated**: 2025-01-15
**Maintained by**: MirrorDNA-Reflection-Protocol

**DISCLAIMER**: This template is provided for informational purposes only and does not constitute legal advice. Consult qualified legal counsel before using this template or entering into any data processing agreement.
