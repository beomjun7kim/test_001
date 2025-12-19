# v0.1.0 — Initial release

요약:

- 간단한 테스트용 파이썬 프로그램과 관련 테스트/CI를 추가한 초기 릴리스입니다.

주요 변경 사항:

- `main.py`: CLI 엔트리포인트와 함수 `add(a, b)`, `greet(name)` 추가 (`--greet`, `--sum`).
- `tests/test_main.py`: `pytest` 기반 단위테스트 5개 (함수 동작 및 CLI 동작 검증).
- `requirements.txt`: 테스트 의존성(`pytest`).
- `README.md`: 사용법 및 테스트 실행 방법 문서화.
- CI: `.github/workflows/ci.yml` — Python 3.11/3.12에서 `pytest`와 `flake8` 실행, pip 캐시 사용.
- Lint 설정: `.flake8` (max-line-length=88, `E203`, `W503` 무시).

설치 및 실행 예시:

```bash
pip install -r requirements.txt
pytest -q
python3 main.py --greet Alice
python3 main.py --sum 2 3
```

참고:

- PR: Add simple test program with tests and README
- 테스트 및 CI가 설정되어 있으며, 릴리스 태그는 `v0.1.0`입니다.

감사합니다.
