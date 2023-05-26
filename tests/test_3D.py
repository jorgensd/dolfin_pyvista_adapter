import dolfin
from dolfin_pyvista_adapter import plot
import pytest
from pathlib import Path


@pytest.fixture()
def testing_dir():
    cwd = Path("test_results")
    cwd.mkdir(exist_ok=True)
    return cwd


def test_plot_vector_3D(testing_dir):
    mesh = dolfin.UnitCubeMesh(2, 2, 2)
    Vv = dolfin.VectorFunctionSpace(mesh, "Lagrange", 3)
    v = dolfin.Function(Vv)
    v.interpolate(dolfin.Expression(("x[0]", "x[1]", "x[2]"), degree=1))
    filename = testing_dir / "vector.png"
    plot(v, filename=filename, show_edges=True, glyph_factor=0.1)


def test_plot_scalar_3D(testing_dir):
    mesh = dolfin.UnitCubeMesh(2, 2, 2)
    V = dolfin.FunctionSpace(mesh, "Lagrange", 2)
    u = dolfin.Function(V)
    u.interpolate(dolfin.Expression("x[0]+3*x[1]+2", degree=1))
    filename = testing_dir / "scalar.png"
    plot(u, filename=filename, show_edges=True)
