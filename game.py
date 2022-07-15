import pygame
from network import Network
import tkinter
import random



class Player():


    def __init__(self):

        self.root = tkinter.Tk()
        self.root.geometry('600x600')
        self.root.title('Roll Dice')


        label = tkinter.Label(self.root, text='', font=('Helvetica', 260))

        def roll_dice():
            dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
            self.roll1 = random.choice(dice)
            #self.roll2 = random.choice(dice)
            label.configure(text=f'{self.roll1} ')
            label.pack()

        global button
        button = tkinter.Button(self.root, text='roll dice', foreground='blue', command=roll_dice)
        button.pack()
        self.root.mainloop()



        def draw(self, g):
            pygame.draw.rect(g,self.roll1, 0)



        def get_value(self, r):  # a getter
            return self.r

        def set_value(self, r, value):  # a setter
            self.r = value

        def get_mouse(self, r, player):
            if self.get_value(r) == 0:
                self.set_value(r, player)


class Game:

    def __init__(self):
        self.net = Network()
        self.player = Player()  # positon
        self.player2 = Player()
        self.canvas = Canvas( "Testing...")



    def run(self):
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.K_ESCAPE:
                    run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    r = pygame.draw.rect.roll1


            # Send Network Stuff
            self.player2.r = self.parse_data(self.send_data())

            # Update Canvas
            self.canvas.draw_background()
            self.player.draw(self.canvas.get_canvas())
            self.player2.draw(self.canvas.get_canvas())
            self.canvas.update()

        pygame.quit()

        def send_data(self):
            """
            Send random num to server
            :return: None
            """
            data = str(self.net.id) + ":" + str(self.player.r)
            reply = self.net.send(data)
            return reply

        @staticmethod
        def parse_data(data):
            try:
                d = data.split(":")[1].split(",")
                return int(d[0]), int(d[1])
            except:
                return 0, 0



class Canvas:

    def __init__(self, name="None"):

        self.screen = pygame.display.set_mode((500,500)) #تحديد حجم الشبكة
        pygame.display.set_caption(name) #لتغير اسم النافذة للبايقرام

    @staticmethod
    def update():
        pygame.display.update()

    def draw_text(self, text, size):
        pygame.font.init()
        font = pygame.font.SysFont("comicsans", size)
        render = font.render(text, 1, (0,0,0))

        self.screen.draw(render, (500,500))

    def get_canvas(self):
        return self.screen

    def draw_background(self):
        self.screen.fill((255,255,255))




