# Changelog

All notable changes to this project will be documented in this file.

## [v0.1.0] - 2025-12-19

### Added

- `main.py`: CLI 엔트리포인트와 함수 `add(a, b)`, `greet(name)` 추가 (`--greet`, `--sum`).
- `tests/test_main.py`: `pytest` 기반 단위테스트 5개 (함수 동작 및 CLI 동작 검증).
- `requirements.txt`: 테스트 의존성(`pytest`).
- `README.md`: 사용법 및 테스트 실행 방법 문서화.
- CI: `.github/workflows/ci.yml` — Python 3.11/3.12에서 `pytest`와 `flake8` 실행, pip 캐시 사용.
- Lint 설정: `.flake8` (max-line-length=88, `E203`, `W503` 무시).

### Notes

- 초기 릴리스로, 기본 기능과 테스트/CI가 설정되어 있습니다.
