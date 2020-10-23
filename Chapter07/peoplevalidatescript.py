import sys
from great_expectations import DataContext
# checkpoint configuration
context = DataContext("/home/paulcrickard/peoplepipeline/great_expectations")
suite = context.get_expectation_suite("people.validate")
# You can modify your BatchKwargs to select different data
batch_kwargs = {
    "path": "/home/paulcrickard/peoplepipeline/people.csv",
    "datasource": "files_datasource",
    "reader_method": "read_csv",
}

# checkpoint validation process
batch = context.get_batch(batch_kwargs, suite)
results = context.run_validation_operator("action_list_operator", [batch])

if not results["success"]:
    print('{"result":"fail"}')
    sys.exit(0)

print('{"result":"pass"}')
sys.exit(0)
