# test_001

간단한 테스트용 파이썬 프로그램과 테스트들을 포함합니다.

설치 및 실행

- **의존성(개발)**: 프로젝트 루트에서 (선택)

	```bash
	pip install -r requirements.txt
	```

- **개발 모드로 설치** (로컬에서 콘솔 스크립트 사용 시 권장)

	```bash
	pip install -e .
	```

- **직접 실행 (개발용)**

	- 모듈로 실행: `python -m test_001.main --greet Alice`
	- 파일 실행(레거시 shim 지원): `python main.py --greet Alice`

- **설치 후 콘솔 스크립트 실행**

	```bash
	# 설치하면 아래 중 하나로 실행 가능
	test-001 --greet Alice
	test_001 --sum 2 3
	```

CLI 사용 예

- 인사 출력:

	```bash
	python -m test_001.main --greet Bob
	# 또는 설치 후
	test-001 --greet Bob
	```

- 두 수 합계 출력:

	```bash
	python -m test_001.main --sum 4 6
	# 또는 설치 후
	test-001 --sum 4 6
	```

테스트

- pytest 실행:

	```bash
	pytest -q
	```

편의성

- 설치 경로가 PATH에 없을 때(예: `pip install -e .` 후 경고가 발생하는 경우) 임시로 PATH를 추가할 수 있습니다:

	```bash
	export PATH="/usr/local/python/3.12.1/bin:$PATH"
	```

- 또는 리포지토리 내의 로컬 실행 스크립트를 사용하세요 (설치 불필요):

	```bash
	./scripts/test-001 --greet Alice
	./scripts/test-001 --sum 4 6
	```

	이 스크립트는 내부적으로 `python -m test_001.main`을 호출합니다.

추가 설명 / 문제해결

- 가상환경 사용 권장

	```bash
	python -m venv .venv
	source .venv/bin/activate  # Windows: .venv\Scripts\activate
	pip install -e .
	```

	가상환경을 사용하면 시스템 전역 PATH를 건드리지 않고 의존성을 관리할 수 있습니다.

- Windows 사용 시

	- 실행: `py -m test_001.main --greet Alice` 또는 `python -m test_001.main ...`
	- 가상환경 활성화: `.venv\Scripts\activate`

- PATH 관련 문제

	- `pip install -e .` 후 `WARNING: The scripts ... is not on PATH` 경고가 뜨면, 설치된 스크립트 위치를 `PATH`에 추가하거나 로컬 `./scripts/test-001`를 사용하세요.
	- 예: `export PATH="/usr/local/python/3.12.1/bin:$PATH"` (영구 적용은 쉘 설정 파일에 추가)

- 언인스톨

	```bash
	python -m pip uninstall -y test-001
	```

- CI/자동화에서 테스트 실행

	- CI에서는 일반적으로 가상환경을 만들고 `pip install -r requirements.txt` 또는 `pip install -e .` 후 `pytest -q`를 실행합니다.
	- 모듈 방식 실행이 안정적입니다: `python -m pytest` 또는 `python -m test_001.main --greet Bob`

- 기타 팁

	- 콘솔 엔트리포인트 이름은 `test-001`(하이픈)과 `test_001`(밑줄) 둘 다 제공됩니다.
	- 상위의 `main.py` 파일은 레거시 shim입니다. 원하면 완전 삭제해서 패키지 전용으로 정리할 수 있습니다.
