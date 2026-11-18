# 렛츠인슈 (Let's Insu) — 전 보험사 시기별 약관 & 보험금 지급 판단 AI 상담 독립 원장

> 대한민국 모든 보험사(생명보험·손해보험)의 모든 상품과 시기별 개정 약관(1~4세대 실손, 3대 질병, 일배책 등) 및 금융감독원 분쟁조정례를 전수 수집·관리하는 독립 보험 데이터 원장입니다.
> 사용자가 가입한 보험과 현재 처한 질병/사고 상황에 대해, 보험사의 면책 논리를 방어하고 정당한 보험금을 청구·지급받을 수 있도록 지원하는 생활밀착형 지능형 서비스를 목표로 합니다.

---

## 1. 글로벌 온톨로지 식별자 체계 (Global Federated URN)
- **약관 식별자**: `urn:insu:policy:{보험사}:{상품군}:{개정시기}` (예: `urn:insu:policy:samsung_fire:actual_loss:gen1_2000`, `urn:insu:policy:all:actual_loss:gen4_2021`)
- **분쟁조정례 식별자**: `urn:insu:dispute:{fss_decision_no}` (예: `urn:insu:dispute:fss-2023-14`)
- **법원 판례 연동**: `urn:law:precedent:{사건번호}` (렛츠로 레포지토리와 교차 온톨로지 연동)

---

## 2. 제공 엔드포인트 및 데이터 정본
- **시기별 핵심 표준약관 원장**: `data/policy_terms_db.json`
- **약관 상담 및 방어 가이드 웹 서비스**: `index.html`
- **시기별 개정 약관 수집기**: `scripts/crawler.py`

## 3. 서비스 간 데이터 연동 방식 (뉴스보드 및 타 서비스)
```javascript
// 외부 서비스에서 렛츠인슈 약관 데이터 연동 예시
async function loadLetInsuPolicies() {
  const url = 'https://pyw31337.github.io/insu/data/policy_terms_db.json';
  const localFallback = '../insu/data/policy_terms_db.json';
  try {
    const res = await fetch(url);
    return await res.json();
  } catch (e) {
    const fallbackRes = await fetch(localFallback);
    return await fallbackRes.json();
  }
}
```
