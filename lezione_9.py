class FitIncrementModel(IncrementModel):

def fit(self, data):

    # Check data    
    self.check_data(data)

    # Compute global avg increment
    self.global_avg_increment = self.compute_avg_increment(data)

def predict(self, data):

    # Check data    
    self.check_data(data)

    local_avg_increment = self.compute_avg_increment(data)

    # Compute increment
    return data[-1] + (self.global_avg_increment + local_avg_increment)/2