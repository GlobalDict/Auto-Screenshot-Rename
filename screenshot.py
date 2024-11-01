from Range import *

class Shoot(types.KX_PythonComponent):

    args = {"Save name": ""}

    def awake(self, args):
        self.Name = args["Save name"]

        self.keyboard = logic.keyboard.inputs
        self.space = self.keyboard[events.SPACEKEY]

        # Folder to save your image file
        self.path = logic.expandPath("//") 

        # Number to add to your image name
        self.num = 0

    def start(self, args):
        pass

    def take(self):
        # Full Image name [name and number joined]
        self.imageName = f"{self.path}{self.Name}{self.num}"

        # Take screenshot
        render.makeScreenshot(self.imageName)

        # Change [add] number by 1 to avoid renaming already saved image(s)
        self.num += 1 

    def update(self):
        # Press spacebar to take a screenshot
        if self.space.activated: self.take()