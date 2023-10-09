import pygame


# A simple button class with no support for images.
class Button:
    def __init__(self, pos, width, height, color=(255, 255, 255), hovering_color=(124, 124, 124), command=lambda: print("No Command(Function) Assigned!"), outline=True, outline_color=(0, 0, 0), text=None, text_color=(0, 0, 0), text_size=20, bold=False, italic=False):
        # The rectangle
        self.pos = pygame.math.Vector2(pos)
        self.rect = pygame.Rect(self.pos[0], self.pos[1], width, height)
        self.rect.topleft = (self.pos[0], self.pos[1])
        
        # Text
        if not (text is None):
            self.font = pygame.font.SysFont("Arial", text_size, bold, italic)
            self.text = self.font.render(text, True, text_color)
            self.text_rect = self.text.get_rect(topleft=self.pos)
        
        # Color
        self.starting_color = color
        self.color = color
        self.hovering_color = hovering_color
        self.outline = outline
        self.outline_color = outline_color
        
        self.command = command
        
    def check_input(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.command()

    def check_hovering(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.color = self.hovering_color
        else:
            self.color = self.starting_color
    
    def render(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        if self.outline:
            pygame.draw.rect(surface, self.outline_color, self.rect, 1)
        if not (self.text is None):
            surface.blit(self.text, self.text_rect)


# A simple icon class which is meant to be a button but with an image.
class Icon(object):
    def __init__(self, pos, width, height, image, command=lambda: print("Hello World"), outline=True, outline_color=(0, 0, 0)):
        # The Rect attrs, image, and command
        self.pos = pygame.math.Vector2(pos)
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(topleft=self.pos)
        
        self.outline = outline
        self.outline_color = outline_color
        self.command = command
    
    def check_input(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.command()
            
    def render(self, surface):
        surface.blit(self.image, self.rect)
        if self.outline:
            pygame.draw.rect(surface, self.outline_color, self.rect, max(self.rect.width % 10, 1))
        


# Basically a button but no hovering and no text.
# Yes, I understand rect's aren't meant for drawing but i dont have the current brain power to do the math to get topleft from x and width.
class CheckBox(object):
    def __init__(self, pos, width, height, color=(255, 255, 255), filled_color=(124, 124, 124), marked_color=(255, 0, 255), outline=True, outline_color=(0, 0, 0)):
        self.pos = pygame.math.Vector2(pos)
        self.rect = pygame.Rect(self.pos[0], self.pos[1], width, height)
        self.rect.topleft = (self.pos[0], self.pos[1])
        
        self.default_color = color
        self.color = color
        
        self.marked_color = marked_color
        self.marked = False
        
        self.outline = outline
        self.outline_color = outline_color
    
    def check_press(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            if self.marked:
                self.color = self.marked_color
                self.marked = False
            elif not self.marked:
                self.color = self.default_color
                self.marked = True
                
    def render(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        if self.outline:
            pygame.draw.rect(surface, self.outline_color, self.rect, 5)



# Idk why im trying to add a label. I just am.
class Label:
    def __init__(self, pos, text, text_size, text_color=(0, 0, 0), bg_color=None, bold=False, italic=False):
        
        self.pos = Vector2(pos)
        font = pygame.font.SysFont("Arial", text_size, bold, italic)
        self.text = font.render(text, True, text_color, bg_color)
        self.rect = self.text.get_rect(topleft=self.pos)
    
    def render(self, surface):
        surface.blit(self.text, self.rect)



# Very useful in so many games. Def an add. Crude. Not circular.
class Bar:
    def __init__(self, pos, value, scale, height, outline=True, outline_color=(0, 0, 0), bar_color=(57, 255, 60), color_under=pygame.Color('red')):
        self.pos = pygame.math.Vector2(pos)
        self.value = value
        self.scale = scale
        self.rect = pygame.Rect(self.pos[0], self.pos[1], value*self.scale, height)
        self.bar_rect = pygame.Rect(self.pos[0], self.pos[1], value*self.scale, height)
        
        self.outline = outline
        self.outline_color = outline_color
        self.color = bar_color
        self.color_under = color_under
        
    def update(self, value):
        self.bar_rect.width = max(0, value)
    
    def render(self, surface):
        pygame.draw.rect(surface, self.color_under, self.rect)
        pygame.draw.rect(surface, self.color, self.bar_rect)
        if self.outline:
            pygame.draw.rect(surface, self.outline_color, self.rect, 1)



# The elliposde version of bar.
class CustomBar:
    pass