from setuptools import find_packages, setup

setup(
    name="my_dagster_code_location",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "dagster-dbt",
        "dbt-duckdb",
        "pandas",
        "html5lib",
        "scikit-learn",
    ],
    extras_require={
        "dev": [
            "dagster-webserver",
        ]
    },
)