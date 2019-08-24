available = roster[['Name','Position','Rating']].set_index(['Name','Position'])
selection = pulp.LpVariable.dicts("selection",((n, p) for n, p in available.index),cat='Binary')

model = pulp.LpProblem("LineUp Selection", pulp.LpMaximize)

model += pulp.lpSum([selection[n, p] * roster.loc[(n, p), 'Ratings'] for n, p in available.index]

# Production in any month must be equal to demand
months = demand.index
for month in months:
    model += production[(month, 'A')] + production[(month, 'B')] == demand.loc[month, 'Demand']

model.solve()
pulp.LpStatus[model.status]
