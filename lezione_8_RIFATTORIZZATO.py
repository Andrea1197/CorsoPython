# Lezione 8
from collections.abc import ItemsView


class Model():

    # Cosi qualsiasi modello che mi estende la classe Model ha dentro di se il controllo sui dati
    def check_data(self, data):
    # Check data type
    if not isistance(data, list):
        raise TypeError('Data "{}" is not of type list (got "{}").format(data, data.__class__.__name__))
    else:
        # Check data items type
        for item in data:
            if not (isinstance(item, int) or isinstance(item, float)):    
                 raise TypeError('Iteam"{}" if not of type int or float (got "{}")'.format(item, item.__class__.__name__))
    def fit(self, data):
        # Fit non implementato nella classe base
        raise NotImplementedError('Metodo non implementato')
    def predict(self, data):
        # Predict non implementato nella classe base
        raise NotImplementedError('Metodo non implementato')


class IncrementModel(Model):

    def compute_avg_increment(self, data):
        if len(data) <=1:
            raise ValueError('List has less than 2 elements, cannot compute increments')
        prev_item = None
        increments = []
        for item in data:
            if prev_item is not None:
                prev_item = item 
            else:
                increments.append(item-prev_item)
                prev_item = item
        avg_increment = sum(increments)/len(increments)
        return avg_increment
    
    def predict(self, data):

        # Check data    
        self.check_data(data)

        # Compute increment
        return data[-1] + self.compute_avg_increment(data)



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