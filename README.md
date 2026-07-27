# 도서출판 민홀릭 홈페이지

정적 HTML 한 파일로 된 출판사 홈페이지입니다. 별도 빌드 과정 없이 GitHub Pages에 바로 올릴 수 있습니다.

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
이때 주소에 들어가는 것은 **계정(또는 조직) 이름**입니다. `https://minholicbooks.github.io/`를 쓰려면
`minholicbooks`라는 계정이나 조직이 있어야 하고, 저장소 이름도 `minholicbooks.github.io`여야 합니다.

## 파일 구성

| 파일 | 용도 |
|---|---|
| `index.html` | 홈페이지 본체 (HTML + CSS + JS 인라인) |
| `favicon.svg` | 파비콘. 판면 + 재단 표시 브래킷 |
| `favicon-32.png` | SVG 파비콘을 못 읽는 구형 브라우저용 폴백 |
| `apple-touch-icon.png` | iOS 홈 화면 아이콘 (180×180) |
| `og.png` | 카카오톡·트위터 등에 링크를 붙일 때 뜨는 미리보기 (1200×630) |

> **주소가 확정되면** `index.html` `<head>`의 절대 URL 3곳(`canonical`, `og:url`, `og:image`)을
> 실제 주소로 바꿔야 합니다. `og:image`는 상대 경로가 통하지 않아 반드시 절대 URL이어야 합니다.

## 도메인 연결 (선택)

1. 저장소 루트에 `CNAME` 파일을 만들고 도메인만 한 줄 적습니다. 예: `minholic.co.kr`
2. 도메인 등록업체 DNS에서
   - 루트 도메인: A 레코드 4개 → `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - www: CNAME → `<계정>.github.io`
3. Settings → Pages에서 `Enforce HTTPS` 체크

## 내용 수정 위치

| 항목 | 찾을 위치 |
|---|---|
| 판형 치수 (188 / 257) | `<svg>` 안의 `<text>` |
| 도서 카드 | `<section id="books">` 안의 `<article class="artboard book">` 블록 복사 |
| 소식 목록 | `<section id="news">` 안의 `<a>` 블록 |
| 연락처 | `<div class="artboard contact">` 안의 `<dl>` |
| 색상 | 최상단 `:root` 의 `--red`, `--blue` 등 |
| 사이트 주소 | `<head>` 의 `canonical`, `og:url`, `og:image` |

## 남은 작업

- 연락처(전화·메일·주소)가 `000-0000-0000`, `hello@example.com` 등 임시값입니다.
- 도서 02·03은 샘플입니다. 실제 목록으로 교체하세요.
- 소식 항목의 `href="#"`를 실제 링크(카페 글 등)로 바꾸면 바로 동작합니다.
- 표지 이미지를 넣으려면 `images/` 폴더를 만들고 카드 안에 `<img>`를 추가하면 됩니다.
- 사이트 주소 확정 후 `<head>`의 절대 URL 3곳을 교체해야 소셜 공유 미리보기가 뜹니다.
