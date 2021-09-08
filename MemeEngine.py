#from QuoteEngine.MemeEngine import MemeEngine
from PIL import Image, ImageDraw, ImageFont
import datetime

class MemeEngine():

    def __init__(self, dir):
        self.dir = dir

    def make_meme(img_path, body, author, width = 500) -> str:
        """Create a photo with a text quote on it.

        Arguments:
        img_path {str} -- the file location for the input image.
        body {str} - quote body.
        author {str} - quote author
        Returns:
            str -- the file path to the output image.
        """
        with Image.open(img_path) as img:
            
            if width > 500:
                width = 500
            ratio = width/float(img.size[0])
            height = int(ratio*float(img.size[1]))
            new_img = img.resize((width, height), Image.NEAREST)

            draw = ImageDraw.Draw(new_img)
            font_object = PIL.ImageFont.load_default()
            draw.text((10, 30), text + " - " + author, font=font_object, fill='white')
            
            now = datetime.datetime.now()
            now_str = str(now)
            extension = ".jpg"
            out_path = f'./static/{now_str}.jpeg'
            
            new_img.save(out_path)
            return out_path


        
