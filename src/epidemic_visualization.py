import matplotlib.pyplot as plt
import matplotlib.animation as animation
from src.epidemic_simulation import EpidemicSimulation

class EpidemicVisualization:
    def __init__(self, simulation):
        self.simulation = simulation
        self.color_map = {0: 'green', 1: 'red', 2: 'blue', 3: 'black'}

        # Visualización
        self.fig, (self.ax_sim, self.ax_stats) = plt.subplots(1, 2, figsize=(12, 6))
        self.scatter = self.ax_sim.scatter(self.simulation.positions[:, 0], self.simulation.positions[:, 1],
                                           c=[self.color_map[state] for state in self.simulation.states], s=10)
        self.ax_sim.set_xlim(0, 1)
        self.ax_sim.set_ylim(0, 1)
        self.ax_sim.set_title("Simulación de Epidemia")

        self.line_infected, = self.ax_stats.plot([], [], label="Infectados", color="red")
        self.line_sane, = self.ax_stats.plot([], [], label="Sanos", color="green")
        self.line_recovered, = self.ax_stats.plot([], [], label="Recuperados", color="blue")
        self.line_deceased, = self.ax_stats.plot([], [], label="Fallecidos", color="black")
        self.ax_stats.set_xlim(0, self.simulation.frames)
        self.ax_stats.set_ylim(0, self.simulation.n_individuals)
        self.ax_stats.legend()
        self.ax_stats.set_title("Evolución de la Epidemia")

    def update(self, frame):
        positions, states, infected_counts, sane_counts, recovered_counts, deceased_counts = self.simulation.update(frame)

        # Actualizar visualización
        self.scatter.set_offsets(positions)
        self.scatter.set_color([self.color_map[state] for state in states])

        # Actualizar gráficos de evolución
        self.line_infected.set_data(range(len(infected_counts)), infected_counts)
        self.line_sane.set_data(range(len(sane_counts)), sane_counts)
        self.line_recovered.set_data(range(len(recovered_counts)), recovered_counts)
        self.line_deceased.set_data(range(len(deceased_counts)), deceased_counts)

        return self.scatter, self.line_infected, self.line_sane, self.line_recovered, self.line_deceased

    def show(self):
        ani = animation.FuncAnimation(self.fig, self.update, frames=self.simulation.frames, interval=50, blit=False)
        plt.show()
