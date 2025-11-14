#!/usr/bin/env python3
"""
TrustByDesign Compliance Checklist Generator

Generates a customized compliance checklist based on safety level and system type.
"""

import argparse
import yaml
from datetime import datetime


def generate_checklist(safety_level: int, system_type: str, system_name: str) -> dict:
    """Generate compliance checklist for given safety level."""

    checklist = {
        'system': {
            'id': f"{system_type}-001",
            'name': system_name,
            'version': '1.0.0',
            'type': system_type,
            'safety_level': safety_level
        },
        'capabilities': {
            'allowed': ['<FILL_IN>'],
            'prohibited': ['<FILL_IN>']
        },
        'boundaries': {
            'limits': {
                'max_memory_mb': 100 if safety_level >= 2 else 0,
                'max_session_duration_minutes': 120,
                'max_api_calls_per_hour': 1000
            },
            'scope': {
                'temporal': get_default_temporal_scope(safety_level),
                'data_access': 'user_provided_only'
            }
        },
        'compliance_checks': {}
    }

    # Add appropriate checks based on level
    checklist['compliance_checks'] = get_compliance_checks(safety_level)

    # Add test results template
    checklist['test_results'] = get_test_results_template(safety_level)

    # Add metadata
    checklist['validated_at'] = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
    checklist['validator_version'] = '1.0'

    # Add guidance notes
    checklist['notes'] = get_guidance_notes(safety_level)

    return checklist


def get_default_temporal_scope(level: int) -> str:
    """Get default temporal scope for safety level."""
    return {
        1: 'session_only',
        2: 'persistent',
        3: 'persistent'
    }.get(level, 'session_only')


def get_compliance_checks(level: int) -> dict:
    """Get compliance checks for safety level."""
    checks = {}

    # Level 1: Basic checks
    checks['capability_boundaries'] = {
        'manifest_exists': False,  # User must set
        'out_of_scope_refused': False,
        'refusal_is_clear': False,
        'no_capability_creep': False
    }

    if level == 1:
        checks['transparency'] = {
            'confidence_levels_present': False,
            'reasoning_available': False,
            'sources_cited': False,
            'uncertainty_acknowledged': False
        }

    # Level 2+: Full checks
    if level >= 2:
        checks['memory_safety'] = {
            'user_can_view': False,
            'user_can_delete_specific': False,
            'user_can_delete_all': False,
            'deletion_is_complete': False,
            'operations_logged': False
        }

        checks['transparency'] = {
            'confidence_levels_present': False,
            'reasoning_available': False,
            'sources_cited': False,
            'uncertainty_acknowledged': False
        }

        checks['consent_mechanisms'] = {
            'explicit_consent_required': False,
            'consent_explanation_clear': False,
            'consent_revocable': False,
            'revocation_triggers_deletion': False
        }

        checks['audit_logging'] = {
            'critical_events_logged': False,
            'log_format_structured': False,
            'log_integrity_verifiable': False,
            'logs_user_accessible': False,
            'retention_policy_defined': False
        }

    # Level 3: Additional governance checks
    if level == 3:
        checks['autonomous_governance'] = {
            'multi_stage_approval': False,
            'emergency_stop_available': False,
            'governance_oversight': False,
            'external_audit_conducted': False
        }

    return checks


def get_test_results_template(level: int) -> dict:
    """Get test results template."""
    results = {}

    if level >= 1:
        results['boundary_violation_test'] = 'not_tested'

    if level >= 2:
        results['memory_deletion_test'] = 'not_tested'
        results['transparency_test'] = 'not_tested'
        results['consent_revocation_test'] = 'not_tested'
        results['audit_log_integrity_test'] = 'not_tested'

    if level == 3:
        results['autonomous_halt_test'] = 'not_tested'
        results['approval_workflow_test'] = 'not_tested'

    return results


