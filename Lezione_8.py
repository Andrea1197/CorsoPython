class Model():
    def fit(self, data):
        raise NotImplementedError('Metodo non implementato')
    def predict(self, data):
        raise NotImplementedError('Metodo non implementato')

class IncrementModel(Model):
    def predict(self, data):
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