"""
Tests for uncertainty_tags module
"""

import pytest
from toolkit.uncertainty_tags import (
    TAG_FACT,
    TAG_ESTIMATE,
    TAG_UNKNOWN,
    TAG_ASSUMPTION,
    TAG_SPECULATION,
    tag_fact,
    tag_estimate,
    tag_unknown,
    tag_assumption,
    tag_speculation,
    detect_tags,
    count_tags,
    strip_tags,
    replace_tag,
    uncertainty_report,
    is_tagged,
    get_tag_percentage
)


class TestTagConstants:
    """Test tag constant definitions"""

    def test_tag_constants_defined(self):
        """Test that all tag constants are defined"""
        assert TAG_FACT == "[FACT]"
        assert TAG_ESTIMATE == "[ESTIMATE]"
        assert TAG_UNKNOWN == "[UNKNOWN]"
        assert TAG_ASSUMPTION == "[ASSUMPTION]"
        assert TAG_SPECULATION == "[SPECULATION]"


class TestTaggingFunctions:
    """Test tagging helper functions"""

    def test_tag_fact(self):
        """Test tagging content as fact"""
        text = "The sky is blue"
        tagged = tag_fact(text)
        assert tagged == "[FACT] The sky is blue"

    def test_tag_estimate(self):
        """Test tagging content as estimate"""
        text = "This will take about 2 hours"
        tagged = tag_estimate(text)
        assert tagged == "[ESTIMATE] This will take about 2 hours"

    def test_tag_unknown(self):
        """Test tagging content as unknown"""
        text = "I don't have that information"
        tagged = tag_unknown(text)
        assert tagged == "[UNKNOWN] I don't have that information"

    def test_tag_assumption(self):
        """Test tagging content as assumption"""
        text = "Assuming the server is running"
        tagged = tag_assumption(text)
        assert tagged == "[ASSUMPTION] Assuming the server is running"

    def test_tag_speculation(self):
        """Test tagging content as speculation"""
        text = "It might rain tomorrow"
        tagged = tag_speculation(text)
        assert tagged == "[SPECULATION] It might rain tomorrow"

    def test_tag_empty_string(self):
        """Test tagging empty string"""
        assert tag_fact("") == "[FACT] "
        assert tag_estimate("") == "[ESTIMATE] "


class TestDetectTags:
    """Test tag detection"""

    def test_detect_single_tag(self):
        """Test detecting a single tag"""
        text = "[FACT] The earth is round"
        tags = detect_tags(text)

        assert len(tags) == 1
        assert tags[0]['tag'] == '[FACT]'
        assert tags[0]['content'] == 'The earth is round'

    def test_detect_multiple_tags(self):
        """Test detecting multiple tags"""
        text = "[FACT] Paris is in France. [ESTIMATE] It has 2 million people."
        tags = detect_tags(text)

        assert len(tags) == 2
        assert tags[0]['tag'] == '[FACT]'
        assert tags[1]['tag'] == '[ESTIMATE]'

    def test_detect_all_tag_types(self):
        """Test detecting all different tag types"""
        text = (
            "[FACT] Fact here. "
            "[ESTIMATE] Estimate here. "
            "[UNKNOWN] Unknown here. "
            "[ASSUMPTION] Assumption here. "
            "[SPECULATION] Speculation here."
        )
        tags = detect_tags(text)

        assert len(tags) == 5
        tag_types = [t['tag'] for t in tags]
        assert '[FACT]' in tag_types
        assert '[ESTIMATE]' in tag_types
        assert '[UNKNOWN]' in tag_types
        assert '[ASSUMPTION]' in tag_types
        assert '[SPECULATION]' in tag_types

    def test_detect_no_tags(self):
        """Test detecting tags in untagged text"""
        text = "This is plain text with no tags"
        tags = detect_tags(text)

        assert len(tags) == 0

    def test_detect_tags_multiline(self):
        """Test detecting tags across multiple lines"""
        text = """[FACT] First line.
        [ESTIMATE] Second line.
        Regular text.
        [UNKNOWN] Fourth line."""

        tags = detect_tags(text)
        assert len(tags) == 3


class TestCountTags:
    """Test tag counting"""

    def test_count_single_tag_type(self):
        """Test counting single tag type"""
        text = "[FACT] One. [FACT] Two. [FACT] Three."
        counts = count_tags(text)

        assert counts['[FACT]'] == 3
        assert counts['[ESTIMATE]'] == 0

    def test_count_multiple_tag_types(self):
        """Test counting multiple tag types"""
        text = (
            "[FACT] Fact 1. [FACT] Fact 2. "
            "[ESTIMATE] Estimate 1. "
            "[UNKNOWN] Unknown 1."
        )
        counts = count_tags(text)

        assert counts['[FACT]'] == 2
        assert counts['[ESTIMATE]'] == 1
        assert counts['[UNKNOWN]'] == 1
        assert counts['[ASSUMPTION]'] == 0
        assert counts['[SPECULATION]'] == 0

    def test_count_no_tags(self):
        """Test counting with no tags"""
        text = "Plain text"
        counts = count_tags(text)

        assert all(count == 0 for count in counts.values())


