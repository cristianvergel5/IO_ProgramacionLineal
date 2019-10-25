# import the library pulp as p 
import pulp as p 

var_desicion = int(input("¿Cuántas variables de decisión tiene el problema?: "))


Lp_prob = p.LpProblem('Problema', p.LpMaximize)

variables_decision = [ p.LpVariable(chr(i), lowBound = 0) for i in range(91-var_desicion, 91)]
print(variables_decision)


# Create a LP Minimization problem 
 
# Create problem Variables  
#x =    # Create a variable x >= 0 
#y = p.LpVariable("y", lowBound = 0)   # Create a variable y >= 0 
  
# Objective Function 
Lp_prob += 8 * variables_decision[0] + 10 * variables_decision[1]    
  
# Constraints: 
Lp_prob += 2 * variables_decision[0] + 3 * variables_decision[1] <= 600
Lp_prob += 2 * variables_decision[0] + variables_decision[1] <= 500
Lp_prob += 4 * variables_decision[1] <= 600
#Lp_prob += variables_decision[1] <= 3
  
# Display the problem 
print(Lp_prob) 
  
status = Lp_prob.solve()   # Solver 
print(p.LpStatus[status])   # The solution status 
  
# Printing the final solution 
print("Valor de  X :", p.value(variables_decision[0])) 
print("Valor de  Y :", p.value(variables_decision[1]))
print("Valor de  Z :", p.value(Lp_prob.objective))

