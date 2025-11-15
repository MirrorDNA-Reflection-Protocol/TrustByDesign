# FEU Contract: Fact/Estimate/Unknown | Bound to Master Citation v15.2
# All outputs must distinguish epistemic status: Fact, Estimate, or Unknown
"""
Risk Registry Module

Manages AI system risks with tracking of severity, likelihood, mitigations, and status.
"""

from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional, Any
from enum import Enum
import yaml
import json


class RiskCategory(Enum):
    """Risk categories for AI systems."""
    HALLUCINATION = "hallucination"
    PRIVACY = "privacy"
    BIAS = "bias"
    AUTONOMY_OVERREACH = "autonomy_overreach"
    MISUSE = "misuse"
    DATA_QUALITY = "data_quality"
    SECURITY = "security"
    PERFORMANCE = "performance"
    COMPLIANCE = "compliance"
    OTHER = "other"


class Severity(Enum):
    """Risk severity levels."""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class Likelihood(Enum):
    """Risk likelihood levels."""
    VERY_HIGH = "very_high"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    VERY_LOW = "very_low"


class RiskStatus(Enum):
    """Risk status tracking."""
    IDENTIFIED = "identified"
    ANALYZING = "analyzing"
    MITIGATING = "mitigating"
    MONITORING = "monitoring"
    CLOSED = "closed"
    ACCEPTED = "accepted"