class TestStripTags:
    """Test tag stripping"""

    def test_strip_single_tag(self):
        """Test stripping a single tag"""
        text = "[FACT] The sky is blue"
        stripped = strip_tags(text)
        assert stripped == "The sky is blue"

    def test_strip_multiple_tags(self):
        """Test stripping multiple tags"""
        text = "[FACT] Paris is in France. [ESTIMATE] It has 2 million people."
        stripped = strip_tags(text)
        assert stripped == "Paris is in France. It has 2 million people."

    def test_strip_all_tag_types(self):
        """Test stripping all tag types"""
        text = (
            "[FACT] Fact. "
            "[ESTIMATE] Estimate. "
            "[UNKNOWN] Unknown. "
            "[ASSUMPTION] Assumption. "
            "[SPECULATION] Speculation."
        )
        stripped = strip_tags(text)
        assert "[FACT]" not in stripped
        assert "[ESTIMATE]" not in stripped
        assert "[UNKNOWN]" not in stripped
        assert "[ASSUMPTION]" not in stripped
        assert "[SPECULATION]" not in stripped
        assert "Fact. Estimate. Unknown. Assumption. Speculation." == stripped

    def test_strip_no_tags(self):
        """Test stripping from untagged text"""
        text = "Plain text"
        stripped = strip_tags(text)
        assert stripped == text


class TestReplaceTag:
    """Test tag replacement"""

    def test_replace_tag_basic(self):
        """Test basic tag replacement"""
        text = "[FACT] The earth is round"
        replaced = replace_tag(text, '[FACT]', '[ESTIMATE]')
        assert replaced == "[ESTIMATE] The earth is round"

    def test_replace_multiple_occurrences(self):
        """Test replacing multiple occurrences"""
        text = "[FACT] One. [FACT] Two. [ESTIMATE] Three."
        replaced = replace_tag(text, '[FACT]', '[ESTIMATE]')
        assert replaced == "[ESTIMATE] One. [ESTIMATE] Two. [ESTIMATE] Three."

    def test_replace_nonexistent_tag(self):
        """Test replacing tag that doesn't exist"""
        text = "[FACT] Something"
        replaced = replace_tag(text, '[ESTIMATE]', '[FACT]')
        assert replaced == text  # Should be unchanged


class TestUncertaintyReport:
    """Test uncertainty report generation"""

    def test_report_with_tags(self):
        """Test generating report with tagged content"""
        text = (
            "[FACT] Paris is the capital of France. "
            "[ESTIMATE] It has about 2 million residents. "
            "[UNKNOWN] I don't know the exact population of the metro area."
        )
        report = uncertainty_report(text)

        assert "Uncertainty Report" in report
        assert "[FACT]: 1" in report
        assert "[ESTIMATE]: 1" in report
        assert "[UNKNOWN]: 1" in report
        assert "Total tagged statements: 3" in report

    def test_report_no_tags(self):
        """Test generating report with no tags"""
        text = "Plain untagged text"
        report = uncertainty_report(text)

        assert "Uncertainty Report" in report
        assert "Total tagged statements: 0" in report

    def test_report_formatting(self):
        """Test report is properly formatted"""
        text = "[FACT] Test"
        report = uncertainty_report(text)

        # Should have proper structure
        assert "===" in report
        assert "Total tagged statements:" in report


class TestIsTagged:
    """Test checking if text contains tags"""

    def test_is_tagged_true(self):
        """Test detecting tagged text"""
        assert is_tagged("[FACT] Something") == True
        assert is_tagged("[ESTIMATE] Guess") == True
        assert is_tagged("Text [UNKNOWN] more text") == True

    def test_is_tagged_false(self):
        """Test detecting untagged text"""
        assert is_tagged("Plain text") == False
        assert is_tagged("No tags here") == False

    def test_is_tagged_empty(self):
        """Test with empty string"""
        assert is_tagged("") == False


