from WOWS.WOWS_RDS import wows_database


class rds(object):
    def __init__(self):
        self.db = wows_database()

    def __del__(self):
        self.db.close_db()

    def update_winRate(self):
        sql = """UPDATE `wows_stats`
        SET `winRate` = `win` / `total`
        WHERE (`accountID` <> 0 AND `total` IS NOT NULL)"""
        self.db.execute_single(sql=sql)

    def get_detail(self, total_thres=100):
        sql = """SELECT * FROM wowstats.wows_stats
        WHERE (`total` > %d AND `winRate` is not null)""" % total_thres
        detail = self.db.execute_single(sql=sql)
        print(detail)
