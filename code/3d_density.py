import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.ticker as ticker

# ---------------------------------------------------------
# 1. ТОЧНЫЕ ВОЛНОВЫЕ ФУНКЦИИ В АТОМНЫХ ЕДИНИЦАХ (ħ = m_e = e = 1)
# ---------------------------------------------------------

def psi_1s(x, y, z, Z=1.0):
    """Волновая функция 1s состояния (сферически симметричная)"""
    r = np.sqrt(x**2 + y**2 + z**2) + 1e-12
    a0 = 1.0  # атомная единица длины
    return (Z**3 / np.pi)**0.5 * np.exp(-Z * r / a0)

def psi_2p0(x, y, z, Z=1.0):
    """Волновая функция 2p₀ состояния (m=0)"""
    r = np.sqrt(x**2 + y**2 + z**2) + 1e-12
    a0 = 1.0
    # Сферическая гармоника Y₁₀ = √(3/(4π)) * cosθ
    cos_theta = z / r
    Y_10 = np.sqrt(3 / (4 * np.pi)) * cos_theta
    # Радиальная часть R₂₁
    R_21 = (1 / (2 * np.sqrt(6))) * (Z/a0)**1.5 * (r/a0) * np.exp(-Z * r / (2 * a0))
    return R_21 * Y_10

# ---------------------------------------------------------
# 2. ПАРАМЕТРЫ СЕТКИ (ОПТИМИЗИРОВАНЫ ДЛЯ ЧЁТКОСТИ)
# ---------------------------------------------------------

# Для 1s: меньшая область, так как плотность сосредоточена близко к ядру
grid_1s = np.linspace(-6, 6, 200)
# Для 2p₀: большая область, так как орбиталь более размазана
grid_2p = np.linspace(-12, 12, 300)

# ---------------------------------------------------------
# 3. ВИЗУАЛИЗАЦИЯ: ТРИ ОРТОГОНАЛЬНЫХ СЕЧЕНИЯ ДЛЯ ОБОИХ СОСТОЯНИЙ
# ---------------------------------------------------------

fig, axes = plt.subplots(2, 3, figsize=(16, 10), constrained_layout=True)

# Цветовые карты для научной визуализации
cmap_1s = cm.viridis
cmap_2p = cm.plasma

# ---------------------------------------------------------
# 3.1. СОСТОЯНИЕ 1s
# ---------------------------------------------------------

X1, Y1, Z1 = np.meshgrid(grid_1s, grid_1s, grid_1s)
rho_1s = np.abs(psi_1s(X1, Y1, Z1))**2
rho_1s /= rho_1s.max()  # Нормировка для визуализации

mid_1s = len(grid_1s) // 2

# XY-сечение (z=0)
im1 = axes[0, 0].imshow(rho_1s[:, :, mid_1s].T, 
                       extent=[-6, 6, -6, 6],
                       cmap=cmap_1s, 
                       origin='lower',
                       vmin=0, vmax=1)
axes[0, 0].set_title('Состояние 1s: сечение XY (z=0)', fontsize=12, pad=10)
axes[0, 0].set_xlabel('$x$ [$a_0$]', fontsize=11)
axes[0, 0].set_ylabel('$y$ [$a_0$]', fontsize=11)
axes[0, 0].grid(True, alpha=0.3, linestyle='--')
fig.colorbar(im1, ax=axes[0, 0], label='$|\psi|^2$ (нормированная)')

# XZ-сечение (y=0)
im2 = axes[0, 1].imshow(rho_1s[:, mid_1s, :].T,
                       extent=[-6, 6, -6, 6],
                       cmap=cmap_1s,
                       origin='lower',
                       vmin=0, vmax=1)
axes[0, 1].set_title('Состояние 1s: сечение XZ (y=0)', fontsize=12, pad=10)
axes[0, 1].set_xlabel('$x$ [$a_0$]', fontsize=11)
axes[0, 1].set_ylabel('$z$ [$a_0$]', fontsize=11)
axes[0, 1].grid(True, alpha=0.3, linestyle='--')

# YZ-сечение (x=0)
im3 = axes[0, 2].imshow(rho_1s[mid_1s, :, :].T,
                       extent=[-6, 6, -6, 6],
                       cmap=cmap_1s,
                       origin='lower',
                       vmin=0, vmax=1)
