import sys

import pygame

from flappyball.config import *
from flappyball.obj.ball import Ball
from flappyball.obj.pipeline import Pipeline


class Game(object):
    def __init__(self, screen, highest_score):
        self._screen = screen
        self._font = pygame.font.SysFont(None, game_font_size)
        self._score = 0
        self._highest_score = highest_score
        self._dead = False

    def run(self):
        clock = pygame.time.Clock()
        ball = Ball(self._screen)
        pipelines = [Pipeline(self._screen, window_size_x)]
        while True:
            frame_time = clock.tick(game_frame) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return self._highest_score
                if (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN) and not self._dead:
                    ball.jump = True
            self._screen.fill(game_background_color)
            pipelines_new = []
            for pipeline in pipelines:
                pipeline.update(frame_time)
                if not pipeline.is_over_range():
                    pipelines_new.append(pipeline)
            while True:
                child = pipelines_new[-1].get_child()
                if child is None:
                    break
                pipelines_new.append(child)
            for pipeline in pipelines_new:
                pipeline.draw()
            ball.update(frame_time)
            ball.draw()
            if self._check_dead(ball, pipelines):
                return self._highest_score
            self._update_score(pipelines)
            pipelines = pipelines_new
            pygame.display.update()

    def _update_score(self, pipelines):
        for pipeline in pipelines:
            if pipeline.first_time_been_jumped():
                self._score += 1
        self._highest_score = max(self._score, self._highest_score)
        score_text = self._font.render('score: ' + str(self._score) + ' highest: ' + str(self._highest_score), True,
                                       text_color)
        self._screen.blit(score_text, (0, 0))

    def _check_dead(self, ball, pipelines):
        ball_x, ball_y = ball.get_position()
        for pipeline in pipelines:
            if pipeline.is_hit_ball(ball_x, ball_y):
                self._dead = True
                return True
        return False
