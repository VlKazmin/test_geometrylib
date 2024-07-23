from pyspark.sql import SparkSession

# Создаем SparkSession
spark = SparkSession.builder.master("local[*]").getOrCreate()

# Пример данных
product_data = [
    (1, "ProductA"),
    (2, "ProductB"),
    (3, "ProductC"),
    (4, "ProductD"),
]

categories_data = [
    (10, "CategoryA"),
    (20, "CategoryB"),
    (30, "CategoryC"),
]

product_category_data = [
    (1, 10),
    (1, 20),
    (2, 20),
    (3, 30),
]

# Создаем DataFrame из данных
products_df = spark.createDataFrame(product_data, ["product_id", "product_name"])
categories_df = spark.createDataFrame(categories_data, ["category_id", "category_name"])
product_category_df = spark.createDataFrame(product_category_data, ["product_id", "category_id"])

# Регистрация временных таблиц
products_df.createOrReplaceTempView("products_df")
categories_df.createOrReplaceTempView("categories_df")
product_category_df.createOrReplaceTempView("product_category_df")

# Запрос продукты – категория
query_product_name_category_name = """
SELECT
    p.product_name, c.category_name
FROM
    product_category_df pc
JOIN 
    products_df p ON p.product_id = pc.product_id
JOIN
    categories_df c ON c.category_id = pc.category_id
"""

# Запрос продукты без категории
query_without_category = """
SELECT
    p.product_name
FROM 
    products_df p
LEFT JOIN
    product_category_df pc ON p.product_id = pc.product_id
WHERE
    pc.product_id IS NULL   
"""

def main():
    print("Все пары 'Имя продукта – Имя категории':")
    spark.sql(query_product_name_category_name).orderBy("product_name").show()

    print("Имя продукта без категории:")
    spark.sql(query_without_category).show()

if __name__ == "__main__":
    main()
