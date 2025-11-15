#!/usr/bin/env python3
# FEU Contract: Fact/Estimate/Unknown | Bound to Master Citation v15.2
# All outputs must distinguish epistemic status: Fact, Estimate, or Unknown
"""
TrustByDesign Package Setup
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="trustbydesign",
    version="0.2.0-hardening",
    author="N1 Intelligence (OPC) Private Limited",
    author_email="contact@n1intelligence.com",
    description="Safety and governance framework for reflective AI systems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MirrorDNA-Reflection-Protocol/TrustByDesign",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords=[
        "MirrorDNA",
        "Reflective AI",
        "ActiveMirrorOS",
        "LingOS",
        "AI Safety",
        "AI Governance",
        "Trust Framework",
        "Transparency",
        "AI Ethics",
        "Master Citation v15.2",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    include_package_data=True,
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "trustbydesign-validate=scripts.validate_safety:main",
            "trustbydesign-assess=scripts.assess_trust:main",
            "trustbydesign-governance=scripts.generate_governance:main",
            "trustbydesign-checklist=scripts.generate_compliance_checklist:main",
        ],
    },
)
