"""
Trust Report Builder Module

Generates comprehensive trust reports from risk registry, policy checks,
and additional manual notes.
"""

from typing import Dict, List, Any, Optional
from datetime import datetime
from .risk_registry import RiskRegistry
from .policy_checker import PolicyChecker


class TrustReportBuilder:
    """
    Builds comprehensive trust reports for AI systems.

    Combines:
    - Risk registry data
    - Policy compliance checks
    - Manual notes and observations
    - Summary statistics
    """

    def __init__(self):
        """Initialize report builder."""
        self.risk_registry: Optional[RiskRegistry] = None
        self.policy_checker: Optional[PolicyChecker] = None
        self.manual_notes: List[str] = []
        self.system_name: str = "AI System"
        self.system_version: str = "1.0.0"

    def set_risk_registry(self, registry: RiskRegistry):
        """Set risk registry for report."""
        self.risk_registry = registry

    def set_policy_checker(self, checker: PolicyChecker):
        """Set policy checker for report."""
        self.policy_checker = checker

    def add_note(self, note: str):
        """Add manual note to report."""
        self.manual_notes.append(note)

    def set_system_info(self, name: str, version: str = "1.0.0"):
        """Set system name and version."""
        self.system_name = name
        self.system_version = version

    def build_markdown(self) -> str:
        """
        Build trust report in Markdown format.

        Returns:
            Formatted markdown string
        """
        lines = []

        # Header
        lines.append(f"# Trust Report: {self.system_name}")
        lines.append(f"**Version**: {self.system_version}")
        lines.append(f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append("")
        lines.append("---")
        lines.append("")

        # Executive Summary
        lines.append("## Executive Summary")
        lines.append("")
        lines.extend(self._build_executive_summary())
        lines.append("")

        # Risk Assessment
        if self.risk_registry:
            lines.append("## Risk Assessment")
            lines.append("")
            lines.extend(self._build_risk_section())
            lines.append("")

        # Policy Compliance
        if self.policy_checker and self.policy_checker.issues:
            lines.append("## Policy Compliance")
            lines.append("")
            lines.extend(self._build_policy_section())
            lines.append("")

        # Manual Notes
        if self.manual_notes:
            lines.append("## Additional Notes")
            lines.append("")
            for note in self.manual_notes:
                lines.append(f"- {note}")
            lines.append("")

        # Recommendations
        lines.append("## Recommendations")
        lines.append("")
        lines.extend(self._build_recommendations())
        lines.append("")

        # Footer
        lines.append("---")
        lines.append("")
        lines.append("*This report was generated automatically by TrustByDesign toolkit.*")

        return "\n".join(lines)

    def _build_executive_summary(self) -> List[str]:
        """Build executive summary section."""
        lines = []

        # Risk summary
        if self.risk_registry:
            risk_summary = self.risk_registry.get_summary()
            total_risks = risk_summary['total']
            critical_risks = risk_summary['by_severity'].get('critical', 0)
            high_risks = risk_summary['by_severity'].get('high', 0)

            lines.append(f"**Total Risks Identified**: {total_risks}")
            lines.append(f"- Critical: {critical_risks}")
            lines.append(f"- High: {high_risks}")
            lines.append("")

        # Policy summary
        if self.policy_checker and self.policy_checker.issues:
            policy_summary = self.policy_checker.get_summary()
            lines.append(f"**Policy Compliance**: {'✅ Passed' if policy_summary['passed'] else '❌ Failed'}")
            lines.append(f"- Errors: {policy_summary['errors']}")
            lines.append(f"- Warnings: {policy_summary['warnings']}")
            lines.append("")

        return lines

    def _build_risk_section(self) -> List[str]:
        """Build risk assessment section."""
        lines = []

        if not self.risk_registry:
            return lines

        risk_summary = self.risk_registry.get_summary()

        # Summary statistics
        lines.append("### Risk Summary")
        lines.append("")
        lines.append(f"Total Risks: {risk_summary['total']}")
        lines.append("")

        # By severity
        lines.append("**By Severity:**")
        for severity, count in risk_summary['by_severity'].items():
            lines.append(f"- {severity.title()}: {count}")
        lines.append("")

        # By category
        lines.append("**By Category:**")
        for category, count in risk_summary['by_category'].items():
            lines.append(f"- {category.replace('_', ' ').title()}: {count}")
        lines.append("")

        # Top risks (critical and high)
        critical_risks = self.risk_registry.list_risks(severity=None)
        high_priority = [r for r in critical_risks if r.severity.value in ['critical', 'high']]

        if high_priority:
            lines.append("### High Priority Risks")
            lines.append("")
            lines.append("| ID | Title | Severity | Status | Owner |")
            lines.append("|---|---|---|---|---|")

            for risk in sorted(high_priority, key=lambda r: (r.severity.value, r.id)):
                lines.append(
                    f"| {risk.id} | {risk.title} | {risk.severity.value} | "
                    f"{risk.status.value} | {risk.owner or 'Unassigned'} |"
                )
            lines.append("")

        return lines

    def _build_policy_section(self) -> List[str]:
        """Build policy compliance section."""
        lines = []

        if not self.policy_checker or not self.policy_checker.issues:
            lines.append("✅ No policy compliance issues found.")
            return lines

        summary = self.policy_checker.get_summary()

        lines.append(f"**Status**: {'❌ Failed' if not summary['passed'] else '⚠️  Passed with warnings'}")
        lines.append("")

        # Errors
        errors = [i for i in self.policy_checker.issues if i.severity == 'error']
        if errors:
            lines.append("### Errors")
            lines.append("")
            for issue in errors:
                lines.append(f"- **{issue.section}**: {issue.message}")
            lines.append("")

        # Warnings
        warnings = [i for i in self.policy_checker.issues if i.severity == 'warning']
        if warnings:
            lines.append("### Warnings")
            lines.append("")
            for issue in warnings:
                lines.append(f"- **{issue.section}**: {issue.message}")
            lines.append("")

        return lines

    def _build_recommendations(self) -> List[str]:
        """Build recommendations section."""
        lines = []

        recommendations = []

        # Risk-based recommendations
        if self.risk_registry:
            risk_summary = self.risk_registry.get_summary()

            critical_count = risk_summary['by_severity'].get('critical', 0)
            if critical_count > 0:
                recommendations.append(
                    f"🔴 **URGENT**: Address {critical_count} critical risk(s) before deployment"
                )

            identified_risks = [
                r for r in self.risk_registry.risks.values()
                if r.status.value == 'identified'
            ]
            if identified_risks:
                recommendations.append(
                    f"⚠️  Move {len(identified_risks)} identified risk(s) to active mitigation"
                )

        # Policy-based recommendations
        if self.policy_checker and self.policy_checker.issues:
            summary = self.policy_checker.get_summary()

            if summary['errors'] > 0:
                recommendations.append(
                    f"❌ Fix {summary['errors']} policy error(s) before proceeding"
                )

            if summary['warnings'] > 5:
                recommendations.append(
                    "⚠️  High number of policy warnings - consider comprehensive policy review"
                )

        # General recommendations
        if not recommendations:
            recommendations.append("✅ No urgent recommendations at this time")
            recommendations.append("💡 Continue monitoring and regular risk reviews")

        for rec in recommendations:
            lines.append(f"- {rec}")

        return lines

    def build_dict(self) -> Dict[str, Any]:
        """
        Build trust report as dictionary for JSON export.

        Returns:
            Report data as dict
        """
        report = {
            'system': {
                'name': self.system_name,
                'version': self.system_version
            },
            'generated_at': datetime.now().isoformat(),
            'risks': None,
            'policy': None,
            'notes': self.manual_notes
        }

        # Add risk data
        if self.risk_registry:
            report['risks'] = {
                'summary': self.risk_registry.get_summary(),
                'details': self.risk_registry.export_risks_to_dict()
            }

        # Add policy data
        if self.policy_checker and self.policy_checker.issues:
            report['policy'] = {
                'summary': self.policy_checker.get_summary(),
                'issues': [issue.to_dict() for issue in self.policy_checker.issues]
            }

        return report

    def save_markdown(self, filepath: str):
        """Save trust report as Markdown file."""
        with open(filepath, 'w') as f:
            f.write(self.build_markdown())

    def save_json(self, filepath: str):
        """Save trust report as JSON file."""
        import json
        with open(filepath, 'w') as f:
            json.dump(self.build_dict(), f, indent=2)
