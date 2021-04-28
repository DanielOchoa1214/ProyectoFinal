import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

simulator = Aer.get_backend('qasm_simulator')

circuit = QuantumCircuit(2, 1)

circuit.x(1)
circuit.barrier()
circuit.h(0)
circuit.h(1)
circuit.barrier()
circuit.id(0)
circuit.id(1)
circuit.barrier()
circuit.h(0)
circuit.barrier()


# Map the quantum measurement to the classical bits
circuit.measure([0], [0])

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)

result = job.result()

counts = result.get_counts(circuit)

print(circuit)

plot_histogram(counts)
plt.show()
