# Dinner Menu Toy Project (Streamlit)

DuckDuckGo에서 `장어덮밥 맛집`을 검색한 결과를 보여주는 간단한 Streamlit 웹페이지입니다.

## 1) 로컬 실행 (venv)

```bash
cd /Users/a09246/Desktop/projects/toy
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

브라우저에서 기본적으로 `http://localhost:8501`로 접속됩니다.

## 2) Streamlit Community Cloud 배포

1. 이 저장소를 GitHub에 push
2. [Streamlit Community Cloud](https://share.streamlit.io/) 접속 후 GitHub 연동
3. `New app` 생성
4. 설정값 입력
   - Repository: 본 프로젝트 저장소
   - Branch: `main` (또는 원하는 브랜치)
   - Main file path: `app.py`
5. `Deploy` 클릭

`requirements.txt`를 자동으로 읽어 의존성이 설치됩니다.

## 3) 검색 결과가 비어 있을 때

네트워크 환경에 따라 검색 결과가 비어 있거나 차단될 수 있습니다.  
이 경우 앱에서 제공하는 `DuckDuckGo에서 직접 검색하기` 버튼으로 바로 확인할 수 있습니다.