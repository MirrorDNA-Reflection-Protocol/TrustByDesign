"""
Tests for PolicyChecker module
"""

import pytest
import tempfile
import os
import yaml
import json
from lib.policy_checker import PolicyChecker, PolicyIssue


class TestPolicyIssue:
    """Test PolicyIssue dataclass"""

    def test_policy_issue_creation(self):
        """Test creating a policy issue"""
        issue = PolicyIssue(
            section="scope",
            severity="error",
            message="Missing required field"
        )

        assert issue.section == "scope"
        assert issue.severity == "error"
        assert issue.message == "Missing required field"


class TestPolicyChecker:
    """Test PolicyChecker class"""

    def test_checker_creation(self):
        """Test creating policy checker"""
        checker = PolicyChecker()
        assert checker is not None
        assert len(checker.issues) == 0

    def test_valid_minimal_policy(self):
        """Test checking a valid minimal policy"""
        policy = {
            'scope': {
                'system_name': 'Test System',
                'system_description': 'A test system',
                'boundaries': 'Can do X, cannot do Y'
            },
            'responsibilities': {
                'product_owner': 'Alice',
                'ml_lead': 'Bob',
                'security_lead': 'Charlie'
            },
            'data_handling': {
                'pii_protection': 'AES-256 encryption',
                'retention_policy': '90 days',
                'privacy_measures': 'Data minimization, encryption'
            },
            'incident_response': {
                'severity_levels': ['P0', 'P1', 'P2'],
                'response_time_p0': '15 minutes',
                'on_call_team': 'engineering@example.com',
                'response_procedures': 'Detect, contain, investigate, resolve',
                'escalation_path': 'On-call -> Manager -> VP'
            },
            'monitoring': {
                'dashboards': ['Operations', 'Quality'],
                'metrics': {
                    'accuracy': 0.9,
                    'latency': 200
                }
            },
            'escalation': {
                'triggers': ['User request', 'Low confidence'],
                'sla': '2 minutes'
            }
        }

        checker = PolicyChecker()
        issues = checker.check_policy(policy)

        # Should have no errors, only warnings for recommended sections
        errors = [i for i in issues if i.severity == 'error']
        assert len(errors) == 0

    def test_missing_required_section(self):
        """Test that missing required section raises error"""
        policy = {
            'scope': {
                'system_name': 'Test'
            }
            # Missing all other required sections
        }

        checker = PolicyChecker()
        issues = checker.check_policy(policy)

        errors = [i for i in issues if i.severity == 'error']
        # Should have errors for missing required sections
        assert len(errors) > 0

        error_sections = [i.section for i in errors]
        assert 'responsibilities' in error_sections
        assert 'data_handling' in error_sections

    def test_missing_recommended_section_warning(self):
        """Test that missing recommended section generates warning"""
        # Create minimal valid policy
        policy = {
            'scope': {
                'system_name': 'Test',
                'system_description': 'Test',
                'boundaries': 'Test'
            },
            'responsibilities': {
                'product_owner': 'Alice'
            },
            'data_handling': {
                'pii_protection': 'Yes',
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
            # Missing recommended sections like risk_assessment, uncertainty_handling
        }

        checker = PolicyChecker()
        issues = checker.check_policy(policy)

        warnings = [i for i in issues if i.severity == 'warning']
        warning_sections = [i.section for i in warnings]

        assert 'risk_assessment' in warning_sections
        assert 'uncertainty_handling' in warning_sections

    def test_scope_validation(self):
        """Test scope section validation"""
        # Missing system_description
        policy = {
            'scope': {
                'system_name': 'Test',
                'boundaries': 'Test'
            }
        }

        checker = PolicyChecker()
        issues = checker.check_policy(policy)

        warnings = [i for i in issues if i.severity == 'warning' and i.section == 'scope']
        messages = [i.message for i in warnings]

        assert any('system_description' in msg for msg in messages)

    def test_responsibilities_validation(self):
        """Test responsibilities section validation"""
        policy = {
            'responsibilities': {
                'product_owner': 'Alice'
                # Missing system_owner, incident_responder, data_steward
            }
        }

        checker = PolicyChecker()
        issues = checker.check_policy(policy)

        info = [i for i in issues if i.severity == 'info' and i.section == 'responsibilities']
        messages = [i.message for i in info]

        # Should suggest key roles
        assert any('system_owner' in msg for msg in messages)
        assert any('incident_responder' in msg for msg in messages)

    def test_data_handling_validation(self):
        """Test data handling section validation"""
        policy = {
            'data_handling': {
                'pii_protection': 'AES-256'
                # Missing retention_policy, privacy_measures
            }
        }

        checker = PolicyChecker()
        issues = checker.check_policy(policy)

        # Should have info/warning for missing fields
        data_issues = [i for i in issues if i.section == 'data_handling']
        assert len(data_issues) > 0

    def test_incident_response_validation(self):
        """Test incident response section validation"""
        # Missing critical field: response_procedures
        policy = {
            'incident_response': {
                'severity_levels': ['P0', 'P1'],
                'response_time_p0': '15 minutes',
                'on_call_team': 'team@example.com',
                'escalation_path': 'Standard'
                # Missing response_procedures
            }
        }

        checker = PolicyChecker()
        issues = checker.check_policy(policy)

        errors = [i for i in issues if i.severity == 'error' and i.section == 'incident_response']
        messages = [i.message for i in errors]

        assert any('response_procedures' in msg for msg in messages)

    def test_monitoring_validation(self):
        """Test monitoring section validation"""
        policy = {
            'monitoring': {
                'dashboards': ['Operations']
                # Missing metrics
            }
        }

        checker = PolicyChecker()
        issues = checker.check_policy(policy)

        warnings = [i for i in issues if i.severity == 'warning' and i.section == 'monitoring']
        messages = [i.message for i in warnings]

        assert any('metrics' in msg for msg in messages)

    def test_escalation_validation(self):
        """Test escalation section validation"""
        policy = {
            'escalation': {
                'sla': '2 minutes',
                'triggers': ['User request', 'Low confidence']
            }
        }

        checker = PolicyChecker()
        issues = checker.check_policy(policy)

        # Escalation section present should not cause errors
        # (PolicyChecker doesn't have specific field validation for escalation)
        escalation_errors = [i for i in issues if i.severity == 'error' and i.section == 'escalation']
        assert len(escalation_errors) == 0

    def test_get_summary(self):
        """Test getting issue summary"""
        policy = {
            'scope': {
                'system_name': 'Test'
            }
            # Minimal policy with many issues
        }

        checker = PolicyChecker()
        checker.check_policy(policy)

        summary = checker.get_summary()

        assert 'total_issues' in summary
        assert 'errors' in summary
        assert 'warnings' in summary
        assert 'info' in summary
        assert summary['total_issues'] > 0

    def test_check_policy_file_yaml(self):
        """Test checking policy from YAML file"""
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

        # Save to temp YAML file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            yaml.dump(policy, f)
            temp_path = f.name

        try:
            checker = PolicyChecker()
            issues = checker.check_policy_file(temp_path)

            assert isinstance(issues, list)
            # Should have some issues (warnings for recommended sections)
            assert len(issues) > 0

        finally:
            os.unlink(temp_path)

    def test_check_policy_file_json(self):
        """Test checking policy from JSON file"""
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

        # Save to temp JSON file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump(policy, f)
            temp_path = f.name

        try:
            checker = PolicyChecker()
            issues = checker.check_policy_file(temp_path)

            assert isinstance(issues, list)

        finally:
            os.unlink(temp_path)

    def test_empty_policy(self):
        """Test checking completely empty policy"""
        policy = {}

        checker = PolicyChecker()
        issues = checker.check_policy(policy)

        errors = [i for i in issues if i.severity == 'error']
        # Should have errors for all required sections
        assert len(errors) >= len(PolicyChecker.REQUIRED_SECTIONS)

    def test_comprehensive_policy(self):
        """Test checking a comprehensive policy with all sections"""
        policy = {
            'scope': {
                'system_name': 'Comprehensive System',
                'system_description': 'Fully documented',
                'boundaries': 'Clear boundaries'
            },
            'responsibilities': {
                'product_owner': 'Alice',
                'ml_lead': 'Bob',
                'security_lead': 'Charlie'
            },
            'data_handling': {
                'pii_protection': 'AES-256',
                'retention_policy': '90 days',
                'privacy_measures': 'Comprehensive'
            },
            'incident_response': {
                'severity_levels': ['P0', 'P1', 'P2'],
                'response_time_p0': '15 minutes',
                'on_call_team': 'team@example.com',
                'response_procedures': 'Detailed procedures',
                'escalation_path': 'Clear path'
            },
            'monitoring': {
                'dashboards': ['Operations', 'Quality', 'Security'],
                'metrics': {
                    'accuracy': 0.95,
                    'latency': 100,
                    'uptime': 0.999
                }
            },
            'escalation': {
                'triggers': ['User request', 'Low confidence', 'Error'],
                'sla': '2 minutes'
            },
            'risk_assessment': {
                'risk_registry': 'risks.yaml',
                'review_frequency': 'Monthly'
            },
            'uncertainty_handling': {
                'confidence_thresholds': {'high': 0.9, 'medium': 0.6},
                'explicit_markers': True
            },
            'audit_trail': {
                'logging': 'Comprehensive',
                'retention': '2 years'
            },
            'user_consent': {
                'required': True,
                'opt_out': True
            },
            'model_governance': {
                'change_process': 'Documented',
                'approval_required': True
            },
            'deployment_process': {
                'testing': 'Required',
                'rollback_plan': True
            }
        }

        checker = PolicyChecker()
        issues = checker.check_policy(policy)

        errors = [i for i in issues if i.severity == 'error']
        # Should have no errors
        assert len(errors) == 0

        # May still have some info messages
        summary = checker.get_summary()
        assert summary['errors'] == 0


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
