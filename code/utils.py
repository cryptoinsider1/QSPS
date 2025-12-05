# utils.py
"""
Вспомогательные функции для расчёта радиальных волновых функций
и плотностей вероятности для водородоподобных атомов.

По умолчанию используются атомные единицы:
ħ = m_e = e = a0 = 1.
"""

from __future__ import annotations

import math
from typing import Union

import numpy as np
from scipy.special import genlaguerre

ArrayLike = Union[np.ndarray, float]


# Эффективный Боровский радиус (в выбранных единицах)
A0: float = 1.0


def _as_array(r: ArrayLike) -> np.ndarray:
    """Преобразовать вход в numpy-массив с типом float."""
    return np.asarray(r, dtype=float)


def scaled_radius(r: ArrayLike, n: int, Z: float = 1.0, a0: float = A0) -> np.ndarray:
    """
    Безразмерная переменная ρ = 2 Z r / (n a0).

    Используется в аналитической форме радиальной волновой функции.
    """
    r_arr = _as_array(r)
    return 2.0 * Z * r_arr / (n * a0)


def radial_wavefunction(
    r: ArrayLike,
    n: int,
    l: int,
    Z: float = 1.0,
    a0: float = A0,
) -> np.ndarray:
    """
    Нормированная радиальная волновая функция R_{n,l}(r)
    для водородоподобного атома.

    Формула:
        R_{n,l}(r) = (2Z / (n a0))^{3/2}
                     * sqrt[(n-l-1)! / (2n (n+l)!)]
                     * e^{-ρ/2} ρ^{l} L_{n-l-1}^{2l+1}(ρ),

    где ρ = 2 Z r / (n a0), L — обобщённый полином Лагерра.

    Параметры
    ---------
    r : float или array-like
        Радиус(ы) r.
    n : int
        Главное квантовое число (n = 1, 2, ...).
    l : int
        Орбитальное квантовое число (0 ≤ l ≤ n-1).
    Z : float, optional
        Заряд ядра (по умолчанию 1 — атом водорода).
    a0 : float, optional
        Боровский радиус в используемых единицах.

    Возвращает
    ----------
    np.ndarray
        Значения R_{n,l}(r).
    """
    if n <= 0:
        raise ValueError("Главное квантовое число n должно быть положительным.")
    if l < 0 or l >= n:
        raise ValueError("Орбитальное квантовое число l должно удовлетворять 0 <= l <= n-1.")

    rho = scaled_radius(r, n=n, Z=Z, a0=a0)

    # Нормировочный множитель
    num = math.factorial(n - l - 1)
    den = 2 * n * math.factorial(n + l)
    norm = (2.0 * Z / (n * a0)) ** 1.5 * math.sqrt(num / den)

    # Обобщённые полиномы Лагерра L_{n-l-1}^{2l+1}(ρ)
    L = genlaguerre(n - l - 1, 2 * l + 1)(rho)

    return norm * np.exp(-rho / 2.0) * rho**l * L


def radial_probability_density(
    r: ArrayLike,
    n: int,
    l: int,
    Z: float = 1.0,
    a0: float = A0,
) -> np.ndarray:
    """
    Радиальная плотность вероятности P_{n,l}(r) = r^2 |R_{n,l}(r)|^2.

    Это величина, которую удобно визуализировать на графиках
    (максимумы соответствуют «оболочкам»).
    """
    r_arr = _as_array(r)
    R = radial_wavefunction(r_arr, n=n, l=l, Z=Z, a0=a0)
    return r_arr**2 * np.abs(R) ** 2


def radius_from_cartesian(x: ArrayLike, y: ArrayLike, z: ArrayLike) -> np.ndarray:
    """
    Радиус r = sqrt(x^2 + y^2 + z^2) по декартовым координатам.

    Используется при построении 3D-плотности из радиально-симметричной
    волновой функции (например, состояний типа s).
    """
    x_arr = _as_array(x)
    y_arr = _as_array(y)
    z_arr = _as_array(z)
    return np.sqrt(x_arr**2 + y_arr**2 + z_arr**2)
