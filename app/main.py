import read_csv
import grafica
import utils
import pandas as pd


def run():
    """
  data = list(filter(lambda item : item ["Continent"] == "South America",data))
  labels = list(map(lambda x: x["Country/Territory"],data))
  values = list(map(lambda x: x["World Population Percentage"], data))
  grafica.generate_pie_chart(labels, values)
  """
    df = pd.read_csv("data.csv")
    df = df[df["Continent"] == "South America"]
    labels = df["Country/Territory"].values
    values = df["World Population Percentage"].values
    grafica.generate_pie_chart(labels, values)

    data = read_csv.read_csv('data.csv')
    country = input("Escribe el pais =>").capitalize()
    result = utils.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        grafica.generate_bar_chart(country["Country/Territory"], labels, values)


if __name__ == "__main__":
    run()
