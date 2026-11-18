# Let's Insu (렛츠인슈) 에이전트 공통 인수인계 계약

> 이 문서는 Codex, Claude, Gemini 및 로컬 에이전트가 렛츠인슈 보험 약관·상담 데이터베이스를 이어서 운영하기 위한 단일 계약서입니다.

## 1. 정본 및 저장소 원칙
- **정본 경로**: `/Users/pyw31337/Developer/insu`
- **단일 진실 공급원(SSOT)**: 전 보험사 시기별 약관 원문, 금감원 분쟁조정례, 소비자 부지급 방어 가이드 데이터는 오직 이 레포지토리에서만 수정·확장한다.
- **연합 소비**: 뉴스보드 등 타 서비스는 이 레포지토리의 `data/policy_terms_db.json`을 온디맨드 fetch하여 표시한다.

## 2. 데이터 스키마 및 URN 규정
- **약관 URN**: `urn:insu:policy:{insurer}:{product_code}:{generation}`
- **분쟁조정 URN**: `urn:insu:dispute:{fss_no}`
- **필수 필드**: `category`, `insurer_coverage`, `effective_period`, `key_coverage`, `insurer_defense`, `court_precedent`, `consumer_defense`.
- **소비자 상담 목표**: 가입 시기와 처한 질병 상황에 따라 보험사의 면책 논리를 방어할 수 있는 법적 근거(상법 제638조의3 설명의무, 상법 제680조 손해방지비용 등)를 필수로 매핑한다.
