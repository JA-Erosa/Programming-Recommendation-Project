#Book exercises (ipynb tries)
import dictionary as d
print(d.critics['Lisa Rose']['Lady in the Water'])
d.critics['Toby']['Snakes on a Plane']=4.5
print(d.critics['Toby'])
from math import sqrt
print(sqrt(pow(5-4,2)+pow(4-1,2)))
print(1/(1+sqrt(pow(5-4,2)+pow(4-1,2))))
#euclidean distance (0-1)
print("Euclidean dist",d.sim_distance(d.critics,'Lisa Rose','Gene Seymour'))
print(d.sim_distance(d.critics,'Lisa Rose','Michael Phillips'))
print(d.sim_distance(d.critics,'Lisa Rose','Claudia Puig'))
print(d.sim_distance(d.critics,'Lisa Rose','Mick LaSalle'))
print(d.sim_distance(d.critics,'Lisa Rose','Jack Matthews'))
print(d.sim_distance(d.critics,'Lisa Rose','Toby'))
#Pearson r (-1 - 1)
print("Pearson",d.sim_pearson(d.critics,'Lisa Rose','Gene Seymour'))
#Top critics matches delimited by n
print("TopCritics",d.topMatches(d.critics, 'Toby', n=6))
#Recommendations using pearson
print("RecPear",d.getRecommendations(d.critics,'Toby'))
#Recommendations using euclidean
print("recEu",d.getRecommendations(d.critics, 'Toby', similarity=d.sim_distance))
