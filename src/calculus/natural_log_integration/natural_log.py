# 자연로그 함수의 적분 (Natural Log Integration)
# 실행 방법: python src/calculus/natural_log_integration/natural_log.py

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import sympy as sp

# 자연로그 함수의 적분 (Natural Logarithm Integration)
# ln(x) 관련 적분들의 계산

def basic_ln_integration():
    """
    기본적인 ln(x) 적분
    integral of ln(x) dx = x*ln(x) - x + C
    부분적분법 사용: u = ln(x), dv = dx
    """
    print("=== 기본 ln(x) 적분 ===")
    print("integral of ln(x) dx")
    print("부분적분법 사용:")
    print("u = ln(x), dv = dx")
    print("du = (1/x) dx, v = x")
    print("integral of ln(x) dx = x*ln(x) - integral of x*(1/x) dx")
    print("= x*ln(x) - integral of 1 dx = x*ln(x) - x + C")
    print("= x(ln(x) - 1) + C")
    
    # sympy로 확인
    x = sp.Symbol('x')
    expr = sp.log(x)
    result = sp.integrate(expr, x)
    print(f"SymPy 결과: {result}")
    
    # 수치적 검증
    x_val = np.e
    original = np.log(x_val)
    antiderivative = x_val * (np.log(x_val) - 1)
    
    print(f"\nx = e = {x_val:.4f}일 때:")
    print(f"ln(x) = {original:.4f}")
    print(f"원함수 값: {antiderivative:.4f}")

def power_of_ln_integration():
    """(ln(x))^n 형태의 적분들"""
    print("\n=== (ln(x))^n 적분 ===")
    
    x = sp.Symbol('x')
    
    # (ln(x))^2 적분
    print("1. integral of (ln(x))^2 dx")
    expr2 = sp.log(x)**2
    result2 = sp.integrate(expr2, x)
    print(f"SymPy 결과: {result2}")
    
    print("부분적분법 반복 사용:")
    print("u = (ln(x))^2, dv = dx")
    print("du = 2*ln(x)*(1/x) dx, v = x")
    print("integral of (ln(x))^2 dx = x*(ln(x))^2 - integral of x*2*ln(x)*(1/x) dx")
    print("= x*(ln(x))^2 - 2*integral of ln(x) dx")
    print("= x*(ln(x))^2 - 2*x*(ln(x) - 1) + C")
    print("= x*((ln(x))^2 - 2*ln(x) + 2) + C")
    
    # (ln(x))^3 적분
    print("\n2. integral of (ln(x))^3 dx")
    expr3 = sp.log(x)**3
    result3 = sp.integrate(expr3, x)
    print(f"SymPy 결과: {result3}")
    
    # 일반적인 공식
    print("\n일반적인 공식:")
    print("integral of (ln(x))^n dx = x*[(ln(x))^n - n*integral of (ln(x))^(n-1) dx]")

def reciprocal_integrations():
    """1/x 관련 적분들"""
    print("\n=== 1/x 관련 적분들 ===")
    
    x = sp.Symbol('x')
    
    print("1. integral of (1/x) dx = ln|x| + C")
    print("   (이것이 ln의 정의!)")
    
    expr1 = 1/x
    result1 = sp.integrate(expr1, x)
    print(f"   SymPy: {result1}")
    
    print("\n2. integral of 1/(ax + b) dx = (1/a)*ln|ax + b| + C")
    a, b = sp.symbols('a b')
    expr2 = 1/(a*x + b)
    result2 = sp.integrate(expr2, x)
    print(f"   SymPy: {result2}")
    
    print("\n3. integral of f'(x)/f(x) dx = ln|f(x)| + C")
    print("   예시: integral of (2x)/(x^2 + 1) dx = ln(x^2 + 1) + C")
    
    expr3 = 2*x/(x**2 + 1)
    result3 = sp.integrate(expr3, x)
    print(f"   SymPy: {result3}")
    
    # 수치적 예시
    x_val = 2
    example1 = 1/x_val
    antiderivative1 = np.log(abs(x_val))
    
    print(f"\nx = {x_val}에서의 예시:")
    print(f"1/x = {example1}")
    print(f"ln|x| = {antiderivative1:.4f}")

