import pygame

# 초기화 (반드시 필요)
pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('Boring Game')

# 배경 이미지 불러오기
background = pygame.image.load('C:/Workspace/nado_coding_practice_01/background.png')

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load('C:/Workspace/nado_coding_practice_01/character.png')
character_size = character.get_rect().size 
character_width = character_size[0]  
character_height = character_size[1] 
character_x_pos = (screen_width / 2) - (character_width / 2) 
character_y_pos = screen_height - character_height  

# 이동할 좌표
to_x = 0
to_y = 0

# 이벤트 루프
running = True 
while running:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            running = False  
        
        if event.type == pygame.KEYDOWN:  # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:  # 캐릭터를 왼쪽으로
                to_x -= 5  # to_x = to_x - 5
            elif event.key == pygame.K_RIGHT:  # 캐릭터를 오른쪽으로
                to_x += 5
            elif event.key == pygame.K_UP:  # 캐릭터를 위로
                to_y -= 5
            elif event.key == pygame.K_DOWN:  # 캐릭터를 아래로
                to_y += 5

        if event.type == pygame.KEYUP:  # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > (screen_width - character_width):
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > (screen_height - character_height):
        character_y_pos = screen_height - character_height

    screen.blit(background, (0, 0))  # 배경 그리기 

    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기

    pygame.display.update()  

# pygame 종료
pygame.quit()