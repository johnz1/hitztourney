#hitztourney.py


matchup = [];
players = ["Nick","Ziplox","Safa","Jeff","Magoo","Rosen","Ced","Rob","Adi","James","Bader","Koplow","Sean", "Arambula","Jesse"];
playerList = [];
for player in players:
  playerList.append({"name":player,"wins":0,"games":0});
tv=["Samsung","Sony"]

matchup.append( {"home":[2,10,8],"away":[14,1,5], "winners":[ ], "tv":tv[0]});
matchup.append( {"home":[15,12,9],"away":[11,3,7], "winners":[ ], "tv":tv[1]});
matchup.append( {"home":[3,6,9],"away":[15,2,1], "winners":[ ], "tv":tv[0]});
matchup.append( {"home":[11,13,10],"away":[12,4,8], "winners":[ ], "tv":tv[1]});
matchup.append( {"home":[4,7,10],"away":[11,3,2], "winners":[ ], "tv":tv[0]});
matchup.append( {"home":[12,14,6],"away":[13,5,9], "winners":[ ], "tv":tv[1]});
matchup.append( {"home":[5,8,6],"away":[12,4,3], "winners":[ ], "tv":tv[0]});
matchup.append( {"home":[13,15,7],"away":[14,1,10], "winners":[ ], "tv":tv[1]});
matchup.append( {"home":[1,9,7],"away":[13,5,4], "winners":[ ], "tv":tv[0]});
matchup.append( {"home":[14,11,8],"away":[15,2,6], "winners":[ ], "tv":tv[1]});
matchup.append( {"home":[7,11,6],"away":[10,1,5], "winners":[ ], "tv":tv[0]});
matchup.append( {"home":[4,15,9],"away":[2,14,12], "winners":[ ], "tv":tv[1]});
matchup.append( {"home":[8,12,7],"away":[6,2,1], "winners":[ ], "tv":tv[0]});
matchup.append( {"home":[5,11,10],"away":[3,15,13], "winners":[ ], "tv":tv[1]});
matchup.append( {"home":[9,13,8],"away":[7,3,2], "winners":[ ], "tv":tv[0]});
matchup.append( {"home":[1,12,6],"away":[4,11,14], "winners":[ ], "tv":tv[1]});
matchup.append( {"home":[10,14,9],"away":[8,4,3], "winners":[ ], "tv":tv[0]});
matchup.append( {"home":[2,13,7],"away":[5,12,15], "winners":[ ], "tv":tv[1]});
matchup.append( {"home":[6,15,10],"away":[9,5,4], "winners":[ ], "tv":tv[0]});
matchup.append( {"home":[3,14,8],"away":[1,13,11], "winners":[ ], "tv":tv[1]});
matchup.append( {"home":[8,15,1],"away":[12,9,10], "winners":[ ], "tv":tv[0]});
matchup.append( {"home":[13,2,14],"away":[6,3,5], "winners":[ ], "tv":tv[1]});
matchup.append( {"home":[9,11,2],"away":[13,10,6], "winners":[ ], "tv":tv[0]});
matchup.append( {"home":[14,3,15],"away":[7,4,1], "winners":[ ], "tv":tv[1]});
matchup.append( {"home":[10,12,3],"away":[14,6,7], "winners":[ ], "tv":tv[0]});
matchup.append( {"home":[15,4,11],"away":[8,5,2], "winners":[ ], "tv":tv[1]});
matchup.append( {"home":[6,13,4],"away":[15,7,8], "winners":[ ], "tv":tv[0]});
matchup.append( {"home":[11,5,12],"away":[9,1,3], "winners":[ ], "tv":tv[1]});
matchup.append( {"home":[7,14,5],"away":[11,8,9], "winners":[ ], "tv":tv[0]});
matchup.append( {"home":[12,1,13],"away":[10,2,4], "winners":[ ], "tv":tv[1]});

for i in len(matchup):
  print "Game "+ str(i+1) + " is " + playerList[matchup[i]["home"][0]-1]["name"] + ", " + playerList[matchup[i]["home"][1]-1]["name"] + ", and "+playerList[matchup[i]["home"][2]-1]["name"] +" against "+playerList[matchup[i]["away"][0]-1]["name"]+", "+playerList[matchup[i]["away"][1]-1]["name"]+", and " + playerList[matchup[i]["away"][2]-1]["name"] + "on the "+matchup[i]["tv"]+" TV"