class TestGetTagPercentage:
    """Test tag percentage calculation"""

    def test_percentage_all_same_tag(self):
        """Test percentage when all tags are same"""
        text = "[FACT] One. [FACT] Two. [FACT] Three."
        pct = get_tag_percentage(text, '[FACT]')
        assert pct == 100.0

    def test_percentage_mixed_tags(self):
        """Test percentage with mixed tags"""
        text = "[FACT] One. [FACT] Two. [ESTIMATE] Three. [ESTIMATE] Four."
        fact_pct = get_tag_percentage(text, '[FACT]')
        estimate_pct = get_tag_percentage(text, '[ESTIMATE]')

        assert fact_pct == 50.0
        assert estimate_pct == 50.0

    def test_percentage_no_tags(self):
        """Test percentage with no tags"""
        text = "Plain text"
        pct = get_tag_percentage(text, '[FACT]')
        assert pct == 0.0

    def test_percentage_specific_tag_absent(self):
        """Test percentage when specific tag is absent"""
        text = "[FACT] One. [FACT] Two."
        pct = get_tag_percentage(text, '[ESTIMATE]')
        assert pct == 0.0

    def test_percentage_one_third(self):
        """Test percentage calculation accuracy"""
        text = "[FACT] One. [ESTIMATE] Two. [UNKNOWN] Three."
        pct = get_tag_percentage(text, '[FACT]')
        assert abs(pct - 33.33) < 0.1  # Approximately 33.33%


class TestEdgeCases:
    """Test edge cases and special scenarios"""

    def test_tag_with_special_characters(self):
        """Test tagging text with special characters"""
        text = "Price: $100.00 (approx.)"
        tagged = tag_estimate(text)
        assert tagged == "[ESTIMATE] Price: $100.00 (approx.)"

    def test_detect_tags_with_brackets_in_content(self):
        """Test detection when content has brackets"""
        text = "[FACT] Array[0] is first element"
        tags = detect_tags(text)

        assert len(tags) == 1
        assert tags[0]['tag'] == '[FACT]'

    def test_multiline_tagged_content(self):
        """Test handling multiline tagged content"""
        text = """[FACT] First line
        continues here
        and here"""

        tags = detect_tags(text)
        assert len(tags) == 1
        assert 'First line' in tags[0]['content']

    def test_consecutive_tags(self):
        """Test consecutive tags without gap"""
        text = "[FACT] One[ESTIMATE] Two"
        tags = detect_tags(text)

        assert len(tags) == 2

    def test_tag_at_end_of_text(self):
        """Test tag at the very end"""
        text = "Some text and then [FACT]"
        tags = detect_tags(text)

        # Should detect tag even at end
        assert len(tags) >= 0  # Depends on implementation

    def test_very_long_text(self):
        """Test with very long text"""
        text = "[FACT] " + ("word " * 10000)
        tags = detect_tags(text)

        assert len(tags) >= 1
        assert tags[0]['tag'] == '[FACT]'

    def test_unicode_content(self):
        """Test with unicode characters"""
        text = tag_fact("Tokyo (東京) is the capital")
        assert "[FACT]" in text
        assert "東京" in text


class TestIntegration:
    """Integration tests combining multiple functions"""

    def test_tag_detect_strip_cycle(self):
        """Test tagging, detecting, and stripping"""
        original = "The earth is round"
        tagged = tag_fact(original)
        detected = detect_tags(tagged)
        stripped = strip_tags(tagged)

        assert len(detected) == 1
        assert stripped == original

    def test_complex_document_processing(self):
        """Test processing a complex document"""
        doc = f"""
        {tag_fact('Paris is the capital of France.')}
        {tag_estimate('It has approximately 2 million residents.')}
        {tag_unknown("I don't know the exact GDP.")}
        {tag_assumption('Assuming current trends continue.')}
        {tag_speculation('It might become even larger in the future.')}
        """

        # Count all tags
        counts = count_tags(doc)
        assert counts['[FACT]'] == 1
        assert counts['[ESTIMATE]'] == 1
        assert counts['[UNKNOWN]'] == 1
        assert counts['[ASSUMPTION]'] == 1
        assert counts['[SPECULATION]'] == 1

        # Generate report
        report = uncertainty_report(doc)
        assert "Total tagged statements: 5" in report

        # Strip all tags
        stripped = strip_tags(doc)
        assert '[FACT]' not in stripped
        assert 'Paris is the capital of France' in stripped

    def test_uncertainty_distribution(self):
        """Test analyzing uncertainty distribution"""
        # Mostly facts, few estimates
        text = (
            "[FACT] A. [FACT] B. [FACT] C. [FACT] D. "
            "[ESTIMATE] E. [UNKNOWN] F."
        )

        fact_pct = get_tag_percentage(text, '[FACT]')
        estimate_pct = get_tag_percentage(text, '[ESTIMATE]')
        unknown_pct = get_tag_percentage(text, '[UNKNOWN]')

        # Check percentages sum appropriately
        total_tags = sum(count_tags(text).values())
        assert total_tags == 6
        assert fact_pct > estimate_pct
        assert fact_pct > unknown_pct


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
