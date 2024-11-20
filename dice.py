import random
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import tkinter as tk

# Create the main window for the GUI
root = tk.Tk()
root.title("Quantum Dice Roll")

# Create a label to display the dice result
label_result = tk.Label(root, text="Roll Result: ", font=("Helvetica", 16))
label_result.pack(pady=20)

# Function to roll the quantum dice (simulate the quantum circuit)
def roll_dice():
    # Create the quantum circuit with 6 qubits and 6 classical bits
    qc = QuantumCircuit(6, 6)
    
    # Apply random gates to the qubits
    for qubit in range(6):
        # Randomly apply either a Hadamard, Pauli-X, or Pauli-Z gate
        gate_choice = random.choice(['h', 'x', 'z'])
        if gate_choice == 'h':
            qc.h(qubit)  # Apply Hadamard gate
        elif gate_choice == 'x':
            qc.x(qubit)  # Apply Pauli-X gate (NOT gate)
        elif gate_choice == 'z':
            qc.z(qubit)  # Apply Pauli-Z gate
    
    # Measure all qubits and store the results in the classical register
    qc.measure(range(6), range(6))
    
    # Use AerSimulator to simulate the quantum circuit directly
    simulator = AerSimulator()
    result = simulator.run(qc, shots=1).result()  # Run the circuit directly
    
    # Get the measurement results (counts)
    counts = result.get_counts()
    
    # Extract the outcome from the counts
    binary_result = list(counts.keys())[0]  # Get the first outcome (assuming 1 shot)
    
    # Convert the binary result to an integer
    decimal_result = int(binary_result, 2)  # Convert binary string to a decimal number
    
    # Map the result to a dice roll (1 to 6)
    dice_roll = (decimal_result % 6) + 1
    
    # Update the GUI label with the dice roll result
    label_result.config(text=f"Roll Result: {dice_roll}")

    # Display the quantum circuit diagram in the console
    print("Quantum Circuit:")
    print(qc.draw())

# Create a button that will trigger the roll_dice function when clicked
button_roll = tk.Button(root, text="Roll the Dice", font=("Helvetica", 14), command=roll_dice)
button_roll.pack(pady=20)

# Run the GUI loop
root.mainloop()
