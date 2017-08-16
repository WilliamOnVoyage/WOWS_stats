import flask

from database.db_connector import DatabaseConnector

app = flask.Flask(__name__)
# app.config['IMAGE_STORE_BASE_URL'] = 'http://127.0.0.1:5000/'
# app.config['IMAGE_STORE_PATH'] = '/pics'
image_store_config = app.config.get_namespace('IMAGE_STORE_')
DB_TYPE = 'mongo'


@app.route('/')
def index():
    return flask.render_template("WOWS_Stats.html")


@app.route('/databaseinfo')
def get_database_info():
    battle_threshold = flask.request.args.get('battles', 0, type=int)
    active_player_number = DatabaseConnector(database_type=DB_TYPE).get_database_info(threshold=battle_threshold)
    return flask.jsonify(active_player_number=active_player_number)


@app.route('/overallstats')
def get_overall_stats():
    battle_threshold = flask.request.args.get('battles', 0, type=int)
    player_list = DatabaseConnector(database_type=DB_TYPE).get_top_players_by_battles(threshold=battle_threshold)
    return flask.jsonify(player_list=player_list)


if __name__ == '__main__':
    app.run(debug=False)
