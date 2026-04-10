import pandas as pd


def calculate_demographic_data(print_data=True):
    # Cargar el dataset en un DataFrame de pandas
    df = pd.read_csv("adult.data.csv")

    # Q1: ¿Cuántas personas hay de cada raza?
    # value_counts() cuenta cuántas veces aparece cada valor en la columna "race"
    race_count = df["race"].value_counts()

    # Q2: ¿Cuál es la edad promedio de los hombres?
    # Se filtran las filas donde sex == "Male", se toma la columna age y se calcula el promedio
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)

    # Q3: ¿Qué porcentaje de personas tiene título de Bachelors?
    # La comparación devuelve True/False; mean() calcula la proporción de True; luego se multiplica por 100
    percentage_bachelors = round((df["education"] == "Bachelors").mean() * 100, 1)

    # Q4: ¿Qué porcentaje de personas con educación avanzada gana más de 50K?
    # Educación avanzada: Bachelors, Masters o Doctorate
    higher_education = df[df["education"].isin(["Bachelors", "Masters", "Doctorate"])]

    # Q5: ¿Qué porcentaje de personas sin educación avanzada gana más de 50K?
    # Se niega la condición anterior con ~ para tomar el resto
    lower_education = df[~df["education"].isin(["Bachelors", "Masters", "Doctorate"])]

    # Calcular porcentaje >50K dentro del grupo con educación avanzada
    higher_education_rich = round((higher_education["salary"] == ">50K").mean() * 100, 1)

    # Calcular porcentaje >50K dentro del grupo sin educación avanzada
    lower_education_rich = round((lower_education["salary"] == ">50K").mean() * 100, 1)

    # Q6: ¿Cuál es el mínimo de horas trabajadas por semana?
    min_work_hours = df["hours-per-week"].min()

    # Q7: ¿Qué porcentaje de las personas que trabajan el mínimo de horas gana más de 50K?
    # Se filtran solo las personas que trabajan el mínimo de horas
    num_min_workers = df[df["hours-per-week"] == min_work_hours]

    # Se calcula el porcentaje >50K dentro de ese grupo
    rich_percentage = round((num_min_workers["salary"] == ">50K").mean() * 100, 1)

    # Q8: ¿Qué país tiene el mayor porcentaje de personas que ganan más de 50K?
    # Se agrupa por país y se calcula el porcentaje >50K en cada grupo
    country_stats = df.groupby("native-country")["salary"].apply(
        lambda x: (x == ">50K").mean() * 100
    )

    # País con el porcentaje más alto
    highest_earning_country = country_stats.idxmax()

    # Porcentaje más alto redondeado a 1 decimal
    highest_earning_country_percentage = round(country_stats.max(), 1)

    # Q9: ¿Cuál es la ocupación más común de quienes ganan >50K en India?
    # Se filtran personas de India con salario >50K, se toma occupation y se busca la más frecuente
    top_IN_occupation = df[
        (df["native-country"] == "India") & (df["salary"] == ">50K")
    ]["occupation"].value_counts().idxmax()

    # Retornar los resultados en el formato esperado por FreeCodeCamp
    return {
        "race_count": race_count,
        "average_age_men": float(average_age_men),
        "percentage_bachelors": float(percentage_bachelors),
        "higher_education_rich": float(higher_education_rich),
        "lower_education_rich": float(lower_education_rich),
        "min_work_hours": int(min_work_hours),
        "rich_percentage": float(rich_percentage),
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": float(highest_earning_country_percentage),
        "top_IN_occupation": top_IN_occupation
    }