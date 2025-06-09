# 치환 적분법 (Substitution Integration)
# 실행 방법: python src/calculus/substitution_integration/substitution.py

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import sympy as sp

# 치환 적분법 (Substitution Integration)
# u-substitution method for integration

def substitution_example1():
    print("\n# 예시 1: integral of 2x(x^2+1)^3 dx")
    print("u = x^2 + 1로 치환")
    print("du = 2x dx")
    print("integral of 2x(x^2+1)^3 dx = integral of u^3 du = u^4/4 + C = (x^2+1)^4/4 + C")
    
    # sympy로 해석적 계산
    x = sp.Symbol('x')
    expr = 2*x*(x**2 + 1)**3
    integral_result = sp.integrate(expr, x)
    print(f"SymPy 결과: {integral_result}")
    
    # 수치적 검증 (x=2에서)
    x_val = 2
    original = 2 * x_val * (x_val**2 + 1)**3
    antiderivative = (x_val**2 + 1)**4 / 4
    
    print(f"x={x_val}일 때:")
    print(f"피적분함수 값: {original}")
    print(f"원함수 값: {antiderivative}")

def substitution_example2():
    print("\n# 예시 2: integral of sin(3x) dx")
    print("u = 3x로 치환")
    print("du = 3 dx, dx = du/3")
    print("integral of sin(3x) dx = integral of sin(u) * (1/3) du = -cos(u)/3 + C = -cos(3x)/3 + C")
    
    # sympy로 해석적 계산
    x = sp.Symbol('x')
    expr = sp.sin(3*x)
    integral_result = sp.integrate(expr, x)
    print(f"SymPy 결과: {integral_result}")
    
    # 수치적 검증
    x_val = np.pi / 6
    original = np.sin(3 * x_val)
    antiderivative = -np.cos(3 * x_val) / 3
    
    print(f"x={x_val:.4f}일 때:")
    print(f"피적분함수 값: {original:.4f}")
    print(f"원함수 값: {antiderivative:.4f}")

def substitution_example3():
    print("\n# 예시 3: integral of x/(x^2+1) dx")
    print("u = x^2 + 1로 치환")
    print("du = 2x dx, x dx = du/2")
    print("integral of x/(x^2+1) dx = integral of (1/u) * (1/2) du = (1/2)ln|u| + C = (1/2)ln(x^2+1) + C")
    
    # sympy로 해석적 계산
    x = sp.Symbol('x')
    expr = x / (x**2 + 1)
    integral_result = sp.integrate(expr, x)
    print(f"SymPy 결과: {integral_result}")
    
    # 수치적 검증
    x_val = 3
    original = x_val / (x_val**2 + 1)
    antiderivative = 0.5 * np.log(x_val**2 + 1)
    
    print(f"x={x_val}일 때:")
    print(f"피적분함수 값: {original:.4f}")
    print(f"원함수 값: {antiderivative:.4f}")

def substitution_patterns():
    print("\n# 치환적분법의 주요 패턴들")
    print("1. integral of f'(x) * [f(x)]^n dx = [f(x)]^(n+1)/(n+1) + C")
    print("2. integral of f'(x)/f(x) dx = ln|f(x)| + C")
    print("3. integral of f'(x) * e^(f(x)) dx = e^(f(x)) + C")
    print("4. integral of f'(x) * sin(f(x)) dx = -cos(f(x)) + C")
    print("5. integral of f'(x) * cos(f(x)) dx = sin(f(x)) + C")

def definite_integral_substitution():
    print("\n# 정적분에서의 치환적분법")
    print("integral from 0 to 1 of 2x(x^2+1)^3 dx")
    print("u = x^2 + 1로 치환")
    print("x=0일 때 u=1, x=1일 때 u=2")
    print("integral from 1 to 2 of u^3 du = [u^4/4] from 1 to 2 = 16/4 - 1/4 = 15/4")
    
    result = 15/4
    print(f"해석적 결과: {result}")
    
    # scipy로 수치적 검증
    def f(x):
        return 2 * x * (x**2 + 1)**3
    
    numerical_result, error = integrate.quad(f, 0, 1)
    print(f"수치적 검증: {numerical_result:.4f}")
    print(f"오차: {abs(result - numerical_result):.8f}")

def plot_substitution_example():
    x = np.linspace(0, 2, 1000)
    y = 2 * x * (x**2 + 1)**3
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b-', linewidth=2, label='f(x) = 2x(x^2+1)^3')
    plt.fill_between(x, 0, y, alpha=0.3, color='blue')
    plt.grid(True, alpha=0.3)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('치환적분 예시: 2x(x^2+1)^3')
    plt.legend()
    plt.show()

def run_substitution_examples():
    print("# 치환 적분법 (Substitution Integration)")
    substitution_example1()
    substitution_example2()
    substitution_example3()
    substitution_patterns()
    definite_integral_substitution()
    
    # 그래프 그리기 (선택적)
    try:
        plot_substitution_example()
    except:
        print("그래프를 표시할 수 없습니다. matplotlib 설정을 확인하세요.")

if __name__ == "__main__":
    run_substitution_examples()
