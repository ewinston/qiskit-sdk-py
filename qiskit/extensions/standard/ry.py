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
Rotation around the y-axis.
"""
import math
import numpy
from qiskit.circuit import Gate
from qiskit.circuit import QuantumCircuit
from qiskit.circuit import QuantumRegister
from qiskit.qasm import pi
from qiskit.extensions.standard.r import RGate


class RYGate(Gate):
    """The rotation around the y-axis."""

    def __init__(self, theta):
        """Create new RY single qubit gate."""
        super().__init__('ry', 1, [theta])

    def _define(self):
        """
        gate ry(theta) a { r(theta, pi/2) a; }
        """
        definition = []
        q = QuantumRegister(1, 'q')
        rule = [
            (RGate(self.params[0], pi / 2), [q[0]], [])
        ]
        for inst in rule:
            definition.append(inst)
        self.definition = definition

    def inverse(self):
        """Invert this gate.

        ry(theta)^dagger = ry(-theta)
        """
        return RYGate(-self.params[0])

    def to_matrix(self):
        """Return a numpy.array for the RY gate."""
        cos = math.cos(self.params[0] / 2)
        sin = math.sin(self.params[0] / 2)
        return numpy.array([[cos, -sin],
                            [sin, cos]], dtype=complex)


def ry(self, theta, q):  # pylint: disable=invalid-name
    """Apply RY to q."""
    return self.append(RYGate(theta), [q], [])


QuantumCircuit.ry = ry
