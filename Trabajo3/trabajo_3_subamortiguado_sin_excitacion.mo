model trabajo_3_subamortiguado_sin_excitacion
  Modelica.Mechanics.Translational.Components.Fixed fixed annotation(
    Placement(visible = true, transformation(origin = {0, 32}, extent = {{-10, -10}, {10, 10}}, rotation = 180)));
  Modelica.Mechanics.Translational.Components.Mass mass(m = 10, s(fixed = true, start = 1), v(fixed = true, start = 0))  annotation(
    Placement(visible = true, transformation(origin = {0, -38}, extent = {{-10, -10}, {10, 10}}, rotation = -90)));
  Modelica.Mechanics.Translational.Components.Spring spring(c = 1594.76)  annotation(
    Placement(visible = true, transformation(origin = {20, 0}, extent = {{-10, -10}, {10, 10}}, rotation = 90)));
  Modelica.Mechanics.Translational.Components.Damper damper(d = 25)  annotation(
    Placement(visible = true, transformation(origin = {-20, 0}, extent = {{-10, -10}, {10, 10}}, rotation = 90)));
equation
  connect(damper.flange_b, fixed.flange) annotation(
    Line(points = {{-20, 10}, {0, 10}, {0, 32}}, color = {0, 127, 0}));
  connect(spring.flange_b, fixed.flange) annotation(
    Line(points = {{20, 10}, {0, 10}, {0, 32}}, color = {0, 127, 0}));
  connect(mass.flange_a, spring.flange_a) annotation(
    Line(points = {{0, -28}, {20, -28}, {20, -10}}, color = {0, 127, 0}));
  connect(mass.flange_a, damper.flange_a) annotation(
    Line(points = {{0, -28}, {-20, -28}, {-20, -10}}, color = {0, 127, 0}));

annotation(
    uses(Modelica(version = "3.2.3")));
end trabajo_3_subamortiguado_sin_excitacion;