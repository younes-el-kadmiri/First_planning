from src.load import load_data
from src.clean import clean_data
from src.summary import show_stats, count_gender

def main():
    df = load_data("DataSet.csv")
    df = clean_data(df)

    print("🔹 Aperçu des données :")
    print(df.head())

    print("\n🔹 Statistiques descriptives :")
    show_stats(df)

    print("\n🔹 Répartition des genres :")
    count_gender(df)

if __name__ == "__main__":
    main()
