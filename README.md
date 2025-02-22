# 미국 자전거 공유 데이터 분석

## 소개
이 프로그램은 사용자가 시카고, 뉴욕시 및 워싱턴의 미국 자전거 공유 데이터를 탐색하고 분석할 수 있도록 합니다. 

사용자는 도시, 월 및 요일별로 데이터를 필터링하여 자전거 공유 사용 패턴에 대한 통찰력을 얻을 수 있습니다.

## 데이터 파일
프로그램은 다음 CSV 파일을 사용합니다:
- `chicago.csv`
- `new_york_city.csv`
- `washington.csv`

## 함수

### 1. `get_filters()`
이 함수는 사용자가 분석할 도시, 월 및 요일을 지정하도록 요청합니다. 입력값이 예상되는 값과 일치하는지 확인합니다.

**반환값:**
- `city`: 분석할 도시의 이름.
- `month`: 필터링할 월의 이름 또는 "all"로 월 필터를 적용하지 않음.
- `day`: 필터링할 요일의 이름 또는 "all"로 요일 필터를 적용하지 않음.

### 2. `load_data(city, month, day)`
이 함수는 지정된 도시의 데이터를 로드하고, 해당하는 경우 월 및 요일로 필터링합니다.

**인수:**
- `city`: 분석할 도시의 이름.
- `month`: 필터링할 월의 이름 또는 "all"로 월 필터를 적용하지 않음.
- `day`: 필터링할 요일의 이름 또는 "all"로 요일 필터를 적용하지 않음.

### 3. `time_stats(df)`
이 함수는 가장 빈번한 여행 시간에 대한 통계를 표시합니다. 포함 내용:
- 가장 일반적인 월.
- 가장 일반적인 요일.
- 가장 일반적인 시작 시간.

### 4. `station_stats(df)`
이 함수는 가장 인기 있는 역과 여행에 대한 통계를 표시합니다. 포함 내용:
- 가장 많이 사용된 시작 역.
- 가장 많이 사용된 종료 역.
- 시작 역과 종료 역의 가장 빈번한 조합.

### 5. `trip_duration_stats(df)`
이 함수는 총 여행 시간과 평균 여행 시간에 대한 통계를 표시합니다. 포함 내용:
- 총 여행 시간.
- 평균 여행 시간.

### 6. `user_stats(df)`
이 함수는 자전거 공유 사용자에 대한 통계를 표시합니다. 포함 내용:
- 사용자 유형의 수.
- 성별의 수.
- 가장 이른, 가장 최근 및 가장 일반적인 출생 연도.

### 7. `display_raw_data(df)`
이 함수는 사용자가 원시 데이터를 보고 싶어하는지 묻고, 한 번에 5행을 출력합니다.

## 실행 방법
프로그램을 실행하려면 필요한 CSV 파일이 스크립트와 동일한 디렉토리에 있는지 확인하십시오. Python 환경에서 스크립트를 실행하고, 자전거 공유 데이터를 분석하기 위해 프롬프트에 따라 진행하십시오.

## 결론
이 프로그램은 자전거 공유 데이터에 대한 포괄적인 분석을 제공하여 사용자가 여행 패턴과 사용자 인구 통계에 대한 통찰력을 얻을 수 있도록 합니다.
