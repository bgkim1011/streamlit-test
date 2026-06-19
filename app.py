from urllib.parse import quote_plus

import streamlit as st
from duckduckgo_search import DDGS


st.set_page_config(
    page_title="서희선의 오늘의 저녁메뉴 - 장어덮밥 맛집 찾기",
    page_icon="🍱",
    layout="centered",
)


def _normalize_result(title: str, url: str, description: str):
    return {
        "title": title or "제목 없음",
        "url": url,
        "description": description or "설명 정보가 없습니다.",
    }


@st.cache_data(show_spinner=False, ttl=1800)
def get_duckduckgo_results(query: str, num_results: int):
    results = []
    with DDGS() as ddgs:
        for item in ddgs.text(keywords=query, region="kr-kr", max_results=num_results):
            results.append(
                _normalize_result(
                    item.get("title", ""),
                    item.get("href", ""),
                    item.get("body", ""),
                )
            )
    return results


st.title("🍱 서희선의 오늘의 저녁메뉴: 장어덮밥")
st.caption("DuckDuckGo 검색 결과를 바탕으로 장어덮밥 맛집 후보를 확인해요.")

default_query = "장어덮밥 맛집"

with st.form("search_form"):
    query = st.text_input("검색어", value=default_query)
    num_results = st.slider("표시할 결과 수", min_value=3, max_value=15, value=8)
    submitted = st.form_submit_button("DuckDuckGo 검색하기")

if submitted:
    with st.spinner("DuckDuckGo 검색 결과를 불러오는 중..."):
        try:
            results = get_duckduckgo_results(query, num_results)
            if not results:
                st.warning("검색 결과를 가져오지 못했습니다. 아래 버튼으로 DuckDuckGo에서 직접 검색해보세요.")
                st.link_button("DuckDuckGo에서 직접 검색하기", f"https://duckduckgo.com/?q={quote_plus(query)}")
            else:
                st.success(f"총 {len(results)}개의 결과를 찾았습니다. (출처: DuckDuckGo)")
                for idx, result in enumerate(results, start=1):
                    st.markdown(f"### {idx}. {result['title']}")
                    st.write(result["description"])
                    st.markdown(f"[링크 열기]({result['url']})")
                    st.divider()
        except Exception as exc:
            st.warning("검색 중 오류가 발생했습니다. 네트워크 상태를 확인한 뒤 다시 시도해 주세요.")
            st.link_button("DuckDuckGo에서 직접 검색하기", f"https://duckduckgo.com/?q={quote_plus(query)}")
            with st.expander("오류 상세 보기"):
                st.code(str(exc))
else:
    st.info("검색어를 확인한 뒤 **DuckDuckGo 검색하기** 버튼을 눌러 주세요.")
