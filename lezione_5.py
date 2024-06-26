class NumericalCSVFile(CSVFile):

    def get_data(self):

        # Chiamo la get_data del genitore 
        string_data = super().get_data()

        # Preparo lista per contenere i dati ma in formato numerico
        numerical_data = []

        # Ciclo su tutte le "righe" corrispondenti al file originale 
        for string_row in string_data:

            # Preparo una lista di supporto per salvare la riga
            # in "formato" nuumerico (tranne il primo elemento)
            numerical_row = []

            # Ciclo su tutti gli elementi della riga con un
            # enumeratore: cosi' ho gratis l'indice "i" della
            # posizione dell'elemento nella riga.
            for i,element in enumerate(string_row):

                if i == 0:
                    # Il primo elemento della riga lo lascio in formato stringa
                    numerical_row.append(element)

                else:
                    # Converto a float tutto gli altri. Ma se fallisco, stampo
                    # l'errore e rompo il ciclo (e poi saltero' la riga).
                    try:
                        numerical_row.append(float(element))
                    except Exception as e:
                        print('Errore in conversione del valore "{}" a numerico: "{}"'.format(element, e))
                        break

            # Alla fine aggiungo la riga in formato numerico alla lista
            # "esterna", ma solo se sono riuscito a processare tutti gli
            # elementi. Qui controllo per la lunghezza, ma avrei anche potuto
            # usare una variabile di supporto o fare due break in cascata.
            if len(numerical_row) == len(string_row):
                numerical_data.append(numerical_row)

        return numerical_data