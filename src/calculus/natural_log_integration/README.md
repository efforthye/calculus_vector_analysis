# 자연로그 함수의 적분 (Natural Log Integration)

## 기본 공식

- 기본 ln(x) 적분
`
integral of ln(x) dx = x(ln(x) - 1) + C
`

- 1/x의 적분 (ln의 정의)
`
integral of (1/x) dx = ln|x| + C
`

- 일반적인 1/f(x) 형태
`
integral of f'(x)/f(x) dx = ln|f(x)| + C
`

## 주요 적분 공식

- Power of ln(x)
`
integral of (ln(x))^2 dx = x((ln(x))^2 - 2ln(x) + 2) + C
`

- ln(x)와 다른 함수의 곱
`
integral of x*ln(x) dx = (x^2/4)(2ln(x) - 1) + C
integral of x^n*ln(x) dx = x^(n+1)/(n+1) * [ln(x) - 1/(n+1)] + C
`

- 특수한 ln 적분
`
integral of (ln(x))^n/x dx = (ln(x))^(n+1)/(n+1) + C
`

## 정적분 예시
`
integral from 1 to e of ln(x) dx = 1
integral from 1 to e of (1/x) dx = 1
`
