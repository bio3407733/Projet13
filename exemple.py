# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 17:20:47 2016

@author: 3407733

"""
from TME2 import goalkeeper  
import soccersimulator
from  soccersimulator.settings import *
from soccersimulator import BaseStrategy, SoccerAction
from soccersimulator import SoccerTeam, SoccerMatch
from soccersimulator import Vector2D, Player, SoccerTournament
class RandomStrategy (BaseStrategy):
    def __init__(self):
        BaseStrategy.__init__(self,"Random")
    def compute_strategy(self,state , id_team, id_player):
        p_pos = state.player_state(id_team,id_player).position
        pose_de_bale=state.ball.position
        acc = pose_de_bale -p_pos
        shoot = Vector2D()
        if p_pos.distance(pose_de_bale)< PLAYER_RADIUS+BALL_RADIUS:
            if(id_team==1): 
                shoot = Vector2D(GAME_WIDTH,GAME_HEIGHT/2.)- pose_de_bale
            else:
                shoot = Vector2D(0,GAME_HEIGHT/2.)- pose_de_bale
        if ((id_team==1) and ((id_player=="Goalkeeper1")):
             if(me.distance(my_position)-me.distance(ball_position)<SEUIL):
                 acc=me.aller(me.but_position())
            
            
            
        """if(pose_de_bale==Vector((GAME_WiIDTH*3)/4),0) """       
                
        return SoccerAction(acc,shoot)


class GKStrategy (BaseStrategy):
    def __init__(self):
        BaseStrategy.__init__(self,"Random")
    def compute_strategy(self,state , id_team, id_player):
        p_pos = state.player_state(id_team,id_player).position
        pose_de_bale=state.ball.position
        acc = pose_de_bale -p_pos
        shoot = Vector2D()
        if p_pos.distance(pose_de_bale)< PLAYER_RADIUS+BALL_RADIUS:
            if(id_team==1): 
                shoot = Vector2D(GAME_WIDTH,GAME_HEIGHT/2.)- pose_de_bale
            else:
                shoot = Vector2D(0,GAME_HEIGHT/2.)- pose_de_bale
        if ((id_team==1) and ((id_player=="Goalkeeper1")):
             if(me.distance(my_position)-me.distance(ball_position)<SEUIL):
                 acc=me.aller(me.but_position())
            

        
team1= SoccerTeam("team1", [(Player("t1j1",RandomStrategy())),(Player("Goalkeeper1",RandomStrategy()))])
team2=SoccerTeam("team2", [(Player("t2j1",RandomStrategy())),(Player("Goalkeeper2",RandomStrategy()))])

match=SoccerMatch(team1, team2)
soccersimulator.show(match)
