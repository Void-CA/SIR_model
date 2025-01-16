from src.epidemic_simulation import EpidemicSimulation
from src.epidemic_visualization import EpidemicVisualization

if __name__ == "__main__":
    # Inicializar la simulación y la visualización
    simulation = EpidemicSimulation()
    visualization = EpidemicVisualization(simulation)
    
    # Mostrar la animación
    visualization.show()
