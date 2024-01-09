import pygame
import pygame.gfxdraw



# Button with image. 
class ImageButton:
    def __init__(self, pos, image, function=lambda: print("No Command Assigned!")):
        self.pos = pos
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect(topleft=self.pos)
        
        self.function = function
    
    def check_press(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.function()
    
    def render(self, surface):
        surface.blit(self.image, self.pos)


# A button that can recieve input and do something. Can also check if hovering to change color. 
class Button:
    def __init__(self, pos, width, height, color=(255, 255, 255), hovering_color=(124, 124, 124), function=lambda: print("No Command(Function) Assigned!"), outline=True, outline_color=(0, 0, 0), text=None, text_color=(0, 0, 0), text_size=20, bold=False, italic=False, alpha=255):
        # The rectangle
        self.pos = pygame.math.Vector2(pos)
        self.alpha = alpha
        self.rect = pygame.Rect(*self.pos, width, height)
        
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
        
        self.function = function
        
    def check_press(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.function()

    def check_hovering(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.color = self.hovering_color
        else:
            self.color = self.starting_color
    
    def render(self, surface):
        pygame.gfxdraw.box(surface, self.rect, (*self.color, self.alpha))
        if self.outline:
            pygame.draw.rect(surface, self.outline_color, self.rect, 1)
        if self.text is not None:
            surface.blit(self.text, self.text_rect)



# A simple icon class which is meant to be a button but with an image.
class Icon:
    def __init__(self, pos, width, height, image, command=lambda: print("Hello World"), outline=True, outline_color=(0, 0, 0)):
        # The Rect attrs, image, and command
        self.pos = pygame.math.Vector2(pos)
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(topleft=self.pos)
        
        self.outline = outline
        self.outline_color = outline_color
        self.command = command
    
    def check_press(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.command()
            
    def render(self, surface):
        surface.blit(self.image, self.rect)
        if self.outline:
            pygame.draw.rect(surface, self.outline_color, self.rect, max(self.rect.width % 10, 1))
        


# A box which can be filled to indicate something. Able to recieve input.
class CheckBox:
    def __init__(self, pos, width, height, color=(255, 255, 255), filled_color=(124, 124, 124), marked_color=(255, 0, 255), outline=True, outline_color=(0, 0, 0)):
        self.pos = pygame.math.Vector2(pos)
        self.rect = pygame.Rect(*self.pos, width, height)
        
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



# Label that can be placed on a surface and updated.
class Label:
    def __init__(self, pos, text, text_size, text_color=(0, 0, 0), bg_color=None, anti_alias=True, bold=False, italic=False, alpha=255):
        self.pos = pygame.math.Vector2(pos)
        self.alpha = alpha
        
        self.text_color = text_color
        self.bg_color = bg_color
        
        self.anti_alias = anti_alias
        self.font = pygame.font.SysFont("Arial", text_size, bold, italic)
        self.text = self.font.render(text, self.anti_alias, self.text_color, self.bg_color)
        self.rect = self.text.get_rect(topleft=self.pos)
        
    def update_text(self, text):
        self.text = self.font.render(text, self.anti_alias, self.text_color, self.bg_color)
    
    def render(self, surface):
        self.text.set_alpha(self.alpha)
        surface.blit(self.text, self.rect)



# A bar that is meant to track a value. Can be updated, and drawn unto a surface.
class Bar:
    def __init__(self, pos, value, scale, height, outline=True, outline_color=(0, 0, 0), bar_color=(57, 255, 60), color_under=pygame.Color('red')):
        self.pos = pygame.math.Vector2(pos)
        self.value = value
        self.scale = scale
        self.rect = pygame.Rect(*self.pos, value * self.scale, height)
        self.bar_rect = pygame.Rect(*self.pos, value * self.scale, height)
        
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



# Backdrop is a way to create a semi-transperant background easily. 
class Backdrop:
    def __init__(self, pos, size, image=None, color=(0, 0, 0), alpha=255):
        self.size = size
        
        self.pos = pygame.math.Vector2(pos)
        
        self.image_name = image
        
        if self.image_name is not None:
            self.image = pygame.transform.scale(pygame.image.load(self.image_name).convert_alpha(), self.size)
        else:
            self.alpha = alpha
            self.rect = pygame.Rect(*pos, *self.size)
            self.color = (*color, self.alpha)
        
        
    def render(self, surface):
        if self.image_name is not None:
            surface.blit(self.image, self.pos)
        else:
            pygame.gfxdraw.box(surface, self.rect, self.color)
            
