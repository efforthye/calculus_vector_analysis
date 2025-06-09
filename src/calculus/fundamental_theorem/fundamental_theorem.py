# 미적분학의 기본정리 (Fundamental Theorem of Calculus)
# 실행 방법: python src/calculus/fundamental_theorem/fundamental_theorem.py

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import sympy as sp

# 미적분학의 기본정리 (Fundamental Theorem of Calculus)
# 미분과 적분의 역관계를 보여주는 핵심 정리

def fundamental_theorem_part1():
    """
    미적분학의 기본정리 제1법칙
    d/dx integral from a to x of f(t) dt = f(x)
    """
    print("=== 미적분학의 기본정리 제1법칙 ===")
    print("d/dx integral from a to x of f(t) dt = f(x)")
    print("\n즉, 정적분의 상한을 미분하면 피적분함수가 나옵니다!")
    
    t, x = sp.symbols('t x')
    
    # 예시 1: d/dx integral from 0 to x of t^2 dt
    print("\n예시 1: d/dx integral from 0 to x of t^2 dt")
    
    # 먼저 적분 계산
    f_t = t**2
    integral_result = sp.integrate(f_t, (t, 0, x))
    print(f"integral from 0 to x of t^2 dt = {integral_result}")
    
    # 그 다음 x에 대해 미분
    derivative_result = sp.diff(integral_result, x)
    print(f"d/dx of above = {derivative_result}")
    print(f"원래 함수 f(x) = x^2와 같음을 확인!")
    
    # 예시 2: d/dx integral from 1 to x of 1/t dt
    print("\n예시 2: d/dx integral from 1 to x of (1/t) dt")
    f_t2 = 1/t
    integral_result2 = sp.integrate(f_t2, (t, 1, x))
    print(f"integral from 1 to x of (1/t) dt = {integral_result2}")
    
    derivative_result2 = sp.diff(integral_result2, x)
    print(f"d/dx of above = {derivative_result2}")
    print(f"원래 함수 f(x) = 1/x와 같음을 확인!")

def fundamental_theorem_part2():
    """
    미적분학의 기본정리 제2법칙
    integral from a to b of f(x) dx = F(b) - F(a)
    여기서 F'(x) = f(x)
    """
    print("\n=== 미적분학의 기본정리 제2법칙 ===")
    print("integral from a to b of f(x) dx = F(b) - F(a)")
    print("여기서 F'(x) = f(x) (F는 f의 원함수)")
    
    x = sp.Symbol('x')
    
    # 예시 1: integral from 0 to 1 of x^2 dx
    print("\n예시 1: integral from 0 to 1 of x^2 dx")
    f_x = x**2
    F_x = sp.integrate(f_x, x)  # 원함수 구하기
    print(f"f(x) = {f_x}")
    print(f"F(x) = {F_x} + C")
    
    # 정적분 계산
    definite_integral = sp.integrate(f_x, (x, 0, 1))
    print(f"integral from 0 to 1 of x^2 dx = {definite_integral}")
    
    # F(b) - F(a) 계산
    F_1 = (1**3)/3
    F_0 = (0**3)/3
    manual_calc = F_1 - F_0
    print(f"F(1) - F(0) = {F_1} - {F_0} = {manual_calc}")
    print("두 결과가 같음을 확인!")
    
    # 예시 2: integral from 1 to e of (1/x) dx
    print("\n예시 2: integral from 1 to e of (1/x) dx")
    f_x2 = 1/x
    F_x2 = sp.integrate(f_x2, x)
    print(f"f(x) = {f_x2}")
    print(f"F(x) = {F_x2} + C")
    
    definite_integral2 = sp.integrate(f_x2, (x, 1, sp.E))
    print(f"integral from 1 to e of (1/x) dx = {definite_integral2}")
    
    # ln(e) - ln(1) = 1 - 0 = 1
    manual_calc2 = np.log(np.e) - np.log(1)
    print(f"ln(e) - ln(1) = {manual_calc2}")

