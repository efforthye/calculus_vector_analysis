# 부분 적분법 (Integration by Parts)

## 기본 공식
`
integral of u dv = uv - integral of v du
`

## LIATE 규칙

u를 선택하는 우선순위:

- Logarithmic (로그함수): ln(x), log(x)
- Inverse trigonometric (역삼각함수): arcsin(x), arccos(x)
- Algebraic (다항함수): x, x^2, x^3
- Trigonometric (삼각함수): sin(x), cos(x)
- Exponential (지수함수): e^x, a^x

## 주요 예시

- 다항함수 × 지수함수
`
integral of x * e^x dx = e^x(x - 1) + C
`

- 다항함수 × 삼각함수
`
integral of x * sin(x) dx = -x*cos(x) + sin(x) + C
`

- 로그함수 (중요!)
`
integral of ln(x) dx = x(ln(x) - 1) + C
`
