model trabajo1
Real Y(start=0);
Real Z(start=0);
equation
  der(Y)=(13/3)-3*Y;
equation
  der(Z)=(5/3)+(cos(time)/3)-(3*Z);
end trabajo1;