def ln_product_integrations():
    """ln과 다른 함수의 곱 적분"""
    print("\n=== ln(x)와 다른 함수의 곱 ===")
    
    x = sp.Symbol('x')
    
    # x * ln(x)
    print("1. integral of x*ln(x) dx")
    expr1 = x * sp.log(x)
    result1 = sp.integrate(expr1, x)
    print(f"SymPy 결과: {result1}")
    
    print("부분적분법: u = ln(x), dv = x dx")
    print("du = (1/x) dx, v = x^2/2")
    print("integral of x*ln(x) dx = (x^2/2)*ln(x) - integral of (x^2/2)*(1/x) dx")
    print("= (x^2/2)*ln(x) - integral of x/2 dx")
    print("= (x^2/2)*ln(x) - x^2/4 + C")
    print("= (x^2/4)*(2*ln(x) - 1) + C")
    
    # x^2 * ln(x)
    print("\n2. integral of x^2*ln(x) dx")
    expr2 = x**2 * sp.log(x)
    result2 = sp.integrate(expr2, x)
    print(f"SymPy 결과: {result2}")
    
    # x^n * ln(x) 일반 공식
    print("\n3. integral of x^n*ln(x) dx (일반 공식)")
    n = sp.Symbol('n')
    print("= x^(n+1)/(n+1) * [ln(x) - 1/(n+1)] + C")
    
    # 수치적 검증
    x_val = np.e
    original = x_val * np.log(x_val)
    antiderivative = (x_val**2/4) * (2*np.log(x_val) - 1)
    
    print(f"\nx = e에서의 검증:")
    print(f"x*ln(x) = {original:.4f}")
    print(f"원함수 값: {antiderivative:.4f}")

def definite_integrals_with_ln():
    """정적분에서의 ln 함수"""
    print("\n=== ln 함수의 정적분 ===")
    
    x = sp.Symbol('x')
    
    # integral from 1 to e of ln(x) dx
    print("1. integral from 1 to e of ln(x) dx")
    result1 = sp.integrate(sp.log(x), (x, 1, sp.E))
    print(f"SymPy 결과: {result1}")
    
    print("= [x*(ln(x) - 1)] from 1 to e")
    print("= e*(ln(e) - 1) - 1*(ln(1) - 1)")
    print("= e*(1 - 1) - 1*(0 - 1)")
    print("= 0 - (-1) = 1")
    
    # integral from 1 to e of (1/x) dx
    print("\n2. integral from 1 to e of (1/x) dx")
    result2 = sp.integrate(1/x, (x, 1, sp.E))
    print(f"SymPy 결과: {result2}")
    
    print("= [ln(x)] from 1 to e")
    print("= ln(e) - ln(1) = 1 - 0 = 1")
    
    # 수치적 검증
    def numerical_integration(f, a, b, n=1000):
        dx = (b - a) / n
        x_vals = np.linspace(a + dx/2, b - dx/2, n)
        return np.sum(f(x_vals)) * dx
    
    result1_num = numerical_integration(lambda x: np.log(x), 1, np.e)
    result2_num = numerical_integration(lambda x: 1/x, 1, np.e)
    
    print(f"\n수치적 검증:")
    print(f"integral from 1 to e of ln(x) dx = {result1_num:.6f}")
    print(f"integral from 1 to e of (1/x) dx = {result2_num:.6f}")

def special_ln_integrals():
    """특수한 ln 적분들"""
    print("\n=== 특수한 ln 적분들 ===")
    
    x = sp.Symbol('x')
    
    print("1. integral of ln(x + sqrt(x^2 + a^2)) dx")
    print("   (이것은 역쌍곡함수 관련)")
    
    print("\n2. integral of ln(sin(x)) dx")
    print("   (매우 복잡한 적분, 특수함수 필요)")
    
    print("\n3. integral of ln|x^2 - a^2| dx")
    print("   (부분분수 분해 후 적분)")
    
    print("\n4. integral of (ln(x))^2/x dx")
    print("   치환적분: u = ln(x), du = (1/x) dx")
    expr4 = sp.log(x)**2 / x
    result4 = sp.integrate(expr4, x)
    print(f"   = integral of u^2 du = u^3/3 + C = (ln(x))^3/3 + C")
    print(f"   SymPy: {result4}")
    
    print("\n5. integral of (ln(x))^n/x dx (일반)")
    print("   = (ln(x))^(n+1)/(n+1) + C")