def derivative_integral_relationship():
    """미분과 적분의 역관계"""
    print("\n=== 미분과 적분의 역관계 ===")
    
    x = sp.Symbol('x')
    
    # 함수들과 그 미분/적분
    functions = [
        (x**3, "x^3"),
        (sp.sin(x), "sin(x)"),
        (sp.exp(x), "e^x"),
        (sp.log(x), "ln(x)")
    ]
    
    print("함수 -> 미분 -> 적분 -> 원래 함수")
    print("-" * 50)
    
    for func, name in functions:
        derivative = sp.diff(func, x)
        back_to_original = sp.integrate(derivative, x)
        
        print(f"{name} -> {derivative} -> {back_to_original} + C")
        
        # 차이 확인 (상수항 제외)
        difference = sp.simplify(func - back_to_original)
        print(f"   차이: {difference} (상수항)")
        print()

def numerical_verification():
    """기본정리의 수치적 검증"""
    print("=== 수치적 검증 ===")
    
    # 함수 정의: f(x) = x^2
    def f(x):
        return x**2
    
    def F(x):  # f의 원함수
        return x**3 / 3
    
    # 구간 [0, 2]에서 검증
    a, b = 0, 2
    
    # 방법 1: 수치적 적분
    numerical_integral, _ = integrate.quad(f, a, b)
    
    # 방법 2: 기본정리 사용
    fundamental_theorem_result = F(b) - F(a)
    
    print(f"f(x) = x^2, 구간 [{a}, {b}]")
    print(f"수치적 적분: {numerical_integral:.8f}")
    print(f"F(b) - F(a): {fundamental_theorem_result:.8f}")
    print(f"오차: {abs(numerical_integral - fundamental_theorem_result):.10f}")
    
    # 더 복잡한 함수로 검증
    def g(x):
        return np.sin(x) * np.exp(-x/2)
    
    def G(x):  # 해석적으로 구하기 어려운 원함수
        # 수치적으로 적분하여 원함수 근사
        result, _ = integrate.quad(g, 0, x)
        return result
    
    # 기본정리 제1법칙 검증: d/dx G(x) = g(x)
    x_test = 1.5
    h = 1e-7
    
    numerical_derivative = (G(x_test + h) - G(x_test)) / h
    function_value = g(x_test)
    
    print(f"\n더 복잡한 함수 g(x) = sin(x)*exp(-x/2)")
    print(f"x = {x_test}에서:")
    print(f"수치 미분 dG/dx: {numerical_derivative:.8f}")
    print(f"함수값 g(x): {function_value:.8f}")
    print(f"오차: {abs(numerical_derivative - function_value):.10f}")

def applications_of_fundamental_theorem():
    """기본정리의 응용"""
    print("\n=== 기본정리의 응용 ===")
    
    x = sp.Symbol('x')
    
    # 응용 1: 변수가 상한에 있는 경우
    print("1. 변수가 적분의 상한에 있는 경우")
    print("d/dx integral from 0 to x^2 of sin(t) dt")
    
    # 연쇄법칙과 함께 사용
    # d/dx integral from 0 to u(x) of f(t) dt = f(u(x)) * u'(x)
    u_x = x**2
    f_u = sp.sin(u_x)  # sin(x^2)
    u_prime = sp.diff(u_x, x)  # 2x
    
    result_chain = f_u * u_prime
    print(f"= sin(x^2) * d/dx(x^2) = sin(x^2) * 2x = {result_chain}")
    
    # 응용 2: 변수가 하한에 있는 경우
    print("\n2. 변수가 적분의 하한에 있는 경우")
    print("d/dx integral from x to 1 of t^2 dt")
    print("= -d/dx integral from 1 to x of t^2 dt = -x^2")
    
    # 응용 3: 변수가 상한과 하한 모두에 있는 경우
    print("\n3. 변수가 상한과 하한 모두에 있는 경우")
    print("d/dx integral from x to x^2 of sin(t) dt")
    print("= d/dx integral from 0 to x^2 of sin(t) dt - d/dx integral from 0 to x of sin(t) dt")
    print("= sin(x^2) * 2x - sin(x) * 1")
    print("= 2x*sin(x^2) - sin(x)")

