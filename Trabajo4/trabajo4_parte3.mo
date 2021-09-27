model trabajo4_parte3
  Modelica.Blocks.Continuous.TransferFunction transferFunction(a = {1, 4, 5}, b = {-4, -10})  annotation(
    Placement(visible = true, transformation(origin = {34, 56}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
  Modelica.Blocks.Sources.Sine sine(amplitude = 4, freqHz = 0.1591549431)  annotation(
    Placement(visible = true, transformation(origin = {-24, 56}, extent = {{-10, -10}, {10, 10}}, rotation = 0)));
equation
  connect(sine.y, transferFunction.u) annotation(
    Line(points = {{-12, 56}, {22, 56}}, color = {0, 0, 127}));
  annotation(
    uses(Modelica(version = "3.2.3")));

end trabajo4_parte3;