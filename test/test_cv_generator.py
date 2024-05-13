import pytest
from cv_generator.cv_generator import read_template, parse_template, merge


def test_read_template_returns_stripped_string():
    actual = read_template('assets/personal_summary_template.txt')
    expected = "I'm {Name} and I have Bachelor's degree in {major} and Currently working as a {job_title}  -  at {company_name}."
    assert actual == expected


# @pytest.mark.skip("pending")
def test_parse_template():
    actual_stripped, actual_parts = parse_template(
        "I'm {Name} and I have Bachelor's degree in {major} and Currently working as a {job_title}  -  at {company_name}."
    )
    expected_stripped = "I'm {} and I have Bachelor's degree in {} and Currently working as a {}  -  at {}."
    expected_parts = ("Name", "major", "job_title","company_name")

    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts


# @pytest.mark.skip("pending")
def test_merge():
    actual = merge("I'm {} and I have Bachelor's degree in {} and Currently working as a {}  -  at {}.", ("john", "CS", "developer","ABCIT"))
    expected = "I'm john and I have Bachelor's degree in CS and Currently working as a developer  -  at ABCIT."
    assert actual == expected


# @pytest.mark.skip("pending")
def test_read_template_raises_exception_with_bad_path():
    path = "missing.txt"
    with pytest.raises(IOError):  
        read_template(path)