# Lezione 8
from collections.abc import ItemsView


class Model():
    
    def fit(self, data):
        # Fit non implementato nella classe base
        raise NotImplementedError('Metodo non implementato')
    def predict(self, data):
        # Predict non implementato nella classe base
        raise NotImplementedError('Metodo non implementato')
        

class IncrementModel(Model):
    
    def predict(self, data):

        # Check data type
        if not isistance(data, list):
            raise TypeError('Data "{}" is not of type list (got "{}").format(data, data.__class__.__name__))
        else:
            # Check data items type
            for item in data:
                if not (isinstance(item, int) or isinstance(item, float)):    
                     raise TypeError('Iteam"{}" if not of type int or float (got "{}")'.format(item, item.__class__.__name__))

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
        return data[-1] + avg_increment



        
        prev_value = None
        differenza=[]
        for item in data:
            if prev_value is None: 
                prev_value=item
            else:
                valore=(item-prev_value)/2
                differenza.append(valore)
        prediction=(sum(differenza))+item
        return prediction

lista = [0,2,10]

increment_model = IncrementModel()
prediction_value = increment_model.predict(lista)
print(prediction_value)