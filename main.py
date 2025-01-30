import pygame
import os
from codes import button
from codes import sendImage
from codes import importFile


from PIL import Image
import os
import shutil

# import tkinter as tk
# resolution_screen = tk.Tk()
# SX = resolution_screen.winfo_screenwidth()
# SY = resolution_screen.winfo_screenheight()

SX = 900 
SY = 500

U = int(SY*.05)

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SX, SY))
pygame.display.set_caption("Send Image Client")

direc = os.path.dirname(os.path.abspath(__file__)).replace('\'', '/')

with open(f"{direc}/assets/last_ip.txt", "r") as ip_file:
    ip_str = ip_file.readline()
    
ip_selected = False

image_direc = None

btn_h = (SY + 5*U)*0.25

BACKGROUND = (30, 30, 30)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
GREEN = (30, 200, 30)

general_font = pygame.font.Font(f"{direc}/assets/CONSOLA.TTF", int((SY - 5*U)*0.15))          

select_img_btn = button.Button(
    x = U,
    y = 3*U + (SY - 5*U)*0.25*2,
    width = SX - 2*U,
    height = (SY - 5*U)*0.25,
    
    color_rgb = GRAY,
    text = "Select Image",
    text_color_rgb= WHITE,
    
    surface = screen,
    font = general_font
)

send_img_btn = button.Button(
    x = U,
    y = 4*U + (SY - 5*U)*0.25*3,
    width = SX - 2*U,
    height = (SY - 5*U)*0.25,
    
    color_rgb = GREEN,
    text = "Send Image",
    text_color_rgb= WHITE,
    
    surface = screen,
    font = general_font
)

while (True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open(f"{direc}/assets/last_ip.txt", "w") as ip_file:
                ip_file.write(ip_str)
            
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.dict['button'] == 1:
            if U < event.dict['pos'][0] < U + (SX*0.5 - U*1.5) and \
               U < event.dict['pos'][1] < U + ((SY - 5*U)*0.25):
                
                if not ip_selected:
                    ip_selected = True
            else:
                ip_selected = False
            
            if select_img_btn.is_clicked(event.dict['pos']):
                image_direc = importFile.get_path_of_image()
                
                if image_direc:
                    
                    filename, ext = os.path.splitext(os.path.basename(image_direc))
                    new_file_path = f"{direc}\Images\image.jpg"

                    if ext.lower() != ".jpg":
                        img = Image.open(image_direc)
                        img = img.convert("RGB") 
                        img.save(new_file_path, "JPEG")
                        print(f"Imagen convertida y guardada en: {new_file_path}")
                    else:
                        shutil.copy(image_direc, new_file_path)
                        print(f"Imagen copiada a: {new_file_path}")
                else:
                    print("No se seleccionó ningún archivo.")

            if send_img_btn.is_clicked(event.dict['pos']):
                print(sendImage.sendImage(ip_str, direc))
            
        if event.type == pygame.KEYDOWN and ip_selected:
            if event.dict['unicode'] == "\x08":
                ip_str = ip_str[0:-1]
            elif event.dict['unicode'].isnumeric() or  event.dict['unicode'] == '.':
                ip_str += event.dict['unicode']
                
    screen.fill(BACKGROUND)
      
    rendered_text = general_font.render(f"IP: {ip_str}", True, GREEN if ip_selected else WHITE)
    screen.blit(rendered_text, rendered_text.get_rect(midleft = (U, U + (SY - U*5)*0.125)))
                
    mouse_pos = pygame.mouse.get_pos()
    select_img_btn.draw_button(mouse_pos)
    send_img_btn.draw_button(mouse_pos)
    
    pygame.display.update()
    clock.tick(60)