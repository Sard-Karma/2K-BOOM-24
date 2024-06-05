import streams
from riverdi.displays.bt81x import ctp50
from bridgetek.bt81x import bt81x

port = streams.serial(SERIAL1)
port2 = streams.serial()
while True:
    mess = port.read()
    if mess == "w":
        port2.write(mess)
        # choose one logo to be loaded on flash
        #new_resource('zerynth_logo.bin')
        new_resource('blanc.png')
        LOGO_W = 800
        LOGO_H = 480
        linestride = LOGO_W * 2 # with ARGB1555 and ARGB4 formats, 2 bytes per pixel
        
        #layout = (bt81x.ARGB1555, linestride) # choose this layout for zerynth_logo.bin
        layout = (bt81x.ARGB4, linestride)  # choose this layout for zerynth_logo.png
        
        blanc = bt81x.Bitmap(1, 0, layout,
                            (bt81x.BILINEAR, bt81x.BORDER, bt81x.BORDER, LOGO_W, LOGO_H))
        
        bt81x.init(SPI0, D4, D33, D34)
        
        #bt81x.inflate(0, 'zerynth_logo.bin')
        bt81x.load_image(0, 0, 'blanc.png')
        
        bt81x.dl_start()
        bt81x.clear_color(rgb=(0xff, 0xff, 0xff))
        bt81x.clear(1, 1, 0)
        
        blanc.prepare_draw()
        blanc.draw(((bt81x.display_conf.width - LOGO_W)//2, (bt81x.display_conf.height - LOGO_H)//2), vertex_fmt=0)
        
        bt81x.display()
        bt81x.swap_and_empty()
        
    elif mess == "a":
        port2.write(mess)
        # choose one logo to be loaded on flash
        #new_resource('zerynth_logo.bin')
        new_resource('bleu.png')
        LOGO_W = 800
        LOGO_H = 480
        linestride = LOGO_W * 2 # with ARGB1555 and ARGB4 formats, 2 bytes per pixel
        
        #layout = (bt81x.ARGB1555, linestride) # choose this layout for zerynth_logo.bin
        layout = (bt81x.ARGB4, linestride)  # choose this layout for zerynth_logo.png
        
        bleu = bt81x.Bitmap(1, 0, layout,
                            (bt81x.BILINEAR, bt81x.BORDER, bt81x.BORDER, LOGO_W, LOGO_H))
        
        bt81x.init(SPI0, D4, D33, D34)
        
        #bt81x.inflate(0, 'zerynth_logo.bin')
        bt81x.load_image(0, 0, 'bleu.png')
        
        bt81x.dl_start()
        bt81x.clear_color(rgb=(0xff, 0xff, 0xff))
        bt81x.clear(1, 1, 0)
        
        bleu.prepare_draw()
        bleu.draw(((bt81x.display_conf.width - LOGO_W)//2, (bt81x.display_conf.height - LOGO_H)//2), vertex_fmt=0)
        
        bt81x.display()
        bt81x.swap_and_empty()
        
    elif mess == "r":
        port2.write(mess)
        # choose one logo to be loaded on flash
        #new_resource('zerynth_logo.bin')
        new_resource('rouge.png')
        LOGO_W = 800
        LOGO_H = 480
        linestride = LOGO_W * 2 # with ARGB1555 and ARGB4 formats, 2 bytes per pixel
        
        #layout = (bt81x.ARGB1555, linestride) # choose this layout for zerynth_logo.bin
        layout = (bt81x.ARGB4, linestride)  # choose this layout for zerynth_logo.png
        
        rouge = bt81x.Bitmap(1, 0, layout,
                            (bt81x.BILINEAR, bt81x.BORDER, bt81x.BORDER, LOGO_W, LOGO_H))
        
        bt81x.init(SPI0, D4, D33, D34)
        
        #bt81x.inflate(0, 'zerynth_logo.bin')
        bt81x.load_image(0, 0, 'rouge.png')
        
        bt81x.dl_start()
        bt81x.clear_color(rgb=(0xff, 0xff, 0xff))
        bt81x.clear(1, 1, 0)
        
        rouge.prepare_draw()
        rouge.draw(((bt81x.display_conf.width - LOGO_W)//2, (bt81x.display_conf.height - LOGO_H)//2), vertex_fmt=0)
        
        bt81x.display()
        bt81x.swap_and_empty()
        
    elif mess == "v":
        port2.write(mess)
        # choose one logo to be loaded on flash
        #new_resource('zerynth_logo.bin')
        new_resource('vert.png')
        LOGO_W = 800
        LOGO_H = 480
        linestride = LOGO_W * 2 # with ARGB1555 and ARGB4 formats, 2 bytes per pixel
        
        #layout = (bt81x.ARGB1555, linestride) # choose this layout for zerynth_logo.bin
        layout = (bt81x.ARGB4, linestride)  # choose this layout for zerynth_logo.png
        
        vert = bt81x.Bitmap(1, 0, layout,
                            (bt81x.BILINEAR, bt81x.BORDER, bt81x.BORDER, LOGO_W, LOGO_H))
        
        bt81x.init(SPI0, D4, D33, D34)
        
        #bt81x.inflate(0, 'zerynth_logo.bin')
        bt81x.load_image(0, 0, 'vert.png')
        
        bt81x.dl_start()
        bt81x.clear_color(rgb=(0xff, 0xff, 0xff))
        bt81x.clear(1, 1, 0)
        
        vert.prepare_draw()
        vert.draw(((bt81x.display_conf.width - LOGO_W)//2, (bt81x.display_conf.height - LOGO_H)//2), vertex_fmt=0)
        
        bt81x.display()
        bt81x.swap_and_empty()
        
    elif mess == "h":
        port2.write(mess)
        # choose one logo to be loaded on flash
        #new_resource('zerynth_logo.bin')
        new_resource('haut.png')
        LOGO_W = 800
        LOGO_H = 480
        linestride = LOGO_W * 2 # with ARGB1555 and ARGB4 formats, 2 bytes per pixel
        
        #layout = (bt81x.ARGB1555, linestride) # choose this layout for zerynth_logo.bin
        layout = (bt81x.ARGB4, linestride)  # choose this layout for zerynth_logo.png
        
        haut = bt81x.Bitmap(1, 0, layout,
                            (bt81x.BILINEAR, bt81x.BORDER, bt81x.BORDER, LOGO_W, LOGO_H))
        
        bt81x.init(SPI0, D4, D33, D34)
        
        #bt81x.inflate(0, 'zerynth_logo.bin')
        bt81x.load_image(0, 0, 'haut.png')
        
        bt81x.dl_start()
        bt81x.clear_color(rgb=(0xff, 0xff, 0xff))
        bt81x.clear(1, 1, 0)
        
        haut.prepare_draw()
        haut.draw(((bt81x.display_conf.width - LOGO_W)//2, (bt81x.display_conf.height - LOGO_H)//2), vertex_fmt=0)
        
        bt81x.display()
        bt81x.swap_and_empty()
        
    elif mess == "b":
        port2.write(mess)
        # choose one logo to be loaded on flash
        #new_resource('zerynth_logo.bin')
        new_resource('bas.png')
        LOGO_W = 800
        LOGO_H = 480
        linestride = LOGO_W * 2 # with ARGB1555 and ARGB4 formats, 2 bytes per pixel
        
        #layout = (bt81x.ARGB1555, linestride) # choose this layout for zerynth_logo.bin
        layout = (bt81x.ARGB4, linestride)  # choose this layout for zerynth_logo.png
        
        bas = bt81x.Bitmap(1, 0, layout,
                            (bt81x.BILINEAR, bt81x.BORDER, bt81x.BORDER, LOGO_W, LOGO_H))
        
        bt81x.init(SPI0, D4, D33, D34)
        
        #bt81x.inflate(0, 'zerynth_logo.bin')
        bt81x.load_image(0, 0, 'bas.png')
        
        bt81x.dl_start()
        bt81x.clear_color(rgb=(0xff, 0xff, 0xff))
        bt81x.clear(1, 1, 0)
        
        bas.prepare_draw()
        bas.draw(((bt81x.display_conf.width - LOGO_W)//2, (bt81x.display_conf.height - LOGO_H)//2), vertex_fmt=0)
        
        bt81x.display()
        bt81x.swap_and_empty()
        
    elif mess == "g":
        port2.write(mess)
        # choose one logo to be loaded on flash
        #new_resource('zerynth_logo.bin')
        new_resource('gauche.png')
        LOGO_W = 800
        LOGO_H = 480
        linestride = LOGO_W * 2 # with ARGB1555 and ARGB4 formats, 2 bytes per pixel
        
        #layout = (bt81x.ARGB1555, linestride) # choose this layout for zerynth_logo.bin
        layout = (bt81x.ARGB4, linestride)  # choose this layout for zerynth_logo.png
        
        gauche = bt81x.Bitmap(1, 0, layout,
                            (bt81x.BILINEAR, bt81x.BORDER, bt81x.BORDER, LOGO_W, LOGO_H))
        
        bt81x.init(SPI0, D4, D33, D34)
        
        #bt81x.inflate(0, 'zerynth_logo.bin')
        bt81x.load_image(0, 0, 'gauche.png')
        
        bt81x.dl_start()
        bt81x.clear_color(rgb=(0xff, 0xff, 0xff))
        bt81x.clear(1, 1, 0)
        
        gauche.prepare_draw()
        gauche.draw(((bt81x.display_conf.width - LOGO_W)//2, (bt81x.display_conf.height - LOGO_H)//2), vertex_fmt=0)
        
        bt81x.display()
        bt81x.swap_and_empty()
        
    elif mess == "d":
        port2.write(mess)
        # choose one logo to be loaded on flash
        #new_resource('zerynth_logo.bin')
        new_resource('droite.png')
        LOGO_W = 800
        LOGO_H = 480
        linestride = LOGO_W * 2 # with ARGB1555 and ARGB4 formats, 2 bytes per pixel
        
        #layout = (bt81x.ARGB1555, linestride) # choose this layout for zerynth_logo.bin
        layout = (bt81x.ARGB4, linestride)  # choose this layout for zerynth_logo.png
        
        droite = bt81x.Bitmap(1, 0, layout,
                            (bt81x.BILINEAR, bt81x.BORDER, bt81x.BORDER, LOGO_W, LOGO_H))
        
        bt81x.init(SPI0, D4, D33, D34)
        
        #bt81x.inflate(0, 'zerynth_logo.bin')
        bt81x.load_image(0, 0, 'droite.png')
        
        bt81x.dl_start()
        bt81x.clear_color(rgb=(0xff, 0xff, 0xff))
        bt81x.clear(1, 1, 0)
        
        droite.prepare_draw()
        droite.draw(((bt81x.display_conf.width - LOGO_W)//2, (bt81x.display_conf.height - LOGO_H)//2), vertex_fmt=0)
        
        bt81x.display()
        bt81x.swap_and_empty()
        
    elif mess == "p":
        port2.write(mess)
        # choose one logo to be loaded on flash
        #new_resource('zerynth_logo.bin')
        new_resource('appui.png')
        LOGO_W = 800
        LOGO_H = 480
        linestride = LOGO_W * 2 # with ARGB1555 and ARGB4 formats, 2 bytes per pixel
        
        #layout = (bt81x.ARGB1555, linestride) # choose this layout for zerynth_logo.bin
        layout = (bt81x.ARGB4, linestride)  # choose this layout for zerynth_logo.png
        
        appui = bt81x.Bitmap(1, 0, layout,
                            (bt81x.BILINEAR, bt81x.BORDER, bt81x.BORDER, LOGO_W, LOGO_H))
        
        bt81x.init(SPI0, D4, D33, D34)
        
        #bt81x.inflate(0, 'zerynth_logo.bin')
        bt81x.load_image(0, 0, 'appui.png')
        
        bt81x.dl_start()
        bt81x.clear_color(rgb=(0xff, 0xff, 0xff))
        bt81x.clear(1, 1, 0)
        
        appui.prepare_draw()
        appui.draw(((bt81x.display_conf.width - LOGO_W)//2, (bt81x.display_conf.height - LOGO_H)//2), vertex_fmt=0)
        
        bt81x.display()
        bt81x.swap_and_empty()
        
    elif mess == "1":
        port2.write(mess)
        # choose one logo to be loaded on flash
        #new_resource('zerynth_logo.bin')
        new_resource('Start.png')
        LOGO_W = 800
        LOGO_H = 480
        linestride = LOGO_W * 2 # with ARGB1555 and ARGB4 formats, 2 bytes per pixel
        
        #layout = (bt81x.ARGB1555, linestride) # choose this layout for zerynth_logo.bin
        layout = (bt81x.ARGB4, linestride)  # choose this layout for zerynth_logo.png
        
        start = bt81x.Bitmap(1, 0, layout,
                            (bt81x.BILINEAR, bt81x.BORDER, bt81x.BORDER, LOGO_W, LOGO_H))
        
        bt81x.init(SPI0, D4, D33, D34)
        
        #bt81x.inflate(0, 'zerynth_logo.bin')
        bt81x.load_image(0, 0, 'Start.png')
        
        bt81x.dl_start()
        bt81x.clear_color(rgb=(0xff, 0xff, 0xff))
        bt81x.clear(1, 1, 0)
        
        start.prepare_draw()
        start.draw(((bt81x.display_conf.width - LOGO_W)//2, (bt81x.display_conf.height - LOGO_H)//2), vertex_fmt=0)
        
        bt81x.display()
        bt81x.swap_and_empty()
        
    if mess == "2":
        port2.write(mess)
        # choose one logo to be loaded on flash
        #new_resource('zerynth_logo.bin')
        new_resource('Goodend.png')
        LOGO_W = 800
        LOGO_H = 480
        linestride = LOGO_W * 2 # with ARGB1555 and ARGB4 formats, 2 bytes per pixel
        
        #layout = (bt81x.ARGB1555, linestride) # choose this layout for zerynth_logo.bin
        layout = (bt81x.ARGB4, linestride)  # choose this layout for zerynth_logo.png
        
        good = bt81x.Bitmap(1, 0, layout,
                            (bt81x.BILINEAR, bt81x.BORDER, bt81x.BORDER, LOGO_W, LOGO_H))
        
        bt81x.init(SPI0, D4, D33, D34)
        
        #bt81x.inflate(0, 'zerynth_logo.bin')
        bt81x.load_image(0, 0, 'Goodend.png')
        
        bt81x.dl_start()
        bt81x.clear_color(rgb=(0xff, 0xff, 0xff))
        bt81x.clear(1, 1, 0)
        
        good.prepare_draw()
        good.draw(((bt81x.display_conf.width - LOGO_W)//2, (bt81x.display_conf.height - LOGO_H)//2), vertex_fmt=0)
        
        bt81x.display()
        bt81x.swap_and_empty()
        
    if mess == "3":
        port2.write(mess)
        # choose one logo to be loaded on flash
        #new_resource('zerynth_logo.bin')
        new_resource('PAD.png')
        LOGO_W = 800
        LOGO_H = 480
        linestride = LOGO_W * 2 # with ARGB1555 and ARGB4 formats, 2 bytes per pixel
        
        #layout = (bt81x.ARGB1555, linestride) # choose this layout for zerynth_logo.bin
        layout = (bt81x.ARGB4, linestride)  # choose this layout for zerynth_logo.png
        
        PAD = bt81x.Bitmap(1, 0, layout,
                            (bt81x.BILINEAR, bt81x.BORDER, bt81x.BORDER, LOGO_W, LOGO_H))
        
        bt81x.init(SPI0, D4, D33, D34)
        
        #bt81x.inflate(0, 'zerynth_logo.bin')
        bt81x.load_image(0, 0, 'PAD.png')
        
        bt81x.dl_start()
        bt81x.clear_color(rgb=(0xff, 0xff, 0xff))
        bt81x.clear(1, 1, 0)
        
        PAD.prepare_draw()
        PAD.draw(((bt81x.display_conf.width - LOGO_W)//2, (bt81x.display_conf.height - LOGO_H)//2), vertex_fmt=0)
        
        bt81x.display()
        bt81x.swap_and_empty()
        
    if mess == "4":
        port2.write(mess)
        # choose one logo to be loaded on flash
        #new_resource('zerynth_logo.bin')
        new_resource('Interrupteurs.png')
        LOGO_W = 800
        LOGO_H = 480
        linestride = LOGO_W * 2 # with ARGB1555 and ARGB4 formats, 2 bytes per pixel
        
        #layout = (bt81x.ARGB1555, linestride) # choose this layout for zerynth_logo.bin
        layout = (bt81x.ARGB4, linestride)  # choose this layout for zerynth_logo.png
        
        interrupteur = bt81x.Bitmap(1, 0, layout,
                            (bt81x.BILINEAR, bt81x.BORDER, bt81x.BORDER, LOGO_W, LOGO_H))
        
        bt81x.init(SPI0, D4, D33, D34)
        
        #bt81x.inflate(0, 'zerynth_logo.bin')
        bt81x.load_image(0, 0, 'Interrupteurs.png')
        
        bt81x.dl_start()
        bt81x.clear_color(rgb=(0xff, 0xff, 0xff))
        bt81x.clear(1, 1, 0)
        
        interrupteur.prepare_draw()
        interrupteur.draw(((bt81x.display_conf.width - LOGO_W)//2, (bt81x.display_conf.height - LOGO_H)//2), vertex_fmt=0)
        
        bt81x.display()
        bt81x.swap_and_empty()
        
    if mess == "5":
        port2.write(mess)
        # choose one logo to be loaded on flash
        #new_resource('zerynth_logo.bin')
        new_resource('Joystick.png')
        LOGO_W = 800
        LOGO_H = 480
        linestride = LOGO_W * 2 # with ARGB1555 and ARGB4 formats, 2 bytes per pixel
        
        #layout = (bt81x.ARGB1555, linestride) # choose this layout for zerynth_logo.bin
        layout = (bt81x.ARGB4, linestride)  # choose this layout for zerynth_logo.png
        
        joystick = bt81x.Bitmap(1, 0, layout,
                            (bt81x.BILINEAR, bt81x.BORDER, bt81x.BORDER, LOGO_W, LOGO_H))
        
        bt81x.init(SPI0, D4, D33, D34)
        
        #bt81x.inflate(0, 'zerynth_logo.bin')
        bt81x.load_image(0, 0, 'Joystick.png')
        
        bt81x.dl_start()
        bt81x.clear_color(rgb=(0xff, 0xff, 0xff))
        bt81x.clear(1, 1, 0)
        
        joystick.prepare_draw()
        joystick.draw(((bt81x.display_conf.width - LOGO_W)//2, (bt81x.display_conf.height - LOGO_H)//2), vertex_fmt=0)
        
        bt81x.display()
        bt81x.swap_and_empty()
        
    if mess == "6":
        port2.write(mess)
        # choose one logo to be loaded on flash
        #new_resource('zerynth_logo.bin')
        new_resource('Boutons.png')
        LOGO_W = 800
        LOGO_H = 480
        linestride = LOGO_W * 2 # with ARGB1555 and ARGB4 formats, 2 bytes per pixel
        
       #layout = (bt81x.ARGB1555, linestride) # choose this layout for zerynth_logo.bin
        layout = (bt81x.ARGB4, linestride)  # choose this layout for zerynth_logo.png
        
        boutons = bt81x.Bitmap(1, 0, layout,
                            (bt81x.BILINEAR, bt81x.BORDER, bt81x.BORDER, LOGO_W, LOGO_H))
        
        bt81x.init(SPI0, D4, D33, D34)
        
        #bt81x.inflate(0, 'zerynth_logo.bin')
        bt81x.load_image(0, 0, 'Boutons.png')
        
        bt81x.dl_start()
        bt81x.clear_color(rgb=(0xff, 0xff, 0xff))
        bt81x.clear(1, 1, 0)
        
        boutons.prepare_draw()
        boutons.draw(((bt81x.display_conf.width - LOGO_W)//2, (bt81x.display_conf.height - LOGO_H)//2), vertex_fmt=0)
        
        bt81x.display()
        bt81x.swap_and_empty()
        
    if mess == "7":
        port2.write(mess)
        # choose one logo to be loaded on flash
        #new_resource('zerynth_logo.bin')
        new_resource('Badend.png')
        LOGO_W = 800
        LOGO_H = 480
        linestride = LOGO_W * 2 # with ARGB1555 and ARGB4 formats, 2 bytes per pixel
        
        #layout = (bt81x.ARGB1555, linestride) # choose this layout for zerynth_logo.bin
        layout = (bt81x.ARGB4, linestride)  # choose this layout for zerynth_logo.png
        
        bad = bt81x.Bitmap(1, 0, layout,
                            (bt81x.BILINEAR, bt81x.BORDER, bt81x.BORDER, LOGO_W, LOGO_H))
        
        bt81x.init(SPI0, D4, D33, D34)
        
        #bt81x.inflate(0, 'zerynth_logo.bin')
        bt81x.load_image(0, 0, 'Badend.png')
        
        bt81x.dl_start()
        bt81x.clear_color(rgb=(0xff, 0xff, 0xff))
        bt81x.clear(1, 1, 0)
        
        bad.prepare_draw()
        bad.draw(((bt81x.display_conf.width - LOGO_W)//2, (bt81x.display_conf.height - LOGO_H)//2), vertex_fmt=0)
        
        bt81x.display()
        bt81x.swap_and_empty()
        