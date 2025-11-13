#!/usr/bin/env python3
"""
TrustByDesign Safety Validation Tool

Validates a system configuration against TrustByDesign safety requirements.
"""

import argparse
import json
import sys
import yaml
from typing import Dict, List, Tuple
from pathlib import Path


class SafetyValidator:
    """Validates TrustByDesign safety compliance."""

    def __init__(self, safety_level: int):
        self.safety_level = safety_level
        self.checks_passed = []
        self.checks_failed = []

    def validate(self, config: Dict) -> Tuple[bool, int, List[str]]:
        """
        Validate configuration against safety requirements.

        Returns: (all_passed, score_percentage, gaps)
        """
        print(f"\n🔍 Validating TrustByDesign Level {self.safety_level} Compliance\n")
        print("=" * 60)

        # Run level-appropriate checks
        self._check_system_info(config)
        self._check_capability_boundaries(config)

        if self.safety_level >= 1:
            self._check_transparency(config, required=False)

        if self.safety_level >= 2:
            self._check_memory_safety(config)
            self._check_transparency(config, required=True)
            self._check_consent_mechanisms(config)
            self._check_audit_logging(config)

        if self.safety_level >= 3:
            self._check_governance_oversight(config)

        # Calculate results
        total_checks = len(self.checks_passed) + len(self.checks_failed)
        score = int((len(self.checks_passed) / total_checks * 100)) if total_checks > 0 else 0
        all_passed = len(self.checks_failed) == 0

        self._print_results(score, all_passed)

        return all_passed, score, self.checks_failed

    def _check_system_info(self, config: Dict):
        """Validate system information is complete."""
        print("\n📋 System Information")
        print("-" * 60)

        required_fields = ['id', 'name', 'version']
        system = config.get('system', {})

        for field in required_fields:
            if field in system and system[field]:
                self._pass(f"System {field} defined: {system[field]}")
            else:
                self._fail(f"System {field} missing or empty")

    def _check_capability_boundaries(self, config: Dict):
        """Validate capability boundaries are defined."""
        print("\n🛡️  Capability Boundaries")
        print("-" * 60)

        capabilities = config.get('capabilities', {})

        if 'allowed' in capabilities and len(capabilities['allowed']) > 0:
            self._pass(f"Capabilities defined: {len(capabilities['allowed'])} allowed")
        else:
            self._fail("No capabilities defined")

        if 'prohibited' in capabilities:
            self._pass(f"Prohibited actions listed: {len(capabilities['prohibited'])}")
        else:
            self._fail("No prohibited actions listed")

        # Check boundaries
        boundaries = config.get('boundaries', {})
        if 'limits' in boundaries:
            self._pass("Resource limits defined")
        else:
            self._fail("Resource limits not defined")

        if 'scope' in boundaries:
            self._pass("Operational scope defined")
        else:
            self._fail("Operational scope not defined")

    def _check_memory_safety(self, config: Dict):
        """Validate memory safety implementation."""
        print("\n🧠 Memory Safety (Level 2+ Required)")
        print("-" * 60)

        checks = config.get('compliance_checks', {}).get('memory_safety', {})

        required = {
            'user_can_view': 'Users can view stored data',
            'user_can_delete_specific': 'Users can delete specific items',
            'user_can_delete_all': 'Users can delete all data',
            'deletion_is_complete': 'Deletion is complete',
            'operations_logged': 'Memory operations logged'
        }

        for key, description in required.items():
            if checks.get(key) is True:
                self._pass(description)
            else:
                self._fail(f"Memory safety: {description}")

    def _check_transparency(self, config: Dict, required: bool = True):
        """Validate transparency implementation."""
        level_text = "Required" if required else "Recommended"
        print(f"\n💡 Transparency ({level_text})")
        print("-" * 60)

        checks = config.get('compliance_checks', {}).get('transparency', {})

        requirements = {
            'confidence_levels_present': 'Confidence levels in outputs',
            'reasoning_available': 'Reasoning traces available',
            'sources_cited': 'Sources cited for recalled info',
            'uncertainty_acknowledged': 'Uncertainty acknowledged'
        }

        for key, description in requirements.items():
            if checks.get(key) is True:
                self._pass(description)
            elif required:
                self._fail(f"Transparency: {description}")
            else:
                self._warn(f"Transparency: {description} (recommended)")

    def _check_consent_mechanisms(self, config: Dict):
        """Validate consent implementation."""
        print("\n✋ Consent Mechanisms (Level 2+ Required)")
        print("-" * 60)

        checks = config.get('compliance_checks', {}).get('consent_mechanisms', {})

        required = {
            'explicit_consent_required': 'Explicit consent required',
            'consent_explanation_clear': 'Consent explanation clear',
            'consent_revocable': 'Consent is revocable',
            'revocation_triggers_deletion': 'Revocation triggers deletion'
        }

        for key, description in required.items():
            if checks.get(key) is True:
                self._pass(description)
            else:
                self._fail(f"Consent: {description}")

    def _check_audit_logging(self, config: Dict):
        """Validate audit logging implementation."""
        print("\n📝 Audit Logging (Level 2+ Required)")
        print("-" * 60)

        checks = config.get('compliance_checks', {}).get('audit_logging', {})

        required = {
            'critical_events_logged': 'Critical events logged',
            'log_format_structured': 'Log format structured',
            'log_integrity_verifiable': 'Log integrity verifiable',
            'logs_user_accessible': 'Logs user-accessible',
            'retention_policy_defined': 'Retention policy defined'
        }

        for key, description in required.items():
            if checks.get(key) is True:
                self._pass(description)
            else:
                self._fail(f"Audit: {description}")

    def _check_governance_oversight(self, config: Dict):
        """Validate governance oversight (Level 3)."""
        print("\n⚖️  Governance Oversight (Level 3 Required)")
        print("-" * 60)

        # Check for governance declaration reference
        if 'governance' in config:
            self._pass("Governance structure defined")
        else:
            self._fail("Governance structure not defined")

        # Check for external audit plan
        governance = config.get('governance', {})
        if governance.get('external_audit'):
            self._pass("External audit configured")
        else:
            self._fail("External audit not configured (required for Level 3)")

    def _pass(self, check: str):
        """Record passed check."""
        self.checks_passed.append(check)
        print(f"  ✅ {check}")

    def _fail(self, check: str):
        """Record failed check."""
        self.checks_failed.append(check)
        print(f"  ❌ {check}")

    def _warn(self, check: str):
        """Record warning (not counted in pass/fail)."""
        print(f"  ⚠️  {check}")

    def _print_results(self, score: int, all_passed: bool):
        """Print validation results summary."""
        print("\n" + "=" * 60)
        print("\n📊 VALIDATION RESULTS")
        print("=" * 60)

        total = len(self.checks_passed) + len(self.checks_failed)
        print(f"\nChecks Passed: {len(self.checks_passed)} / {total}")
        print(f"Compliance Score: {score}%")

        if all_passed:
            print("\n✅ STATUS: COMPLIANT")
            print(f"   System meets all Level {self.safety_level} requirements")
        elif score >= 80:
            print("\n⚠️  STATUS: MOSTLY COMPLIANT")
            print(f"   Address {len(self.checks_failed)} gap(s) before deployment")
        else:
            print("\n❌ STATUS: NON-COMPLIANT")
            print(f"   Significant gaps must be addressed")

        if self.checks_failed:
            print("\n🔧 GAPS TO ADDRESS:")
            for gap in self.checks_failed:
                print(f"   - {gap}")

        print("\n" + "=" * 60 + "\n")


