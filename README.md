# Cucumber / Behave

This package implements step definitions for the the BDD packages cucumber.js and Python's behave.

Both sets of step definitions will satisfy the the tests in the `.feature` files found.
Cucumber.js will look for step definitions in `features/step_definitions` while Python's behave will look in `features/steps` for step definitions.

Cucumber.js will process the hooks in `features/step_definitions/hooks.js` while behave's equivalent uses `features/environment.py`