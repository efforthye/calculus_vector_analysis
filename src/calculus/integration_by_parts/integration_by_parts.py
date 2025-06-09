# 부분 적분법 (Integration by Parts)
# 실행 방법: python src/calculus/integration_by_parts/integration_by_parts.py

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import sympy as sp

# 부분 적분법 (Integration by Parts)
# integral of u dv = uv - integral of v du

def integration_by_parts_example1():
    """
    예시 1: integral of x*e^x dx
    u = x, dv = e^x dx
    du = dx, v = e^x
    """
    print("=== 예시 1: integral of x*e^x dx ===")
    print("u = x, dv = e^x dx")
    print("du = dx, v = e^x")
    print("integral of x*e^x dx = x*e^x - integral of e^x dx = x*e^x - e^x + C = e^x(x-1) + C")
    
    # sympy로 해석적 계산
    x = sp.Symbol('x')
    expr = x * sp.exp(x)
    integral_result = sp.integrate(expr, x)
    print(f"SymPy 결과: {integral_result}")
    
    # 수치적 검증 (x=1에서)
    x_val = 1
    original = x_val * np.exp(x_val)
    antiderivative = np.exp(x_val) * (x_val - 1)
    
    print(f"x={x_val}일 때:")
    print(f"피적분함수 값: {original:.4f}")
    print(f"원함수 값: {antiderivative:.4f}")

def integration_by_parts_example2():
    """
    예시 2: integral of x*sin(x) dx
    u = x, dv = sin(x) dx
    du = dx, v = -cos(x)
    """
    print("\n=== 예시 2: integral of x*sin(x) dx ===")
    print("u = x, dv = sin(x) dx")
    print("du = dx, v = -cos(x)")
    print("integral of x*sin(x) dx = x*(-cos(x)) - integral of (-cos(x)) dx")
    print("= -x*cos(x) + integral of cos(x) dx = -x*cos(x) + sin(x) + C")
    
    # sympy로 해석적 계산
    x = sp.Symbol('x')
    expr = x * sp.sin(x)
    integral_result = sp.integrate(expr, x)
    print(f"SymPy 결과: {integral_result}")
    
    # 수치적 검증
    x_val = np.pi / 4
    original = x_val * np.sin(x_val)
    antiderivative = -x_val * np.cos(x_val) + np.sin(x_val)
    
    print(f"x={x_val:.4f}일 때:")
    print(f"피적분함수 값: {original:.4f}")
    print(f"원함수 값: {antiderivative:.4f}")

def integration_by_parts_example3():
    """
    예시 3: integral of ln(x) dx (중요한 예시)
    u = ln(x), dv = dx
    du = (1/x) dx, v = x
    """
    print("\n=== 예시 3: integral of ln(x) dx ===")
    print("u = ln(x), dv = dx")
    print("du = (1/x) dx, v = x")
    print("integral of ln(x) dx = x*ln(x) - integral of x*(1/x) dx")
    print("= x*ln(x) - integral of 1 dx = x*ln(x) - x + C = x(ln(x) - 1) + C")
    
    # sympy로 해석적 계산
    x = sp.Symbol('x')
    expr = sp.log(x)
    integral_result = sp.integrate(expr, x)
    print(f"SymPy 결과: {integral_result}")
    
    # 수치적 검증
    x_val = np.e  # e에서 계산
    original = np.log(x_val)
    antiderivative = x_val * (np.log(x_val) - 1)
    
    print(f"x={x_val:.4f}일 때:")
    print(f"피적분함수 값: {original:.4f}")
    print(f"원함수 값: {antiderivative:.4f}")

def integration_by_parts_example4():
    """
    예시 4: integral of x^2*e^x dx (두 번 부분적분)
    첫 번째: u = x^2, dv = e^x dx
    두 번째: u = x, dv = e^x dx
    """
    print("\n=== 예시 4: integral of x^2*e^x dx (두 번 부분적분) ===")
    print("첫 번째 부분적분:")
    print("u = x^2, dv = e^x dx -> du = 2x dx, v = e^x")
    print("integral of x^2*e^x dx = x^2*e^x - integral of 2x*e^x dx")
    
    print("\n두 번째 부분적분 (integral of 2x*e^x dx):")
    print("u = 2x, dv = e^x dx -> du = 2 dx, v = e^x")
    print("integral of 2x*e^x dx = 2x*e^x - integral of 2*e^x dx = 2x*e^x - 2e^x")
    
    print("\n최종 결과:")
    print("integral of x^2*e^x dx = x^2*e^x - (2x*e^x - 2e^x) + C")
    print("= x^2*e^x - 2x*e^x + 2e^x + C = e^x(x^2 - 2x + 2) + C")
    
    # sympy로 해석적 계산
    x = sp.Symbol('x')
    expr = x**2 * sp.exp(x)
    integral_result = sp.integrate(expr, x)
    print(f"SymPy 결과: {integral_result}")
    
    # 수치적 검증
    x_val = 1
    original = x_val**2 * np.exp(x_val)
    antiderivative = np.exp(x_val) * (x_val**2 - 2*x_val + 2)
    
    print(f"x={x_val}일 때:")
    print(f"피적분함수 값: {original:.4f}")
    print(f"원함수 값: {antiderivative:.4f}")

