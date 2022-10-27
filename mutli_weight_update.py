import random
import operator
import math
# Input Parameters
random.random()

L = 4
player_data = {"Najee":[10.9,10.1,8.9,8.6,8,100,100], "Ezekiel":[17.7,14.6,8.1,7.8,4.9,4.9], "Javonte":[8.8, 8.5, 6, 2.7, 1,1,20], "Mike":[17.3,14.6,13.4,12,7.5,1.7,1]}
names = list(player_data.keys())
scores = list(player_data.values())
n = len(names)  # number of experts
T = len(scores[0]) # time horizon
eps = (math.log(n)/T)**.5 # parameter epsilon

# Run the multiplicative weights update algorithm
def mWWUA():
  res = []
  count = 0
  weights = [1] * n
  lo = 1
  #weights is a list of nums that has a length of n
  # each asset's individual loss
  Loss = {"Najee":[],"Ezekiel":[],"Javonte":[],"Mike":[],"Algorithm":[]}
  weights = {"Najee":1,"Ezekiel":1,"Javonte":1,"Mike":1}
  #initialize cumulative loss
  for i in range(T-1):
    curr_loss = []
    if i == 0:
      #first round choose a player randomly
      k = random.randint(0,n-1)
      player_1 = names[k] #replace w/ week 1 data
      player_1 = player_data[player_1]
      #retrieve values at T=1 and at T=0
      #find loss
      correct_value = max(scores, key=lambda x: x[i])
      #curr_loss.append()
      #update weight
      #replace w/ wk2 data
      #pred_growth_values = list(map(operator.truediv, next_values, curr_values))
      #return pred_growth_values (next_values/current_values)
      pred = names[k]
      val = player_data[pred][i]
      #prediction is the random value
      #correct_value = pred_growth_values.index(max(pred_growth_values))
      correct_score = scores.index(correct_value)
      correct_name = names[correct_score]
      correct_predictor = player_data[correct_name][i]
      if pred != correct_name:
        #return Loss[]
        Loss["Algorithm"].append(math.log(val))
      else:
        Loss["Algorithm"].append(0)
      for name in names:
        if name != correct_name:
          val = pred_val = player_data[name][i]
          Loss[name].append(lo)
          weights[name] *= (1-(eps*Loss[name][i]/L))
        else:
          Loss[name].append(0)
      count += 1
    else:
        w = list(weights.values()) #list of all the weights
        w_index = w.index(max(w)) #index of the biggest weight
        max_weight_name = names[w_index] #name with index of biggest weight
        name_pred = weights[max_weight_name]
        weight_sum = sum(w)
        p = [player_weight/weight_sum for player_weight in w]
        #return p
        name_pred = random.choices(w, weights=p)[0]
       # return w, name_pred
        name_pred = w.index(name_pred)
        name_pred = names[name_pred]
        res.append(name_pred)
        pred_score = player_data[max_weight_name][i]
        correct_list = max(scores, key=lambda x: x[i])
        correct_value = max(scores, key=lambda x: x[i])[i]
       # return correct_value[i]
        correct_name = names[w_index]
        #update loss, weights
        #make new prediction
        if name_pred != correct_name:
        #return Loss[]
          Loss["Algorithm"].append(lo)
        else:
             Loss["Algorithm"].append(0)
        for name in names:
             if name != correct_name:
                val = player_data[name][i]
                if val < 5:
                  lo = -math.log(val)
                else:
                  lo = 0
                Loss[name].append(lo)
                weights[name] *= (1-(eps*Loss[name][i]/L))
             else:
                Loss[name].append(0)
  return res, weights
#add probability to it
print(mWWUA())

