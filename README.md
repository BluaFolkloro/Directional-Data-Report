# Definition and Calculation of the Mean Direction

In statistics, the **mean direction** refers to the central tendency of a set of directional data, commonly used for circular or angular data, such as wind direction or movement direction. Since directional data is periodic, meaning $0^\circ = 360^\circ$, the typical arithmetic mean does not apply to such data. Thus, the mean of directions is calculated using vector-based methods.


## Calculation of the Mean Direction

Suppose we have a set of directional data, denoted as $\theta_1, \theta_2, \dots, \theta_n$, which are measured in either radians or degrees. To calculate the mean direction, we first convert each direction to a unit vector and sum them:

$$
C = \sum_{i=1}^n \cos \theta_i \quad S = \sum_{i=1}^n \sin \theta_i
$$

Next, the resultant vector's length $R$ is computed (and thus we have the mean resultant length $\bar{R} = R/n$ ,) as well as the cosine and sine values of the mean direction:

$$
R^2 = C^2 + S^2 \quad \text{(where} \, R \geq 0 \text{)}
$$ $$
\cos \bar{\theta} = \frac{C}{R} \quad \sin \bar{\theta} = \frac{S}{R}
$$

Here, $$\bar{\theta}$$ represents the mean direction, which is the direction of the unit vector defined by $C$ and $S$. However, directly using $\cos \bar{\theta} = C/R$ and $\sin \bar{\theta} = S/R$ may lead to undefined results when $C = 0$ or $S = 0$. Therefore, a more robust approach is to use the **atan2** function to compute the mean direction.

## Using the $\text{atan2}$ Function to Calculate the Mean Direction

The function **atan2** is a special arctangent function that takes into account both the values of $S$ and $C$, and it correctly handles the signs of these values to return the proper angle. Unlike the standard arctangent function $\text{atan}(y/x)$, $\text{atan2}(y, x)$ can handle boundary cases, such as when $C = 0$ or $S = 0$, without producing undefined results.

$$
\bar{\theta} = \text{atan2}(S, C)
$$

Where:

-   $S = \sum_{i=1}^n \sin \theta_i$
-   $C = \sum_{i=1}^n \cos \theta_i$

The result of $$\text{atan2}(S, C)$$ will always be an angle in the interval $(-\pi, \pi]$, ensuring a unique result and avoiding ambiguities due to the periodic nature of angles.

## Definition of the $\text{atan2}$ Function

The $\text{atan2}$ function computes the principal argument of the complex number $x + iy$, which is also the imaginary part of the complex logarithm. Specifically, the definition of $\text{atan2}(y, x)$ is:

$$
\text{atan2}(y, x) = \arg(x + iy) = \text{Im} \log(x + iy)
$$

-   $\text{atan2}(y, x)$ calculates the principal argument of the complex number $x + iy$, which is the imaginary part of its logarithm.
-   Adding any integer multiple of $2\pi$ (representing complete rotations around the origin) gives another argument of the same complex number, but the principal argument is defined as the unique representative angle in the interval $(-\pi, \pi]$.

In terms of the standard arctangent function, whose image is $(-\frac{\pi}{2}, \frac{\pi}{2})$, $\text{atan2}$ can be expressed piecewise:

$$
\text{atan2}(y, x) =
\begin{cases}
\text{atan}(y/x) & \text{if} \, x > 0 \\
\text{atan}(y/x) + \pi & \text{if} \, x < 0 \text{ and } y \geq 0 \\
\text{atan}(y/x) - \pi & \text{if} \, x < 0 \text{ and } y < 0 \\
\text{atan}(y/x) + 2\pi & \text{if} \, x = 0 \text{ and } y > 0 \\
\text{atan}(y/x) - 2\pi & \text{if} \, x = 0 \text{ and } y < 0 \\
\text{undefined} & \text{if} \, x = 0 \text{ and } y = 0
\end{cases}
$$

# The von Mises Distribution

The **von Mises distribution** is a symmetric unimodal distribution widely used for modeling circular data. It is commonly used when we have samples that exhibit a central tendency around a single mean direction.

![Probability density functions for the von Mises distribution, copied from Fisher's book, may be replaced by an image newly drawed.](von_mises.png)

*Probability density functions for the von Mises distribution, copied from Fisher's book, may be replaced by an image newly drawed.*

## Probability Density Function (PDF)

The probability density function (PDF) for the von Mises distribution is:

$$
f(\theta) = \frac{1}{2\pi I_0(\kappa)} \exp\left( \kappa \cos(\theta - \mu) \right), \quad 0 \leq \theta < 2\pi, \quad 0 \leq \kappa < \infty
$$

Where: - $\mu$ is the **mean direction**, - $\kappa$ is the **concentration parameter**, which measures how tightly the data points cluster around the mean direction, - $I_0(\kappa)$ is the modified Bessel function of order zero, which normalizes the distribution.

## Cumulative Distribution Function (CDF)

The cumulative distribution function (CDF) does not have a simple closed form, but it can be computed numerically:

$$
F(\theta) = \frac{1}{2\pi I_0(\kappa)} \int_0^\theta \exp\left( \kappa \cos(\phi - \mu) \right) d\phi
$$

## Moments

The key moments for the von Mises distribution are:

1.  **Mean Direction** ($\mu$): The central direction around which the data points are clustered.
2.  **Mean Resultant Length** ($\rho = A_1 (\kappa)$ ): A measure of how tightly the data points are clustered around the mean direction. It ranges from 0 (uniform distribution) to 1 (all points at the mean direction).
3.  **Circular Dispersion** ($\delta = \left[ \kappa A_1(\kappa) \right]^{-1}$): A measure of the spread or concentration of the data points.
4.  **Higher Moments** ($\alpha_p = A_p(\kappa)$ ): These moments are used to describe higher-order features of the distribution.

As $\kappa$ increases, the distribution becomes more concentrated around the mean direction $\mu$, and as $\kappa \to 0$, the distribution approaches a uniform distribution over the circle.

## Limiting Forms

-   As $\kappa \to 0$, the von Mises distribution approaches the **uniform distribution** on the circle ($U_C$).
-   As $\kappa \to \infty$, the von Mises distribution becomes a **point distribution** concentrated around the mean direction $\mu$.
