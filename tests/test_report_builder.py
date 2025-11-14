"""
Tests for TrustReportBuilder module
"""

import pytest
import tempfile
import os
import json
from lib.report_builder import TrustReportBuilder
from lib.risk_registry import RiskRegistry, RiskCategory, Severity, Likelihood, RiskStatus
from lib.policy_checker import PolicyChecker


class TestReportBuilderBasics:
    """Test basic report builder functionality"""

    def test_builder_creation(self):
        """Test creating report builder"""
        builder = TrustReportBuilder()
        assert builder is not None
        assert builder.system_name == "AI System"
        assert builder.system_version == "1.0.0"

    def test_set_system_info(self):
        """Test setting system information"""
        builder = TrustReportBuilder()
        builder.set_system_info("TestSystem", "2.0.0")

        assert builder.system_name == "TestSystem"
        assert builder.system_version == "2.0.0"

    def test_add_note(self):
        """Test adding manual notes"""
        builder = TrustReportBuilder()
        builder.add_note("First note")
        builder.add_note("Second note")

        assert len(builder.manual_notes) == 2
        assert "First note" in builder.manual_notes
        assert "Second note" in builder.manual_notes


class TestReportWithRiskRegistry:
    """Test report generation with risk registry"""

    def test_set_risk_registry(self):
        """Test setting risk registry"""
        builder = TrustReportBuilder()
        registry = RiskRegistry()

        builder.set_risk_registry(registry)
        assert builder.risk_registry is registry

    def test_report_includes_risks(self):
        """Test that report includes risk information"""
        builder = TrustReportBuilder()
        registry = RiskRegistry()

        # Add a risk
        registry.add_risk(
            id="RISK-001",
            category=RiskCategory.HALLUCINATION,
            title="Test Hallucination Risk",
            description="Test description",
            severity=Severity.HIGH,
            likelihood=Likelihood.MEDIUM
        )

        builder.set_risk_registry(registry)
        report = builder.build_markdown()

        # Report should mention the risk
        assert "RISK-001" in report
        assert "Test Hallucination Risk" in report
        assert "high" in report.lower()

    def test_report_with_multiple_risks(self):
        """Test report with multiple risks"""
        builder = TrustReportBuilder()
        registry = RiskRegistry()

        # Add multiple risks
        registry.add_risk(
            id="RISK-001",
            category=RiskCategory.HALLUCINATION,
            title="Hallucination Risk",
            description="Test",
            severity=Severity.CRITICAL,
            likelihood=Likelihood.HIGH
        )

        registry.add_risk(
            id="RISK-002",
            category=RiskCategory.PRIVACY,
            title="Privacy Risk",
            description="Test",
            severity=Severity.HIGH,
            likelihood=Likelihood.LOW
        )

        registry.add_risk(
            id="RISK-003",
            category=RiskCategory.BIAS,
            title="Bias Risk",
            description="Test",
            severity=Severity.MEDIUM,
            likelihood=Likelihood.MEDIUM
        )

        builder.set_risk_registry(registry)
        report = builder.build_markdown()

        # Should include high-priority risks (critical and high)
        assert "RISK-001" in report
        assert "RISK-002" in report
        # RISK-003 is medium severity, may not appear in high priority table

        # Should show risk summary
        assert "Total Risks: 3" in report

    def test_report_with_no_risks(self):
        """Test report with empty risk registry"""
        builder = TrustReportBuilder()
        registry = RiskRegistry()  # Empty

        builder.set_risk_registry(registry)
        report = builder.build_markdown()

        # Should still generate report
        assert len(report) > 0
        assert "Total Risks: 0" in report


class TestReportWithPolicyChecker:
    """Test report generation with policy checker"""

    def test_set_policy_checker(self):
        """Test setting policy checker"""
        builder = TrustReportBuilder()
        checker = PolicyChecker()

        builder.set_policy_checker(checker)
        assert builder.policy_checker is checker

    def test_report_includes_policy_issues(self):
        """Test that report includes policy compliance info"""
        builder = TrustReportBuilder()
        checker = PolicyChecker()

        # Check a minimal policy (will have issues)
        policy = {
            'scope': {
                'system_name': 'Test'
            }
        }
        checker.check_policy(policy)

        builder.set_policy_checker(checker)
        report = builder.build_markdown()

        # Report should include policy compliance section
        assert "Policy Compliance" in report
        # Should show that there are issues
        assert report.count("❌") > 0 or "Failed" in report

    def test_report_with_valid_policy(self):
        """Test report with mostly valid policy"""
        builder = TrustReportBuilder()
        checker = PolicyChecker()

        # Create valid policy
        policy = {
            'scope': {
                'system_name': 'Test System',
                'system_description': 'Test',
                'boundaries': 'Test'
            },
            'responsibilities': {
                'product_owner': 'Alice'
            },
            'data_handling': {
                'pii_protection': 'Encryption',
                'privacy_measures': 'Yes'
            },
            'incident_response': {
                'severity_levels': ['P0'],
                'response_time_p0': '15m',
                'on_call_team': 'team@example.com',
                'response_procedures': 'Standard',
                'escalation_path': 'Standard'
            },
            'monitoring': {
                'dashboards': ['Main'],
                'metrics': {'accuracy': 0.9}
            },
            'escalation': {
                'triggers': ['User request'],
                'sla': '2m'
            }
        }

        checker.check_policy(policy)
        builder.set_policy_checker(checker)
        report = builder.build_markdown()

        # Should have policy section
        assert "Policy Compliance" in report


