import random, urllib2, sys
from lib import tqdm

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
imgurLink = "http://imgur.com/"
fileExt = ".jpg"

class randomImgur():

    def fiveCharString(self):
        '''
        Seven char string is completely possible, but a test i made
        created 0 valid imgur links out of 2700, so it's not worth it.
        '''

        #randLettersSeven = ""
        randLettersFive = ""

        for chars in range(0,5):
            char = alphabet[random.randrange(0, 62)]
            randLettersFive = char + randLettersFive

        #for chars in range(0,7):
        #    char = alphabet[random.randrange(0, 62)]
        #    randLettersSeven = char + randLettersSeven

        #choice = [randLettersFive,randLettersSeven]

        return randLettersFive

    def getImage(self):
        fileName = self.fiveCharString()
        img = urllib2.urlopen(imgurLink + fileName + fileExt).read()

        if len(img) == 503:
            self.getImage()
        else:
            with open("testdir/" + fileName + ".jpg", "wb") as f:
                f.write(img)

    def getImgLink(self):
        fileName = self.fiveCharString()
        img = urllib2.urlopen(imgurLink + fileName + fileExt)

        if img.geturl() == "http://i.imgur.com/removed.png":
            self.getImgLink()
        else:
            print img.geturl()

if __name__ == "__main__":

    randomImg = randomImgur()

    if len(sys.argv) == 1:
        print "python2 main.py [-n || -s] [number of images you want]"
    elif sys.argv[1] == str("-s"):
        try:
            print "Downloading..."
            for i in tqdm.tqdm(range(0, int(sys.argv[2]))):
                randomImg.getImage()
            print "Download complete!"
        except:
            print "Must be number 1 or higher."
    elif sys.argv[1] == str('-n'):
        try:
            print "Retrieving links..."
            for i in range(0, int(sys.argv[2])):
                randomImg.getImgLink()
            print "Done."
        except:
            print "Must be number 1 or higher."
    else:
        print "Option not valid."


