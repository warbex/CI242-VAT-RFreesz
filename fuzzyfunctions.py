#Trapeze Functions
def trap_desc(c,d,ass,x):
    if x <= c:
        return ass
    elif x >= d:
        return 0
    else:
        return ass*(d-x)/(d-c)
    
def trap_asc(a,b,ass,x):
    if x <= a:
        return 0
    elif x >= b:
        return ass
    else:
        return ass*(x-a)/(b-a)
    
def trap_full(a,b,c,d,ass,x):
    if x <= a or x >= d:
        return 0
    elif x > a and x < b:
        return ass*(x-a)/(b-a)
    elif x > c and x < d:
        return ass*(d-x)/(d-c)
    else:
        return ass

#Triangle Functions
def tri_desc(m,b,x):
    if x < m or x > b:
        return 0
    else:
        return (b-x)/(b-m)
    
def tri_asc(a,m,x):
    if x < a or x > m:
        return 0
    else:
        return (x-a)/(m-a)
    
def tri_full(a,b,m,x):
    if x >= a and x <= m:
        return (x-a)/(m-a)
    elif x > m and x < b:
        return (b-x)/(b-m)
    else:
        return 0

#Funções reversas pra encontrar pontos a,b,c,d
#Vira um trap_asc
def reverse_tri_asc(group, trigged_rule):
    new_b = group.a + trigged_rule.values[-1]*(group.m-group.a)
    group.b = new_b
    group.m = ""
    group.ass = trigged_rule.values[-1]
    group.f_type="trap_asc"
    group.define_f()

#Vira um trap_desc
def reverse_tri_desc(group, trigged_rule):
    new_c = group.b - trigged_rule.values[-1]*(group.b-group.m)
    group.c = new_c
    group.d = group.b
    group.b = ""
    group.m = ""
    group.ass = trigged_rule.values[-1]
    group.f_type="trap_desc"
    group.define_f()
    
#Vira um trap_full
def reverse_tri_full(group, trigged_rule):
    new_b = group.a + trigged_rule.values[-1]*(group.m-group.a)
    new_c = group.b - trigged_rule.values[-1]*(group.b-group.m)
    group.c = new_c
    group.d = group.b
    group.b = new_b
    group.m = ""
    group.ass = trigged_rule.values[-1]
    group.f_type="trap_full"
    group.define_f()

#Vira um trap_asc
def reverse_trap_asc(group, trigged_rule):
    new_b = group.a + trigged_rule.values[-1]*(group.b-group.a)
    group.b = new_b
    group.ass = trigged_rule.values[-1]

#Vira um trap_desc
def reverse_trap_desc(group, trigged_rule):
    new_c = group.d - trigged_rule.values[-1]*(group.d-group.c)
    group.c = new_c
    group.ass = trigged_rule.values[-1]

#Vira um trap_full
def reverse_trap_full(group, trigged_rule):
    new_c = group.b + trigged_rule.values[-1]*(group.b-group.m)
    new_b = group.a + trigged_rule.values[-1]*(group.b-group.a)
    group.b = new_b
    group.c = new_c
    group.ass = trigged_rule.values[-1]