@dataclass
class Risk:
    """
    Represents a single risk in the AI system.

    Attributes:
        id: Unique risk identifier
        category: Risk category (hallucination, privacy, etc.)
        title: Short risk description
        description: Detailed risk description
        severity: Impact severity (critical, high, medium, low)
        likelihood: Probability of occurrence
        mitigations: List of mitigation measures
        owner: Person/team responsible
        status: Current risk status
        metadata: Additional custom fields
    """
    id: str
    category: RiskCategory
    title: str
    description: str
    severity: Severity
    likelihood: Likelihood
    mitigations: List[str] = field(default_factory=list)
    owner: str = ""
    status: RiskStatus = RiskStatus.IDENTIFIED
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """Convert risk to dictionary."""
        return {
            'id': self.id,
            'category': self.category.value,
            'title': self.title,
            'description': self.description,
            'severity': self.severity.value,
            'likelihood': self.likelihood.value,
            'mitigations': self.mitigations,
            'owner': self.owner,
            'status': self.status.value,
            'metadata': self.metadata
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Risk':
        """Create risk from dictionary."""
        return cls(
            id=data['id'],
            category=RiskCategory(data['category']),
            title=data['title'],
            description=data['description'],
            severity=Severity(data['severity']),
            likelihood=Likelihood(data['likelihood']),
            mitigations=data.get('mitigations', []),
            owner=data.get('owner', ''),
            status=RiskStatus(data.get('status', 'identified')),
            metadata=data.get('metadata', {})
        )


class RiskRegistry:
    """
    Registry for tracking AI system risks.

    Provides methods to add, update, filter, and export risks.
    """

    def __init__(self):
        """Initialize empty risk registry."""
        self.risks: Dict[str, Risk] = {}

    def add_risk(
        self,
        id: str,
        category: RiskCategory,
        title: str,
        description: str,
        severity: Severity,
        likelihood: Likelihood,
        mitigations: Optional[List[str]] = None,
        owner: str = "",
        status: RiskStatus = RiskStatus.IDENTIFIED,
        metadata: Optional[Dict[str, Any]] = None
    ) -> Risk:
        """
        Add a new risk to the registry.

        Args:
            id: Unique risk identifier
            category: Risk category
            title: Short description
            description: Detailed description
            severity: Impact severity
            likelihood: Probability of occurrence
            mitigations: List of mitigation measures
            owner: Responsible person/team
            status: Current status
            metadata: Additional custom fields

        Returns:
            The created Risk object

        Raises:
            ValueError: If risk ID already exists
        """
        if id in self.risks:
            raise ValueError(f"Risk with ID '{id}' already exists")

        risk = Risk(
            id=id,
            category=category,
            title=title,
            description=description,
            severity=severity,
            likelihood=likelihood,
            mitigations=mitigations or [],
            owner=owner,
            status=status,
            metadata=metadata or {}
        )

        self.risks[id] = risk
        return risk

    def update_risk(
        self,
        id: str,
        **kwargs
    ) -> Risk:
        """
        Update an existing risk.

        Args:
            id: Risk identifier
            **kwargs: Fields to update (category, title, description, etc.)

        Returns:
            Updated Risk object

        Raises:
            KeyError: If risk ID not found
        """
        if id not in self.risks:
            raise KeyError(f"Risk with ID '{id}' not found")

        risk = self.risks[id]

        # Update fields
        for key, value in kwargs.items():
            if hasattr(risk, key):
                # Convert string enum values to enums
                if key == 'category' and isinstance(value, str):
                    value = RiskCategory(value)
                elif key == 'severity' and isinstance(value, str):
                    value = Severity(value)
                elif key == 'likelihood' and isinstance(value, str):
                    value = Likelihood(value)
                elif key == 'status' and isinstance(value, str):
                    value = RiskStatus(value)

                setattr(risk, key, value)

        return risk

    def get_risk(self, id: str) -> Optional[Risk]:
        """Get risk by ID."""
        return self.risks.get(id)

    def list_risks(
        self,
        category: Optional[RiskCategory] = None,
        severity: Optional[Severity] = None,
        status: Optional[RiskStatus] = None,
        owner: Optional[str] = None
    ) -> List[Risk]:
        """
        List risks with optional filtering.

        Args:
            category: Filter by category
            severity: Filter by severity
            status: Filter by status
            owner: Filter by owner

        Returns:
            List of matching risks
        """
        results = list(self.risks.values())

        if category:
            results = [r for r in results if r.category == category]
        if severity:
            results = [r for r in results if r.severity == severity]
        if status:
            results = [r for r in results if r.status == status]
        if owner:
            results = [r for r in results if r.owner == owner]

        return results

    def export_risks_to_dict(self) -> List[Dict[str, Any]]:
        """Export all risks as list of dictionaries."""
        return [risk.to_dict() for risk in self.risks.values()]

    def to_yaml(self, filepath: str):
        """Export risks to YAML file."""
        data = {'risks': self.export_risks_to_dict()}
        with open(filepath, 'w') as f:
            yaml.dump(data, f, default_flow_style=False, sort_keys=False)

    def to_json(self, filepath: str):
        """Export risks to JSON file."""
        data = {'risks': self.export_risks_to_dict()}
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)

    def load_from_yaml(self, filepath: str):
        """Load risks from YAML file."""
        with open(filepath, 'r') as f:
            data = yaml.safe_load(f)

        for risk_data in data.get('risks', []):
            risk = Risk.from_dict(risk_data)
            self.risks[risk.id] = risk

    def load_from_json(self, filepath: str):
        """Load risks from JSON file."""
        with open(filepath, 'r') as f:
            data = json.load(f)

        for risk_data in data.get('risks', []):
            risk = Risk.from_dict(risk_data)
            self.risks[risk.id] = risk

    def get_summary(self) -> Dict[str, Any]:
        """Get summary statistics of risks."""
        total = len(self.risks)

        by_severity = {}
        by_status = {}
        by_category = {}

        for risk in self.risks.values():
            # Count by severity
            sev = risk.severity.value
            by_severity[sev] = by_severity.get(sev, 0) + 1

            # Count by status
            stat = risk.status.value
            by_status[stat] = by_status.get(stat, 0) + 1

            # Count by category
            cat = risk.category.value
            by_category[cat] = by_category.get(cat, 0) + 1

        return {
            'total': total,
            'by_severity': by_severity,
            'by_status': by_status,
            'by_category': by_category
        }
