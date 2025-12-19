import os
import sys
import pathlib

# 프로젝트 루트를 import 경로에 추가합니다. (pytest가 패키지 `test_001`를 찾게 하기 위함)
ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
