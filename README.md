# E8 Universe

Mathematical simulations and visualizations of the E8 lattice structure.

## Description

This project explores the E8 lattice, a mathematical structure with 240 roots in 8-dimensional space. The simulations demonstrate various properties including triality, symmetry, and connections to theoretical physics.

## Features

- E8 triality demonstrations
- Loop Quantum Gravity (LQG) calculations
- Orchestrated Objective Reduction (Orch-OR) models
- String theory connections
- 3D visualizations of E8 root lattice projections

## Running the Simulations

### Prerequisites

```bash
pip install numpy matplotlib
```

### Execute

```bash
python E8_simulations.py
```

## Live Demo Code

```python
# E8 triality
import numpy as np
T = np.array([[0,0,1],[1,0,0],[0,1,0]])
print("T³ = I:", np.allclose(np.linalg.matrix_power(T,3), np.eye(3)))
```

## Visualizations

The script generates 3D visualizations of the E8 root lattice projections using matplotlib.

## License

Open source - feel free to use and modify.
