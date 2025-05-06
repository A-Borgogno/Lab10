from database.DB_connect import DBConnect
from model.country import Country


class DAO():

    @staticmethod
    def getAllNodes(anno):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        res = []

        query = """select c.*
                    from country c, contiguity c2
                    where c.CCode = c2.state1no
                    and c2.`year` < %s
                    group by c.CCode """

        cursor.execute(query, (anno,))

        for row in cursor:
            res.append(Country(**row))

        cursor.close()
        conn.close()
        return res


    @staticmethod
    def getEdges(anno):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        res = []

        query = """select c2.state1no as s1, c2.state2no as s2
                    from contiguity c2
                    where c2.state1no < c2.state2no
                    and c2.conttype = 1
                    and c2.`year` < %s"""

        cursor.execute(query, (anno,))

        for row in cursor:
            res.append((row["s1"], row["s2"]))

        cursor.close()
        conn.close()
        return res