def liate_rule():
    """
    LIATE 규칙 설명
    L - Logarithmic (로그함수)
    I - Inverse trigonometric (역삼각함수) 
    A - Algebraic (다항함수)
    T - Trigonometric (삼각함수)
    E - Exponential (지수함수)
    """
    print("\n=== LIATE 규칙 ===")
    print("부분적분에서 u를 선택하는 우선순위:")
    
    liate_order = [
        ("L", "Logarithmic", "ln(x), log(x)"),
        ("I", "Inverse trigonometric", "arcsin(x), arccos(x), arctan(x)"),
        ("A", "Algebraic", "x, x^2, x^3, ..."),
        ("T", "Trigonometric", "sin(x), cos(x), tan(x)"),
        ("E", "Exponential", "e^x, a^x")
    ]
    
    for letter, name, examples in liate_order:
        print(f"{letter} - {name}: {examples}")
    
    print("\n앞에 있는 것일수록 u로 선택하기 좋습니다!")

def definite_integral_by_parts():
    """
    정적분에서의 부분적분법
    예시: integral from 1 to e of ln(x) dx
    """
    print("\n=== 정적분에서의 부분적분법 ===")
    print("integral from 1 to e of ln(x) dx")
    print("= [x(ln(x) - 1)] from 1 to e")
    print("= e(ln(e) - 1) - 1(ln(1) - 1)")
    print("= e(1 - 1) - 1(0 - 1)")
    print("= 0 - (-1) = 1")
    
    result = 1
    print(f"해석적 결과: {result}")
    
    # scipy로 수치적 검증
    def f(x):
        return np.log(x)
    
    numerical_result, error = integrate.quad(f, 1, np.e)
    print(f"수치적 검증: {numerical_result:.6f}")
    print(f"오차: {abs(result - numerical_result):.8f}")

def cyclic_integration():
    """
    순환 적분 (Cyclic Integration)
    예시: integral of e^x * sin(x) dx
    """
    print("\n=== 순환 적분 예시 ===")
    print("integral of e^x * sin(x) dx")
    print("I = integral of e^x * sin(x) dx 라고 하자")
    
    print("\n첫 번째 부분적분:")
    print("u = sin(x), dv = e^x dx -> du = cos(x) dx, v = e^x")
    print("I = e^x * sin(x) - integral of e^x * cos(x) dx")
    
    print("\n두 번째 부분적분 (integral of e^x * cos(x) dx):")
    print("u = cos(x), dv = e^x dx -> du = -sin(x) dx, v = e^x")
    print("integral of e^x * cos(x) dx = e^x * cos(x) - integral of e^x * (-sin(x)) dx")
    print("= e^x * cos(x) + integral of e^x * sin(x) dx = e^x * cos(x) + I")
    
    print("\n원래 식에 대입:")
    print("I = e^x * sin(x) - (e^x * cos(x) + I)")
    print("I = e^x * sin(x) - e^x * cos(x) - I")
    print("2I = e^x * sin(x) - e^x * cos(x)")
    print("I = (e^x/2)(sin(x) - cos(x)) + C")
    
    # sympy로 확인
    x = sp.Symbol('x')
    expr = sp.exp(x) * sp.sin(x)
    integral_result = sp.integrate(expr, x)
    print(f"SymPy 확인: {integral_result}")

def plot_integration_by_parts_examples():
    """부분적분 예시들의 그래프"""
    x = np.linspace(0, 2*np.pi, 1000)
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # x * e^x
    y1 = x * np.exp(x/2)  # 너무 크지 않게 조정
    axes[0,0].plot(x, y1, 'b-', linewidth=2)
    axes[0,0].set_title('x * e^(x/2)')
    axes[0,0].grid(True, alpha=0.3)
    
    # x * sin(x)
    y2 = x * np.sin(x)
    axes[0,1].plot(x, y2, 'r-', linewidth=2)
    axes[0,1].set_title('x * sin(x)')
    axes[0,1].grid(True, alpha=0.3)
    
    # ln(x) (x > 0)
    x_ln = np.linspace(0.1, 10, 1000)
    y3 = np.log(x_ln)
    axes[1,0].plot(x_ln, y3, 'g-', linewidth=2)
    axes[1,0].set_title('ln(x)')
    axes[1,0].grid(True, alpha=0.3)
    
    # e^x * sin(x)
    y4 = np.exp(x/4) * np.sin(x)  # 너무 크지 않게 조정
    axes[1,1].plot(x, y4, 'm-', linewidth=2)
    axes[1,1].set_title('e^(x/4) * sin(x)')
    axes[1,1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

def run_integration_by_parts_examples():
    """모든 예시 실행"""
    print("=== 부분 적분법 (Integration by Parts) ===\n")
    integration_by_parts_example1()
    integration_by_parts_example2()
    integration_by_parts_example3()
    integration_by_parts_example4()
    liate_rule()
    definite_integral_by_parts()
    cyclic_integration()
    
    # 그래프 그리기 (선택적)
    try:
        plot_integration_by_parts_examples()
    except:
        print("그래프를 표시할 수 없습니다. matplotlib 설정을 확인하세요.")

if __name__ == "__main__":
    run_integration_by_parts_examples()
