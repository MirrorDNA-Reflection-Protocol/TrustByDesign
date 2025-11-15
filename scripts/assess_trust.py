#!/usr/bin/env python3
# FEU Contract: Fact/Estimate/Unknown | Bound to Master Citation v15.2
# All outputs must distinguish epistemic status: Fact, Estimate, or Unknown
"""
TrustByDesign Trust Assessment Tool

Generates a comprehensive trust assessment for an AI system.
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict


class TrustAssessor:
    """Assesses trust dimensions of AI systems."""

    def __init__(self, system_name: str):
        self.system_name = system_name
        self.scores = {}
        self.notes = {}

    def assess(self) -> Dict:
        """Run interactive trust assessment."""
        print("\n" + "=" * 70)
        print("  TrustByDesign Trust Assessment")
        print("=" * 70)
        print(f"\nSystem: {self.system_name}")
        print(f"Date: {datetime.now().strftime('%Y-%m-%d')}")
        print("\nThis assessment evaluates six dimensions of trust.")
        print("For each dimension, answer the questions and provide a score (0-10).")
        print("=" * 70 + "\n")

        # Assess each dimension
        self._assess_identity_trust()
        self._assess_continuity_trust()
        self._assess_behavioral_trust()
        self._assess_governance_trust()
        self._assess_transparency_trust()
        self._assess_user_agency_trust()

        # Calculate overall score
        average_score = sum(self.scores.values()) / len(self.scores)
        trust_level = self._calculate_trust_level(average_score)

        # Generate report
        report = self._generate_report(average_score, trust_level)

        return report

    def _assess_identity_trust(self):
        """Assess identity trust dimension."""
        print("\n1️⃣  IDENTITY TRUST")
        print("-" * 70)
        print("Who/what is this agent? Can its identity be verified?")

        questions = {
            "Has clear identity": "Does the system have a clear, documented identity?",
            "Identity verifiable": "Can the identity be verified through MirrorDNA or similar?",
            "Constitutional compliance": "Does it comply with stated constitutional principles?"
        }

        self._ask_questions("identity_trust", questions)

    def _assess_continuity_trust(self):
        """Assess continuity trust dimension."""
        print("\n2️⃣  CONTINUITY TRUST")
        print("-" * 70)
        print("Does memory persist correctly? Is state consistent?")

        questions = {
            "Memory reliable": "Is memory storage and retrieval reliable?",
            "State consistent": "Is system state consistent across interactions?",
            "No corruption": "Is there evidence of memory corruption or drift?"
        }

        self._ask_questions("continuity_trust", questions)

    def _assess_behavioral_trust(self):
        """Assess behavioral trust dimension."""
        print("\n3️⃣  BEHAVIORAL TRUST")
        print("-" * 70)
        print("Does it act within declared bounds? Is behavior predictable?")

        questions = {
            "Respects boundaries": "Does it respect declared capability boundaries?",
            "Predictable behavior": "Is behavior consistent and predictable?",
            "No capability creep": "Are there undeclared capabilities being used?",
            "Safe failure modes": "Does it fail gracefully when limits exceeded?"
        }

        self._ask_questions("behavioral_trust", questions)

    def _assess_governance_trust(self):
        """Assess governance trust dimension."""
        print("\n4️⃣  GOVERNANCE TRUST")
        print("-" * 70)
        print("Can it be audited and verified? Is governance structure clear?")

        questions = {
            "Audit logs complete": "Are audit logs complete and accessible?",
            "Governance current": "Is governance declaration current and accurate?",
            "Self-governance works": "Does self-governance function as declared?",
            "External audit": "Has external audit been conducted (if applicable)?"
        }

        self._ask_questions("governance_trust", questions)

    def _assess_transparency_trust(self):
        """Assess transparency trust dimension."""
        print("\n5️⃣  TRANSPARENCY TRUST")
        print("-" * 70)
        print("Can users understand what it's doing and why?")

        questions = {
            "Explanations clear": "Are explanations clear and helpful?",
            "Confidence communicated": "Are confidence levels communicated?",
            "Sources cited": "Are sources cited for recalled information?",
            "Uncertainty acknowledged": "Is uncertainty acknowledged appropriately?"
        }

        self._ask_questions("transparency_trust", questions)

    def _assess_user_agency_trust(self):
        """Assess user agency trust dimension."""
        print("\n6️⃣  USER AGENCY TRUST")
        print("-" * 70)
        print("Do users have control over their data and the relationship?")

        questions = {
            "Consent respected": "Is user consent properly obtained and respected?",
            "Memory inspectable": "Can users inspect stored memories?",
            "Memory deletable": "Can users delete their data?",
            "Preferences honored": "Are user preferences consistently honored?"
        }

        self._ask_questions("user_agency_trust", questions)

    def _ask_questions(self, dimension: str, questions: Dict[str, str]):
        """Ask questions for a dimension and collect score."""
        for short, full in questions.items():
            answer = input(f"\n  ❓ {full} (y/n): ").strip().lower()
            print(f"     → {short}: {'✅ Yes' if answer == 'y' else '❌ No'}")

        while True:
            try:
                score_str = input(f"\n  📊 Score for this dimension (0-10): ").strip()
                score = float(score_str)
                if 0 <= score <= 10:
                    self.scores[dimension] = score
                    break
                else:
                    print("     Please enter a number between 0 and 10")
            except ValueError:
                print("     Please enter a valid number")

        notes = input(f"  📝 Notes (optional): ").strip()
        if notes:
            self.notes[dimension] = notes

    def _calculate_trust_level(self, score: float) -> str:
        """Calculate trust level from score."""
        if score >= 8.5:
            return "Excellent"
        elif score >= 6.5:
            return "High"
        elif score >= 4.0:
            return "Medium"
        else:
            return "Low"

    def _generate_report(self, average_score: float, trust_level: str) -> Dict:
        """Generate assessment report."""
        print("\n" + "=" * 70)
        print("  ASSESSMENT COMPLETE")
        print("=" * 70)

        print("\n📊 SCORES BY DIMENSION:")
        for dimension, score in self.scores.items():
            dim_name = dimension.replace('_', ' ').title()
            print(f"  {dim_name}: {score:.1f} / 10")

        print(f"\n⭐ OVERALL TRUST SCORE: {average_score:.1f} / 10")
        print(f"   Trust Level: {trust_level}")

        print("\n" + "=" * 70 + "\n")

        # Create report dictionary
        report = {
            "assessment": {
                "id": f"ASSESS-{datetime.now().strftime('%Y%m%d-%H%M%S')}",
                "date": datetime.now().strftime('%Y-%m-%d'),
                "assessor": {
                    "role": "manual"
                }
            },
            "system": {
                "name": self.system_name
            },
            "trust_dimensions": {
                dim: {"score": score, "notes": self.notes.get(dim, "")}
                for dim, score in self.scores.items()
            },
            "overall": {
                "average_score": round(average_score, 2),
                "trust_level": trust_level.lower()
            },
            "summary": f"Trust assessment completed for {self.system_name}. "
                      f"Overall trust score: {average_score:.1f}/10 ({trust_level}). "
                      f"See dimension scores for detailed breakdown."
        }

        return report


def main():
    parser = argparse.ArgumentParser(
        description='Generate trust assessment for AI system',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Interactive assessment
  python assess_trust.py --system "My AI Agent"

  # Save results
  python assess_trust.py --system "My Agent" --output assessment.json
        """
    )

    parser.add_argument(
        '--system',
        type=str,
        required=True,
        help='Name of system to assess'
    )

    parser.add_argument(
        '--output',
        type=str,
        help='Output file for assessment (JSON)'
    )

    args = parser.parse_args()

    # Run assessment
    assessor = TrustAssessor(args.system)
    report = assessor.assess()

    # Save if requested
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(report, f, indent=2)
        print(f"📄 Assessment saved to: {args.output}\n")
    else:
        # Print JSON to stdout
        print("\n📋 ASSESSMENT REPORT (JSON):")
        print(json.dumps(report, indent=2))
        print()


if __name__ == '__main__':
    main()
