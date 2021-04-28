model trabajo2
Real Y(start=0);
equation
der(Y) = if time < 2 then 5 -((3/2)*Y) else -(1/2)*Y;

end trabajo2;