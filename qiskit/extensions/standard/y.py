# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2017.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""
Pauli Y (bit-phase-flip) gate.
"""
import numpy
from qiskit.circuit import Gate
from qiskit.circuit import ControlledGate
from qiskit.circuit import QuantumRegister
from qiskit.circuit import QuantumCircuit
from qiskit.qasm import pi
from qiskit.extensions.standard.s import SGate
from qiskit.extensions.standard.s import SdgGate
from qiskit.extensions.standard.cx import CXGate


class YGate(Gate):
    """Pauli Y (bit-phase-flip) gate."""

    def __init__(self, label=None):
        """Create new Y gate."""
        super().__init__('y', 1, [], label=label)

    def _define(self):
        from qiskit.extensions.standard.u3 import U3Gate
        definition = []
        q = QuantumRegister(1, 'q')
        rule = [
            (U3Gate(pi, pi / 2, pi / 2), [q[0]], [])
        ]
        for inst in rule:
            definition.append(inst)
        self.definition = definition

    def control(self, num_ctrl_qubits=1, label=None):
        """Controlled version of this gate.

        Args:
            num_ctrl_qubits (int): number of control qubits.
            label (str or None): An optional label for the gate [Default: None]

        Returns:
            ControlledGate: controlled version of this gate.
        """
        if num_ctrl_qubits == 1:
            return CyGate()
        return super().control(num_ctrl_qubits=num_ctrl_qubits, label=label)

    def inverse(self):
        """Invert this gate."""
        return YGate()  # self-inverse

    def to_matrix(self):
        """Return a numpy.array for the Y gate."""
        return numpy.array([[0, -1j],
                            [1j, 0]], dtype=complex)


def y(self, q):
    """Apply Y to q."""
    return self.append(YGate(), [q], [])


QuantumCircuit.y = y


class CYMeta(type):
    """A metaclass to ensure that CyGate and CYGate are of the same type.

    Can be removed when CyGate gets removed.
    """
    @classmethod
    def __instancecheck__(mcs, inst):
        return type(inst) in {CYGate, CyGate}  # pylint: disable=unidiomatic-typecheck


class CYGate(ControlledGate, metaclass=CYMeta):
    """The controlled-Y gate."""

    def __init__(self):
        """Create new CY gate."""
        super().__init__('cy', 2, [], num_ctrl_qubits=1)
        self.base_gate = YGate
        self.base_gate_name = 'y'

    def _define(self):
        """
        gate cy a,b { sdg b; cx a,b; s b; }
        """
        definition = []
        q = QuantumRegister(2, "q")
        rule = [
            (SdgGate(), [q[1]], []),
            (CXGate(), [q[0], q[1]], []),
            (SGate(), [q[1]], [])
        ]
        for inst in rule:
            definition.append(inst)
        self.definition = definition

    def inverse(self):
        """Invert this gate."""
        return CYGate()  # self-inverse

    def to_matrix(self):
        """Return a numpy.array for the CY gate."""
        return numpy.array([[1, 0, 0, 0],
                            [0, 0, 0, -1j],
                            [0, 0, 1, 0],
                            [0, 1j, 0, 0]], dtype=complex)


class CyGate(CYGate, metaclass=CYMeta):
    """A deprecated CYGate class."""

    def __init__(self):
        import warnings
        warnings.warn('The class CyGate is deprecated as of 0.12.0, and '
                      'will be removed no earlier than 3 months after that release date. '
                      'You should use the class CYGate instead.',
                      DeprecationWarning, stacklevel=2)
        super().__init__()


def cy(self, ctl, tgt):  # pylint: disable=invalid-name
    """Apply CY to circuit."""
    return self.append(CYGate(), [ctl, tgt], [])


QuantumCircuit.cy = cy
