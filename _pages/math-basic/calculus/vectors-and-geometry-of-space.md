---
title: "Vectors and the Geometry of Space"
permalink: /calculus/vectors-and-geometry-of-space/
header:
  overlay_image: /assets/images/headers/calculus.png
  overlay_opacity: 0.8
nav: "calculus"
---

To move from single-variable calculus to multivariable calculus, we first need to develop a language for describing points and motion in three-dimensional space. This is the language of **vectors**.

## Three-Dimensional Coordinate Systems

To locate a point in space, we use three mutually perpendicular axes: the x-axis, y-axis, and z-axis. A point is represented by an ordered triple $(x, y, z)$.

<img src="/assets/images/calculus/3d-coordinates.png" alt="3D Coordinate System" style="width: 400px; max-width: 100%; margin: 1rem auto; display: block;">

**Distance Formula:** The distance between two points $P_1(x_1, y_1, z_1)$ and $P_2(x_2, y_2, z_2)$ is:
$$
|P_1 P_2| = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}
$$

**Equation of a Sphere:** A sphere with center $(h, k, l)$ and radius $r$ is the set of all points $(x, y, z)$ such that:
$$ (x-h)^2 + (y-k)^2 + (z-l)^2 = r^2 $$

## Vectors

A **vector** is a quantity that has both **magnitude** (or length) and **direction**. It is represented geometrically by an arrow. We denote a vector by a boldface letter (e.g., **v**) or an arrow over the letter (e.g., $\vec{v}$).

A vector can be represented by its components. If a vector **v**'s tail is at the origin and its head is at the point $(v_1, v_2, v_3)$, we can write:
$$ \mathbf{v} = \langle v_1, v_2, v_3 \rangle $$
This is the **component form** of the vector.

**Magnitude (or Norm):** The length of the vector **v** is:
$$ |→→| = \sqrt{v_1^2 + v_2^2 + v_3^2} $$

### Vector Operations

-   **Addition:** $\mathbf{u} + \mathbf{v} = \langle u_1+v_1, u_2+v_2, u_3+v_3 \rangle$ (Geometrically, the "head-to-tail" rule).
-   **Scalar Multiplication:** $c\mathbf{v} = \langle cv_1, cv_2, cv_3 \rangle$ (Scales the length of the vector).

### Standard Basis Vectors

Any vector in 3D can be expressed as a combination of the standard basis vectors:
-   $→→ = \langle 1, 0, 0 \rangle$
-   $→→ = \langle 0, 1, 0 \rangle$
-   $→→ = \langle 0, 0, 1 \rangle$

So, $\mathbf{v} = \langle v_1, v_2, v_3 \rangle$ can be written as $\mathbf{v} = v_1\mathbf{i} + v_2\mathbf{j} + v_3\mathbf{k}$.

## The Dot Product

The **dot product** of two vectors $\mathbf{u}$ and $\mathbf{v}$ is a **scalar** (a number) defined as:
$$ \mathbf{u} \cdot \mathbf{v} = u_1v_1 + u_2v_2 + u_3v_3 $$

The dot product has a very useful geometric interpretation:
$$ \mathbf{u} \cdot \mathbf{v} = |\mathbf{u}| |\mathbf{v}| \cos(\theta) $$
where $\theta$ is the angle between the two vectors.

**Key Property:** Two non-zero vectors **u** and **v** are **orthogonal** (perpendicular) if and only if their dot product is zero: $\mathbf{u} \cdot \mathbf{v} = 0$.

## The Cross Product

The **cross product** of two vectors $\mathbf{u}$ and $\mathbf{v}$ in 3D space is another **vector**, denoted $\mathbf{u} \times \mathbf{v}$.

**Geometric Definition:**
-   The vector $\mathbf{u} \times \mathbf{v}$ is **orthogonal** to both **u** and **v**.
-   Its direction is given by the **right-hand rule**.
-   Its magnitude is $\|→→ \times →→\| = \|\mathbf{u}\| \|\mathbf{v}\| \sin(\theta)$.

The magnitude of the cross product is equal to the **area of the parallelogram** spanned by **u** and **v**.

**Key Property:** Two non-zero vectors **u** and **v** are **parallel** if and only if their cross product is the zero vector: $\mathbf{u} \times \mathbf{v} = \mathbf{0}$.

**Component Formula:**
$$ \mathbf{u} \times \mathbf{v} = \langle u_2v_3 - u_3v_2, u_3v_1 - u_1v_3, u_1v_2 - u_2v_1 \rangle $$
This is often computed using the determinant of a matrix:
$$ \mathbf{u} \times \mathbf{v} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \end{vmatrix} $$

## Equations of Lines and Planes

Vectors provide a powerful way to describe lines and planes in space.

### Lines

A line $L$ is determined by a point $P_0(x_0, y_0, z_0)$ on the line and a **direction vector** $\mathbf{v} = \langle a, b, c \rangle$ that is parallel to the line.

-   **Vector Equation:** $\mathbf{r}(t) = \mathbf{r}_0 + t\mathbf{v}$
-   **Parametric Equations:**
    $$ x = x_0 + at, \quad y = y_0 + bt, \quad z = z_0 + ct $$

### Planes

A plane in space is determined by a point $P_0(x_0, y_0, z_0)$ in the plane and a **normal vector** $\mathbf{n} = \langle a, b, c \rangle$ that is orthogonal to the plane.

The equation of the plane is:
$$ a(x - x_0) + b(y - y_0) + c(z - z_0) = 0 $$

## Summary

-   Vectors are essential for describing quantities with both magnitude and direction in 3D space.
-   The **dot product** is a tool for finding angles between vectors and checking for orthogonality.
-   The **cross product** produces a new vector that is orthogonal to the original two and is useful for finding areas and defining planes.
-   Vectors provide a concise way to write equations for lines and planes.

This framework for working in three dimensions is the necessary prerequisite for the next step in calculus.

Next, we will use these vector concepts to analyze functions of multiple variables with [Partial Derivatives](partial-derivatives.md).

---

[View Problems and Solutions for Vectors And Geometry Of Space](/math-basic/calculus/problems/vectors-and-geometry-of-space-problems/)
