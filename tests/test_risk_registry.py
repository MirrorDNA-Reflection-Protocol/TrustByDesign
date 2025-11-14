"""
Tests for RiskRegistry module
"""

import pytest
import tempfile
import os
from toolkit.risk_registry import (
    RiskRegistry,
    Risk,
    RiskCategory,
    Severity,
    Likelihood,
    RiskStatus
)


class TestRisk:
    """Test Risk dataclass"""

    def test_risk_creation(self):
        """Test creating a risk"""
        risk = Risk(
            id="RISK-001",
            category=RiskCategory.HALLUCINATION,
            title="Test Risk",
            description="Test description",
            severity=Severity.HIGH,
            likelihood=Likelihood.MEDIUM,
            mitigations=["Mitigation 1"],
            owner="Test Owner",
            status=RiskStatus.IDENTIFIED
        )

        assert risk.id == "RISK-001"
        assert risk.category == RiskCategory.HALLUCINATION
        assert risk.title == "Test Risk"
        assert risk.severity == Severity.HIGH
        assert risk.likelihood == Likelihood.MEDIUM
        assert len(risk.mitigations) == 1
        assert risk.owner == "Test Owner"
        assert risk.status == RiskStatus.IDENTIFIED

    def test_risk_to_dict(self):
        """Test converting risk to dictionary"""
        risk = Risk(
            id="RISK-001",
            category=RiskCategory.PRIVACY,
            title="Test Risk",
            description="Test description",
            severity=Severity.CRITICAL,
            likelihood=Likelihood.LOW
        )

        risk_dict = risk.to_dict()

        assert risk_dict['id'] == "RISK-001"
        assert risk_dict['category'] == "privacy"
        assert risk_dict['severity'] == "critical"
        assert risk_dict['likelihood'] == "low"
        assert risk_dict['status'] == "identified"

    def test_risk_from_dict(self):
        """Test creating risk from dictionary"""
        data = {
            'id': 'RISK-002',
            'category': 'bias',
            'title': 'Bias Risk',
            'description': 'Test bias',
            'severity': 'medium',
            'likelihood': 'high',
            'mitigations': ['Fix bias'],
            'owner': 'ML Team',
            'status': 'mitigating'
        }

        risk = Risk.from_dict(data)

        assert risk.id == 'RISK-002'
        assert risk.category == RiskCategory.BIAS
        assert risk.severity == Severity.MEDIUM
        assert risk.likelihood == Likelihood.HIGH
        assert risk.status == RiskStatus.MITIGATING


