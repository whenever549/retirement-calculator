
# 은퇴 자금 계산기 - 시작 월 저축액 보정 방식 적용

def calculate_retirement_fv(start_monthly, inflation_rate=0.07, return_rate=0.07, years=28):
    fv = 0
    for year in range(years):
        monthly_saving = start_monthly * ((1 + inflation_rate) ** year)
        for m in range(12):
            months_left = (years - year - 1) * 12 + (12 - m)
            fv += monthly_saving * ((1 + return_rate / 12) ** months_left)
    return fv

def find_optimal_start_saving(target_fv, inflation_rate=0.07, return_rate=0.07, years=28):
    best_guess = 0
    min_diff = float('inf')
    for guess in range(850_000, 1_200_000, 1000):
        fv = calculate_retirement_fv(guess, inflation_rate, return_rate, years)
        diff = abs(fv - target_fv)
        if diff < min_diff:
            min_diff = diff
            best_guess = guess
    return best_guess

if __name__ == "__main__":
    # 목표 은퇴자금 (순현가치 3.3억을 28년 후로 명목 변환)
    target_fv = 3_300_000_000 * ((1 + 0.07) ** 28)  # 약 21.94억

    # 적정 시작 월 저축액 찾기
    optimal_start = find_optimal_start_saving(target_fv)
    print(f"\n[추천 시작 월 저축액]: {optimal_start:,}원")
    
    # 도달 가능한 미래가치 확인
    final_fv = calculate_retirement_fv(optimal_start)
    print(f"[2053년 도달 예상 금액]: {round(final_fv):,}원")
