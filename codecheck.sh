#!/bin/bash

CODE=$@
if [ -z $1 ] ; then
  CODE="sophie setup.py"
fi

echo "== Pylint =="

# Don't generate reports
OPTIONS="--reports=n"

# Include message ids in output
OPTIONS="$OPTIONS --include-ids=y"

# Ignore twisted reactor generated methods
OPTIONS="$OPTIONS --generated-members=md5"

# Increase miniumum similarity lines to 10
OPTIONS="$OPTIONS --min-similarity-lines=10"

# Increase maximum attribute name length to 40
OPTIONS="$OPTIONS --attr-rgx=[a-z_][a-z0-9_]{2,40}$"

# Increase maximum method name length to 40
OPTIONS="$OPTIONS --method-rgx=[a-z_][a-z0-9_]{2,40}$"

# Increase maximum function name length to 40
OPTIONS="$OPTIONS --function-rgx=[a-z_][a-z0-9_]{2,40}$"

# Ignore test case methods that don't match name pattern
OPTIONS="$OPTIONS --good-names=_,setUp,setUpModule,tearDown,tearDownModule"

# Increase number of maximum arguments to 10
OPTIONS="$OPTIONS --max-args=10"

# I0011: Locally disabling xxxxx
# W0703: Catch "Exception"
# R0902: Too many instance attributes
# R0903: Too few public methods
# R0904: Too many public methods
# E0202: An attribute inherited from 'x' hide this method
OPTIONS="$OPTIONS --disable=I0011,W0703,R0902,R0903,R0904,E0202"

pylint $OPTIONS $CODE
pylint_return=$?

echo "== Pyflakes =="
pyflakes $CODE
pyflakes_return=$?

echo "== Pep8 =="
pep8 $CODE
pep8_return=$?

return=$pylint_return || $pyflakes || $pep8_return
exit $return
