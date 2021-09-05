"""
Quiz) 하늘에서 떨어지는 똥 피하기 게임을 만드시오

[게임 조건]
1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능
2. 똥은 화면 가장 위에서 떨어짐. x 좌표는 매번 랜덤으로 설정
3. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
4. 캐릭터가 똥과 충돌하면 게임 종료
5. FPS 는 30으로 고정

[게임 이미지]
1. 배경 : 640 * 480 (세로, 가로) - background.png
2. 캐릭터 : 70 * 70 - character.png
3. 똥 : 70 * 70 - enemy.png
"""

import pygame
import random

# 초기화
pygame.init()

# 화면 크기
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 타이틀
pygame.display.set_caption('Quiz')

# FPS
clock = pygame.time.Clock()

# 배경
background = pygame.image.load('C:/Workspace/nado_coding_practice_01/background.png')


# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
# 캐릭터
character = pygame.image.load('C:/Workspace/nado_coding_practice_01/character.png')
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# 캐릭터가 이동할 좌표
to_x = 0
to_y = 0

# enemy
enemy = pygame.image.load('C:/Workspace/nado_coding_practice_01/enemy.png')
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = 0

# 이동 속도
character_speed = 0.6
enemy_speed = 0.4

# 폰트 정의 (폰트 객체 생성 - 폰트, 크기)
game_font = pygame.font.Font(None, 40)

# 총 플레이 시간
total_time = 10

# 시작 시간
start_ticks = pygame.time.get_ticks()  # 현재 tick


running = True
while running:
    dt = clock.tick(30)  # 게임화면의 초당 프레임 수를 설정

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0



    # 3. 게임 캐릭터 위치 정의
    character_x_pos += (to_x * dt)
    enemy_y_pos += (enemy_speed * dt)

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > (screen_width - character_width):
        character_x_pos = (screen_width - character_width)

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width - enemy_width)


    # 4. 충돌 처리
    # rect 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print('BOOM!')
        running = False


    # 5. 화면에 그리기
    screen.blit(background, (0, 0))  # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))  # enemy

    # 타이머 넣기
    # 경과 시간
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    # render(출력할 글자, True, 글자 색상)
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    screen.blit(timer, (10, 10))

    if total_time - elapsed_time <= 0:
        print('TIME OUT!')
        running = False



    pygame.display.update()

# 종료 전 대기
pygame.time.delay(1300)  # 1.3초 (ms)


# pygame 종료
pygame.quit()