axes[0, 2].set_title('Состояние 1s: сечение YZ (x=0)', fontsize=12, pad=10)
axes[0, 2].set_xlabel('$y$ [$a_0$]', fontsize=11)
axes[0, 2].set_ylabel('$z$ [$a_0$]', fontsize=11)
axes[0, 2].grid(True, alpha=0.3, linestyle='--')

# ---------------------------------------------------------
# 3.2. СОСТОЯНИЕ 2p₀
# ---------------------------------------------------------

X2, Y2, Z2 = np.meshgrid(grid_2p, grid_2p, grid_2p)
rho_2p = np.abs(psi_2p0(X2, Y2, Z2))**2
rho_2p /= np.abs(rho_2p).max()  # Нормировка с учётом знака

mid_2p = len(grid_2p) // 2

# XY-сечение (z=0)
im4 = axes[1, 0].imshow(rho_2p[:, :, mid_2p].T,
                       extent=[-12, 12, -12, 12],
                       cmap=cmap_2p,
                       origin='lower',
                       vmin=-0.3, vmax=0.3)  # Показываем и положительные, и отрицательные значения
axes[1, 0].set_title('Состояние 2p$_0$: сечение XY (z=0)', fontsize=12, pad=10)
axes[1, 0].set_xlabel('$x$ [$a_0$]', fontsize=11)
axes[1, 0].set_ylabel('$y$ [$a_0$]', fontsize=11)
axes[1, 0].grid(True, alpha=0.3, linestyle='--')
fig.colorbar(im4, ax=axes[1, 0], label='$|\psi|^2$ (нормированная)')

# XZ-сечение (y=0) - НАИБОЛЕЕ ИНФОРМАТИВНОЕ ДЛЯ 2p₀
im5 = axes[1, 1].imshow(rho_2p[:, mid_2p, :].T,
                       extent=[-12, 12, -12, 12],
                       cmap=cmap_2p,
                       origin='lower',
                       vmin=-0.3, vmax=0.3)
axes[1, 1].set_title('Состояние 2p$_0$: сечение XZ (y=0)', fontsize=12, pad=10)
axes[1, 1].set_xlabel('$x$ [$a_0$]', fontsize=11)
axes[1, 1].set_ylabel('$z$ [$a_0$]', fontsize=11)
axes[1, 1].grid(True, alpha=0.3, linestyle='--')
# Контурные линии для выделения структуры
contour_levels = np.linspace(-0.25, 0.25, 11)
CS = axes[1, 1].contour(grid_2p, grid_2p, rho_2p[:, mid_2p, :].T, 
                       levels=contour_levels, 
                       colors='white', alpha=0.5, linewidths=0.5)

# YZ-сечение (x=0)
im6 = axes[1, 2].imshow(rho_2p[mid_2p, :, :].T,
                       extent=[-12, 12, -12, 12],
                       cmap=cmap_2p,
                       origin='lower',
                       vmin=-0.3, vmax=0.3)
axes[1, 2].set_title('Состояние 2p$_0$: сечение YZ (x=0)', fontsize=12, pad=10)
axes[1, 2].set_xlabel('$y$ [$a_0$]', fontsize=11)
axes[1, 2].set_ylabel('$z$ [$a_0$]', fontsize=11)
axes[1, 2].grid(True, alpha=0.3, linestyle='--')

# ---------------------------------------------------------
# 4. НАСТРОЙКИ ОБЩЕГО ВИДА
# ---------------------------------------------------------

fig.suptitle('Трёхмерная плотность вероятности $|\psi_{nlm}|^2$ для состояний 1s и 2p$_0$ водородоподобного атома',
             fontsize=14, y=1.02)

# Добавление аннотаций
axes[0, 0].text(0.05, 0.95, 'A', transform=axes[0, 0].transAxes, 
                fontsize=16, fontweight='bold', va='top', color='white')
axes[1, 0].text(0.05, 0.95, 'B', transform=axes[1, 0].transAxes, 
                fontsize=16, fontweight='bold', va='top', color='white')

plt.savefig('3d_density_comparison.png', dpi=400, bbox_inches='tight', facecolor='white')
plt.show()

print("✅ График сохранён как '3d_density_comparison.png'")
print("   Размер: 16×10 дюймов, DPI: 400")
print("   Формат: научный, готовый для публикации")
