import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

simulator = Aer.get_backend('qasm_simulator')

circuit = QuantumCircuit(3, 2)

circuit.x(2)
circuit.barrier()
circuit.h(0)
circuit.h(1)
circuit.h(2)
circuit.barrier()
circuit.i(0)
circuit.i(1)
circuit.i(2)
circuit.barrier()
circuit.h(0)
circuit.h(1)
circuit.barrier()

# Map the quantum measurement to the classical bits
circuit.measure([0,1], [1,0])

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)

result = job.result()

counts = result.get_counts(circuit)


print(circuit)

plot_histogram(counts)
plt.show()
