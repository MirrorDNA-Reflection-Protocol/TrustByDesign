#!/usr/bin/env python3
"""
Simple Trust Report Demo

Demonstrates the TrustByDesign toolkit by:
1. Loading example risks from YAML
2. Checking a sample trust policy
3. Generating a comprehensive trust report

Run this to see the toolkit in action!
"""

import sys
import os

# Add parent directory to path so we can import toolkit
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from toolkit import RiskRegistry, PolicyChecker, TrustReportBuilder
import yaml


def load_example_risks():
    """Load risks from example_risk_register.yaml"""
    print("📋 Loading example risks...")

    registry = RiskRegistry()

    # Load from the example YAML file
    example_path = os.path.join(os.path.dirname(__file__), 'example_risk_register.yaml')
    registry.load_from_yaml(example_path)

    print(f"   ✓ Loaded {len(registry.risks)} risks\n")
    return registry


def create_sample_policy():
    """
    Create a sample trust policy for demonstration.

    In practice, you'd load this from a YAML file or your config system.
    This is a simplified version for demo purposes.
    """
    print("📄 Creating sample trust policy...")

    policy = {
        'scope': {
            'system_name': 'SupportBot v2.3',
            'description': 'AI-powered customer support assistant',
            'capabilities': [
                'Answer customer questions',
                'Retrieve account information',
                'Create support tickets',
                'Escalate to human agents'
            ],
            'limitations': [
                'Cannot process payments',
                'Cannot provide medical advice',
                'Cannot make binding commitments'
            ]
        },
        'responsibilities': {
            'product_owner': 'Alex Martinez',
            'ml_lead': 'Dr. Sarah Chen',
            'security_lead': 'James Park'
        },
        'data_handling': {
            'pii_protection': 'AES-256 encryption',
            'retention_policy': '90 days for PII, 1 year for anonymized logs',
            'data_minimization': True
        },
        'incident_response': {
            'severity_levels': ['P0', 'P1', 'P2', 'P3'],
            'response_time_p0': '15 minutes',
            'on_call_team': 'engineering@company.com'
        },
        'monitoring': {
            'accuracy_target': 0.92,
            'hallucination_threshold': 0.02,
            'user_satisfaction_target': 4.2,
            'dashboards': ['Operations', 'Trust', 'Quality']
        },
        'escalation': {
            'triggers': [
                'User request',
                'Low confidence (<60%)',
                'Out of scope',
                'User frustration'
            ],
            'sla': '2 minutes'
        },
        # Note: Missing some recommended sections for demo purposes
    }

    print("   ✓ Policy created\n")
    return policy


def check_policy(policy):
    """Run policy checker on sample policy"""
    print("🔍 Checking policy compliance...")

    checker = PolicyChecker()
    issues = checker.check_policy(policy)

    print(f"   Found {len(issues)} issues:")

    # Print issues by type
    errors = [i for i in issues if i.severity == 'error']
    warnings = [i for i in issues if i.severity == 'warning']
    info = [i for i in issues if i.severity == 'info']

    if errors:
        print(f"   ❌ {len(errors)} errors")
        for issue in errors:
            print(f"      - {issue.message}")

    if warnings:
        print(f"   ⚠️  {len(warnings)} warnings")
        for issue in warnings:
            print(f"      - {issue.message}")

    if info:
        print(f"   ℹ️  {len(info)} info")

    print()
    return checker


def generate_report(registry, checker):
    """Generate comprehensive trust report"""
    print("📊 Generating trust report...")

    builder = TrustReportBuilder()

    # Set system info
    builder.set_system_info("SupportBot v2.3", "2.3.0")

    # Add risk registry
    builder.set_risk_registry(registry)

    # Add policy checker
    builder.set_policy_checker(checker)

    # Add some manual notes
    builder.add_note(
        "**Recent Incident**: INC-2025-003 (medical hallucination) occurred on 2025-01-08. "
        "Fixes deployed same day. Enhanced monitoring active. "
        "See example_incident_report.md for full details."
    )

    builder.add_note(
        "**Deployment Status**: Currently at 100% rollout after successful canary deployment. "
        "All metrics within acceptable ranges."
    )

    builder.add_note(
        "**System Details**: Model: Fine-tuned LLM (GPT-4 class) | "
        "Deployment: 2025-01-05 | Uptime: 99.8% | Daily users: ~5,000"
    )

    # Generate markdown report
    report = builder.build_markdown()

    print("   ✓ Report generated\n")
    return report


def print_summary(registry, checker, report):
    """Print summary of what was demonstrated"""
    print("=" * 70)
    print("DEMO SUMMARY")
    print("=" * 70)
    print()

    # Risk summary
    summary = registry.get_summary()
    print(f"📋 Risk Registry: {summary['total']} risks")
    print(f"   By Severity: {summary['by_severity']}")
    print(f"   By Status: {summary['by_status']}")
    print()

    # Policy summary
    policy_summary = checker.get_summary()
    print(f"📄 Policy Check: {policy_summary['total_issues']} issues found")
    print(f"   Errors: {policy_summary['errors']}")
    print(f"   Warnings: {policy_summary['warnings']}")
    print(f"   Info: {policy_summary['info']}")
    print()

    # Report summary
    print(f"📊 Trust Report: {len(report)} characters generated")
    print()

    # Example risks
    print("📌 Example Risks:")
    for risk in list(registry.risks.values())[:3]:
        print(f"   • [{risk.id}] {risk.title}")
        print(f"     Severity: {risk.severity.value.upper()} | Status: {risk.status.value}")
    print()

    print("=" * 70)
    print()


def save_report(report):
    """Save report to file"""
    output_path = os.path.join(os.path.dirname(__file__), 'demo_trust_report.md')

    with open(output_path, 'w') as f:
        f.write(report)

    print(f"✅ Full report saved to: {output_path}")
    print()


def print_report_preview(report):
    """Print first few lines of report"""
    lines = report.split('\n')
    preview_lines = 40

    print("=" * 70)
    print("REPORT PREVIEW (first 40 lines)")
    print("=" * 70)
    print()
    print('\n'.join(lines[:preview_lines]))
    print()
    print(f"... ({len(lines) - preview_lines} more lines)")
    print()


def main():
    """Run the demo"""
    print()
    print("=" * 70)
    print("TrustByDesign Toolkit Demo")
    print("=" * 70)
    print()
    print("This demo shows how to use the toolkit to:")
    print("  1. Manage AI system risks")
    print("  2. Validate trust policies")
    print("  3. Generate trust reports")
    print()
    print("=" * 70)
    print()

    try:
        # Load example risks
        registry = load_example_risks()

        # Create and check policy
        policy = create_sample_policy()
        checker = check_policy(policy)

        # Generate report
        report = generate_report(registry, checker)

        # Print summary
        print_summary(registry, checker, report)

        # Save report
        save_report(report)

        # Show preview
        print_report_preview(report)

        print("=" * 70)
        print("✅ Demo completed successfully!")
        print("=" * 70)
        print()
        print("Next steps:")
        print("  • Review the generated report: examples/demo_trust_report.md")
        print("  • Explore example files: example_trust_policy.md, example_risk_register.yaml")
        print("  • Read the docs: docs/")
        print("  • Try the toolkit with your own AI system!")
        print()

    except Exception as e:
        print(f"❌ Error running demo: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
