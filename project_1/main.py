from datetime import datetime, timedelta
# datetime:
# 날짜와 시간을 다루는 파이썬 내장 클래스
# 문자열 형태의 날짜를 실제 날짜 객체로 변환할 때 사용

# timedelta:
# 날짜끼리 더하거나 빼서 기간 계산할 때 사용
# 하루씩 증가시키는 기능 등에 사용

print("=== 카카오테크 부트캠프 출석 계산기 ===")

# 전체 교육 기간
BOOTCAMP_START = "2025-05-12"
BOOTCAMP_END = "2025-11-17"

# 단위기간 정보
unit_periods = [
    {"name": "1단위기간", "start": "2025-05-12", "end": "2025-06-11"},
    {"name": "2단위기간", "start": "2025-06-12", "end": "2025-07-11"},
    {"name": "3단위기간", "start": "2025-07-12", "end": "2025-08-11"},
    {"name": "4단위기간", "start": "2025-08-12", "end": "2025-09-11"},
    {"name": "5단위기간", "start": "2025-09-12", "end": "2025-10-11"},
    {"name": "6단위기간", "start": "2025-10-12", "end": "2025-11-11"},
    {"name": "7단위기간", "start": "2025-11-12", "end": "2025-11-17"},
]

# 휴강 및 공휴일
holidays = [
    "2025-05-25",
    "2025-06-03",
    "2025-06-26",
    "2025-07-17",
    "2025-08-13",
    "2025-08-14",
    "2025-08-17",
    "2025-09-24",
    "2025-09-25",
    "2025-10-05",
    "2025-10-09",
]

# 문자열로 된 휴강일을 datetime.date 객체로 변환하여 리스트에 저장
holiday_dates = [
    datetime.strptime(day, "%Y-%m-%d").date() for day in holidays
]

# 날짜 문자열을 datetime.date 객체로 변환하는 함수
def to_date(date_string):
    return datetime.strptime(date_string, "%Y-%m-%d").date()

# 두 날짜 사이의 실제 수업일 수를 계산하는 함수
def count_class_days(start, end):
    count = 0
    current = start

    # 6월 13일까지는 토요일도 수업
    saturday_class_end = to_date("2025-06-13")

    while current <= end:
        is_weekday = current.weekday() < 5
        is_saturday_class_period = (
            current.weekday() == 5 and current <= saturday_class_end
        )

        if (is_weekday or is_saturday_class_period) and current not in holiday_dates:
            count += 1

        current += timedelta(days=1)

    return count


# 입력한 날짜가 어느 단위기간에 속하는지 찾는 함수
def find_current_period(today):
    for period in unit_periods:
        start = to_date(period["start"])
        end = to_date(period["end"])

        if start <= today <= end:
            return period

    return None

# 사용자로부터 오늘 날짜 입력 받기
today_input = input("오늘 날짜를 입력하세요 (YYYY-MM-DD): ")
today = to_date(today_input)

# 전체 교육 기간과 단위기간의 날짜를 datetime.date 객체로 변환
bootcamp_start = to_date(BOOTCAMP_START)
bootcamp_end = to_date(BOOTCAMP_END)

current_period = find_current_period(today)

# 입력한 날짜가 전체 교육 기간에 포함되는지 확인
if current_period is None:
    print("\n입력한 날짜가 부트캠프 교육 기간에 포함되지 않습니다.")
    print("교육 기간:", BOOTCAMP_START, "~", BOOTCAMP_END)

else:
    total_class_days = count_class_days(bootcamp_start, bootcamp_end)
    passed_class_days = count_class_days(bootcamp_start, today)
    remaining_class_days = total_class_days - passed_class_days

    current_period_start = to_date(current_period["start"])
    current_period_end = to_date(current_period["end"])

    current_period_total_days = count_class_days(
        current_period_start,
        current_period_end
    )

    current_period_passed_days = count_class_days(
        current_period_start,
        today
    )

    # 사용자로부터 출석 기록 입력 받기
    print("\n=== 출석 기록 입력 ===")
    absence = int(input("전체 결석 횟수 입력: "))
    late = int(input("전체 지각 횟수 입력: "))
    early_leave = int(input("전체 조퇴 횟수 입력: "))
    outing = int(input("전체 외출 횟수 입력: "))

    # 사용자로부터 현재 단위기간 출석 기록 입력 받기
    print("\n=== 현재 단위기간 출석 기록 입력 ===")
    unit_absence = int(input("현재 단위기간 결석 횟수 입력: "))
    unit_late = int(input("현재 단위기간 지각 횟수 입력: "))
    unit_early_leave = int(input("현재 단위기간 조퇴 횟수 입력: "))
    unit_outing = int(input("현재 단위기간 외출 횟수 입력: "))

    # 전체 출석 계산
    penalty_count = late + early_leave + outing
    converted_absence = penalty_count // 3
    total_absence = absence + converted_absence

    attended_days = passed_class_days - total_absence
    total_attendance_rate = (attended_days / passed_class_days) * 100

    # 단위기간 출석 계산
    unit_penalty_count = unit_late + unit_early_leave + unit_outing
    unit_converted_absence = unit_penalty_count // 3
    unit_total_absence = unit_absence + unit_converted_absence

    unit_attended_days = current_period_passed_days - unit_total_absence
    unit_attendance_rate = (unit_attended_days / current_period_passed_days) * 100

    # 결과 출력
    print("\n==============================")
    print("        출석 계산 결과")
    print("==============================")

    print("\n[교육 기간 정보]")
    print("전체 교육 기간:", BOOTCAMP_START, "~", BOOTCAMP_END)
    print("총 실제 수업일 수:", total_class_days, "일")
    print("현재까지 진행된 실제 수업일 수:", passed_class_days, "일")
    print("남은 실제 수업일 수:", remaining_class_days, "일")

    print("\n[현재 단위기간 정보]")
    print("현재 단위기간:", current_period["name"])
    print("단위기간:", current_period["start"], "~", current_period["end"])
    print("현재 단위기간 전체 수업일 수:", current_period_total_days, "일")
    print("현재 단위기간 진행 수업일 수:", current_period_passed_days, "일")

    print("\n[전체 출석 정보]")
    print("직접 결석:", absence, "회")
    print("지각:", late, "회")
    print("조퇴:", early_leave, "회")
    print("외출:", outing, "회")
    print("지각/조퇴/외출 누적:", penalty_count, "회")
    print("누적에 따른 결석 처리:", converted_absence, "일")
    print("최종 결석 처리 일수:", total_absence, "일")
    print("전체 출석률:", round(total_attendance_rate, 2), "%")

    print("\n[현재 단위기간 출석 정보]")
    print("단위기간 결석:", unit_absence, "회")
    print("단위기간 지각:", unit_late, "회")
    print("단위기간 조퇴:", unit_early_leave, "회")
    print("단위기간 외출:", unit_outing, "회")
    print("단위기간 최종 결석 처리 일수:", unit_total_absence, "일")
    print("단위기간 출석률:", round(unit_attendance_rate, 2), "%")

    print("\n==============================")
    print("        판정 결과")
    print("==============================")

    if unit_attendance_rate < 50:
        print("단위기간 출석률이 50% 미만입니다.")
        print("판정: 제적 위험")
    else:
        print("단위기간 출석률이 50% 이상입니다.")
        print("판정: 단위기간 조건 충족")

    if total_attendance_rate < 80:
        print("전체 출석률이 80% 미만입니다.")
        print("판정: 수료 불가능")
    else:
        print("전체 출석률이 80% 이상입니다.")
        print("판정: 수료 가능")