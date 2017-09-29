# Cucumber / Behave

This package implements step definitions for the the BDD packages cucumber.js and Python's behave.

Both sets of step definitions will satisfy the the tests in the `.feature` files found in `./features`.
Cucumber.js will look for step definitions in `features/step_definitions` while Python's behave will look in `features/steps` for step definitions.

Cucumber.js will process the hooks in `features/step_definitions/hooks.js` while behave's equivalent uses `features/environment.py`

## Running the tests in Cucumber.js

```
$ ./node_modules/.bin/cucumber-js
```

```
................

4 scenarios (4 passed)
12 steps (12 passed)
0m05.886s
```


## Running the tests with behave

```
$ behave
```

```
2 features passed, 0 failed, 0 skipped
4 scenarios passed, 0 failed, 0 skipped
12 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m4.322s
```