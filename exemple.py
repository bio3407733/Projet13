# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 17:20:47 2016

@author: 3407733

"""
import soccersimulator
from  soccersimulator.settings import *
from soccersimulator import AbstractStrategy, SoccerAction
from soccersimulator import SoccerTeam, SoccerMatch
from soccersimulator import Vector2D, Player, SoccerTournament
class RandomStrategy (AbstractStrategy):
    def __init__(self):
        AbstractStrategy.__init__(self,"Random")
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

        return SoccerAction(acc,shoot)
        
team1= SoccerTeam("team1", [Player("t1j1",RandomStrategy())])
team2=SoccerTeam("team2", [Player("t2j1",RandomStrategy())])
team3= SoccerTeam("team3", [Player("t3j1",RandomStrategy())])
match=SoccerMatch(team1, team2)
soccersimulator.show(match)
