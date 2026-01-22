TARGET, Kp, Ki, Kd = 400.0, 0.5, 0.1, 0.05
class SemanticStabilizer:
    def __init__(self): self.integral, self.last = 0.0, 0.0
    def record(self, mass):
        err = TARGET - mass
        self.integral += err
        c = Kp*err + Ki*self.integral + Kd*(err-self.last)
        self.last = err
        return {"recommendation": "EXPAND" if c>5 else "CONTRACT" if c<-5 else "STEADY"}
