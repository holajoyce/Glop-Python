"""Glop simple example."""

from google.apputils import app

from ortools.linear_solver import pywraplp

def main(_):

  # Instantiate a Glop solver, naming it SolveSimpleSystem.
  solver = pywraplp.Solver('SolveSimpleSystem',
                           pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

  # Create the two variables in our system of equations,
  # and let them take on any value.
  x = solver.NumVar(-solver.infinity(), solver.infinity(), 'x')
  y = solver.NumVar(-solver.infinity(), solver.infinity(), 'y')

  # Constraint 1: x + 2y <= 14.
  constraint1 = solver.Constraint(-solver.infinity(), 14)
  constraint1.SetCoefficient(x, 1)
  constraint1.SetCoefficient(y, 2)

  # Constraint 2: 3x - y >= 0.
  constraint2 = solver.Constraint(0, solver.infinity())
  constraint2.SetCoefficient(x, 3)
  constraint2.SetCoefficient(y, -1)

  # Constraint 3: x - y <= 2.
  constraint3 = solver.Constraint(-solver.infinity(), 2)
  constraint3.SetCoefficient(x, 1)
  constraint3.SetCoefficient(y, -1)

  # Define our objective: maximizing 3x + 4y.
  objective = solver.Objective()
  objective.SetCoefficient(x, 3)
  objective.SetCoefficient(y, 4)
  objective.SetMaximization()

  # Solve the system.
  status = solver.Solve()
  print 'x = ', x.solution_value()
  print 'y = ', y.solution_value()

if __name__ == '__main__':
  app.run()