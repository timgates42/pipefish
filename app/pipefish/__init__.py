"""
Utility functions for processing JUnit XML reports and
Cobertura coverage XML reports into Markdown
"""

from .process_junit import process_junit_xml

__all__ = ['process_junit_xml']