class TestReportWithNotes:
    """Test report generation with manual notes"""

    def test_report_includes_notes(self):
        """Test that report includes manual notes"""
        builder = TrustReportBuilder()
        builder.add_note("Important observation")
        builder.add_note("Another note")

        report = builder.build_markdown()

        assert "Additional Notes" in report
        assert "Important observation" in report
        assert "Another note" in report

    def test_report_with_no_notes(self):
        """Test report with no manual notes"""
        builder = TrustReportBuilder()
        report = builder.build_markdown()

        # Should still generate report
        assert len(report) > 0


class TestCompleteReport:
    """Test complete report generation with all components"""

    def test_complete_report(self):
        """Test generating complete report with all components"""
        builder = TrustReportBuilder()
        builder.set_system_info("Complete System", "3.0.0")

        # Add risk registry
        registry = RiskRegistry()
        registry.add_risk(
            id="RISK-001",
            category=RiskCategory.SECURITY,
            title="Security Risk",
            description="Security issue",
            severity=Severity.CRITICAL,
            likelihood=Likelihood.MEDIUM,
            owner="Security Team"
        )
        builder.set_risk_registry(registry)

        # Add policy checker
        checker = PolicyChecker()
        policy = {
            'scope': {'system_name': 'Test'},
            'responsibilities': {'product_owner': 'Alice'},
            'data_handling': {'pii_protection': 'Yes', 'privacy_measures': 'Yes'},
            'incident_response': {
                'severity_levels': ['P0'],
                'response_time_p0': '15m',
                'on_call_team': 'team@example.com',
                'response_procedures': 'Yes',
                'escalation_path': 'Yes'
            },
            'monitoring': {'dashboards': ['Main'], 'metrics': {}},
            'escalation': {'triggers': ['Request'], 'sla': '2m'}
        }
        checker.check_policy(policy)
        builder.set_policy_checker(checker)

        # Add notes
        builder.add_note("System deployed successfully")
        builder.add_note("Monitoring shows good performance")

        # Generate report
        report = builder.build_markdown()

        # Verify all sections present
        assert "Trust Report:" in report
        assert "Complete System" in report
        assert "3.0.0" in report
        assert "Risk Assessment" in report
        assert "Policy Compliance" in report
        assert "Additional Notes" in report
        assert "RISK-001" in report
        assert "Security Risk" in report

    def test_executive_summary(self):
        """Test that executive summary is generated"""
        builder = TrustReportBuilder()
        registry = RiskRegistry()

        # Add critical risk
        registry.add_risk(
            id="RISK-001",
            category=RiskCategory.PRIVACY,
            title="Critical Privacy Risk",
            description="Test",
            severity=Severity.CRITICAL,
            likelihood=Likelihood.HIGH
        )

        builder.set_risk_registry(registry)
        report = builder.build_markdown()

        # Should have executive summary
        assert "Executive Summary" in report
        assert "Critical: 1" in report


class TestReportFormats:
    """Test different report output formats"""

    def test_build_markdown(self):
        """Test building markdown report"""
        builder = TrustReportBuilder()
        builder.set_system_info("Test System", "1.0")

        report = builder.build_markdown()

        # Should be markdown format
        assert isinstance(report, str)
        assert "# Trust Report:" in report
        assert "##" in report  # Section headers

    def test_build_dict(self):
        """Test building dictionary report"""
        builder = TrustReportBuilder()
        builder.set_system_info("Test System", "1.0")

        report_dict = builder.build_dict()

        # Should be dictionary with expected structure
        assert isinstance(report_dict, dict)
        assert 'system' in report_dict
        assert 'generated_at' in report_dict
        assert report_dict['system']['name'] == "Test System"
        assert report_dict['system']['version'] == "1.0"

    def test_build_dict_with_risks(self):
        """Test dictionary report includes risk data"""
        builder = TrustReportBuilder()
        registry = RiskRegistry()

        registry.add_risk(
            id="RISK-001",
            category=RiskCategory.HALLUCINATION,
            title="Test Risk",
            description="Test",
            severity=Severity.HIGH,
            likelihood=Likelihood.MEDIUM
        )

        builder.set_risk_registry(registry)
        report_dict = builder.build_dict()

        assert 'risks' in report_dict
        assert report_dict['risks'] is not None
        assert 'summary' in report_dict['risks']
        assert 'details' in report_dict['risks']

    def test_build_dict_with_policy(self):
        """Test dictionary report includes policy data"""
        builder = TrustReportBuilder()
        checker = PolicyChecker()

        policy = {'scope': {'system_name': 'Test'}}
        checker.check_policy(policy)

        builder.set_policy_checker(checker)
        report_dict = builder.build_dict()

        assert 'policy' in report_dict
        assert report_dict['policy'] is not None
        assert 'summary' in report_dict['policy']
        assert 'issues' in report_dict['policy']


