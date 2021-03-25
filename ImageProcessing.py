import image


#original size 612x608

original= image.FileImage('tree.jpg')
new= original.copy()
OGWidth= original.getWidth()
OGHeight= original.getHeight()
window=image.ImageWin(OGWidth,OGHeight, "Seasonal Tree")


def main():
	white= image.Pixel(255,255,255)
	for w in range(OGWidth):
		for h in range(OGHeight):
			p=new.getPixel(w,h)
			if p.red<=217 and p.green <=255 and p.blue <=217:
				if p.red >= 5 and p.green>=1 and p.blue >=10:
					if (p.green- p.red)>5 and p.green>p.blue:
						if p.red<=127:
							if p.red- p.green<20:
								p.red=int(p.red*2)
							if p.green>= 40:
								if (p.red-p.green)<=60:
									p.green=p.green
								if 60>(p.red -p. green) <= 80:
									p.green= int(p.green/1.25)
								if (p.red-p.green)>80:
									p.green= int(p.green/2)
						elif p.red>127:
							 p.green= p.red-50
						

			
			new.set_pixel(w,h,p)
			
	new.draw(window)
	new.save('new_tree.jpg')
	window.exitOnClick()
main()