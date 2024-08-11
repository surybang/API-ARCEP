from app.models import init_database, create_merged_data_table, get_search_data

if __name__ == "__main__":
    init_database()
    create_merged_data_table()
    print(get_search_data("06298"))
