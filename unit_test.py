from minesweeper import generate_minefield
import pytest
from textwrap import dedent

def test_empty_minefield_description_outputs_nothing():
    output = generate_minefield("0 0")

    assert output is None

def minefield_description(text):
    return dedent(text).lstrip()

def expected_minefield(text):
    return dedent(text).strip()

@pytest.mark.parametrize("minefield_description,expected_minefield", [
    (
        minefield_description("""
            1 1
            .
        """),
        expected_minefield("""
            0
        """)
    ),
    (
        minefield_description("""
            1 2
            ..
        """),
        expected_minefield("""
            00
        """)
    ),
    (
        minefield_description("""
            2 1
            .
            .
        """),
        expected_minefield("""
            0
            0
        """)
    ),
    (
        minefield_description("""
            3 1
            .
            .
            .
        """),
        expected_minefield("""
            0
            0
            0
        """)
    ),
    (
        minefield_description("""
            2 2
            ..
            ..
        """),
        expected_minefield("""
            00
            00
        """)
    ),
    (
        minefield_description("""
            5 4
            ....
            ....
            ....
            ....
            ....
        """),
        expected_minefield("""
            0000
            0000
            0000
            0000
            0000
        """)
    )
])
def test_outputs_minefield_for_n_by_m_minefield_description_with_no_mines(
    minefield_description,
    expected_minefield):
    assert generate_minefield(minefield_description) == expected_minefield


@pytest.mark.parametrize("minefield_description,expected_minefield", [
    (
        minefield_description("""
            1 1
            *
        """),
        expected_minefield("""
            *
        """)
    ),
    (
        minefield_description("""
            1 2
            .*
        """),
        expected_minefield("""
            1*
        """)
    ),
    (
        minefield_description("""
            1 2
            *.
        """),
        expected_minefield("""
            *1
        """)
    ),
    (
        minefield_description("""
            1 3
            ..*
        """),
        expected_minefield("""
            01*
        """)
    ),
    (
        minefield_description("""
            1 6
            .*..*.
        """),
        expected_minefield("""
            1*11*1
        """)
    ),
    (
        minefield_description("""
            2 2
            .*
            ..
        """),
        expected_minefield("""
            1*
            11
        """)
    )
])
def test_outputs_minefield_for_n_by_m_minefield_description_with_one_adjacent_mine(
    minefield_description,
    expected_minefield):
    assert generate_minefield(minefield_description) == expected_minefield


@pytest.mark.parametrize("minefield_description,expected_minefield", [
    (
        minefield_description("""
            1 3
            *.*
        """),
        expected_minefield("""
            *2*
        """)
    ),
    (
        minefield_description("""
            1 5
            *.*.*
        """),
        expected_minefield("""
            *2*2*
        """)
    ),
    (
        minefield_description("""
            1 5
            ..*.*
        """),
        expected_minefield("""
            01*2*
        """)
    ),
    (
        minefield_description("""
            1 5
            ..**.
        """),
        expected_minefield("""
            01**1
        """)
    ),
    (
        minefield_description("""
            1 5
            ..***
        """),
        expected_minefield("""
            01***
        """)
    ),
    (
        minefield_description("""
            1 5
            *****
        """),
        expected_minefield("""
            *****
        """)
    )
])
def test_outputs_minefield_for_n_by_m_minefield_description_with_two_adjacent_mines(
    minefield_description,
    expected_minefield):
    assert generate_minefield(minefield_description) == expected_minefield


@pytest.mark.parametrize("minefield_description,expected_minefield", [
    (
        minefield_description("""
            2 2
            **
            *.
        """),
        expected_minefield("""
            **
            *3
        """)
    ),
    (
        minefield_description("""
            2 2
            .*
            **
        """),
        expected_minefield("""
            3*
            **
        """)
    ),
    (
        minefield_description("""
            2 2
            .**
            ..*
        """),
        expected_minefield("""
            1**
            13*
        """)
    )
])
def test_outputs_minefield_for_n_by_m_minefield_description_with_three_adjacent_mines(
    minefield_description,
    expected_minefield):
    assert generate_minefield(minefield_description) == expected_minefield