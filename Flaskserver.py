from flask import Flask, jsonify
from Final import CityModel

city_model = CityModel(cars=17)

app = Flask(__name__)

@app.route("/car_position/<int:car_id>", methods=["GET"])
def get_car_position(car_id):
    car = next((car for car in city_model.cars_list if car.unique_id == -car_id), None)
    if not car:
        return jsonify({"error": "Car not found"}), 404

    return jsonify({
        "car_id": car.unique_id,
        "current_position": car.pos
    })

@app.route("/")
def index():
    return jsonify({"Message": "Hello from the Team 7"})

@app.route("/start_pos", methods=["GET", "POST"])
def start_pos():
    # Collect the updated positions of all cars
    car_positions = []
    for car in city_model.cars_list:
        car_positions.append({
            "car_id": car.unique_id,
            "start_parking": car.start_parking
        })
    
    print(f"Number of cars: {len(car_positions)}")
    # Return the updated positions of all cars
    return jsonify({
        "number_of_cars": len(city_model.cars_list),
        "car_positions": car_positions
    })

@app.route("/positions", methods=["GET", "POST"])
def positions():
    car_positions = []
    for car in city_model.cars_list:
        # Store the old position before calling city_model.step()
        old_position = {"x": car.pos[0], "y": car.pos[1]}
        print(f"Old position of car {car.unique_id}: {old_position}")
        
        # Append the car's id and its old position to the car_positions list
        car_positions.append({
            "car_id": car.unique_id,
            "old_position": old_position
        })
    # Update the positions by running the step function for all cars
    city_model.step()

    for car in city_model.cars_list:
        for car_pos in car_positions:
            if car_pos["car_id"] == car.unique_id:
                new_position = {"x": car.pos[0], "y": car.pos[1]}
                car_pos["new_position"] = new_position
    
    # Return the updated positions of all cars
    return jsonify({
        "number_of_cars": len(city_model.cars_list),
        "car_positions": car_positions
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)