# 1. Save _compat.py to src/asve/_compat.py
# 2. Replace all direct StrEnum imports across the codebase
find src/asve -name "*.py" -exec grep -l "from enum import StrEnum" {} \; | xargs sed -i 's/from enum import StrEnum/from asve._compat import StrEnum/'
