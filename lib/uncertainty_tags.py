"""
Uncertainty Tags Module

Helper functions for tagging content with explicit uncertainty markers.
Aligns with reflective AI patterns for transparency and honesty.
"""

import re
from typing import List, Dict, Tuple


# Standard uncertainty tags
TAG_FACT = "[FACT]"
TAG_ESTIMATE = "[ESTIMATE]"
TAG_UNKNOWN = "[UNKNOWN]"
TAG_ASSUMPTION = "[ASSUMPTION]"
TAG_SPECULATION = "[SPECULATION]"

# All recognized tags
ALL_TAGS = [TAG_FACT, TAG_ESTIMATE, TAG_UNKNOWN, TAG_ASSUMPTION, TAG_SPECULATION]


def tag_fact(text: str) -> str:
    """
    Tag text as factual/verified information.

    Args:
        text: Content to tag

    Returns:
        Tagged string

    Example:
        >>> tag_fact("The system was deployed on 2024-01-15")
        '[FACT] The system was deployed on 2024-01-15'
    """
    return f"{TAG_FACT} {text}"


def tag_estimate(text: str) -> str:
    """
    Tag text as an estimate or approximation.

    Args:
        text: Content to tag

    Returns:
        Tagged string

    Example:
        >>> tag_estimate("The model accuracy is around 85%")
        '[ESTIMATE] The model accuracy is around 85%'
    """
    return f"{TAG_ESTIMATE} {text}"


def tag_unknown(text: str) -> str:
    """
    Tag text as unknown or uncertain information.

    Args:
        text: Content to tag

    Returns:
        Tagged string

    Example:
        >>> tag_unknown("The root cause of the performance degradation")
        '[UNKNOWN] The root cause of the performance degradation'
    """
    return f"{TAG_UNKNOWN} {text}"


def tag_assumption(text: str) -> str:
    """
    Tag text as an assumption being made.

    Args:
        text: Content to tag

    Returns:
        Tagged string

    Example:
        >>> tag_assumption("Users will provide accurate training data")
        '[ASSUMPTION] Users will provide accurate training data'
    """
    return f"{TAG_ASSUMPTION} {text}"


def tag_speculation(text: str) -> str:
    """
    Tag text as speculation or hypothesis.

    Args:
        text: Content to tag

    Returns:
        Tagged string

    Example:
        >>> tag_speculation("The issue might be related to concurrent access")
        '[SPECULATION] The issue might be related to concurrent access'
    """
    return f"{TAG_SPECULATION} {text}"


def detect_tags(text: str) -> List[Dict[str, str]]:
    """
    Detect and extract uncertainty tags from text.

    Args:
        text: Text to scan for tags

    Returns:
        List of dicts with 'tag' and 'content' keys

    Example:
        >>> text = "[FACT] System deployed. [ESTIMATE] 85% accuracy."
        >>> detect_tags(text)
        [{'tag': '[FACT]', 'content': 'System deployed.'},
         {'tag': '[ESTIMATE]', 'content': '85% accuracy.'}]
    """
    results = []

    # Pattern to match tags and their content
    # Matches [TAG] followed by text until next tag or end
    pattern = r'(\[(?:FACT|ESTIMATE|UNKNOWN|ASSUMPTION|SPECULATION)\])\s*([^\[]+)'

    matches = re.findall(pattern, text)

    for tag, content in matches:
        results.append({
            'tag': tag,
            'content': content.strip()
        })

    return results


def count_tags(text: str) -> Dict[str, int]:
    """
    Count occurrences of each tag type in text.

    Args:
        text: Text to analyze

    Returns:
        Dict mapping tag names to counts

    Example:
        >>> text = "[FACT] Data. [ESTIMATE] Approx. [FACT] More data."
        >>> count_tags(text)
        {'[FACT]': 2, '[ESTIMATE]': 1, '[UNKNOWN]': 0, ...}
    """
    counts = {tag: 0 for tag in ALL_TAGS}

    for tag in ALL_TAGS:
        counts[tag] = text.count(tag)

    return counts


def strip_tags(text: str) -> str:
    """
    Remove all uncertainty tags from text.

    Args:
        text: Tagged text

    Returns:
        Text with tags removed

    Example:
        >>> strip_tags("[FACT] This is verified. [ESTIMATE] About 85%.")
        'This is verified. About 85%.'
    """
    result = text
    for tag in ALL_TAGS:
        result = result.replace(tag, '')
    # Normalize multiple spaces to single space
    result = re.sub(r'\s+', ' ', result)
    return result.strip()


def replace_tag(text: str, old_tag: str, new_tag: str) -> str:
    """
    Replace one tag type with another.

    Args:
        text: Text with tags
        old_tag: Tag to replace
        new_tag: Replacement tag

    Returns:
        Text with tags replaced

    Example:
        >>> replace_tag("[ESTIMATE] About 85%", "[ESTIMATE]", "[FACT]")
        '[FACT] About 85%'
    """
    return text.replace(old_tag, new_tag)


def uncertainty_report(text: str) -> str:
    """
    Generate a human-readable uncertainty report for tagged text.

    Args:
        text: Tagged text to analyze

    Returns:
        Formatted report string

    Example:
        >>> text = "[FACT] A. [ESTIMATE] B. [UNKNOWN] C."
        >>> print(uncertainty_report(text))
        Uncertainty Report
        ====================
        Total tagged statements: 3
        - [FACT]: 1
        - [ESTIMATE]: 1
        - [UNKNOWN]: 1
        ...
    """
    counts = count_tags(text)
    total = sum(counts.values())
    detected = detect_tags(text)

    lines = [
        "Uncertainty Report",
        "=" * 40,
        f"Total tagged statements: {total}",
        ""
    ]

    # Count summary
    for tag, count in counts.items():
        if count > 0:
            lines.append(f"  {tag}: {count}")

    lines.append("")
    lines.append("Tagged Content:")
    lines.append("-" * 40)

    # Individual tagged items
    for item in detected:
        lines.append(f"{item['tag']} {item['content']}")

    return "\n".join(lines)


def is_tagged(text: str) -> bool:
    """
    Check if text contains any uncertainty tags.

    Args:
        text: Text to check

    Returns:
        True if any tags found, False otherwise
    """
    return any(tag in text for tag in ALL_TAGS)


def get_tag_percentage(text: str, tag: str = None) -> float | Dict[str, float]:
    """
    Calculate percentage of a specific tag type or all tag types.

    Args:
        text: Tagged text
        tag: Specific tag to calculate percentage for (optional)

    Returns:
        Float percentage if tag specified, otherwise dict mapping tags to percentages

    Example:
        >>> text = "[FACT] A. [FACT] B. [ESTIMATE] C."
        >>> get_tag_percentage(text, '[FACT]')
        66.67
        >>> get_tag_percentage(text)
        {'[FACT]': 66.67, '[ESTIMATE]': 33.33, '[UNKNOWN]': 0.0, ...}
    """
    counts = count_tags(text)
    total = sum(counts.values())

    if total == 0:
        if tag:
            return 0.0
        return {t: 0.0 for t in ALL_TAGS}

    if tag:
        # Return percentage for specific tag
        count = counts.get(tag, 0)
        return round((count / total) * 100, 2)

    # Return percentages for all tags
    return {
        t: round((count / total) * 100, 2)
        for t, count in counts.items()
    }
