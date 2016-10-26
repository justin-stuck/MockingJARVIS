import pickle
from motion_detector import MotionDetector 

class State(object):
    def identify(self):
        print "Currently helping ", self.attending

class DetectingMotion(State):

    def __init__(self,jarvis):
        self.jarvis = jarvis
        self.activity = "Detecting Motion..."
    def detect_motion(self):
        print self.activity
        self.jarvis.motion_detector.detect_motion()
        print "Detected Motion"
        self.proceed()
            
            
    def proceed(self):
        self.jarvis.state=self.jarvis.scanningstate
        
    def revert(self):
        return 0 #This is the base state

class Scanning(State):
    def __init__(self,jarvis):
        self.jarvis = jarvis
        self.activity = "Scanning for Faces..."
    def detect_faces():
        print self.activity
    def proceed(self):
        self.jarvis.state =  self.jarvis.facestate

    def revert(self):
        self.jarvis.state = self.jarvis.detectingstate

class FacialRecognition(State):
    def __init__(self,jarvis):
        self.jarvis = jarvis
        self.activity = "Classifying faces..."
        self.classifier = pickle.load(open('Faces.pkl', 'rb'))
    def ClassifyFace():
        
        print self.activty
    def proceed(self):
        self.jarvis.state = self.jarvis.waitingstate
    def revert(self):
        self.jarvis.state = self.jarvis.detectingstate

class WaitingForTask(State):
    def __init__(self,jarvis):
        self.jarvis = jarvis
        self.activity = "Waiting for Task..."
    
    def proceed(self):
        self.jarvis.state = self.jarvis.servingstate
    def revert(self):
        self.jarvis.state = self.jarvis.detectingstate
class Serving(State):
    def __init__(self,jarvis):
        self.jarvis = jarvis
        self.activity = "Serving roommate"
    def proceed(self):
        self.jarvis.state = self.jarvis.waitingstate
    def revert(self):
        self.jarvis.state = self.jarvis.waitingstate



class Jarvis(object):
    #"This is Jarvis, JAy's Replacement and Virtually Intelligent Servant."
    def __init__(self):
        #observer = Observable()
        #motion_detector = MotionObserver('Motion Detector')
        #observer.register(motion_detector)
        self.motion_detector = MotionDetector()
        self.detectingstate = DetectingMotion(self)
        self.scanningstate = Scanning(self)
        self.facestate = FacialRecognition(self)
        self.waitingstate = WaitingForTask(self)
        self.servingstate = Serving(self)
        self.state = self.detectingstate

        
    def proceed(self):
        self.state.proceed()

    def revert(self):
        self.state.revert()



def main():
    jarvis = Jarvis()
    jarvis.state.detect_motion()
    #This could be an integration test
    #actions = [jarvis.proceed,jarvis.revert,jarvis.proceed,jarvis.proceed]
    '''
    for action in actions:
        action()
        print jarvis.state.activity
    '''
if __name__=='__main__':
    main()

