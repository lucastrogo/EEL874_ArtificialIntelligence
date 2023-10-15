import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Cria as variáveis de entrada
avaliacao = ctrl.Antecedent(np.arange(0, 11, 1), 'avaliacao')
popularidade = ctrl.Antecedent(np.arange(0, 11, 1), 'popularidade')
preferencia_genero = ctrl.Antecedent(np.arange(0, 11, 1), 'preferencia_genero')

# Cria a variável de saída
recomendacao = ctrl.Consequent(np.arange(0, 11, 1), 'recomendacao')

# Define funções de pertinência para as variáveis de entrada e saída
avaliacao.automf(3)
popularidade.automf(3)
preferencia_genero.automf(3)

recomendacao['baixa'] = fuzz.trimf(recomendacao.universe, [0, 0, 5])
recomendacao['média'] = fuzz.trimf(recomendacao.universe, [0, 5, 10])
recomendacao['alta'] = fuzz.trimf(recomendacao.universe, [5, 10, 10])

# Regras Fuzzy
regra1 = ctrl.Rule(avaliacao['poor'] | popularidade['poor'] | preferencia_genero['poor'], recomendacao['baixa'])
regra2 = ctrl.Rule(avaliacao['average'] & popularidade['average'] & preferencia_genero['average'], recomendacao['média'])
regra3 = ctrl.Rule(avaliacao['good'] | popularidade['good'] | preferencia_genero['good'], recomendacao['alta'])

# Cria o sistema de controle
sistema_controle = ctrl.ControlSystem([regra1, regra2, regra3])

# Cria a simulação
simulacao = ctrl.ControlSystemSimulation(sistema_controle)

# Defina os valores de entrada
simulacao.input['avaliacao'] = 7.5
simulacao.input['popularidade'] = 6.0
simulacao.input['preferencia_genero'] = 8.0

# Calcule a recomendação
simulacao.compute()

# Obtenha o valor de recomendação
recomendacao_final = simulacao.output['recomendacao']

# Visualize a recomendação
print("Recomendação: {:.2f}".format(recomendacao_final))
