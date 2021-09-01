model trabajo_3_subamortiguado_con_excitacion
  Modelica.Mechanics.Translational.Components.Fixed fixed annotation(
    Placement(visible = true, transformation(origin = {0, 20}, extent = {{-10, -10}, {10, 10}}, rotation = 180)));
  Modelica.Mechanics.Translational.Components.Mass mass(m = 10, s(fixed = true, start = 1), v(fixed = true, start = 0))  annotation(
    Placement(visible = true, transformation(origin = {0, -34}, extent = {{-10, -10}, {10, 10}}, rotation = -90)));
  Modelica.Mechanics.Translational.Components.Spring spring(c = 1594.76)  annotation(
    Placement(visible = true, transformation(origin = {20, 0}, extent = {{-10, -10}, {10, 10}}, rotation = 90)));
  Modelica.Mechanics.Translational.Components.Damper damper(d = 25)  annotation(
    Placement(visible = true, transformation(origin = {-20, 0}, extent = {{-10, -10}, {10, 10}}, rotation = 90)));
  Modelica.Mechanics.Translational.Sources.Force force annotation(
    Placement(visible = true, transformation(origin = {-24, -54}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Sources.Step step(height = 1500, startTime = 2)  annotation(
    Placement(visible = true, transformation(origin = {-80, -58}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
equation
  connect(mass.flange_a, spring.flange_a) annotation(
    Line(points = {{0, -24}, {20, -24}, {20, -10}}, color = {0, 127, 0}));
  connect(mass.flange_a, damper.flange_a) annotation(
    Line(points = {{0, -24}, {-20, -24}, {-20, -10}}, color = {0, 127, 0}));
  connect(damper.flange_b, fixed.flange) annotation(
    Line(points = {{-20, 10}, {0, 10}, {0, 20}}, color = {0, 127, 0}));
  connect(spring.flange_b, fixed.flange) annotation(
    Line(points = {{20, 10}, {0, 10}, {0, 20}}, color = {0, 127, 0}));
  connect(force.flange, mass.flange_b) annotation(
    Line(points = {{-14, -54}, {0, -54}, {0, -44}}, color = {0, 127, 0}));
  connect(force.f, step.y) annotation(
    Line(points = {{-36, -54}, {-68, -54}, {-68, -58}}, color = {0, 0, 127}));
  annotation(
    uses(Modelica(version = "3.2.3")));
end trabajo_3_subamortiguado_con_excitacion;