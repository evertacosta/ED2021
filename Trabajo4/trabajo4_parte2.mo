model trabajo4_parte2
  Modelica.Mechanics.Translational.Components.Fixed fixed annotation(
    Placement(visible = true, transformation(origin = {0, 68}, extent = {{-10, -10}, {10, 10}}, rotation = 180)));
  Modelica.Mechanics.Translational.Components.Mass mass(m = 10, s(fixed = false), v(fixed = false))  annotation(
    Placement(visible = true, transformation(origin = {0, 10}, extent = {{-10, -10}, {10, 10}}, rotation = -90)));
  Modelica.Mechanics.Translational.Components.Spring spring(c = 1595)  annotation(
    Placement(visible = true, transformation(origin = {20, 46}, extent = {{-10, -10}, {10, 10}}, rotation = 90)));
  Modelica.Mechanics.Translational.Components.Damper damper(d = 25)  annotation(
    Placement(visible = true, transformation(origin = {-22, 46}, extent = {{-10, -10}, {10, 10}}, rotation = 90)));
  Modelica.Mechanics.Translational.Sources.ForceStep forceStep(startTime = 2, stepForce = 1500)  annotation(
    Placement(visible = true, transformation(origin = {-38, -16}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Continuous.TransferFunction transferFunction(a = {10, 25, 1595}, b = {1})  annotation(
    Placement(visible = true, transformation(origin = {20, -64}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Sources.Step step(height = 1500, startTime = 2)  annotation(
    Placement(visible = true, transformation(origin = {-36, -64}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
equation
  connect(damper.flange_b, fixed.flange) annotation(
    Line(points = {{-22, 56}, {0, 56}, {0, 68}}, color = {0, 127, 0}));
  connect(spring.flange_b, fixed.flange) annotation(
    Line(points = {{20, 56}, {0, 56}, {0, 68}}, color = {0, 127, 0}));
  connect(mass.flange_a, spring.flange_a) annotation(
    Line(points = {{0, 20}, {20, 20}, {20, 36}}, color = {0, 127, 0}));
  connect(mass.flange_a, damper.flange_a) annotation(
    Line(points = {{0, 20}, {-22, 20}, {-22, 36}}, color = {0, 127, 0}));
  connect(forceStep.flange, mass.flange_b) annotation(
    Line(points = {{-28, -16}, {0, -16}, {0, 0}}, color = {0, 127, 0}));
  connect(step.y, transferFunction.u) annotation(
    Line(points = {{-24, -64}, {8, -64}}, color = {0, 0, 127}));
  annotation(
    uses(Modelica(version = "3.2.3")));
end trabajo4_parte2;