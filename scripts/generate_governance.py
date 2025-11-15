#!/usr/bin/env python3
# FEU Contract: Fact/Estimate/Unknown | Bound to Master Citation v15.2
# All outputs must distinguish epistemic status: Fact, Estimate, or Unknown
"""
TrustByDesign Governance Declaration Generator

Interactive tool to generate a complete governance declaration for your system.
"""

import argparse
import json
import yaml
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict


class GovernanceGenerator:
    """Interactive governance declaration generator."""

    def __init__(self):
        self.declaration = {}

    def generate(self, interactive=True) -> Dict:
        """Generate governance declaration interactively or from template."""
        print("\n" + "=" * 70)
        print("  TrustByDesign Governance Declaration Generator")
        print("=" * 70)
        print("\nThis tool will help you create a complete governance declaration")
        print("for your AI system. Answer the questions to generate your declaration.\n")
        print("=" * 70 + "\n")

        # System Information
        self._collect_system_info()

        # Safety Level
        self._collect_safety_level()

        # Capabilities
        self._collect_capabilities()

        # Boundaries
        self._collect_boundaries()

        # Governance Structure
        self._collect_governance()

        # Audit Configuration
        self._collect_audit_config()

        # Consent (if Level 2+)
        if self.declaration['system']['safety_level'] >= 2:
            self._collect_consent_config()

        # Incident Response
        self._collect_incident_response()

        # Finalize
        self._finalize_declaration()

        return self.declaration

    def _collect_system_info(self):
        """Collect basic system information."""
        print("\n📋 SYSTEM INFORMATION")
        print("-" * 70)

        self.declaration['system'] = {
            'id': self._ask("System ID (e.g., 'chatbot-001'): "),
            'name': self._ask("System Name: "),
            'type': self._ask_choice(
                "System Type: ",
                ['agent', 'service', 'framework', 'tool']
            ),
            'version': self._ask("Version (e.g., '1.0.0'): "),
            'description': self._ask("Brief Description: ")
        }

    def _collect_safety_level(self):
        """Determine appropriate safety level."""
        print("\n🛡️  SAFETY LEVEL DETERMINATION")
        print("-" * 70)
        print("Answer these questions to determine your safety level:")

        persists_data = self._ask_yes_no("Does your system persist data between sessions?")

        if not persists_data:
            read_only = self._ask_yes_no("Is your system read-only (no state changes)?")
            if read_only:
                level = 1
                print("\n→ Recommended Safety Level: 1 (Observational)")
            else:
                level = 2
                print("\n→ Recommended Safety Level: 2 (Interactive, ephemeral)")
        else:
            autonomous = self._ask_yes_no("Does it take autonomous actions without user approval?")
            if autonomous:
                level = 3
                print("\n→ Recommended Safety Level: 3 (Autonomous)")
            else:
                level = 2
                print("\n→ Recommended Safety Level: 2 (Interactive with memory)")

        confirm = self._ask_yes_no(f"Use Safety Level {level}?", default="yes")
        if not confirm:
            level = int(self._ask("Enter safety level (1, 2, or 3): "))

        self.declaration['system']['safety_level'] = level

    def _collect_capabilities(self):
        """Collect system capabilities."""
        print("\n⚙️  CAPABILITIES")
        print("-" * 70)

        allowed = []
        print("Enter allowed capabilities (one per line, empty line when done):")
        while True:
            cap = self._ask("  Capability: ").strip()
            if not cap:
                break
            allowed.append(cap)

        prohibited = []
        print("\nEnter prohibited actions (one per line, empty line when done):")
        while True:
            action = self._ask("  Prohibited: ").strip()
            if not action:
                break
            prohibited.append(action)

        self.declaration['capabilities'] = {
            'allowed': allowed,
            'prohibited': prohibited
        }

        # Level 3: Actions requiring approval
        if self.declaration['system']['safety_level'] == 3:
            requires_approval = []
            print("\nEnter actions requiring approval (one per line, empty when done):")
            while True:
                action = self._ask("  Requires approval: ").strip()
                if not action:
                    break
                requires_approval.append(action)
            self.declaration['capabilities']['requires_approval'] = requires_approval

    def _collect_boundaries(self):
        """Collect system boundaries."""
        print("\n🚧 BOUNDARIES")
        print("-" * 70)

        print("Resource Limits:")
        self.declaration['boundaries'] = {
            'limits': {
                'max_memory_mb': int(self._ask("  Max memory (MB): ", default="100")),
                'max_session_duration_minutes': int(
                    self._ask("  Max session duration (minutes): ", default="120")
                ),
                'max_api_calls_per_hour': int(
                    self._ask("  Max API calls per hour: ", default="1000")
                )
            },
            'scope': {
                'temporal': self._ask_choice(
                    "  Temporal scope: ",
                    ['session_only', 'persistent', 'limited_persistence']
                ),
                'data_access': self._ask_choice(
                    "  Data access: ",
                    ['user_provided_only', 'local_filesystem', 'network']
                )
            }
        }

    def _collect_governance(self):
        """Collect governance configuration."""
        print("\n⚖️  GOVERNANCE")
        print("-" * 70)

        self.declaration['governance'] = {
            'self_governance': self._ask_yes_no(
                "Enable self-governance (real-time checks)?",
                default="yes"
            ),
            'automated_validation': self._ask_yes_no(
                "Enable automated validation (CI/CD)?",
                default="yes"
            ),
            'external_audit': self._ask_yes_no(
                "Require external audit?",
                default="yes" if self.declaration['system']['safety_level'] == 3 else "no"
            )
        }

        if self.declaration['governance']['external_audit']:
            self.declaration['governance']['audit_frequency'] = self._ask_choice(
                "Audit frequency: ",
                ['monthly', 'quarterly', 'annual']
            )

    def _collect_audit_config(self):
        """Collect audit trail configuration."""
        print("\n📝 AUDIT TRAIL")
        print("-" * 70)

        level = self.declaration['system']['safety_level']
        min_retention = 0 if level == 1 else (30 if level == 2 else 90)

        self.declaration['audit_trail'] = {
            'format': self._ask_choice(
                "Log format: ",
                ['json', 'yaml', 'glyphtrail']
            ),
            'retention_days': int(
                self._ask(f"Retention (days, minimum {min_retention}): ", default=str(min_retention))
            ),
            'user_accessible': self._ask_yes_no(
                "Logs user-accessible?",
                default="yes" if level >= 2 else "no"
            )
        }

    def _collect_consent_config(self):
        """Collect consent configuration (Level 2+)."""
        print("\n✋ CONSENT")
        print("-" * 70)

        required_for = []
        print("What requires consent? (one per line, empty when done):")
        suggestions = ['memory_persistence', 'behavioral_adaptation', 'data_sharing']
        for suggestion in suggestions:
            if self._ask_yes_no(f"  {suggestion}?", default="yes"):
                required_for.append(suggestion)

        custom = True
        while custom:
            custom_item = self._ask("  Custom item (empty when done): ").strip()
            if custom_item:
                required_for.append(custom_item)
            else:
                custom = False

        self.declaration['consent'] = {
            'required_for': required_for,
            'consent_flow': {
                'timing': self._ask_choice(
                    "When to request consent: ",
                    ['first_interaction', 'before_first_storage', 'on_demand']
                ),
                'explanation_provided': True,
                'granular_controls': self._ask_yes_no(
                    "Granular controls (users choose what to consent to)?",
                    default="yes"
                ),
                'default_state': 'no_consent'
            },
            'revocation': {
                'user_initiated': True,
                'triggers_deletion': True,
                'immediate_effect': True
            }
        }

    def _collect_incident_response(self):
        """Collect incident response configuration."""
        print("\n🚨 INCIDENT RESPONSE")
        print("-" * 70)

        self.declaration['incident_response'] = {
            'anomaly_detection': self._ask_choice(
                "Anomaly detection: ",
                ['manual', 'automated', 'both']
            ),
            'response_times': {
                'alert_generated_within_minutes': 5,
                'owner_notified_within_minutes': 15,
                'investigation_started_within_hours': 2,
                'users_notified_within_hours': 24
            },
            'emergency_stop': {
                'user_initiated': True,
                'commands': ['stop', 'cancel', 'halt']
            }
        }

    def _finalize_declaration(self):
        """Add final metadata."""
        self.declaration['compliance'] = {
            'framework': 'TrustByDesign',
            'framework_version': '1.0',
            'compliant': True
        }

        self.declaration['updates'] = {
            'last_updated': datetime.now().strftime('%Y-%m-%d'),
            'update_frequency': 'as_needed'
        }

        # Contact info
        print("\n👤 RESPONSIBILITY")
        print("-" * 70)
        self.declaration['responsibility'] = {
            'system_owner': {
                'name': self._ask("System owner name: "),
                'organization': self._ask("Organization (optional): ", required=False)
            }
        }

    def _ask(self, prompt: str, default: str = "", required: bool = True) -> str:
        """Ask for input with optional default."""
        while True:
            if default:
                response = input(f"{prompt}[{default}] ").strip()
                return response if response else default
            else:
                response = input(prompt).strip()
                if response or not required:
                    return response
                print("  This field is required.")

    def _ask_yes_no(self, prompt: str, default: str = "yes") -> bool:
        """Ask yes/no question."""
        response = self._ask(f"{prompt} (y/n): ", default=default[0])
        return response.lower() in ['y', 'yes']

    def _ask_choice(self, prompt: str, choices: list) -> str:
        """Ask user to choose from options."""
        print(prompt)
        for i, choice in enumerate(choices, 1):
            print(f"  {i}. {choice}")

        while True:
            response = self._ask("Choose: ", default="1")
            try:
                idx = int(response) - 1
                if 0 <= idx < len(choices):
                    return choices[idx]
                print(f"  Please choose 1-{len(choices)}")
            except ValueError:
                # Try matching string
                if response in choices:
                    return response
                print(f"  Invalid choice. Choose 1-{len(choices)}")


