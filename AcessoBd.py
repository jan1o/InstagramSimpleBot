import sqlite3

class AcessoBD:

    def AddPessoaMarcavel(self, nome):
        conn = sqlite3.connect('InstagramBot.db')
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO pessoasMarcaveis (nome)
        VALUES (?)
        """, (nome,))
        conn.commit()
        conn.close()

    def AddPessoaExcluida(self, nome):
        conn = sqlite3.connect('InstagramBot.db')
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO pessoasExcluidas (nome)
        VALUES (?)
        """, (nome,))
        conn.commit()
        conn.close()

    def ReadPessoasMarcaveis(self):
        conn = sqlite3.connect('InstagramBot.db')
        cursor = conn.cursor()

        cursor.execute("""
        SELECT nome FROM pessoasMarcaveis;
        """)
        return cursor.fetchall()

    def ReadPessoasExcluidas(self):
        conn = sqlite3.connect('InstagramBot.db')
        cursor = conn.cursor()

        cursor.execute("""
                SELECT nome FROM pessoasExcluidas;
                """)
        return cursor.fetchall()

    def LimparPessoasMarcaveis(self):
        conn = sqlite3.connect('InstagramBot.db')
        cursor = conn.cursor()

        cursor.execute("""
                        DELETE FROM pessoasMarcaveis;
                        """)
        conn.commit()
        conn.close()
