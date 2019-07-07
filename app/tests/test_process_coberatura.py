"""
Test modules for pipefish process_cobertura
"""

import os
import sys

import pytest


def get_basedir():
    """
    Locate the current directory of this file
    """
    return os.path.dirname(os.path.abspath(sys.modules[__name__].__file__))


@pytest.mark.parametrize("outcome_filename,expected_outcome", [
    (
        'cobertura_coverage.xml',
        'Coverage is 60.61% meets minimum of 50.00%'
        ' (20 lines of 33 total).'
    ),
])
def test_outcomes(outcome_filename, expected_outcome):
    """
    GIVEN a sample Cobertura Coverage XML containing specified outcome WHEN
    calling process_cobertura_xml THEN the call returns markdown highlighting
    the expected outcome.
    """
    # Setup
    from pipefish.process_cobertura import process_cobertura_xml
    samplepath = os.path.join(
        os.path.dirname(get_basedir()), 'data', outcome_filename
    )
    # Exercise
    result = process_cobertura_xml(samplepath, 50)
    # Verify
    assert result == expected_outcome  # nosec


def test_invalid_xml():
    """
    GIVEN a sample Cobertura XML containing non-coverage XML WHEN calling
    process_cobertura_xml THEN the call raises an Exception indicating failure
    to process.
    """
    # Setup
    from pipefish.process_cobertura import process_cobertura_xml
    samplepath = os.path.join(
        os.path.dirname(get_basedir()), 'data', 'junit_invalid.xml'
    )
    # Exercise
    with pytest.raises(Exception) as excctxt:
        # Exercise
        process_cobertura_xml(samplepath)
    # Verify
    assert (  # nosec
        excctxt.value.args[0] == 'Failed to process Cobertura Coverage XML'
    )