def get_guidance_notes(level: int) -> str:
    """Get guidance notes for the checklist."""
    notes = {
        1: """Level 1 (Observational) Checklist

This is for read-only, stateless systems with no data persistence.

REQUIRED:
- Define capability boundaries
- Refuse out-of-scope requests clearly

RECOMMENDED:
- Include transparency (confidence levels, reasoning)

To complete this checklist:
1. Fill in your actual capabilities under 'allowed'
2. List prohibited actions under 'prohibited'
3. Implement each check and mark as 'true' when done
4. Run: python tooling/validate_safety.py --level 1 --config this-file.yaml
5. All checks should pass before deployment

To upgrade to Level 2:
- Add memory consent mechanisms
- Implement audit logging
- Enable user data inspection/deletion
""",
        2: """Level 2 (Interactive) Checklist

This is for systems with memory and user data persistence.

REQUIRED - ALL MUST BE TRUE:
- Memory safety (user can view, delete data)
- Capability boundaries (clear limits)
- Transparency (confidence, reasoning)
- Consent mechanisms (explicit, revocable)
- Audit logging (complete, accessible)

To complete this checklist:
1. Fill in your capabilities and boundaries
2. Implement ALL Level 2 requirements
3. Mark each check as 'true' when implemented and tested
4. Run: python tooling/validate_safety.py --level 2 --config this-file.yaml
5. Achieve 100% compliance before deployment

Common pitfalls:
- Storing data before getting consent
- Incomplete data deletion
- Missing confidence levels in outputs
- Inadequate audit logging

To upgrade to Level 3:
- Add multi-stage approval workflows
- Implement emergency stop
- Enable governance oversight
- Schedule external audits
""",
        3: """Level 3 (Autonomous) Checklist

This is for autonomous agents with long-term goals and real-world actions.

REQUIRED - ALL MUST BE TRUE:
- All Level 2 requirements
- Multi-stage approval for high-stakes actions
- Emergency stop mechanism
- Governance oversight
- External audit (quarterly recommended)

To complete this checklist:
1. Ensure ALL Level 2 requirements are met first
2. Implement Level 3-specific requirements
3. Mark each check as 'true' when implemented
4. Schedule external audit
5. Run: python tooling/validate_safety.py --level 3 --config this-file.yaml
6. External audit required before production deployment

Level 3 is HIGH RISK. Only use if you truly need autonomy.
Most use cases are satisfied by Level 2.

Key considerations:
- Approval workflows for all significant actions
- Robust failure modes and rollback
- Comprehensive monitoring
- Regular external review
- Clear escalation procedures
"""
    }

    return notes.get(level, "No guidance available for this level")


def main():
    parser = argparse.ArgumentParser(
        description='Generate TrustByDesign compliance checklist',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate Level 2 checklist for a chatbot
  python generate_compliance_checklist.py --level 2 --type agent --name "My Chatbot"

  # Generate and save
  python generate_compliance_checklist.py -l 2 -t agent -n "My Agent" -o checklist.yaml
        """
    )

    parser.add_argument(
        '-l', '--level',
        type=int,
        required=True,
        choices=[1, 2, 3],
        help='Safety level (1=Observational, 2=Interactive, 3=Autonomous)'
    )

    parser.add_argument(
        '-t', '--type',
        type=str,
        required=True,
        choices=['agent', 'service', 'tool', 'framework'],
        help='System type'
    )

    parser.add_argument(
        '-n', '--name',
        type=str,
        required=True,
        help='System name'
    )

    parser.add_argument(
        '-o', '--output',
        type=str,
        help='Output file (default: print to stdout)'
    )

    args = parser.parse_args()

    # Generate checklist
    checklist = generate_checklist(args.level, args.type, args.name)

    # Output
    if args.output:
        with open(args.output, 'w') as f:
            yaml.dump(checklist, f, default_flow_style=False, sort_keys=False)
        print(f"✅ Compliance checklist generated: {args.output}")
        print(f"\nNext steps:")
        print(f"1. Review and complete the checklist")
        print(f"2. Implement all required safety protocols")
        print(f"3. Run: python tooling/validate_safety.py --level {args.level} --config {args.output}")
    else:
        print(yaml.dump(checklist, default_flow_style=False, sort_keys=False))


if __name__ == '__main__':
    main()
