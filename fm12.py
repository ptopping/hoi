available = roster[['Name','Position','Rating']].set_index(['Name','Position'])
selection = pulp.LpVariable.dicts("selection",((name, position) for name, position in available.index),cat='Binary')

model = pulp.LpProblem("LineUp Selection", pulp.LpMaximize)

model += pulp.lpSum([selection[name, position] * available.loc[(name, position), 'Ratings'] for name, position in available.index]

# Players may only be selected once
for name,position in available.index:
    model += selection[(player, position)] <= 1

# Only one player per position
for name,position in available.index:
    model += selection[(player, position)] <= 1                    
                    
model.solve()
pulp.LpStatus[model.status]