class TestRiskRegistry:
    """Test RiskRegistry class"""

    def test_registry_creation(self):
        """Test creating empty registry"""
        registry = RiskRegistry()
        assert len(registry.risks) == 0

    def test_add_risk(self):
        """Test adding risk to registry"""
        registry = RiskRegistry()

        risk = registry.add_risk(
            id="RISK-001",
            category=RiskCategory.HALLUCINATION,
            title="Test Risk",
            description="Test description",
            severity=Severity.HIGH,
            likelihood=Likelihood.MEDIUM
        )

        assert risk.id == "RISK-001"
        assert len(registry.risks) == 1
        assert "RISK-001" in registry.risks

    def test_add_duplicate_risk_raises_error(self):
        """Test that adding duplicate risk ID raises error"""
        registry = RiskRegistry()

        registry.add_risk(
            id="RISK-001",
            category=RiskCategory.HALLUCINATION,
            title="First Risk",
            description="First",
            severity=Severity.HIGH,
            likelihood=Likelihood.MEDIUM
        )

        with pytest.raises(ValueError, match="already exists"):
            registry.add_risk(
                id="RISK-001",
                category=RiskCategory.PRIVACY,
                title="Second Risk",
                description="Second",
                severity=Severity.LOW,
                likelihood=Likelihood.LOW
            )

    def test_get_risk(self):
        """Test retrieving risk by ID"""
        registry = RiskRegistry()

        registry.add_risk(
            id="RISK-001",
            category=RiskCategory.SECURITY,
            title="Security Risk",
            description="Test",
            severity=Severity.CRITICAL,
            likelihood=Likelihood.LOW
        )

        risk = registry.get_risk("RISK-001")
        assert risk is not None
        assert risk.title == "Security Risk"

        missing = registry.get_risk("RISK-999")
        assert missing is None

    def test_update_risk(self):
        """Test updating existing risk"""
        registry = RiskRegistry()

        registry.add_risk(
            id="RISK-001",
            category=RiskCategory.PERFORMANCE,
            title="Original Title",
            description="Original",
            severity=Severity.LOW,
            likelihood=Likelihood.HIGH
        )

        updated = registry.update_risk(
            id="RISK-001",
            title="Updated Title",
            severity=Severity.CRITICAL
        )

        assert updated.title == "Updated Title"
        assert updated.severity == Severity.CRITICAL
        assert updated.likelihood == Likelihood.HIGH  # unchanged

    def test_update_nonexistent_risk_raises_error(self):
        """Test that updating nonexistent risk raises error"""
        registry = RiskRegistry()

        with pytest.raises(KeyError, match="not found"):
            registry.update_risk(id="RISK-999", title="New Title")

    def test_list_risks_all(self):
        """Test listing all risks"""
        registry = RiskRegistry()

        registry.add_risk(
            id="RISK-001",
            category=RiskCategory.HALLUCINATION,
            title="Risk 1",
            description="Test",
            severity=Severity.HIGH,
            likelihood=Likelihood.MEDIUM
        )

        registry.add_risk(
            id="RISK-002",
            category=RiskCategory.PRIVACY,
            title="Risk 2",
            description="Test",
            severity=Severity.CRITICAL,
            likelihood=Likelihood.LOW
        )

        all_risks = registry.list_risks()
        assert len(all_risks) == 2

    def test_list_risks_by_category(self):
        """Test filtering risks by category"""
        registry = RiskRegistry()

        registry.add_risk(
            id="RISK-001",
            category=RiskCategory.HALLUCINATION,
            title="Hallucination Risk",
            description="Test",
            severity=Severity.HIGH,
            likelihood=Likelihood.MEDIUM
        )

        registry.add_risk(
            id="RISK-002",
            category=RiskCategory.PRIVACY,
            title="Privacy Risk",
            description="Test",
            severity=Severity.CRITICAL,
            likelihood=Likelihood.LOW
        )

        hallucination_risks = registry.list_risks(category=RiskCategory.HALLUCINATION)
        assert len(hallucination_risks) == 1
        assert hallucination_risks[0].title == "Hallucination Risk"

    def test_list_risks_by_severity(self):
        """Test filtering risks by severity"""
        registry = RiskRegistry()

        registry.add_risk(
            id="RISK-001",
            category=RiskCategory.SECURITY,
            title="Critical Risk",
            description="Test",
            severity=Severity.CRITICAL,
            likelihood=Likelihood.MEDIUM
        )

        registry.add_risk(
            id="RISK-002",
            category=RiskCategory.PERFORMANCE,
            title="Low Risk",
            description="Test",
            severity=Severity.LOW,
            likelihood=Likelihood.HIGH
        )

        critical_risks = registry.list_risks(severity=Severity.CRITICAL)
        assert len(critical_risks) == 1
        assert critical_risks[0].title == "Critical Risk"

    def test_list_risks_by_status(self):
        """Test filtering risks by status"""
        registry = RiskRegistry()

        registry.add_risk(
            id="RISK-001",
            category=RiskCategory.BIAS,
            title="Mitigating Risk",
            description="Test",
            severity=Severity.HIGH,
            likelihood=Likelihood.MEDIUM,
            status=RiskStatus.MITIGATING
        )

        registry.add_risk(
            id="RISK-002",
            category=RiskCategory.COMPLIANCE,
            title="Monitoring Risk",
            description="Test",
            severity=Severity.MEDIUM,
            likelihood=Likelihood.LOW,
            status=RiskStatus.MONITORING
        )

        mitigating_risks = registry.list_risks(status=RiskStatus.MITIGATING)
        assert len(mitigating_risks) == 1
        assert mitigating_risks[0].title == "Mitigating Risk"

    def test_list_risks_by_owner(self):
        """Test filtering risks by owner"""
        registry = RiskRegistry()

        registry.add_risk(
            id="RISK-001",
            category=RiskCategory.SECURITY,
            title="Security Team Risk",
            description="Test",
            severity=Severity.HIGH,
            likelihood=Likelihood.MEDIUM,
            owner="Security Team"
        )

        registry.add_risk(
            id="RISK-002",
            category=RiskCategory.HALLUCINATION,
            title="ML Team Risk",
            description="Test",
            severity=Severity.MEDIUM,
            likelihood=Likelihood.HIGH,
            owner="ML Team"
        )

        security_risks = registry.list_risks(owner="Security Team")
        assert len(security_risks) == 1
        assert security_risks[0].title == "Security Team Risk"

    def test_list_risks_multiple_filters(self):
        """Test filtering with multiple criteria"""
        registry = RiskRegistry()

        registry.add_risk(
            id="RISK-001",
            category=RiskCategory.PRIVACY,
            title="High Privacy Risk",
            description="Test",
            severity=Severity.HIGH,
            likelihood=Likelihood.MEDIUM,
            owner="Security Team",
            status=RiskStatus.MITIGATING
        )

        registry.add_risk(
            id="RISK-002",
            category=RiskCategory.PRIVACY,
            title="Low Privacy Risk",
            description="Test",
            severity=Severity.LOW,
            likelihood=Likelihood.LOW,
            owner="Security Team",
            status=RiskStatus.MONITORING
        )

        filtered = registry.list_risks(
            category=RiskCategory.PRIVACY,
            severity=Severity.HIGH,
            owner="Security Team"
        )

        assert len(filtered) == 1
        assert filtered[0].title == "High Privacy Risk"

    def test_get_summary(self):
        """Test getting summary statistics"""
        registry = RiskRegistry()

        registry.add_risk(
            id="RISK-001",
            category=RiskCategory.HALLUCINATION,
            title="Risk 1",
            description="Test",
            severity=Severity.CRITICAL,
            likelihood=Likelihood.HIGH,
            status=RiskStatus.IDENTIFIED
        )

        registry.add_risk(
            id="RISK-002",
            category=RiskCategory.HALLUCINATION,
            title="Risk 2",
            description="Test",
            severity=Severity.HIGH,
            likelihood=Likelihood.MEDIUM,
            status=RiskStatus.MITIGATING
        )

        registry.add_risk(
            id="RISK-003",
            category=RiskCategory.PRIVACY,
            title="Risk 3",
            description="Test",
            severity=Severity.MEDIUM,
            likelihood=Likelihood.LOW,
            status=RiskStatus.MONITORING
        )

        summary = registry.get_summary()

        assert summary['total'] == 3
        assert summary['by_severity']['critical'] == 1
        assert summary['by_severity']['high'] == 1
        assert summary['by_severity']['medium'] == 1
        assert summary['by_category']['hallucination'] == 2
        assert summary['by_category']['privacy'] == 1
        assert summary['by_status']['identified'] == 1
        assert summary['by_status']['mitigating'] == 1
        assert summary['by_status']['monitoring'] == 1

    def test_export_to_dict(self):
        """Test exporting risks to dictionary"""
        registry = RiskRegistry()

        registry.add_risk(
            id="RISK-001",
            category=RiskCategory.SECURITY,
            title="Security Risk",
            description="Test",
            severity=Severity.HIGH,
            likelihood=Likelihood.MEDIUM
        )

        exported = registry.export_risks_to_dict()

        assert len(exported) == 1
        assert exported[0]['id'] == "RISK-001"
        assert exported[0]['category'] == "security"
        assert exported[0]['severity'] == "high"

    def test_save_and_load_yaml(self):
        """Test saving and loading from YAML"""
        registry = RiskRegistry()

        registry.add_risk(
            id="RISK-001",
            category=RiskCategory.BIAS,
            title="Bias Risk",
            description="Test bias",
            severity=Severity.HIGH,
            likelihood=Likelihood.MEDIUM,
            mitigations=["Mitigation 1", "Mitigation 2"],
            owner="ML Team",
            status=RiskStatus.MITIGATING
        )

        # Save to temporary file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            temp_path = f.name

        try:
            registry.to_yaml(temp_path)

            # Load into new registry
            new_registry = RiskRegistry()
            new_registry.load_from_yaml(temp_path)

            assert len(new_registry.risks) == 1
            risk = new_registry.get_risk("RISK-001")
            assert risk is not None
            assert risk.title == "Bias Risk"
            assert risk.category == RiskCategory.BIAS
            assert risk.severity == Severity.HIGH
            assert len(risk.mitigations) == 2
            assert risk.owner == "ML Team"

        finally:
            os.unlink(temp_path)

    def test_save_and_load_json(self):
        """Test saving and loading from JSON"""
        registry = RiskRegistry()

        registry.add_risk(
            id="RISK-001",
            category=RiskCategory.PERFORMANCE,
            title="Performance Risk",
            description="Test performance",
            severity=Severity.MEDIUM,
            likelihood=Likelihood.HIGH,
            owner="Engineering Team"
        )

        # Save to temporary file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            temp_path = f.name

        try:
            registry.to_json(temp_path)

            # Load into new registry
            new_registry = RiskRegistry()
            new_registry.load_from_json(temp_path)

            assert len(new_registry.risks) == 1
            risk = new_registry.get_risk("RISK-001")
            assert risk is not None
            assert risk.title == "Performance Risk"
            assert risk.category == RiskCategory.PERFORMANCE

        finally:
            os.unlink(temp_path)

    def test_metadata_handling(self):
        """Test that metadata is properly stored and retrieved"""
        registry = RiskRegistry()

        metadata = {
            'detected_date': '2025-01-01',
            'impact_score': 8.5,
            'related_incidents': ['INC-001', 'INC-002']
        }

        registry.add_risk(
            id="RISK-001",
            category=RiskCategory.SECURITY,
            title="Security Risk",
            description="Test",
            severity=Severity.HIGH,
            likelihood=Likelihood.MEDIUM,
            metadata=metadata
        )

        risk = registry.get_risk("RISK-001")
        assert risk.metadata['detected_date'] == '2025-01-01'
        assert risk.metadata['impact_score'] == 8.5
        assert len(risk.metadata['related_incidents']) == 2


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
