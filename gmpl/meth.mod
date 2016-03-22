set P := 1..3;
set W := 1..3;
set Ops dimen 2, within P cross W := {(1, 1), (2, 1), (2, 3), (3, 1), (3, 2), (3, 3)};
set W_Mass within W := {1, 2};
set W_Manual within W := W diff W_Mass;

set W_P{w in W} := setof {(i, w) in Ops} i;

param price{p in P};      # ���� �� ����� ���������, ���.
param demand{p in P};     # ����� � ������ �� ����� ���������, ��.
param cost{p in P};       # ������ ��������� �� ������������ ���������, ��
param prod{w in W_Mass};  # ������������������ �����, ��. � ������
param prod_m_cost{w in W_Manual, p in P};  # ������� ������� �� ������� 
                                           # ���������, ����
param prod_m{w in W_Manual};  # ���� �������� �������, ����
param materials;              # �������� ���������� � ������, ��

var x{p in P} >= 0;

s.t. mass{w in W_Mass}: sum{p in W_P[w]} x[p] <= prod[w];
s.t. manual{w in W_Manual}: sum{p in W_P[w]} x[p] * prod_m_cost[w, p] <= prod_m[w];
s.t. dem{p in P}: x[p] <= demand[p];
s.t. mat: sum{p in P} x[p] <= materials;

maximize profit : sum{p in P} price[p] * x[p];

solve;

display P;
display W;
display Ops;
display W_Mass;
display W_P;

end;
