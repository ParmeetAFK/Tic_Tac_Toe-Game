import pygame
import random
from tkinter import *
from tkinter import messagebox

#TASKS
#Winning

board = [' ','_','_','_',
		'_','_','_',
		'_','_','_']

gate = True

pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 120)

win = pygame.display.set_mode((550,550))
pygame.display.set_caption("TIC-TAC-TOE")


		# All available empty positions
def emptypos(board):

	global valid_pos
	valid_pos = []
	for pos in range(1,10):
		if board[pos] == '_':
			valid_pos.append(pos)

def turn(board):
	global player
	nX = 0
	nO = 0

	for n in range(len(board)):
		if board[n] == 'X':
			nX = nX + 1

		elif board[n] == 'O':
			nO = nO + 1

		else:
			pass
	
	if len(valid_pos) == 0:
		gameover(board)
		print("Draw")

	elif len(valid_pos) == 9:
		player = 'X'

	elif nX > nO:
		player = 'O'
		AImove(board)

	elif nX == nO:
		player = 'X'

	return player

def dX(x,y):

	X = font.render('X', True, (255,0, 0))
	win.blit(X,(x,y))


def uplay(board,a):

	if a in valid_pos:
		board[a] = 'X'

	else:
		print("BITCH")
			

def dO(x,y):

	O = font.render('O', True, (0,255, 0))
	win.blit(O,(x,y))

		#Computer's turn who alwayss plays as O
def AImove(board):

	if len(valid_pos) == 0:
		print("Draw")
		gate = False

	else:

		b = random.choice(valid_pos)
		board[b] = 'O'

		if b == 1:
			dO(50,15)

		elif b == 2:
			dO(230,15)

		elif b == 3:
			dO(400,15)

		elif b == 4:
			dO(50,190)

		elif b == 5:
			dO(230,190)

		elif b == 6:
			dO(400,190)

		elif b == 7:
			dO(50,370)

		elif b == 8:
			dO(230,370)

		elif b == 9:
			dO(400,370)


def winner(board,player):

	win_list = [
			[board[1],board[2],board[3]],
			[board[4],board[5],board[6]],
			[board[7],board[8],board[9]],
			[board[1],board[4],board[7]],
			[board[2],board[5],board[8]],
			[board[3],board[6],board[9]],
			[board[1],board[5],board[9]],
			[board[3],board[5],board[7]]]

	if [player, player, player] in win_list:
		msg(player)
		gameover(board)

	else:
		pass

def gameover(board):
	globals()['gate'] = False

def but_wh(position):

	if first.collidepoint(pos):
		uplay(board,1)
		dX(50,15)

	elif second.collidepoint(pos):
		uplay(board,2)
		dX(230,15)
				

	elif third.collidepoint(pos):
		uplay(board,3)
		dX(400,15)
				

	elif fourth.collidepoint(pos):
		uplay(board,4)
		dX(50,190)
				

	elif fifth.collidepoint(pos):
		uplay(board,5)
		dX(230,190)
				

	elif sixth.collidepoint(pos):
		uplay(board,6)
		dX(400,190)
				

	elif seventh.collidepoint(pos):
		uplay(board,7)
		dX(50,370)
				

	elif eight.collidepoint(pos):
		uplay(board,8)
		dX(230,370)
				

	elif ninth.collidepoint(pos):
		uplay(board,9)
		dX(400,370)

def msg(player):
	messagebox.showinfo( "Winner",player + 'Has won the game')
				


def pyboard():

	global first,second,third,fourth,fifth,sixth,seventh,eight,ninth
	
			# ---Draw Board ----
	first = pygame.draw.rect(win , (255,255,255), (25,25,150,150))
	second = pygame.draw.rect(win , (255,255,255), (200,25,150,150))
	third = pygame.draw.rect(win , (255,255,255), (375,25,150,150))
	fourth = pygame.draw.rect(win , (255,255,255), (25,200,150,150))
	fifth = pygame.draw.rect(win , (255,255,255), (200,200,150,150))
	sixth = pygame.draw.rect(win , (255,255,255), (375,200,150,150))
	seventh = pygame.draw.rect(win , (255,255,255), (25,375,150,150))
	eight = pygame.draw.rect(win , (255,255,255), (200,375,150,150))
	ninth = pygame.draw.rect(win , (255,255,255), (375,375,150,150))

pyboard()
while gate:
	pygame.display.update()
	pygame.time.delay(100)
	
	for event in pygame.event.get():
		emptypos(board)
		turn(board)
		if event.type == pygame.QUIT:
			pygame.quit()

		if event.type == pygame.MOUSEBUTTONUP:
			pos = pygame.mouse.get_pos()
			but_wh(pos)
			pygame.display.update()
			winner(board,player)

			if gate == False:
				pass

			else:
				emptypos(board)
				turn(board)
				winner(board,player)

pygame.time.delay(1000)
pygame.quit()