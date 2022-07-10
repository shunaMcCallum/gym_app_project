from flask import Flask, render_template

from controllers.booking_controller import bookings_blueprint
from controllers.member_controller import members_blueprint
from controllers.workout_controller import workouts_blueprint

app = Flask(__name__)

app.register_blueprint(bookings_blueprint)
app.register_blueprint(members_blueprint)
app.register_blueprint(workouts_blueprint)

@app.route('/')
def home():
    route_name = "the gym"
    return render_template('index.html',route_name=route_name)

if __name__ == '__main__':
    app.run(debug=True)
    