def plot_fundamental_theorem():
    """기본정리의 시각적 설명"""
    x = np.linspace(0, 3, 1000)
    
    # f(x) = x^2
    f_x = x**2
    F_x = x**3 / 3  # 원함수
    
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
    
    # 원함수 f(x)
    ax1.plot(x, f_x, 'b-', linewidth=2, label='f(x) = x^2')
    ax1.fill_between(x[x <= 2], 0, f_x[x <= 2], alpha=0.3, color='blue', label='Area = integral from 0 to 2')
    ax1.axvline(x=2, color='r', linestyle='--', alpha=0.7)
    ax1.set_xlabel('x')
    ax1.set_ylabel('f(x)')
    ax1.set_title('원함수와 면적')
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    
    # 적분함수 (면적함수)
    area_x = x**3 / 3  # integral from 0 to x of t^2 dt
    ax2.plot(x, area_x, 'g-', linewidth=2, label='A(x) = integral from 0 to x of t^2 dt')
    ax2.set_xlabel('x')
    ax2.set_ylabel('A(x)')
    ax2.set_title('적분함수 (면적함수)')
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    # 적분함수의 도함수
    derivative_area = x**2  # dA/dx = x^2 = f(x)
    ax3.plot(x, derivative_area, 'r-', linewidth=2, label="A'(x) = f(x)")
    ax3.plot(x, f_x, 'b--', linewidth=2, alpha=0.7, label='f(x) = x^2')
    ax3.set_xlabel('x')
    ax3.set_ylabel("A'(x)")
    ax3.set_title('적분함수의 도함수 = 원함수')
    ax3.grid(True, alpha=0.3)
    ax3.legend()
    
    plt.tight_layout()
    plt.show()

def interactive_fundamental_theorem():
    """기본정리의 상호작용적 예시"""
    print("\n=== 상호작용적 예시 ===")
    
    # 사용자가 다양한 함수로 실험할 수 있는 프레임워크
    x = sp.Symbol('x')
    
    test_functions = [
        (x**2, "x^2"),
        (sp.sin(x), "sin(x)"),
        (sp.exp(x), "e^x"),
        (1/(x+1), "1/(x+1)"),
        (x*sp.log(x), "x*ln(x)")
    ]
    
    print("다양한 함수들에 대한 기본정리 확인:")
    print("=" * 60)
    
    for func, name in test_functions:
        print(f"\nf(x) = {name}")
        
        try:
            # 원함수 구하기
            antiderivative = sp.integrate(func, x)
            print(f"F(x) = {antiderivative} + C")
            
            # 미분해서 원래 함수 복원
            derivative_check = sp.diff(antiderivative, x)
            simplified = sp.simplify(derivative_check - func)
            
            if simplified == 0:
                print("✓ F'(x) = f(x) 확인됨")
            else:
                print(f"△ 차이: {simplified}")
                
            # 정적분 예시
            if name != "x*ln(x)":  # ln(x)는 x=0에서 정의되지 않음
                definite_val = sp.integrate(func, (x, 1, 2))
                manual_calc = antiderivative.subs(x, 2) - antiderivative.subs(x, 1)
                print(f"integral from 1 to 2: {definite_val}")
                print(f"F(2) - F(1): {manual_calc}")
                
        except Exception as e:
            print(f"계산 중 오류: {str(e)}")

def run_fundamental_theorem_examples():
    """모든 예시 실행"""
    print("=== 미적분학의 기본정리 (Fundamental Theorem of Calculus) ===\n")
    fundamental_theorem_part1()
    fundamental_theorem_part2()
    derivative_integral_relationship()
    numerical_verification()
    applications_of_fundamental_theorem()
    interactive_fundamental_theorem()
    
    # 그래프 그리기 (선택적)
    try:
        plot_fundamental_theorem()
    except:
        print("그래프를 표시할 수 없습니다. matplotlib 설정을 확인하세요.")

if __name__ == "__main__":
    run_fundamental_theorem_examples()
