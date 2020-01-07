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
Identity gate.
"""
import numpy
import warnings
from qiskit.circuit import Gate
from qiskit.circuit import QuantumCircuit


class IGate(Gate):
    """Identity gate.

    Identity gate corresponds to a single-qubit gate wait cycle,
    and should not be optimized or unrolled (it is an opaque gate).
    """

    def __init__(self, label=None):
        """Create new Identity gate."""
        super().__init__('id', 1, [], label=label)

    def inverse(self):
        """Invert this gate."""
        return IGate()  # self-inverse

    def to_matrix(self):
        """Return a numpy.array for the identity gate."""
        return numpy.array([[1, 0],
                            [0, 1]], dtype=complex)


def i(self, q):
    """Apply Identity to q.

    Identity gate corresponds to a single-qubit gate wait cycle,
    and should not be optimized or unrolled (it is an opaque gate).
    """
    return self.append(IGate(), [q], [])


def iden(self, q):
    """ Deprecated identity gate. """
    warnings.warn('The method qc.iden() is deprecated, use qc.i() instead', DeprecationWarning, 2)
    return self.append(IGate(), [q], [])


# support both i and iden as methods of QuantumCircuit, however iden contains a deprecation warning
QuantumCircuit.i = i
QuantumCircuit.iden = iden