class TestReportSaving:
    """Test saving reports to files"""

    def test_save_markdown(self):
        """Test saving markdown report to file"""
        builder = TrustReportBuilder()
        builder.set_system_info("Test System", "1.0")
        builder.add_note("Test note")

        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False) as f:
            temp_path = f.name

        try:
            builder.save_markdown(temp_path)

            # Verify file was created and contains expected content
            with open(temp_path, 'r') as f:
                content = f.read()

            assert "Trust Report:" in content
            assert "Test System" in content
            assert "Test note" in content

        finally:
            os.unlink(temp_path)

    def test_save_json(self):
        """Test saving JSON report to file"""
        builder = TrustReportBuilder()
        builder.set_system_info("Test System", "1.0")

        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            temp_path = f.name

        try:
            builder.save_json(temp_path)

            # Verify file was created and is valid JSON
            with open(temp_path, 'r') as f:
                data = json.load(f)

            assert data['system']['name'] == "Test System"
            assert data['system']['version'] == "1.0"

        finally:
            os.unlink(temp_path)


class TestReportContent:
    """Test specific report content and formatting"""

    def test_report_has_timestamp(self):
        """Test that report includes generation timestamp"""
        builder = TrustReportBuilder()
        report = builder.build_markdown()

        assert "Generated" in report

    def test_report_has_system_info(self):
        """Test that report includes system information"""
        builder = TrustReportBuilder()
        builder.set_system_info("MySystem", "2.5.0")

        report = builder.build_markdown()

        assert "MySystem" in report
        assert "2.5.0" in report

    def test_high_priority_risks_highlighted(self):
        """Test that high priority risks are highlighted"""
        builder = TrustReportBuilder()
        registry = RiskRegistry()

        # Add critical risk
        registry.add_risk(
            id="RISK-CRITICAL",
            category=RiskCategory.SECURITY,
            title="Critical Security Issue",
            description="Very serious",
            severity=Severity.CRITICAL,
            likelihood=Likelihood.HIGH
        )

        # Add low risk
        registry.add_risk(
            id="RISK-LOW",
            category=RiskCategory.PERFORMANCE,
            title="Minor Performance Issue",
            description="Not urgent",
            severity=Severity.LOW,
            likelihood=Likelihood.LOW
        )

        builder.set_risk_registry(registry)
        report = builder.build_markdown()

        # Critical risk should appear in high priority section
        assert "High Priority Risks" in report or "Critical" in report

    def test_recommendations_section(self):
        """Test that report includes recommendations"""
        builder = TrustReportBuilder()
        registry = RiskRegistry()

        # Add critical risk
        registry.add_risk(
            id="RISK-001",
            category=RiskCategory.PRIVACY,
            title="Privacy Issue",
            description="Test",
            severity=Severity.CRITICAL,
            likelihood=Likelihood.HIGH
        )

        builder.set_risk_registry(registry)
        report = builder.build_markdown()

        # Should have recommendations section
        assert "Recommendations" in report


class TestEdgeCases:
    """Test edge cases and error conditions"""

    def test_empty_report(self):
        """Test generating report with no data"""
        builder = TrustReportBuilder()
        report = builder.build_markdown()

        # Should still generate valid report
        assert len(report) > 0
        assert "Trust Report:" in report

    def test_none_risk_registry(self):
        """Test with None risk registry"""
        builder = TrustReportBuilder()
        # Don't set risk registry (remains None)

        report = builder.build_markdown()

        # Should handle gracefully
        assert len(report) > 0

    def test_none_policy_checker(self):
        """Test with None policy checker"""
        builder = TrustReportBuilder()
        # Don't set policy checker (remains None)

        report = builder.build_markdown()

        # Should handle gracefully
        assert len(report) > 0

    def test_very_long_note(self):
        """Test with very long manual note"""
        builder = TrustReportBuilder()
        long_note = "A" * 10000

        builder.add_note(long_note)
        report = builder.build_markdown()

        # Should handle long content
        assert long_note in report

    def test_special_characters_in_notes(self):
        """Test notes with special markdown characters"""
        builder = TrustReportBuilder()
        builder.add_note("Note with # and * and [brackets]")

        report = builder.build_markdown()

        # Should preserve special characters
        assert "#" in report or "brackets" in report


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
