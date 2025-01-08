import pygame
import sys
MainClock = pygame.time.Clock()
pygame.display.set_caption("WHITE TO MOVE")
pygame.display.set_icon(pygame.image.load(r"Images\WhiteKing.png"))
screen = pygame.display.set_mode((647, 600))

white_pawn_image = pygame.image.load(r"Images\WhitePawn.png").convert_alpha()
white_knight_image = pygame.image.load(r"Images\WhiteKnight.png").convert_alpha()
white_bishop_image = pygame.image.load(r"Images\WhiteBishop.png").convert_alpha()
white_rook_image = pygame.image.load(r"Images\WhiteRook.png").convert_alpha()
white_queen_image = pygame.image.load(r"Images\WhiteQueen.png").convert_alpha()
white_king_image = pygame.image.load(r"Images\WhiteKing.png").convert_alpha()

black_pawn_image = pygame.image.load(r"Images\BlackPawn.png").convert_alpha()
black_knight_image = pygame.image.load(r"Images\BlackKnight.png").convert_alpha()
black_bishop_image = pygame.image.load(r"Images\BlackBishop.png").convert_alpha()
black_rook_image = pygame.image.load(r"Images\BlackRook.png").convert_alpha()
black_queen_image = pygame.image.load(r"Images\BlackQueen.png").convert_alpha()
black_king_image = pygame.image.load(r"Images\BlackKing.png").convert_alpha()

piece_key = {"P" : white_pawn_image,
             "N" : white_knight_image,
             "B" : white_bishop_image,
             "R" : white_rook_image,
             "Q" : white_queen_image,
             "K" : white_king_image,
             "p" : black_pawn_image,
             "n" : black_knight_image,
             "b" : black_bishop_image, 
             "r" : black_rook_image,
             "q" : black_queen_image,
             "k" : black_king_image}

white_pawn_icon = pygame.image.load(r"Images\WhitePawnIcon.png").convert_alpha()
white_knight_icon = pygame.image.load(r"Images\WhiteKnightIcon.png").convert_alpha()
white_bishop_icon = pygame.image.load(r"Images\WhiteBishopIcon.png").convert_alpha()
white_rook_icon = pygame.image.load(r"Images\WhiteRookIcon.png").convert_alpha()
white_queen_icon = pygame.image.load(r"Images\WhiteQueenIcon.png").convert_alpha()
white_king_icon = pygame.image.load(r"Images\WhiteKingIcon.png").convert_alpha()
black_pawn_icon = pygame.image.load(r"Images\BlackPawnIcon.png").convert_alpha()
black_knight_icon = pygame.image.load(r"Images\BlackKnightIcon.png").convert_alpha()
black_bishop_icon = pygame.image.load(r"Images\BlackBishopIcon.png").convert_alpha()
black_rook_icon = pygame.image.load(r"Images\BlackRookIcon.png").convert_alpha()
black_queen_icon = pygame.image.load(r"Images\BlackQueenIcon.png").convert_alpha()
black_king_icon = pygame.image.load(r"Images\BlackKingIcon.png").convert_alpha()
kingside_castle_on_icon = pygame.image.load(r"Images\KingsideCastleOnIcon.png").convert_alpha()
kingside_castle_off_icon = pygame.image.load(r"Images\KingsideCastleOffIcon.png").convert_alpha()
queenside_castle_on_icon = pygame.image.load(r"Images\QueensideCastleOnIcon.png").convert_alpha()
queenside_castle_off_icon = pygame.image.load(r"Images\QueensideCastleOffIcon.png").convert_alpha()
reset_board_icon = pygame.image.load(r"Images\ResetBoardIcon.png").convert_alpha()
clear_board_icon = pygame.image.load(r"Images\ClearBoardIcon.png").convert_alpha()
flip_board_icon = pygame.image.load(r"Images\FlipBoardIcon.png").convert_alpha()

def input_fen(fen_string):
    global turn
    global white_castling_rights
    global black_castling_rights
    global en_passant_square
    global board
    global past_board
    try:
        fen_string = fen_string.split()
        turn = (fen_string[1] == "b")
        fen_board = fen_string[0].split("/")
        board_output = [[] for _ in range(8)]
        for rank, fen_rank in enumerate(fen_board):
            for charecter in fen_rank:
                if charecter.isnumeric():
                    for file in range(int(charecter)):
                        board_output[rank].append(None)
                else:
                    board_output[rank].append(charecter)
        board = board_output
        past_board = [[board[rank][file] for file in range(8)] for rank in range(8)]
        white_castling_rights = ["K" in fen_string[2], "Q" in fen_string[2]]
        black_castling_rights = ["k" in fen_string[2], "q" in fen_string[2]]
        if fen_string[3] != "-":
            en_passant_square = (ord(fen_string[3][0]) - 97,8 - int(fen_string[3][1]))
        else:
            en_passant_square = None
    except:
        print("Invalid FEN")

