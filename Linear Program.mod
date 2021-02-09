set Student = 1 .. 18;
set Stop = 0 .. 9;
set Bus = 1 .. 5;

param n := card{Stop}-1;
set S := 1 .. n;
set SS := 1 .. 2**(n-1) - 1;
set POW{k in SS} := {i in S: (k div 2**i) mod 2 = 1};

param capacity >= 0;
param mdist{Stop, Stop};
param reach{Stop, Student};

var x{Bus, Stop, Stop} binary;     # 1 if bus k traverses the edge i-j, otherwise
var y{Bus, Stop} binary;           # 1 if bus k visits stop i, otherwise 0
var z{Student, Bus, Stop} binary;  # 1 if student s is picked up by bus k at stop i, otherwise 0

minimize total_distance:
sum{i in Stop, j in Stop, k in Bus} mdist[i,j] * x[k,i,j];



subject to StopisVisitedDef1{i in Stop, k in Bus}:
sum{j in Stop} x[k,i,j] = y[k,i];

subject to StopisVisitedDef2{i in Stop, k in Bus}:
sum{j in Stop} x[k,j,i] = sum{j in Stop} x[k,i,j];

# Each potential stop is visited at most once (0 is for school so it's excluded)
subject to VisitOnce{i in Stop: i!=0}: 
sum{k in Bus} y[k,i] <= 1;

# Each student is picked up at a stop they can reach.
subject to CanReach{s in Student, i in Stop}: 
sum{k in Bus} z[s,k,i] <= reach[i,s];

# The number of students must be less or equal to the capacity of the bus.
subject to BusCap{k in Bus}: 
sum{s in Student, i in Stop} z[s,k,i] <= capacity;

# If route/bus k does not visit stop i, student s is not picked up at stop i by bus k.
subject to NotVisited{s in Student, i in Stop, k in Bus}: 
z[s,k,i] <= y[k,i];

# Each student is picked up once.
subject to PickUpOnce{s in Student}: 
sum{k in Bus, i in Stop}z[s,k,i] = 1;

# the number of edges connecting the stops in the route of bus k must be 
# less or equal to the number of elements in subset q minus 1
subject to Connected{m in SS, k in Bus: m>=2}: 
sum{i in POW[m], j in POW[m]}x[k,i,j] <= card(POW[m])-1;