def ln_differentiation_integration_relation():
    """ln의 미분과 적분 관계"""
    print("\n=== ln의 미분과 적분 관계 ===")
    
    x = sp.Symbol('x')
    
    print("미분:")
    ln_x = sp.log(x)
    ln_derivative = sp.diff(ln_x, x)
    print(f"d/dx[ln(x)] = {ln_derivative}")
    
    f = sp.Function('f')(x)
    ln_f = sp.log(f)
    ln_f_derivative = sp.diff(ln_f, x)
    print(f"d/dx[ln(f(x))] = {ln_f_derivative}")
    
    print("\n적분:")
    reciprocal = 1/x
    reciprocal_integral = sp.integrate(reciprocal, x)
    print(f"integral of (1/x) dx = {reciprocal_integral}")
    print("integral of f'(x)/f(x) dx = ln|f(x)| + C")
    
    print("\n이 관계는 미적분학의 기본정리를 보여줍니다:")
    print("미분과 적분은 서로 역연산입니다!")
    
    # 수치적 검증
    x_val = 3
    step = 0.0001
    
    # 수치 미분으로 ln'(x) 근사
    numerical_derivative = (np.log(x_val + step) - np.log(x_val)) / step
    analytical_derivative = 1/x_val
    
    print(f"\nx = {x_val}에서의 검증:")
    print(f"수치 미분: {numerical_derivative:.6f}")
    print(f"해석적 미분: {analytical_derivative:.6f}")
    print(f"오차: {abs(numerical_derivative - analytical_derivative):.8f}")

def plot_ln_functions():
    """ln 관련 함수들의 그래프"""
    x = np.linspace(0.1, 5, 1000)
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # ln(x)
    y1 = np.log(x)
    axes[0,0].plot(x, y1, 'b-', linewidth=2, label='ln(x)')
    axes[0,0].axhline(y=0, color='k', linestyle='-', alpha=0.3)
    axes[0,0].axvline(x=1, color='r', linestyle='--', alpha=0.5, label='x=1')
    axes[0,0].set_title('ln(x)')
    axes[0,0].grid(True, alpha=0.3)
    axes[0,0].legend()
    
    # 1/x
    y2 = 1/x
    axes[0,1].plot(x, y2, 'r-', linewidth=2, label='1/x')
    axes[0,1].set_title('1/x (ln의 도함수)')
    axes[0,1].grid(True, alpha=0.3)
    axes[0,1].legend()
    
    # x*ln(x)
    y3 = x * np.log(x)
    axes[1,0].plot(x, y3, 'g-', linewidth=2, label='x*ln(x)')
    axes[1,0].set_title('x*ln(x)')
    axes[1,0].grid(True, alpha=0.3)
    axes[1,0].legend()
    
    # (ln(x))^2
    y4 = np.log(x)**2
    axes[1,1].plot(x, y4, 'm-', linewidth=2, label='(ln(x))^2')
    axes[1,1].set_title('(ln(x))^2')
    axes[1,1].grid(True, alpha=0.3)
    axes[1,1].legend()
    
    plt.tight_layout()
    plt.show()

def run_natural_log_integration_examples():
    """모든 예시 실행"""
    print("=== 자연로그 함수의 적분 (Natural Log Integration) ===\n")
    basic_ln_integration()
    power_of_ln_integration()
    reciprocal_integrations()
    ln_product_integrations()
    definite_integrals_with_ln()
    special_ln_integrals()
    ln_differentiation_integration_relation()
    
    # 그래프 그리기 (선택적)
    try:
        plot_ln_functions()
    except:
        print("그래프를 표시할 수 없습니다. matplotlib 설정을 확인하세요.")

if __name__ == "__main__":
    run_natural_log_integration_examples()
