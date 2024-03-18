from sympy.matrices.exceptions import NonSquareMatrixError, ShapeError
from sympy.matrices.kind import MatrixKind
from sympy.matrices.dense import GramSchmidt, MutableDenseMatrix, casoratian, diag, eye, hessian, jordan_cell, list2numpy, matrix2numpy, matrix_multiply_elementwise, ones, randMatrix, rot_axis1, rot_axis2, rot_axis3, rot_ccw_axis1, rot_ccw_axis2, rot_ccw_axis3, rot_givens, symarray, wronskian, zeros
from sympy.matrices.matrixbase import DeferredVector, MatrixBase
from sympy.matrices.sparse import MutableSparseMatrix
from sympy.matrices.sparsetools import banded
from sympy.matrices.immutable import ImmutableDenseMatrix, ImmutableSparseMatrix
from sympy.matrices.expressions import Adjoint, BlockDiagMatrix, BlockMatrix, Determinant, DiagMatrix, DiagonalMatrix, DiagonalOf, DotProduct, FunctionMatrix, HadamardPower, HadamardProduct, Identity, Inverse, KroneckerProduct, MatAdd, MatMul, MatPow, MatrixExpr, MatrixPermute, MatrixSet, MatrixSlice, MatrixSymbol, OneMatrix, Permanent, PermutationMatrix, Trace, Transpose, ZeroMatrix, block_collapse, blockcut, det, diagonalize_vector, hadamard_product, kronecker_product, matrix_symbols, per, trace
from sympy.matrices.utilities import dotprodsimp

MutableMatrix = MutableDenseMatrix
Matrix = MutableMatrix
ImmutableMatrix = ImmutableDenseMatrix
SparseMatrix = MutableSparseMatrix
__all__ = ['ShapeError', 'NonSquareMatrixError', 'MatrixKind', 'GramSchmidt', 'casoratian', 'diag', 'eye', 'hessian', 'jordan_cell', 'list2numpy', 'matrix2numpy', 'matrix_multiply_elementwise', 'ones', 'randMatrix', 'rot_axis1', 'rot_axis2', 'rot_axis3', 'symarray', 'wronskian', 'zeros', 'rot_ccw_axis1', 'rot_ccw_axis2', 'rot_ccw_axis3', 'rot_givens', 'MutableDenseMatrix', 'DeferredVector', 'MatrixBase', 'Matrix', 'MutableMatrix', 'MutableSparseMatrix', 'banded', 'ImmutableDenseMatrix', 'ImmutableSparseMatrix', 'ImmutableMatrix', 'SparseMatrix', 'MatrixSlice', 'BlockDiagMatrix', 'BlockMatrix', 'FunctionMatrix', 'Identity', 'Inverse', 'MatAdd', 'MatMul', 'MatPow', 'MatrixExpr', 'MatrixSymbol', 'Trace', 'Transpose', 'ZeroMatrix', 'OneMatrix', 'blockcut', 'block_collapse', 'matrix_symbols', 'Adjoint', 'hadamard_product', 'HadamardProduct', 'HadamardPower', 'Determinant', 'det', 'diagonalize_vector', 'DiagMatrix', 'DiagonalMatrix', 'DiagonalOf', 'trace', 'DotProduct', 'kronecker_product', 'KroneckerProduct', 'PermutationMatrix', 'MatrixPermute', 'MatrixSet', 'Permanent', 'per', 'dotprodsimp']
