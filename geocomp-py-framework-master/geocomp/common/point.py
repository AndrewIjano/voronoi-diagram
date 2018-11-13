#!/usr/bin/env python

from . import control
from geocomp import config

class Point:
	"Um ponto representado por suas coordenadas cartesianas"

	def __init__ (self, x, y, z=None):
		"Para criar um ponto, passe suas coordenadas."
		self.x = x
		self.y = y
		self.z = z
		self.lineto_id = {}

	################# ANDREW E EDUARDO MUDARAM ##############
	def plot (self, color=config.COLOR_POINT, radius=config.RADIUS):
		"Desenha o ponto na cor especificada"
		self.plot_id = control.plot_disc (self.x, self.y, color, radius)
		return self.plot_id
	######################### FIM ##########################

    ################### VICTOR MUDOU #######################

	def unplot(self, id = None):
		if id == None: id = self.plot_id
		control.plot_delete(id)



	################## FIM ############################

	def hilight (self, color=config.COLOR_HI_POINT):
		"Desenha o ponto com 'destaque' (raio maior e cor diferente)"
		self.hi = control.plot_disc (self.x, self.y, color,
						config.RADIUS_HILIGHT)
		return self.hi

	def unhilight (self, id = None):
		"Apaga o 'destaque' do ponto"
		if id == None: id = self.hi
		control.plot_delete (id)

	def lineto (self, p, color=config.COLOR_LINE):
		"Desenha uma linha ate um ponto p na cor especificada"
		self.lineto_id[p] = control.plot_line (self.x, self.y, p.x, p.y, color)
		return self.lineto_id[p]

	def remove_lineto (self, p, id = None):
		"Apaga a linha ate o ponto p"
		if id == None: id = self.lineto_id[p]
		control.plot_delete (id)
