import mesa
print(mesa.__version__)
from mesa.visualization import SolaraViz, make_space_component

from Final import CityModel
from Final import Car
from Final import SemaphoreAgent

def agent_portrayal(agent):
    alpha = 1.0
    
    if isinstance(agent, Car):
        marker = "o"
        size = 80
        color = "black"
    elif isinstance(agent, SemaphoreAgent):
        if agent.light_state == "red":
            color = "red"
            marker = "s"
            size = 100
            alpha = 0.7
        elif agent.light_state == "yellow":
            color = "yellow"
            marker = "s"
            size = 100
            alpha = 0.7
        elif agent.light_state == "green":
            color = "green"
            marker = "s"
            size = 100
            alpha = 0.7
    return {"size": size, "color": color, "marker": marker, "alpha": alpha}


# Configure property layers colors
propertylayer_portrayal = {
    "buildings": {"color": "blue", "colorbar": False},
    "parking_lots": {"color": "cyan", "colorbar": False},
    "roundabout": {"color": "tab:brown", "colorbar": False}
}

# Create initial instance of the model
model_params = {"cars": 17}
try:
    model1 = CityModel(cars=model_params["cars"])
except TypeError as e:
    print(f"Error creating CityModel: {e}")
    print("Please check the CityModel class definition and ensure it accepts 'cars' parameter correctly.")
    exit()

SpaceGraph = make_space_component(agent_portrayal, propertylayer_portrayal=propertylayer_portrayal)
page = SolaraViz(
    model1,
    components=[SpaceGraph],
    model_params=model_params,
    name="Integrative Activity - Team7",
)
page
