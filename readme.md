# AI Stock 예측 프로젝트
이 저장소는 웹 서비스 파트만을 다루는 저장소입니다.

# 필요한 라이브러리
* django (asgiref, pytz, sqlparse 포함됨)
* mysqlclient


# 셋팅

# 구성
## 폴더 구성
기본 구성
* config : 설정
* templates : front-end (view) 
* static : css, js, images 등

추가된 구성
* stock : 주가 종목 정보


## URL 구성
* /admin/ : 사이트 관리자
* /portfolios/ : 포트폴리오 기능
** /portfolios/{portfolioId}/
* /stocks/{stockId}
* /equities/{종목명} : (예) /equities/samsung~




## 서비스 구성
Account(유저 정보 기능)
* 회원가입/탈퇴, 로그인/로그아웃, 정보변경


Admin(관리자 기능)
* 


메인 페이지
* 코스피 정보
* 최근 뉴스


포트폴리오 관리
* 포트폴리오 추천 기준 선택
* 포트폴리오 목록 관리 : 포트폴리오 추가/삭제/이름 변경
* 포트폴리오의 종목 관리
  * 종목 추가/삭제
    

주식 종목 조회
* 주식 종목 전체 보기
* 주식 종목 검색
* 주식 종목 갱신 (새로 받아옴)


주식 가격 조회
* 주식 항목 선택 후 > 가격 조회



## 데이터베이스 구성
유저 테이블 auth_user
* id

주가 종목 테이블
* id (종목 key)
* 종목명 
* code (짧은 종목코드) : 숫자 6자리의 짧은 형태의 종목 코드.  
* expcode (긴 종목코드) : 'KR7003670007'같은 긴 형태의 종목 코드.
* is_eft (ETF 유무) : ETF 인지 여부.


주가 시세 테이블


포트폴리오 테이블 (유저 x 주가 종목)
* user_id
* 


# 용어
* 주식 stock
* 지수 indices
* 원자재 commodities
* 외환 forex
* 최근의 시세 Recent Quotes
* 투자전문기관 Market Movers
* 주식분할 stock split
* 배당 dividends
* 거래량 volume
* 매수/매도 Bid/Ask
* 금일 변동 Day's Range


* 시가 총액 : Market Cap
* 거래소 Exchange
* 기호 Symbol
* 매출 Revenue
* 평균거래량(주식수의 평균값) Average Volume : 지난 52주간 거래된 주식 수의 평균값
* 주당순이익 EPS
* 주가수익비율 P/E Ratio(PER)
* 배당수익률 Dividend Yield


* 적극 매수 Strong Buy
* 매수 Buy
* 매도 Sell
* 적극 매도 Strong Sell
* Neutral 중립


* 1년 변동률 1-Year Change
* 주당매출액 비율 Price to Sales
* 주당현금흐름 비율 Price to Cash Flow
* 주당잉여현금흐름 비율 Price to Free Cash Flow
* 주당순자산 비율 Price to Book
* 주당유형자산 비율 Price to Tangible Book

* 자산회전율 Asset Turnover
* 재고자산회전율 Inventory Turnover
* 직원당 수익 Revenue/Employee
* 종업원 일인당 순이익 Net Income/Employee
* 매출채권회전율 Receivable Turnover



기간 단위
* TTM (Trailing Twelve Months) 최근 12개월
* MRQ (Most Recent Quarter) 최근 분기 
* YOY (year over year) 지난해 대비







