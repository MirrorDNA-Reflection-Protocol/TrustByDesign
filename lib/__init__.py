# FEU Contract: Fact/Estimate/Unknown | Bound to Master Citation v15.2
# All outputs must distinguish epistemic status: Fact, Estimate, or Unknown
"""
TrustByDesign Toolkit

A practical toolkit for building trustworthy AI systems with transparency,
accountability, and explicit uncertainty handling.

Modules:
- risk_registry: Track and manage AI system risks
- policy_checker: Validate trust policies against requirements
- uncertainty_tags: Tag content with uncertainty markers
- report_builder: Generate trust reports
"""

__version__ = "0.2.0-hardening"

from .risk_registry import RiskRegistry, Risk
from .policy_checker import PolicyChecker
from .uncertainty_tags import tag_fact, tag_estimate, tag_unknown, detect_tags
from .report_builder import TrustReportBuilder

__all__ = [
    'RiskRegistry',
    'Risk',
    'PolicyChecker',
    'tag_fact',
    'tag_estimate',
    'tag_unknown',
    'detect_tags',
    'TrustReportBuilder',
]
