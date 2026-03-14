# Importa o módulo random para usarmos funcionalidades aleatórias
import random

# 3 listas: uma de verbos, uma de adjetivo, e uma de substantivos
verbs = [
    "Leverage", "Sync", "Target",
    "Gamify", "Offline", "Crowd-sourced",
    "24/7", "Lean-in", "30,000 foot"
]
adjectives = [
    "A/B Tested", "Freemiun",
    "Hyperlocal", "Siloed", "B-to-B",
    "Oriented", "Cloud-based", "Api-based"
]
nouns = [
    "Early Adopter", "Low-hanging fruit",
    "Pipeline", "Splash Page", "Productivity",
    "Process", "Tipping point", "Paradigm"
]

# Escolha um verbo, um adjetivo e um substantivo de cada lista
verb = random.choice(verbs)
adjective = random.choice(adjectives)
noun = random.choice(nouns)

# Crie a frase concatenando as palavras
phrase = verb + " " + adjective + " " + noun

# Faça o output da frase
print(phrase)