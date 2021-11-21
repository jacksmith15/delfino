import click

_TEMPLATE = """
[tool.rads_toolbox]
reports_directory = "reports"
sources_directory = "src"
tests_directory = "tests"

# Directories under `tests_directory` that contain specific test type.
test_types = ["unit", "integration"]
"""


@click.command("init")
def run_init():
    """Initializes toolbox for this project."""
    print(
        f"Please copy the following template into '{click.get_current_context().obj}' and "
        f"update to suit your project:\n{_TEMPLATE}"
    )