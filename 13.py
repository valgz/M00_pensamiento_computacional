#ENTRADA

investment = float(input('Inversión: '))
interest_p = float(input('Interes anual: '))
years = float(input('Años transcurridos: '))
compound_frequency = int(input('Numero de veces que se acumula el interés por año: '))

#PROCESO

interest = interest_p / 100

future_value = investment * (1 + (interest / compound_frequency)) ** (compound_frequency * years)

#SALIDA

print("{:.2f}€ invertidos al {} % durante {} años con {} períodos de imposición por año se transforman en {:.2f}€ ".format(investment, interest_p, years, compound_frequency, future_value))






