# **Multi-Agent-Traffic-Simulation**

This project uses **Mesa** and **Solara** to create an interactive visualization for a traffic simulation. It demonstrates the behavior of cars and semaphores in a city model, with visualizations dynamically generated based on agent states.

---

## **How to Run**

### **Prerequisites**
Ensure you have the following installed:  
- Python (3.8 or later)  
- Anaconda (for virtual environment management)  
- Required Python libraries (install them using the commands below).  

### **Setup and Installation**
1. **Clone the Repository**  
   Download or clone the repository where the `visualization.py` file is located.

2. **Create a Virtual Environment (optional but recommended)**  
   ```bash
   conda create -n city_model_env python=3.9
   conda activate city_model_env

3. **Install required Libraries**
   pip install mesa==1.1.0
   pip install solara
   pip install matplotlib
   pip install numpy

4. **Verify Mesa Installation and Version**
   import mesa
   print(mesa.__version__)

5. **Run Visualization**
   solara run visualization.py


## About the Simulation

### Agents
- **Cars**: Represented by black circles (`"o"`).
- **Semaphores**: Represented by squares (`"s"`) with colors indicating light states:
  - **Red**: Semaphore is closed for vehicles.
  - **Yellow**: Semaphore is about to change states.
  - **Green**: Semaphore is open for vehicles.

### Property Layers
- **Buildings**: Blue.
- **Parking Lots**: Cyan.
- **Roundabouts**: Brown.

### Parameters
- The model runs with `17` cars by default.
- You can adjust this in the `model_params` section of the script.
