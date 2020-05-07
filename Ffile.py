class AddBall():
    def __init__(self,balls,temp, max,turn=5):
        self.index=0
        self.max=max
        self.count=0
        self.turn=turn
        self.balls=balls
        self.temp=temp
        
    def update(self):
        if self.count % self.turn==0 and self.index<self.max:
            self.balls.append(self.temp[self.index])
            self.index+=1
        self.count+=1
        return self.balls
       