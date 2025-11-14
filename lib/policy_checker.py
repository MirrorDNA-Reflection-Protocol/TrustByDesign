"""
Policy Checker Module

Validates trust policies against required sections and best practices.
"""

from typing import Dict, List, Any, Optional
import yaml
import json


class PolicyIssue:
    """Represents a policy validation issue."""

    def __init__(self, severity: str, section: str, message: str):
        """
        Initialize policy issue.

        Args:
            severity: 'error', 'warning', or 'info'
            section: Policy section with issue
            message: Description of the issue
        """
        self.severity = severity
        self.section = section
        self.message = message

    def __str__(self) -> str:
        return f"[{self.severity.upper()}] {self.section}: {self.message}"

    def to_dict(self) -> Dict[str, str]:
        """Convert to dictionary."""
        return {
            'severity': self.severity,
            'section': self.section,
            'message': self.message
        }


class PolicyChecker:
    """
    Validates trust policies for completeness and best practices.

    Checks for required sections, recommended content, and common issues.
    """

    # Required sections for a complete trust policy
    REQUIRED_SECTIONS = [
        'scope',
        'responsibilities',
        'data_handling',
        'incident_response',
        'monitoring',
        'escalation',
    ]

    # Recommended sections for robust policies
    RECOMMENDED_SECTIONS = [
        'risk_assessment',
        'uncertainty_handling',
        'audit_trail',
        'user_consent',
        'model_governance',
        'deployment_process',
    ]

    def __init__(self):
        """Initialize policy checker."""
        self.issues: List[PolicyIssue] = []

    def check_policy(self, policy: Dict[str, Any]) -> List[PolicyIssue]:
        """
        Check policy for completeness and issues.

        Args:
            policy: Policy dict (from YAML/JSON or constructed)

        Returns:
            List of PolicyIssue objects
        """
        self.issues = []

        # Check required sections
        self._check_required_sections(policy)

        # Check recommended sections
        self._check_recommended_sections(policy)

        # Check specific section content
        self._check_scope(policy.get('scope'))
        self._check_responsibilities(policy.get('responsibilities'))
        self._check_data_handling(policy.get('data_handling'))
        self._check_incident_response(policy.get('incident_response'))
        self._check_monitoring(policy.get('monitoring'))

        return self.issues

    def _check_required_sections(self, policy: Dict[str, Any]):
        """Check for presence of required sections."""
        for section in self.REQUIRED_SECTIONS:
            if section not in policy or not policy[section]:
                self.issues.append(PolicyIssue(
                    severity='error',
                    section=section,
                    message=f"Required section '{section}' is missing or empty"
                ))

    def _check_recommended_sections(self, policy: Dict[str, Any]):
        """Check for presence of recommended sections."""
        for section in self.RECOMMENDED_SECTIONS:
            if section not in policy or not policy[section]:
                self.issues.append(PolicyIssue(
                    severity='warning',
                    section=section,
                    message=f"Recommended section '{section}' is missing"
                ))

    def _check_scope(self, scope: Optional[Dict[str, Any]]):
        """Check scope section."""
        if not scope:
            return

        # Check for key scope elements
        if 'system_description' not in scope:
            self.issues.append(PolicyIssue(
                severity='warning',
                section='scope',
                message="Missing 'system_description' in scope"
            ))

        if 'boundaries' not in scope:
            self.issues.append(PolicyIssue(
                severity='warning',
                section='scope',
                message="Missing 'boundaries' definition in scope"
            ))

    def _check_responsibilities(self, responsibilities: Optional[Dict[str, Any]]):
        """Check responsibilities section."""
        if not responsibilities:
            return

        # Check for key roles
        key_roles = ['system_owner', 'incident_responder', 'data_steward']
        for role in key_roles:
            if role not in responsibilities:
                self.issues.append(PolicyIssue(
                    severity='info',
                    section='responsibilities',
                    message=f"Consider defining '{role}' role"
                ))

    def _check_data_handling(self, data_handling: Optional[Dict[str, Any]]):
        """Check data handling section."""
        if not data_handling:
            return

        # Check for data handling elements
        if 'retention_policy' not in data_handling:
            self.issues.append(PolicyIssue(
                severity='warning',
                section='data_handling',
                message="Missing 'retention_policy'"
            ))

        if 'privacy_measures' not in data_handling:
            self.issues.append(PolicyIssue(
                severity='warning',
                section='data_handling',
                message="Missing 'privacy_measures'"
            ))

        if 'data_classification' not in data_handling:
            self.issues.append(PolicyIssue(
                severity='info',
                section='data_handling',
                message="Consider adding 'data_classification'"
            ))

    def _check_incident_response(self, incident_response: Optional[Dict[str, Any]]):
        """Check incident response section."""
        if not incident_response:
            return

        # Check for incident response elements
        if 'severity_levels' not in incident_response:
            self.issues.append(PolicyIssue(
                severity='warning',
                section='incident_response',
                message="Missing 'severity_levels' definition"
            ))

        if 'response_procedures' not in incident_response:
            self.issues.append(PolicyIssue(
                severity='error',
                section='incident_response',
                message="Missing 'response_procedures'"
            ))

        if 'escalation_path' not in incident_response:
            self.issues.append(PolicyIssue(
                severity='warning',
                section='incident_response',
                message="Missing 'escalation_path'"
            ))

    def _check_monitoring(self, monitoring: Optional[Dict[str, Any]]):
        """Check monitoring section."""
        if not monitoring:
            return

        # Check for monitoring elements
        if 'metrics' not in monitoring:
            self.issues.append(PolicyIssue(
                severity='warning',
                section='monitoring',
                message="Missing 'metrics' definition"
            ))

        if 'alerting' not in monitoring:
            self.issues.append(PolicyIssue(
                severity='info',
                section='monitoring',
                message="Consider defining 'alerting' mechanisms"
            ))

    def check_policy_file(self, filepath: str) -> List[PolicyIssue]:
        """
        Load and check policy from file.

        Args:
            filepath: Path to YAML or JSON file

        Returns:
            List of PolicyIssue objects
        """
        # Determine file type and load
        if filepath.endswith('.yaml') or filepath.endswith('.yml'):
            with open(filepath, 'r') as f:
                policy = yaml.safe_load(f)
        elif filepath.endswith('.json'):
            with open(filepath, 'r') as f:
                policy = json.load(f)
        else:
            raise ValueError("Policy file must be YAML or JSON")

        return self.check_policy(policy)

    def get_summary(self) -> Dict[str, Any]:
        """Get summary of policy check results."""
        errors = [i for i in self.issues if i.severity == 'error']
        warnings = [i for i in self.issues if i.severity == 'warning']
        infos = [i for i in self.issues if i.severity == 'info']

        return {
            'total_issues': len(self.issues),
            'errors': len(errors),
            'warnings': len(warnings),
            'info': len(infos),
            'passed': len(errors) == 0
        }

    def print_report(self):
        """Print human-readable policy check report."""
        if not self.issues:
            print("✅ Policy check passed - no issues found")
            return

        print(f"\n📋 Policy Check Report")
        print("=" * 60)

        errors = [i for i in self.issues if i.severity == 'error']
        warnings = [i for i in self.issues if i.severity == 'warning']
        infos = [i for i in self.issues if i.severity == 'info']

        if errors:
            print(f"\n❌ ERRORS ({len(errors)}):")
            for issue in errors:
                print(f"  - {issue.section}: {issue.message}")

        if warnings:
            print(f"\n⚠️  WARNINGS ({len(warnings)}):")
            for issue in warnings:
                print(f"  - {issue.section}: {issue.message}")

        if infos:
            print(f"\n💡 RECOMMENDATIONS ({len(infos)}):")
            for issue in infos:
                print(f"  - {issue.section}: {issue.message}")

        print("\n" + "=" * 60)
        summary = self.get_summary()
        print(f"Total Issues: {summary['total_issues']}")
        print(f"Status: {'❌ FAILED' if not summary['passed'] else '✅ PASSED (with warnings)'}")
        print()
