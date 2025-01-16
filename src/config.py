# config.py

class EpidemicConfig:
    def __init__(self, n_individuals=200, infection_radius=0.05, infection_prob=0.2, 
                 recovery_time=50, frames=200, death_prob=0.05):
        self.n_individuals = n_individuals
        self.infection_radius = infection_radius
        self.infection_prob = infection_prob
        self.recovery_time = recovery_time
        self.frames = frames
        self.death_prob = death_prob  

    def __repr__(self):
        return (f"EpidemicConfig(n_individuals={self.n_individuals}, "
                f"infection_radius={self.infection_radius}, infection_prob={self.infection_prob}, "
                f"recovery_time={self.recovery_time}, frames={self.frames}, "
                f"death_prob={self.death_prob})")
