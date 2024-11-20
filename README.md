# Quantum Dice Simulator

This is a **Quantum Dice Simulator** implemented using **Qiskit** and **Tkinter**. The simulator uses quantum principles to generate random dice rolls, where the outcome is determined by quantum superposition and measurement. The project allows you to visualize the quantum circuit and simulate the dice roll using Qiskit's quantum operations.

![alt text](<Screenshot 2024-11-20 203731.png>)

## Features
- **Simulate a Quantum Dice Roll**: Using Hadamard gates, quantum superposition, and measurements to simulate dice rolls.
- **Quantum Circuit Visualization**: The quantum circuit is visualized in the console each time the dice is rolled.
- **Randomized Quantum Gates**: The simulator randomly applies quantum gates (Hadamard, Pauli-X, Pauli-Z) to the qubits before measurement, providing varied results.
- **Graphical User Interface**: A simple GUI built using Tkinter to display the result of each dice roll.

## Technologies Used
- **Qiskit**: For simulating quantum circuits and performing quantum measurements.
- **Tkinter**: For creating the GUI.
- **Python**: For the main programming language.

## Getting Started

### Prerequisites
To run this project, you need to have the following installed:
- **Python 3.x**: Make sure you have Python installed. You can download it from [python.org](https://www.python.org/).
- **Qiskit**: A framework for working with quantum circuits.
- **Tkinter**: For building the GUI.

To install **Qiskit** and **Tkinter**, you can use `pip`:
```bash
pip install qiskit
pip install tk
