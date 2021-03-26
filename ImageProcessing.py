import image


#this application changes the tree for a green springtime tree to a red and yellow fall tree

def spring_to_fall(width,height, new, original):
	for w in range(width):
		for h in range(height):
			p=original.getPixel(w,h)
			if p.red<=190 and p.green <=255 and p.blue <=155: #filter out white pixels
				if (p.green- p.red)>12 and p.green>=p.blue: #filter out dark brown/black pixels
					#adjust red pixels depending on how much red is already in the pixel
					if p.red<=127:
						if p.red- p.green<20:
							p.red=int(p.red*2)
						#adjust green based on the amount of red. Too much difference between red and green makes a pink
						if p.green>= 40:
							if (p.red-p.green)<=60:
								p.green=p.green
							if 60>(p.red -p. green) <= 80:
								p.green= int(p.green/1.25)
							if (p.red-p.green)>80:
								p.green= int(p.green/2)
						#adjusts blue as needed: too much blue contributes to pink
						if p.blue>=70:
							p.blue= int(p.blue/3)
					elif p.red>127:
							p.green= p.red-50
					if p.blue>=100:
							p.blue= int(p.blue/3)
				new.setPixel(w,h,p)
	



def main():
	original= image.FileImage('tree.jpg')
	
	OGWidth= original.getWidth()
	OGHeight= original.getHeight()
	new= image.EmptyImage(OGWidth, OGHeight)
	spring_to_fall(OGWidth,OGHeight, new, original)
	
	
	window=image.ImageWin(OGWidth,OGHeight, "Seasonal Tree")		
	new.draw(window)
	new.save('fall_tree.jpg')
	window.exitOnClick()
main()