def load_config(filepath: str) -> Dict:
    """Load configuration from YAML or JSON file."""
    path = Path(filepath)

    if not path.exists():
        print(f"❌ Error: Config file not found: {filepath}")
        sys.exit(1)

    try:
        with open(path, 'r') as f:
            if path.suffix in ['.yaml', '.yml']:
                return yaml.safe_load(f)
            elif path.suffix == '.json':
                return json.load(f)
            else:
                print(f"❌ Error: Unsupported file format: {path.suffix}")
                sys.exit(1)
    except Exception as e:
        print(f"❌ Error loading config: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description='Validate TrustByDesign safety compliance',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Validate Level 2 system
  python validate_safety.py --level 2 --config my-agent-config.yaml

  # Validate and save results
  python validate_safety.py --level 2 --config my-agent.yaml --output report.json
        """
    )

    parser.add_argument(
        '--level',
        type=int,
        required=True,
        choices=[1, 2, 3],
        help='Safety level to validate against (1=Observational, 2=Interactive, 3=Autonomous)'
    )

    parser.add_argument(
        '--config',
        type=str,
        required=True,
        help='Path to configuration file (YAML or JSON)'
    )

    parser.add_argument(
        '--output',
        type=str,
        help='Output file for validation results (JSON)'
    )

    args = parser.parse_args()

    # Load configuration
    config = load_config(args.config)

    # Validate
    validator = SafetyValidator(args.level)
    all_passed, score, gaps = validator.validate(config)

    # Save results if requested
    if args.output:
        results = {
            'config_file': args.config,
            'safety_level': args.level,
            'compliance_score': score,
            'all_checks_passed': all_passed,
            'gaps': gaps
        }

        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2)

        print(f"📄 Results saved to: {args.output}\n")

    # Exit code based on compliance
    sys.exit(0 if all_passed else 1)


if __name__ == '__main__':
    main()
