import mysql.connector

# MySQL-ə qoşulma və verilənlər bazası/cədvəl yaratma funksiyası
def create_database_table_and_insert():
    try:
        # MySQL serverə qoşul
        connection = mysql.connector.connect(
            host="localhost",  # Server ünvanı
            user="root",       # İstifadəçi adı
            password="2004Aytac@"  # Şifrə (özünüzə uyğun dəyişdirin)
        )
        cursor = connection.cursor()

        # Verilənlər bazasını yarat
        cursor.execute("CREATE DATABASE IF NOT EXISTS my_test_db")
        print("Verilənlər bazası 'my_test_db' uğurla yaradıldı.")

        # Verilənlər bazasına keç
        cursor.execute("USE my_test_db")  # Düzgün verilənlər bazasına keç

        # My_Test_Results cədvəlini yarat
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS My_Test_Results (
            id INT AUTO_INCREMENT PRIMARY KEY,      -- Unikal identifikator
            result VARCHAR(50),                     -- Test nəticəsi (Passed/Failed)
            test VARCHAR(255) NOT NULL,             -- Testin adı
            description TEXT,                       -- Testin təsviri
            duration FLOAT,                         -- Testin icra müddəti (saniyələrdə)
            links TEXT                              -- Əlaqədar linklər
        )
        """)
        print("Cədvəl 'My_Test_Results' uğurla yaradıldı.")

        # Cədvələ məlumatları daxil et
        insert_query = """
        INSERT INTO My_Test_Results (result, test, description, duration, links)
        VALUES 
        ('Failed', 'logo_width', 'Logo genişliyi səhvdir', 5.0, NULL),
        ('Failed', 'logo_height', 'Logo hündürlüyü səhvdir', 4.0, NULL),
        ('Failed', 'page_color', 'Səhifə fon rəngi düzgün deyil.', 5.0, NULL),
        ('Failed', 'font_size', 'Linkin şrift ölçüsü düzgün deyil', 5.0, NULL),
        ('Passed', 'table_css', NULL, 4.0, NULL),
        ('Passed', 'font_family', NULL, 46.0, NULL)
        """
        cursor.execute(insert_query)
        connection.commit()  # Dəyişiklikləri yadda saxla
        print("Məlumatlar 'My_Test_Results' cədvəlinə uğurla daxil edildi.")

    except mysql.connector.Error as err:
        print(f"MySQL Xətası: {err}")
    except Exception as e:
        print(f"Ümumi Xəta: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL bağlantısı bağlandı.")

# Funksiyanı işə sal
create_database_table_and_insert()
