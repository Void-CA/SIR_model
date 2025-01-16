import numpy as np
from src.config import EpidemicConfig

class EpidemicSimulation:
    def __init__(self):
        config = EpidemicConfig()
        self.n_individuals = config.n_individuals
        self.infection_radius = config.infection_radius
        self.infection_prob = config.infection_prob
        self.recovery_time = config.recovery_time
        self.frames = config.frames
        self.death_prob = config.death_prob

        self.positions = np.random.rand(self.n_individuals, 2)
        self.velocities = (np.random.rand(self.n_individuals, 2) - 0.5) * 0.02
        self.states = np.zeros(self.n_individuals)  # 0: Healthy, 1: Infected, 2: Recovered, 3: Deceased
        self.infection_timers = np.zeros(self.n_individuals)
        self.states[np.random.randint(0, self.n_individuals)] = 1  # Some individual is infected

        self.infected_counts = []
        self.sane_counts = []
        self.recovered_counts = []
        self.deceased_counts = []  # Deaths

    def update(self, frame):
        # Actualizar posiciones (solo para individuos que no estén fallecidos)
        for i in range(self.n_individuals):
            if self.states[i] != 3:  # Si no está fallecido
                self.positions[i] += self.velocities[i]  # Actualizamos la posición
                self.positions[i] = np.mod(self.positions[i], 1)  # Condición de frontera periódica

        # Propagar la infección
        for i in range(self.n_individuals):
            if self.states[i] == 1:  # Si está infectado
                self.infection_timers[i] += 1

                # Verificar si muere (probabilidad cada 10 unidades de tiempo)
                if self.infection_timers[i] % 10 == 0:  # Cada 10 unidades de tiempo
                    if np.random.rand() < self.death_prob:
                        self.states[i] = 3  # Fallecido
                        self.velocities[i] = np.zeros(2)  # Detener el movimiento del fallecido

                # Verificar si se cura
                if self.infection_timers[i] > self.recovery_time:
                    self.states[i] = 2  # Recuperado

                # Propagar la infección a otros individuos
                for j in range(self.n_individuals):
                    if self.states[j] == 0:  # Si es susceptible
                        distance = np.linalg.norm(self.positions[i] - self.positions[j])
                        if distance < self.infection_radius and np.random.rand() < self.infection_prob:
                            self.states[j] = 1  # Se infecta

        # Actualizar estadísticas
        self.infected_counts.append(np.sum(self.states == 1))
        self.sane_counts.append(np.sum(self.states == 0))
        self.recovered_counts.append(np.sum(self.states == 2))
        self.deceased_counts.append(np.sum(self.states == 3))

        return self.positions, self.states, self.infected_counts, self.sane_counts, self.recovered_counts, self.deceased_counts
