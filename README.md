# 도서출판 민홀릭 홈페이지

**https://minholicbook.github.io/**

정적 HTML 한 파일로 된 출판사 홈페이지입니다. 별도 빌드 과정 없이 GitHub Pages에 바로 올릴 수 있습니다.

지금까지의 수정 내역은 [CHANGELOG.md](CHANGELOG.md), 디자인 규칙과 주의사항은 [CLAUDE.md](CLAUDE.md) 에 있습니다.

수정 후 `main`에 push하면 1~2분 뒤 자동 반영됩니다.

```bash
git add -A && git commit -m "수정 내용" && git push
```

## GitHub Pages 배포

1. GitHub에서 새 저장소를 만듭니다 (Public).
2. 파일 전체를 저장소 루트에 올립니다.
   ```bash
   git remote add origin https://github.com/<계정>/<저장소>.git
   git push -u origin main
   ```
3. 저장소 → Settings → Pages
   - Source: `Deploy from a branch`
   - Branch: `main` / `/ (root)` → Save
4. 1~2분 뒤 `https://<계정>.github.io/<저장소>/` 에서 열립니다.

저장소 이름을 `<계정>.github.io`로 만들면 주소가 `https://<계정>.github.io/`로 짧아집니다.
이때 주소에 들어가는 것은 **계정(또는 조직) 이름**입니다. 이 사이트는 GitHub 조직 `minholicbook`을
쓰기로 했으므로 주소는 `https://minholicbook.github.io/`, 저장소 이름도 `minholicbook.github.io`입니다.

## 파일 구성

| 파일 | 용도 |
|---|---|
| `index.html` | 홈페이지 본체 (HTML + CSS + JS 인라인) |
| `images/logo-mark.png` | 원피스 마크 (투명). 헤더·OG·아이콘 |
| `images/logo.png` | 마크 + 민홀릭 (투명). 소개 섹션 |
| `images/logo-silhouette.png` | 16px 파비콘 전용 실루엣 |
| `images/minholic-neon.jpg` | 네온 로고. 소개 섹션의 유튜브 채널 타일 |
| `images/cover-*.jpg` | 도서 표지 4종. 히어로와 도서 카드에서 씁니다 |
| `minholic_logo1/2.jpg` | 원본 로고. 페이지에서 직접 쓰지 않고 위 파생 파일을 씁니다 |
| `favicon-16/32/48.png` | 파비콘. 16px만 실루엣, 나머지는 마크 |
| `apple-touch-icon.png` | iOS 홈 화면 아이콘 (180×180) |
| `og.png` | 카카오톡·트위터 등에 링크를 붙일 때 뜨는 미리보기 (1200×630) |
| `tools/make-og.py` | 위 `og.png`·파비콘을 다시 굽는 스크립트. 페이지 빌드와는 무관합니다 |
| `CHANGELOG.md` | 날짜별 수정 내역 |
| `CLAUDE.md` | 디자인 규칙·결정 사항·주의할 함정 |

> 사이트 주소는 `https://minholicbook.github.io/`로 확정되어 `index.html` `<head>`의 절대 URL
> 3곳(`canonical`, `og:url`, `og:image`)에 이미 반영돼 있습니다. **나중에 커스텀 도메인을 붙이면**
> 이 3곳을 다시 새 주소로 바꿔야 합니다. `og:image`는 상대 경로가 통하지 않아 반드시 절대 URL이어야 합니다.

## 도메인 연결 (선택)

1. 저장소 루트에 `CNAME` 파일을 만들고 도메인만 한 줄 적습니다. 예: `minholic.co.kr`
2. 도메인 등록업체 DNS에서
   - 루트 도메인: A 레코드 4개 → `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - www: CNAME → `<계정>.github.io`
3. Settings → Pages에서 `Enforce HTTPS` 체크

## 내용 수정 위치

| 항목 | 찾을 위치 |
|---|---|
| 히어로 표지·문구 | `<figure class="artboard sheet">` 의 `<img>` 와 그 옆 `<h1>`·`<dl class="specs">` |
| 도서 카드 | `<section id="books">` 안의 `<a class="artboard book">` 블록 복사 |
| 도서 표지 | 각 카드 안 첫 `<img class="cover">` |
| 소식 목록 | `<section id="news">` 안의 `<a>` 블록 |
| 연락처 | `<div class="artboard contact">` 안의 `<dl>` |
| 색상 | 최상단 `:root` 의 `--red`, `--green`, `--wash` 등 |
| 사이트 주소 | `<head>` 의 `canonical`, `og:url`, `og:image` |

## 남은 작업

- 연락처는 메일·카카오톡 채널(CHAT)·유튜브·네이버 카페(STUDY) 4개로 확정했습니다. 전화번호·주소는 노출하지 않습니다.
- 도서 4종은 실제 목록이고 소개문도 실제 내용입니다. 다만 03·04(컬러링 북)의 ISBN·발행년도는
  아직 확인하지 못해 `.meta` 행을 넣지 않았습니다.
- 02는 2026-09-11에 신간 『비즈니스 엑셀 & 파워포인트』로 **교체**했습니다. 옛
  『패션실무를 위한 비즈니스 엑셀』은 목록에서 내려갔습니다 (정보는 CLAUDE.md에 남겨 뒀습니다).
- 도서 카드의 카페 링크 4개는 모두 실제 글 주소입니다 (01·03·04는 열리는 것을 확인했고,
  02는 사용자가 알려준 주소입니다).
- 소식 3건은 가상 샘플(`href="#"`)입니다 — 섹션 자체를 유지할지 고민 중입니다.
- 색을 바꿀 때는 `:root` 토큰만 고치면 됩니다. 단 `og.png`와 아이콘 PNG 4개는
  구워진 이미지라 따로 다시 만들어야 합니다 — 스크립트 안의 색 상수도 같이 고친 뒤
  아래 명령을 실행하세요 (Pillow 필요, 윈도우 전용).

  ```bash
  python tools/make-og.py
  ```
- 영문은 모두 대문자, 고딕으로 씁니다 (이메일·유튜브 핸들은 예외).
