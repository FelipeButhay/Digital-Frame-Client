import pygame

class Button:
    def __init__(self, x, y, height, width, color_rgb, text, text_color_rgb, surface, font) -> None:
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        
        self.text = text
        self.color = color_rgb
        self.tcolor = text_color_rgb
        
        self.surface = surface
        self.font = font
        
    def is_clicked(self, mp: tuple[int]) -> bool:
        return  self.x < mp[0] < self.x + self.width and \
                self.y < mp[1] < self.y + self.height
                
    def hover(self, color: tuple[int], mp: tuple[int]) -> tuple[int]:
        if self.is_clicked(mp):
            return (color[0] - 30, color[1] - 30, color[2] - 30)
        else:
            return color
                
    def draw_button(self, mp) -> None:
        rect = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.surface, self.hover(self.color, mp), rect)
        
        rendered_text = self.font.render(self.text, True, self.hover(self.tcolor, mp))
        self.surface.blit(rendered_text, rendered_text.get_rect(center = (self.x + self.width/2, self.y + self.height/2)))