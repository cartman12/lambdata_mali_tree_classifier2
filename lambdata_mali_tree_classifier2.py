def fit(X_train, y_train):
  from sklearn.metrics import accuracy_score
  import pandas as pd
  data = X_train.copy()
  assert len(data) == len(y_train)
  y_train = pd.DataFrame(list(y_train))
  data.index = range(len(data))
  concated_data = pd.concat([data,y_train],axis=1)
  majority_dict = {}
  list_majority_dict = []
  predictions = []
  concated_data_copy = concated_data.copy()
  for i in concated_data.columns[:-1]:
    len_i = len(concated_data[i].value_counts())
    for n in range(len_i):
      temp_dict = {}
      element = concated_data[i].value_counts().index[n]
      temp_data = concated_data[concated_data[i].isin([element])]
      if len(temp_data.iloc[:,-1].mode()) > 0:
        majority_class = temp_data.iloc[:,-1].mode()[0]
      else:
        majority_class = temp_data.iloc[:,-1].mode()
      temp_dict = {element: majority_class}
      concated_data_copy[i] = concated_data_copy[i].map(temp_dict)
      majority_dict.update(temp_dict)
    list_majority_dict.append(majority_dict) 
    
  for ind in concated_data_copy.index:
    row_prediction = concated_data_copy.iloc[ind].mode()[0]
    predictions.append(row_prediction)
      
  return accuracy_score(y_train, predictions), majority_dict    
def predict(X_test,y_test,majority_dict):
  from sklearn.metrics import accuracy_score
  import pandas as pd
  predictions = []
  data = X_test.copy()
  data.index = range(len(data))
  for i in data.columns:
    data[i] = data[i].map(majority_dict)
  for ind in data.index:
    
    row_prediction = data.iloc[ind].mode()[0]
    predictions.append(row_prediction)   
  return accuracy_score(y_test, predictions)