def main():
    parser = argparse.ArgumentParser(
        description='Generate TrustByDesign governance declaration',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Interactive generation
  python generate_governance.py

  # Save to YAML
  python generate_governance.py --output governance.yaml

  # Save to JSON
  python generate_governance.py --output governance.json --format json
        """
    )

    parser.add_argument(
        '--output',
        type=str,
        help='Output file path (YAML or JSON based on extension)'
    )

    parser.add_argument(
        '--format',
        type=str,
        choices=['yaml', 'json'],
        help='Output format (overrides file extension)'
    )

    args = parser.parse_args()

    # Generate declaration
    generator = GovernanceGenerator()
    declaration = generator.generate()

    # Determine format
    output_format = args.format
    if not output_format and args.output:
        ext = Path(args.output).suffix.lower()
        output_format = 'json' if ext == '.json' else 'yaml'
    elif not output_format:
        output_format = 'yaml'

    # Output
    if args.output:
        with open(args.output, 'w') as f:
            if output_format == 'json':
                json.dump(declaration, f, indent=2)
            else:
                yaml.dump(declaration, f, default_flow_style=False, sort_keys=False)
        print(f"\n✅ Governance declaration saved to: {args.output}")
    else:
        # Print to stdout
        print("\n" + "=" * 70)
        print("  GENERATED GOVERNANCE DECLARATION")
        print("=" * 70 + "\n")
        if output_format == 'json':
            print(json.dumps(declaration, indent=2))
        else:
            print(yaml.dump(declaration, default_flow_style=False, sort_keys=False))


if __name__ == '__main__':
    main()
