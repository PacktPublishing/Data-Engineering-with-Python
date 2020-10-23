"""
A basic generated Great Expectations checkpoint that validates a single batch of data.

Data that is validated is controlled by BatchKwargs, which can be adjusted in
this script.

Data are validated by use of the `ActionListValidationOperator` which is
configured by default. The default configuration of this Validation Operator
saves validation results to your results store and then updates Data Docs.

This makes viewing validation results easy for you and your team.

Usage:
- Run this file: `python sv.py`.
- This can be run manually or via a scheduler such as cron.
- If your pipeline runner supports python snippets you can paste this into your
pipeline.
"""
import sys

from great_expectations import DataContext

# checkpoint configuration
context = DataContext("/home/paulcrickard/staging/great_expectations")
suite = context.get_expectation_suite("staging.validation")
# You can modify your BatchKwargs to select different data
batch_kwargs = {"table": "staging", "schema": "public", "datasource": "stagingtable"}

# checkpoint validation process
batch = context.get_batch(batch_kwargs, suite)
results = context.run_validation_operator("action_list_operator", [batch])

if not results["success"]:
    print('{"result":"fail"}')
    sys.exit(0)

print('{"result":"pass"}')
sys.exit(0)
