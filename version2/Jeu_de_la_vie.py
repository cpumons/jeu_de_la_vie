import pygame
from pygame.locals import *
from random import choice

class Cellule():

	def __init__(self,x,y, game):
		self.number = 0
		self.x = x
		self.y = y
		self.game = game
		self.alive = False

class GameMain():

	def __init__(self,width = 1920, height = 1080):
		pygame.mixer.pre_init(44100, -16, 2, 2048)
		pygame.init()
		self.width, self.height = width, height
		pygame.display.set_caption("Jeu de la vie")
		infoObject = pygame.display.Info()
		self.screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h), pygame.FULLSCREEN)
		self.clock = pygame.time.Clock()
		self.done = False
		self.ticker = 0
		self.title_screen = 0
		self.background1 = pygame.image.load("ecran_titre/ecran_titre1.jpg").convert()
		self.background2 = pygame.image.load("ecran_titre/ecran_titre2.jpg").convert()
		self.background3 = pygame.image.load("ecran_titre/ecran_titre3.jpg").convert()
		self.background4 = pygame.image.load("ecran_titre/ecran_titre4.jpg").convert()
		self.background_list = [self.background1,self.background2,self.background3,self.background4]
		self.current_screen = "title"
		self.current_game = None
		self.height_grid = 43
		self.width_grid = 77
		self.grid = []
		self.create_grid()
		self.pause = False
		self.speed = 10		

	def main_loop(self):
		while not self.done:
			if self.current_screen == "game":
				if self.current_game == "libre":
					if not self.pause :
						self.reload_grid()
						self.draw_game()
					self.handle_events()
				
				if self.current_game == "classique":
					self.draw_classique()
					self.handle_events_classique()

			elif self.current_screen == "title":
				self.draw_title()
				self.update_title()
				self.handle_events_title()

			self.ticker += 1
			self.clock.tick(60)

	def draw_game(self):
		self.screen.fill((160,160,160))
		for x in range(self.width_grid):
			for y in range(self.height_grid):
				if not self.grid[x][y].alive :
					pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.grid[x][y].x, self.grid[x][y].y, 20, 20))
				else :
					pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(self.grid[x][y].x, self.grid[x][y].y, 20, 20))
				self.grid[x][y].number = 0
		pygame.display.flip()

	def draw_title(self):
		self.screen.fill((0,0,0))
		self.background = self.background_list[self.title_screen]
		self.screen.blit(self.background,(0,0))
		pygame.display.flip()

	def draw_classique(self):
		self.screen.fill((0,0,0))
		self.background = pygame.image.load("classique/classique.jpg").convert()
		self.screen.blit(self.background,(0,0))
		pygame.display.flip()

	def create_grid(self):
		for x in range(self.width_grid):
			posx = x * 25
			posy = 25
			tab = []
			for y in range(self.height_grid) :
				tab.append(Cellule((posx),(posy) * y, self))
			self.grid.append(tab)
			
	def update_title(self):
		if self.ticker % (self.speed * 3 ) == 0:
			self.title_screen = (self.title_screen + 1) % 4

	def handle_events_title(self):
		events = pygame.event.get()
		for event in events:
			if event.type == pygame.QUIT:
				self.done = True
			if event.type == KEYDOWN:
				if event.key == K_F4:
					self.done = True
			if event.type == MOUSEMOTION :
				self.mousepos = event.pos
			if event.type == MOUSEBUTTONDOWN :
				x, y = self.mousepos
				if 742 < x < 1177 and 490 < y < 590 :
					self.current_game = "libre"
					self.current_screen = "game"
					self.draw_game()
				if 742 < x < 1177 and 667 < y < 767 :
					self.current_game = "classique"
					self.current_screen = "game"

	def handle_events_classique(self):
		events = pygame.event.get()
		for event in events:
			if event.type == pygame.QUIT:
				self.done = True
			if event.type == KEYDOWN:
				if event.key == K_F4:
					self.done = True
				if event.key == K_ESCAPE:
					self.current_screen = "title"
					self.speed = 10
					self.refresh()
					self.draw_game()
			if event.type == MOUSEMOTION :
				self.mousepos = event.pos
			if event.type == MOUSEBUTTONDOWN :
				x, y = self.mousepos
				self.refresh()
				self.pause = True
				if 214 < x < 429 and 122 < y < 337 :
					self.canon_a_glisseurs()
					self.current_game = "libre"
					self.draw_game()
				if 644 < x < 859 and 122 < y < 337 :
					self.vaisseau()
					self.current_game = "libre"
					self.draw_game()
				if 1073 < x < 1288 and 122 < y < 337 :
					self.oscillateur()
					self.current_game = "libre"
					self.draw_game()
				if 1499 < x < 1714 and 122 < y < 337 :
					self.galaxie()
					self.current_game = "libre"			
					self.draw_game()
				if 214 < x < 429 and 568 < y < 783 :
					self.ligne()
					self.current_game = "libre"	
					self.draw_game()
				if 644 < x < 859 and 568 < y < 783 :
					self.puffeur()
					self.current_game = "libre"	
					self.draw_game()
				if 1073 < x < 1288 and 568 < y < 783 :
					self.mathusalem()
					self.current_game = "libre"
					self.draw_game()
				if 1499 < x < 1714 and 568 < y < 783 :
					self.jardin_eden()
					self.current_game = "libre"			
					self.draw_game()

	def handle_events(self):
		events = pygame.event.get()
		for event in events:
			if event.type == pygame.QUIT:
				self.done = True
			if event.type == KEYDOWN:
				if event.key == K_F4:
					self.done = True
				if event.key == K_p:
					self.pause = not self.pause
				if event.key == K_r and self.pause:
					self.refresh()
					self.draw_game()
				if event.key == K_w:
					self.speed = 60
				if event.key == K_x:
					self.speed = 10
				if event.key == K_c:
					self.speed = 5
				if event.key == K_v:
					self.speed = 1
				if event.key == K_ESCAPE:
					self.current_screen = "title"
					self.speed = 10
					self.refresh()
					self.draw_game()
				if event.key == K_b:
					self.refresh()
					self.jardin_eden()
					self.draw_game()
				if event.key == K_g and self.pause :
					self.refresh()
					self.random_grid()
					self.draw_game()
				if event.key == K_s:
					for i in range(self.width_grid) :
						for j in range(self.height_grid) :
							if self.grid[i][j].alive :
								with open ("grille1.data", "a") as fic :
									fic.write("self.grid[" + str(i) + "][" + str(j) + "].alive = True \n")
			if event.type == MOUSEMOTION:
				self.mousepos = event.pos
			if event.type == MOUSEBUTTONDOWN and self.pause :
				x, y = self.mousepos
				i = x // 25
				j = y // 25
				self.grid[i][j].alive = not self.grid[i][j].alive
				self.draw_game()

	def reload_grid(self) :
		if (self.ticker % self.speed) == 0 :
			for i in range(self.width_grid) :
				for j in range(self.height_grid) :
					if self.grid[i][j].alive :
						for k in range(-1, 2) :
							for l in range(-1, 2) :
								if k != 0 or l != 0 :
									if 0 <= i+k < self.width_grid and 0 <= j+l < self.height_grid :
										self.grid[i+k][j+l].number += 1
			for i in range(self.width_grid) :
				for j in range(self.height_grid) :
					if self.grid[i][j].alive :
						if not (self.grid[i][j].number in [2, 3]) :
							self.grid[i][j].alive = False
					else :
						if self.grid[i][j].number == 3 :
							self.grid[i][j].alive = True
						
	def refresh(self):
		for x in range(self.width_grid):
			for y in range(self.height_grid):
				self.grid[x][y].alive = False

	def random_grid(self) :
		for x in range(self.width_grid) :
			for y in range(self.height_grid) :
				self.grid[x][y].alive = choice([True, False, False, False])






	def oscillateur(self):
		self.grid[10][18].alive = True 
		self.grid[11][17].alive = True 
		self.grid[11][18].alive = True 
		self.grid[11][19].alive = True 
		self.grid[12][15].alive = True 
		self.grid[12][16].alive = True 
		self.grid[12][17].alive = True 
		self.grid[12][19].alive = True 
		self.grid[12][20].alive = True 
		self.grid[12][21].alive = True 
		self.grid[13][15].alive = True 
		self.grid[13][21].alive = True 
		self.grid[14][14].alive = True 
		self.grid[14][15].alive = True 
		self.grid[14][21].alive = True 
		self.grid[14][22].alive = True 
		self.grid[15][13].alive = True 
		self.grid[15][14].alive = True 
		self.grid[15][22].alive = True 
		self.grid[15][23].alive = True 
		self.grid[16][14].alive = True 
		self.grid[16][15].alive = True 
		self.grid[16][21].alive = True 
		self.grid[16][22].alive = True 
		self.grid[17][15].alive = True 
		self.grid[17][21].alive = True 
		self.grid[18][15].alive = True 
		self.grid[18][16].alive = True 
		self.grid[18][17].alive = True 
		self.grid[18][19].alive = True 
		self.grid[18][20].alive = True 
		self.grid[18][21].alive = True 
		self.grid[19][17].alive = True 
		self.grid[19][18].alive = True 
		self.grid[19][19].alive = True 
		self.grid[20][18].alive = True 
		self.grid[30][18].alive = True 
		self.grid[30][22].alive = True 
		self.grid[30][23].alive = True 
		self.grid[31][17].alive = True 
		self.grid[31][18].alive = True 
		self.grid[31][19].alive = True 
		self.grid[31][22].alive = True 
		self.grid[31][23].alive = True 
		self.grid[32][15].alive = True 
		self.grid[32][16].alive = True 
		self.grid[32][17].alive = True 
		self.grid[32][19].alive = True 
		self.grid[32][20].alive = True 
		self.grid[32][21].alive = True 
		self.grid[33][15].alive = True 
		self.grid[33][21].alive = True 
		self.grid[34][14].alive = True 
		self.grid[34][15].alive = True 
		self.grid[34][21].alive = True 
		self.grid[34][22].alive = True 
		self.grid[35][13].alive = True 
		self.grid[35][14].alive = True 
		self.grid[35][22].alive = True 
		self.grid[35][23].alive = True 
		self.grid[36][14].alive = True 
		self.grid[36][15].alive = True 
		self.grid[36][21].alive = True 
		self.grid[36][22].alive = True 
		self.grid[37][15].alive = True 
		self.grid[37][21].alive = True 
		self.grid[38][15].alive = True 
		self.grid[38][16].alive = True 
		self.grid[38][17].alive = True 
		self.grid[38][19].alive = True 
		self.grid[38][20].alive = True 
		self.grid[38][21].alive = True 
		self.grid[39][17].alive = True 
		self.grid[39][18].alive = True 
		self.grid[39][19].alive = True 
		self.grid[40][18].alive = True 
		self.grid[51][13].alive = True 
		self.grid[51][14].alive = True 
		self.grid[51][18].alive = True 
		self.grid[51][22].alive = True 
		self.grid[51][23].alive = True 
		self.grid[52][13].alive = True 
		self.grid[52][14].alive = True 
		self.grid[52][17].alive = True 
		self.grid[52][18].alive = True 
		self.grid[52][19].alive = True 
		self.grid[52][22].alive = True 
		self.grid[52][23].alive = True 
		self.grid[53][15].alive = True 
		self.grid[53][16].alive = True 
		self.grid[53][17].alive = True 
		self.grid[53][19].alive = True 
		self.grid[53][20].alive = True 
		self.grid[53][21].alive = True 
		self.grid[54][15].alive = True 
		self.grid[54][21].alive = True 
		self.grid[55][14].alive = True 
		self.grid[55][15].alive = True 
		self.grid[55][21].alive = True 
		self.grid[55][22].alive = True 
		self.grid[56][13].alive = True 
		self.grid[56][14].alive = True 
		self.grid[56][22].alive = True 
		self.grid[56][23].alive = True 
		self.grid[57][14].alive = True 
		self.grid[57][15].alive = True 
		self.grid[57][21].alive = True 
		self.grid[57][22].alive = True 
		self.grid[58][15].alive = True 
		self.grid[58][21].alive = True 
		self.grid[59][15].alive = True 
		self.grid[59][16].alive = True 
		self.grid[59][17].alive = True 
		self.grid[59][19].alive = True 
		self.grid[59][20].alive = True 
		self.grid[59][21].alive = True 
		self.grid[60][13].alive = True 
		self.grid[60][14].alive = True 
		self.grid[60][17].alive = True 
		self.grid[60][18].alive = True 
		self.grid[60][19].alive = True 
		self.grid[60][22].alive = True 
		self.grid[60][23].alive = True 
		self.grid[61][13].alive = True 
		self.grid[61][14].alive = True 
		self.grid[61][18].alive = True 
		self.grid[61][22].alive = True 
		self.grid[61][23].alive = True 




	def ligne(self):
		self.grid[20][21].alive = True 
		self.grid[21][21].alive = True 
		self.grid[22][21].alive = True 
		self.grid[23][21].alive = True 
		self.grid[24][21].alive = True 
		self.grid[25][21].alive = True 
		self.grid[26][21].alive = True 
		self.grid[28][21].alive = True 
		self.grid[29][21].alive = True 
		self.grid[30][21].alive = True 
		self.grid[31][21].alive = True 
		self.grid[32][21].alive = True 
		self.grid[36][21].alive = True 
		self.grid[37][21].alive = True 
		self.grid[38][21].alive = True 
		self.grid[42][21].alive = True 
		self.grid[43][21].alive = True 
		self.grid[44][21].alive = True 
		self.grid[45][21].alive = True 
		self.grid[46][21].alive = True 
		self.grid[48][21].alive = True 
		self.grid[49][21].alive = True 
		self.grid[50][21].alive = True 
		self.grid[51][21].alive = True 
		self.grid[52][21].alive = True 
		self.grid[53][21].alive = True 
		self.grid[54][21].alive = True 
		self.grid[20][21].alive = True 
		self.grid[21][21].alive = True 
		self.grid[22][21].alive = True 
		self.grid[23][21].alive = True 
		self.grid[24][21].alive = True 
		self.grid[25][21].alive = True 
		self.grid[26][21].alive = True 
		self.grid[28][21].alive = True 
		self.grid[29][21].alive = True 
		self.grid[30][21].alive = True 
		self.grid[31][21].alive = True 
		self.grid[32][21].alive = True 
		self.grid[36][21].alive = True 
		self.grid[37][21].alive = True 
		self.grid[38][21].alive = True 
		self.grid[45][21].alive = True 
		self.grid[46][21].alive = True 
		self.grid[47][21].alive = True 
		self.grid[48][21].alive = True 
		self.grid[49][21].alive = True 
		self.grid[50][21].alive = True 
		self.grid[51][21].alive = True 
		self.grid[53][21].alive = True 
		self.grid[54][21].alive = True 
		self.grid[55][21].alive = True 
		self.grid[56][21].alive = True 
		self.grid[57][21].alive = True 




	def vaisseau(self) :
		self.grid[7][29].alive = True 
		self.grid[7][31].alive = True 
		self.grid[8][28].alive = True 
		self.grid[9][13].alive = True 
		self.grid[9][15].alive = True 
		self.grid[9][28].alive = True 
		self.grid[9][32].alive = True 
		self.grid[10][12].alive = True 
		self.grid[10][28].alive = True 
		self.grid[10][32].alive = True 
		self.grid[11][12].alive = True 
		self.grid[11][28].alive = True 
		self.grid[12][12].alive = True 
		self.grid[12][15].alive = True 
		self.grid[12][28].alive = True 
		self.grid[12][31].alive = True 
		self.grid[13][12].alive = True 
		self.grid[13][13].alive = True 
		self.grid[13][14].alive = True 
		self.grid[13][28].alive = True 
		self.grid[13][29].alive = True 
		self.grid[13][30].alive = True 







	def canon_a_glisseurs(self):
		self.grid[3][9].alive = True 
		self.grid[3][10].alive = True 
		self.grid[4][9].alive = True 
		self.grid[4][10].alive = True 
		self.grid[8][11].alive = True 
		self.grid[8][12].alive = True 
		self.grid[13][7].alive = True 
		self.grid[13][8].alive = True 
		self.grid[13][12].alive = True 
		self.grid[13][13].alive = True 
		self.grid[14][8].alive = True 
		self.grid[14][9].alive = True 
		self.grid[14][10].alive = True 
		self.grid[14][11].alive = True 
		self.grid[14][12].alive = True 
		self.grid[15][8].alive = True 
		self.grid[15][9].alive = True 
		self.grid[15][11].alive = True 
		self.grid[15][12].alive = True 
		self.grid[16][8].alive = True 
		self.grid[16][9].alive = True 
		self.grid[16][11].alive = True 
		self.grid[16][12].alive = True 
		self.grid[17][9].alive = True 
		self.grid[17][10].alive = True 
		self.grid[17][11].alive = True 
		self.grid[25][8].alive = True 
		self.grid[26][7].alive = True 
		self.grid[26][8].alive = True 
		self.grid[26][9].alive = True 
		self.grid[27][6].alive = True 
		self.grid[27][7].alive = True 
		self.grid[27][8].alive = True 
		self.grid[27][9].alive = True 
		self.grid[27][10].alive = True 
		self.grid[28][5].alive = True 
		self.grid[28][7].alive = True 
		self.grid[28][9].alive = True 
		self.grid[28][11].alive = True 
		self.grid[29][5].alive = True 
		self.grid[29][6].alive = True 
		self.grid[29][10].alive = True 
		self.grid[29][11].alive = True 
		self.grid[32][8].alive = True 
		self.grid[33][7].alive = True 
		self.grid[33][9].alive = True 
		self.grid[34][7].alive = True 
		self.grid[34][9].alive = True 
		self.grid[35][8].alive = True 
		self.grid[36][7].alive = True 
		self.grid[36][8].alive = True 
		self.grid[37][7].alive = True 
		self.grid[37][8].alive = True 
		self.grid[38][7].alive = True 
		self.grid[38][8].alive = True 


	def galaxie(self):
		self.grid[14][18].alive = True 
		self.grid[14][19].alive = True 
		self.grid[15][18].alive = True 
		self.grid[15][19].alive = True 
		self.grid[17][18].alive = True 
		self.grid[17][19].alive = True 
		self.grid[17][20].alive = True 
		self.grid[17][21].alive = True 
		self.grid[18][17].alive = True 
		self.grid[18][22].alive = True 
		self.grid[18][24].alive = True 
		self.grid[18][25].alive = True 
		self.grid[19][17].alive = True 
		self.grid[19][19].alive = True 
		self.grid[19][20].alive = True 
		self.grid[19][22].alive = True 
		self.grid[19][24].alive = True 
		self.grid[19][25].alive = True 
		self.grid[20][14].alive = True 
		self.grid[20][15].alive = True 
		self.grid[20][17].alive = True 
		self.grid[20][18].alive = True 
		self.grid[20][22].alive = True 
		self.grid[21][14].alive = True 
		self.grid[21][15].alive = True 
		self.grid[21][17].alive = True 
		self.grid[21][22].alive = True 
		self.grid[22][18].alive = True 
		self.grid[22][19].alive = True 
		self.grid[22][20].alive = True 
		self.grid[22][21].alive = True 
		self.grid[24][20].alive = True 
		self.grid[24][21].alive = True 
		self.grid[25][20].alive = True 
		self.grid[25][21].alive = True 
		self.grid[32][16].alive = True 
		self.grid[32][17].alive = True 
		self.grid[32][18].alive = True 
		self.grid[32][19].alive = True 
		self.grid[32][20].alive = True 
		self.grid[32][21].alive = True 
		self.grid[32][23].alive = True 
		self.grid[32][24].alive = True 
		self.grid[33][16].alive = True 
		self.grid[33][17].alive = True 
		self.grid[33][18].alive = True 
		self.grid[33][19].alive = True 
		self.grid[33][20].alive = True 
		self.grid[33][21].alive = True 
		self.grid[33][23].alive = True 
		self.grid[33][24].alive = True 
		self.grid[34][23].alive = True 
		self.grid[34][24].alive = True 
		self.grid[35][16].alive = True 
		self.grid[35][17].alive = True 
		self.grid[35][23].alive = True 
		self.grid[35][24].alive = True 
		self.grid[36][16].alive = True 
		self.grid[36][17].alive = True 
		self.grid[36][23].alive = True 
		self.grid[36][24].alive = True 
		self.grid[37][16].alive = True 
		self.grid[37][17].alive = True 
		self.grid[37][23].alive = True 
		self.grid[37][24].alive = True 
		self.grid[38][16].alive = True 
		self.grid[38][17].alive = True 
		self.grid[39][16].alive = True 
		self.grid[39][17].alive = True 
		self.grid[39][19].alive = True 
		self.grid[39][20].alive = True 
		self.grid[39][21].alive = True 
		self.grid[39][22].alive = True 
		self.grid[39][23].alive = True 
		self.grid[39][24].alive = True 
		self.grid[40][16].alive = True 
		self.grid[40][17].alive = True 
		self.grid[40][19].alive = True 
		self.grid[40][20].alive = True 
		self.grid[40][21].alive = True 
		self.grid[40][22].alive = True 
		self.grid[40][23].alive = True 
		self.grid[40][24].alive = True 
		self.grid[47][18].alive = True 
		self.grid[47][19].alive = True 
		self.grid[48][18].alive = True 
		self.grid[48][19].alive = True 
		self.grid[50][18].alive = True 
		self.grid[50][19].alive = True 
		self.grid[50][20].alive = True 
		self.grid[50][21].alive = True 
		self.grid[51][17].alive = True 
		self.grid[51][19].alive = True 
		self.grid[51][22].alive = True 
		self.grid[51][24].alive = True 
		self.grid[51][25].alive = True 
		self.grid[52][17].alive = True 
		self.grid[52][21].alive = True 
		self.grid[52][22].alive = True 
		self.grid[52][24].alive = True 
		self.grid[52][25].alive = True 
		self.grid[53][14].alive = True 
		self.grid[53][15].alive = True 
		self.grid[53][17].alive = True 
		self.grid[53][20].alive = True 
		self.grid[53][22].alive = True 
		self.grid[54][14].alive = True 
		self.grid[54][15].alive = True 
		self.grid[54][17].alive = True 
		self.grid[54][22].alive = True 
		self.grid[55][18].alive = True 
		self.grid[55][19].alive = True 
		self.grid[55][20].alive = True 
		self.grid[55][21].alive = True 
		self.grid[57][20].alive = True 
		self.grid[57][21].alive = True 
		self.grid[58][20].alive = True 
		self.grid[58][21].alive = True 

	def puffeur(self):
		self.grid[6][15].alive = True 
		self.grid[6][17].alive = True 
		self.grid[6][24].alive = True 
		self.grid[6][29].alive = True 
		self.grid[6][31].alive = True 
		self.grid[7][14].alive = True 
		self.grid[7][20].alive = True 
		self.grid[7][23].alive = True 
		self.grid[7][28].alive = True 
		self.grid[8][14].alive = True 
		self.grid[8][21].alive = True 
		self.grid[8][22].alive = True 
		self.grid[8][23].alive = True 
		self.grid[8][28].alive = True 
		self.grid[9][14].alive = True 
		self.grid[9][17].alive = True 
		self.grid[9][28].alive = True 
		self.grid[9][31].alive = True 
		self.grid[10][14].alive = True 
		self.grid[10][15].alive = True 
		self.grid[10][16].alive = True 
		self.grid[10][28].alive = True 
		self.grid[10][29].alive = True 
		self.grid[10][30].alive = True 





	def mathusalem(self):
		self.grid[33][21].alive = True 
		self.grid[34][19].alive = True 
		self.grid[34][21].alive = True 
		self.grid[36][20].alive = True 
		self.grid[37][21].alive = True 
		self.grid[38][21].alive = True 
		self.grid[39][21].alive = True 


	def jardin_eden(self):
		self.grid[31][21].alive = True 
		self.grid[31][25].alive = True 
		self.grid[31][26].alive = True 
		self.grid[32][17].alive = True 
		self.grid[32][20].alive = True 
		self.grid[32][21].alive = True 
		self.grid[32][22].alive = True 
		self.grid[32][23].alive = True 
		self.grid[32][24].alive = True 
		self.grid[33][18].alive = True 
		self.grid[33][19].alive = True 
		self.grid[33][21].alive = True 
		self.grid[33][22].alive = True 
		self.grid[33][23].alive = True 
		self.grid[33][24].alive = True 
		self.grid[33][25].alive = True 
		self.grid[34][17].alive = True 
		self.grid[34][19].alive = True 
		self.grid[34][20].alive = True 
		self.grid[34][21].alive = True 
		self.grid[34][23].alive = True 
		self.grid[34][25].alive = True 
		self.grid[34][26].alive = True 
		self.grid[35][17].alive = True 
		self.grid[35][18].alive = True 
		self.grid[35][20].alive = True 
		self.grid[35][21].alive = True 
		self.grid[35][22].alive = True 
		self.grid[35][24].alive = True 
		self.grid[35][25].alive = True 
		self.grid[35][26].alive = True 
		self.grid[36][18].alive = True 
		self.grid[36][19].alive = True 
		self.grid[36][20].alive = True 
		self.grid[36][22].alive = True 
		self.grid[36][23].alive = True 
		self.grid[36][24].alive = True 
		self.grid[37][17].alive = True 
		self.grid[37][18].alive = True 
		self.grid[37][19].alive = True 
		self.grid[37][22].alive = True 
		self.grid[37][24].alive = True 
		self.grid[37][25].alive = True 
		self.grid[38][17].alive = True 
		self.grid[38][19].alive = True 
		self.grid[38][20].alive = True 
		self.grid[38][21].alive = True 
		self.grid[38][23].alive = True 
		self.grid[38][25].alive = True 
		self.grid[38][26].alive = True 
		self.grid[39][18].alive = True 
		self.grid[39][20].alive = True 
		self.grid[39][21].alive = True 
		self.grid[39][22].alive = True 
		self.grid[39][25].alive = True 
		self.grid[40][18].alive = True 
		self.grid[40][19].alive = True 
		self.grid[40][20].alive = True 
		self.grid[40][21].alive = True 
		self.grid[40][24].alive = True 
		self.grid[40][26].alive = True 
		self.grid[41][17].alive = True 
		self.grid[41][18].alive = True 
		self.grid[41][21].alive = True 
		self.grid[41][23].alive = True 
		self.grid[41][24].alive = True 
		self.grid[41][25].alive = True 
		self.grid[41][27].alive = True 
		self.grid[42][19].alive = True 
		self.grid[42][20].alive = True 
		self.grid[42][22].alive = True 
		self.grid[42][26].alive = True 


if __name__ == "__main__":
	game = GameMain()
	game.main_loop()
