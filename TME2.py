# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 16:23:35 2016

@author: 3407733
"""

import soccersimulator
from soccersimulator.settings import *
from soccersimulator import BaseStrategy, SoccerAction
from soccersimulator import SoccerTeam, SoccerMatch
from soccersimulator import Vector2D, Player, SoccerTournament


def maketeam1():
   return SoccerTeam("team1",[joueur1,joueur2,joueur3])
def fonceur(me):
  return  me.aller(me.ball_position)+me.shoot(me.but_adv)
def defonsseur (me):
p_pos = state.player_state(id_team,id_player).position
pose_de_bale=state.ball.position
acc = pose_de_bale -p_pos
shoot = Vector2D()

def goalkeeper(me):
    if(me.distance(my_position)-me.distance(ball_position)<SEUIL):
        return me.aller(me.but_position())
        


    
    
        
       """ return SoccerAction(vecteur_vitesse, vecteur_shoot)
        
        
        
    def position_joueur(self):
        return state.player_state(id_team,id_player).position
        
        
    def position_ball(self):
        return self.state.ball.position"""
        
     