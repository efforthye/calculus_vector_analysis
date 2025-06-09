# 치환 적분법 (Substitution Integration)

## 기본 공식
`
integral of f(g(x)) * g'(x) dx = integral of f(u) du (단, u = g(x))
`

## 주요 패턴

- Power Rule 결합
`
integral of f'(x) * [f(x)]^n dx = [f(x)]^(n+1)/(n+1) + C
`

- 로그함수
`
integral of f'(x)/f(x) dx = ln|f(x)| + C
`

- 삼각함수
`
integral of f'(x) * sin(f(x)) dx = -cos(f(x)) + C
integral of f'(x) * cos(f(x)) dx = sin(f(x)) + C
`

## 정적분에서의 치환
`
integral from a to b of f(g(x))*g'(x) dx = integral from g(a) to g(b) of f(u) du
`