def update():
    screen.fill((249, 241, 237))
    if 600 <= pygame.mouse.get_pos()[0] and pygame.mouse.get_pos()[0] <= 647 and\
       pygame.mouse.get_pos()[1] < 444:
        pygame.draw.rect(screen, (239, 233, 224), 
                         (600, (pygame.mouse.get_pos()[1]//37) * 37, 47, 37), 0)
    if 600 <= pygame.mouse.get_pos()[0] and pygame.mouse.get_pos()[0] <= 647 and\
       pygame.mouse.get_pos()[1] >= 444:
        pygame.draw.rect(screen, (239, 233, 224), 
                         (600, 444 + ((pygame.mouse.get_pos()[1]-444)//31) * 31, 47, 31), 0)
    screen.blit(white_pawn_icon, (605, 0))
    screen.blit(white_knight_icon, (605, 37))
    screen.blit(white_bishop_icon, (605, 74))
    screen.blit(white_rook_icon, (605, 111))
    screen.blit(white_queen_icon, (605, 148))
    screen.blit(white_king_icon, (605, 185))
    screen.blit(black_pawn_icon, (605, 222))
    screen.blit(black_knight_icon, (605, 259))
    screen.blit(black_bishop_icon, (605, 296))
    screen.blit(black_rook_icon, (605, 333))
    screen.blit(black_queen_icon, (605, 370))
    screen.blit(black_king_icon, (605, 407))
    if turn:
        if black_castling_rights[0]:
            screen.blit(kingside_castle_on_icon, (600, 444))
        else:
            screen.blit(kingside_castle_off_icon, (600, 444))
        if black_castling_rights[1]:
            screen.blit(queenside_castle_on_icon, (600, 475))
        else:
            screen.blit(queenside_castle_off_icon, (600, 475))
    else:
        if white_castling_rights[0]:
            screen.blit(kingside_castle_on_icon, (600, 444))
        else:
            screen.blit(kingside_castle_off_icon, (600, 444))
        if white_castling_rights[1]:
            screen.blit(queenside_castle_on_icon, (600, 475))
        else:
            screen.blit(queenside_castle_off_icon, (600, 475))
    screen.blit(reset_board_icon, (605, 503))
    screen.blit(clear_board_icon, (605, 534))
    screen.blit(flip_board_icon, (605, 565))
    for file in range(8):
        for rank in range(8):
            pygame.draw.rect(screen, [(235,210,183), (161,111,90)][(rank+file)%2], 
                            (file*75, rank*75, 75, 75), 0)
            if flip:
                if board[7-rank][7-file]:
                    if not drag_piece or [7-file, 7-rank] != drag_piece[:2]:
                        screen.blit(piece_key[board[7-rank][7-file]], (file*75, rank*75))
            else:
                if board[rank][file]:
                    if not drag_piece or [file, rank] != drag_piece[:2]:
                        screen.blit(piece_key[board[rank][file]], (file*75, rank*75))
    if drag_piece and drag_piece[2]:
        screen.blit(piece_key[drag_piece[2]], 
                    (pygame.mouse.get_pos()[0]-37, pygame.mouse.get_pos()[1]-37))
    pygame.display.update()

flip = False
drag_piece = None
input_fen("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
running = True
'''
import threading
def terminal_input():
    while running:
        fen_input = input("Import FEN- ")
        input_fen(fen_input)
input_thread = threading.Thread(target=terminal_input)
input_thread.daemon = True
input_thread.start()
'''
while running:
    mouse_position = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 0 <= mouse_position[0] and mouse_position[0] <= 600 and\
               0 <= mouse_position[1] and mouse_position[1] <= 600:
                if not drag_piece:
                    if flip:
                        drag_piece = [7 - mouse_position[0]//75, 7 - mouse_position[1]//75, 
                                      board[7-mouse_position[1]//75][7-mouse_position[0]//75]]
                    else:
                        drag_piece = [mouse_position[0]//75, mouse_position[1]//75, 
                                      board[mouse_position[1]//75][mouse_position[0]//75]]
            if 600 <= mouse_position[0] and mouse_position[0] <= 647 and mouse_position[1] < 444:
                drag_piece = [None, None, list(piece_key.keys())[pygame.mouse.get_pos()[1]//37]]
            if 600 <= mouse_position[0] and mouse_position[0] <= 647 and\
               444 <= mouse_position[1] and mouse_position[1] < 475:
                if turn:
                    black_castling_rights[0] = not black_castling_rights[0]
                else:
                    white_castling_rights[0] = not white_castling_rights[0]
            if 600 <= mouse_position[0] and mouse_position[0] <= 647 and\
               475 <= mouse_position[1] and mouse_position[1] < 506:
                if turn:
                    black_castling_rights[1] = not black_castling_rights[1]
                else:
                    white_castling_rights[1] = not white_castling_rights[1]
            if 600 <= mouse_position[0] and mouse_position[0] <= 647 and\
               506 <= mouse_position[1] and mouse_position[1] < 537:
                input_fen("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")[0]
            if 600 <= mouse_position[0] and mouse_position[0] <= 647 and\
               537 <= mouse_position[1] and mouse_position[1] < 568:
                input_fen("8/8/8/8/8/8/8/8 w - - 0 1")[0]
            if 600 <= mouse_position[0] and mouse_position[0] <= 647 and 568 <= mouse_position[1]:
                flip = not flip
                
        if event.type == pygame.MOUSEBUTTONUP:
            if drag_piece:
                if 0 <= mouse_position[0] and mouse_position[0] <= 600 and\
                   0 <= mouse_position[1] and mouse_position[1] <= 600:
                    if drag_piece[2]:
                        if drag_piece[0] != None:
                            board[drag_piece[1]][drag_piece[0]] = None
                        if flip:
                            board[7-mouse_position[1]//75][7-mouse_position[0]//75] = drag_piece[2]
                        else:
                            board[mouse_position[1]//75][mouse_position[0]//75] = drag_piece[2]
                        if drag_piece[2].isupper():
                            turn = True
                        if drag_piece[2].islower():
                            turn = False
                else:
                    if drag_piece[0] != None:
                        board[drag_piece[1]][drag_piece[0]] = None
            drag_piece = None
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                flip = not flip 

    if board != past_board:
        move = []
        for rank in range(8):
            for file in range(8):
                if board[rank][file] != past_board[rank][file]:
                    move.append((file, rank))
        if len(move) == 2:
            if board[move[0][1]][move[0][0]]:
                move.append(board[move[0][1]][move[0][0]])
            if board[move[1][1]][move[1][0]]:
                move.append(board[move[1][1]][move[1][0]])
            if move[2] == "K":
                white_castling_rights = [False, False]
            if move[2] == "k":
                black_castling_rights = [False, False]
            if move[2] == "R":
                if (7,7) in move:
                    white_castling_rights[0] = False
                if (0,7) in move:
                    white_castling_rights[1] = False
            if move[2] == "r":
                if (0,7) in move:
                    black_castling_rights[0] = False
                if (0,0) in move:
                    black_castling_rights[1] = False
            if move[2] == "K" and (4,7) in move:
                white_castling_rights == [False, False]
                if (2,7) in move:
                    board[7][0] = None
                    board[7][3] = "R"
                if (6,7) in move:
                    board[7][7] = None
                    board[7][5] = "R"
            if move[2] == "k" and (4,0) in move:
                black_castling_rights == [False, False]
                if (2,0) in move:
                    board[0][0] = None
                    board[0][3] = "r"
                if (6,0) in move:
                    board[0][7] = None
                    board[0][5] = "r"
            if en_passant_square:
                if move[2] == "P" and en_passant_square[1] == 2:
                    if en_passant_square in move:
                        board[3][en_passant_square[0]] = None
                if move[2] == "p" and en_passant_square[1] == 5:
                    if en_passant_square in move:
                        board[4][en_passant_square[0]] = None
                en_passant_square = None
            if move[2] == "P":
                if (move[0][1] == 6 and move[1][1] == 4) or\
                (move[1][1] == 6 and move[0][1] == 4):
                    en_passant_square = (move[0][0], 5)
            if move[2] == "p":
                if (move[0][1] == 3 and move[1][1] == 1) or\
                (move[1][1] == 3 and move[0][1] == 1):
                    en_passant_square = (move[0][0], 2)
        past_board = [[board[rank][file] for file in range(8)] for rank in range(8)]

    if turn:
        pygame.display.set_caption("BLACK TO MOVE")
        pygame.display.set_icon(pygame.image.load(r"Images\BlackKing.png"))
    else:
        pygame.display.set_caption("WHITE TO MOVE")
        pygame.display.set_icon(pygame.image.load(r"Images\WhiteKing.png"))
    update()
    MainClock.tick(30)

pygame.quit()
sys.exit()